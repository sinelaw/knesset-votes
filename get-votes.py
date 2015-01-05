import urllib
import json
import sqlite3

def get_votes():

    conn = sqlite3.connect('votes.sqlite3')
    c = conn.cursor()
    c.execute('''CREATE TABLE votes
                 (for_votes_count int, against_votes_count int, title text, votes_count int, resource_uri text)''')

    try:
        base = 'https://oknesset.org'
        url = base + '/api/v2/vote/'
        while isinstance(url, basestring):
            print 'Retrieving:', url
            u = urllib.urlopen(url)
            print 'Parsing...'
            entry = json.loads(u.read())
            print entry['meta']
            print 'Inserting...',
            rows = list(map(lambda v: (v['for_votes_count'], v['against_votes_count'], v['title'], v['votes_count'], v['resource_uri']), entry['objects']))
            c.executemany("INSERT INTO votes VALUES (?,?,?,?,?)", rows)
            conn.commit()
            print 'Comitted.'
            next_query_url = entry['meta']['next']
            if next_query_url is None:
                break
            url = base + next_query_url
    finally:
        conn.close()
        print 'DB closed.'


if __name__ == '__main__':
    get_votes()

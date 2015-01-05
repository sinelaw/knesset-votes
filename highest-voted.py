import sqlite3
import codecs

# Copied from https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def render_highest_votes_page():
    num = 200
    with codecs.open('highest-voted.html','wb', 'utf-8') as f:
        conn = sqlite3.connect('votes.sqlite3')
        conn.row_factory = dict_factory
        c = conn.cursor()
        for row in c.execute('select * from votes order by votes_count desc limit %d' % (num,)):
            f.write('<tr>')

            titles = ['title', 'votes_count', 'for_votes_count', 'against_votes_count']
            for k in titles:
                f.write('<td class="%s">%s</td>' % (k, row[k]))
            f.write('</tr>\n')

if __name__ == '__main__':
    render_highest_votes_page()

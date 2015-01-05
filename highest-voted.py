import sqlite3

def render_highest_votes_page():
    with file('highest-voted.html','wb') as f:
        conn = sqlite3.connect('votes.sqlite3')
        c = conn.cursor()
        for row in c.execute('select * from votes order by votes_count desc limit 100'):
            f.write('<tr>')
            for k,v in row.items():
                f.write('<td class="%s">%s</td>' % (k, v))
            f.write('</tr>\n')

if __name__ == '__main__':
    render_highest_votes_page()

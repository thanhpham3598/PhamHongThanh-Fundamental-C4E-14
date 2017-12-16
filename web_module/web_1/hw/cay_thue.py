from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    games = [
        {
        'name':'DOTA2',
        'link':'http://127.0.0.1:5000/dota2',
        'link_image':'https://pbs.twimg.com/profile_images/808475349671493632/nvi7WJf4.jpg'
        },
        {
        'name':'LOL',
        'link':'http://127.0.0.1:5000/lol',
        'link_image':'http://www.therendezvous.rocks/wp-content/uploads/2015/06/LolPic.jpg'
        },
        {
        'name':'CSGO',
        'link':'http://127.0.0.1:5000/csgo',
        'link_image':'https://pbs.twimg.com/profile_images/531603782690279426/M3dE27yJ_400x400.png'
        }
    ]

    return render_template('cay_thue.html', games=games)

if __name__ == '__main__':
  app.run(debug=True)

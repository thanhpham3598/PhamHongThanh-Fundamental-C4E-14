from flask import Flask, render_template, url_for, redirect
from mlab import mlab_connect
from models.information import *
app = Flask(__name__)

mlab_connect()


@app.route('/')
def index():
    return render_template('homepage.html', games=Game.objects())

@app.route('/admin')
def admin():
    return render_template('admin.html', games=Game.objects(), accounts=Account.objects())

@app.route('/delete/<acount_id>')
def delete(acount_id):
    del_id = Acount.objects().with_id(acount_id)
    if del_id is None:
        return 'Not found'
    else:
        del_id.delete()
        return redirect(url_for('admin'))

@app.route('/info/<game_id>')
def info(game_id):
    game = Game.objects().with_id(game_id)
    return render_template('info.html', game= game)

if __name__ == '__main__':
  app.run(debug=True)

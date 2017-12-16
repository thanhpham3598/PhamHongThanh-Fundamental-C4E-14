from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def index():
    posts =[
        'Phạm Hồng Thanh',
        'Student',
        'Hust',
        'Games'
    ]
    return render_template('index.html', posts=posts)

@app.route('/school')
def re_di_rect():
    return redirect("http://techkids.vn")

if __name__ == '__main__':
  app.run(debug=True)

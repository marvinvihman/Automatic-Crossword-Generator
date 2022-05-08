from flask import Flask, render_template, url_for, Table, Col
import ristsõna as rs


app = Flask(__name__)


@app.route('/')
def kodu():
    return render_template('kodu.html')


@app.route("/leheküljest")
def leheküljest():
    return render_template('leheküljest.html')


@app.route("/ristsõna")
def ristsõna():

    return render_template('ristsõna.html', sõnastik=rs.lahendus, laud=rs.LAUD)


if __name__ == '__main__':
    app.run()

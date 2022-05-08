from flask import Flask, render_template, url_for
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
    sonastik, laud = rs.toota()
    return render_template('ristsõna.html', sõnastik=sonastik, laud=laud)


if __name__ == '__main__':
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(extra_files=rs)

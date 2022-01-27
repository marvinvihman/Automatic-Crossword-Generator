from flask import Flask, render_template, url_for
import andmestikuEeltöötleja as ae
import estnltk
from estnltk.wordnet import Wordnet

andmestikuEeltöötleja = ae.AndmestikuEeltöötleja("https://www.cl.ut.ee/ressursid/sagedused/tabel1.txt")
sagedus_sõnastik = andmestikuEeltöötleja.looDataFrame()
andmestikuEeltöötleja.sorteeriDataFrame(sagedus_sõnastik)

app = Flask(__name__)

@app.route('/')
def kodu():
    return render_template('kodu.html')

@app.route("/leheküljest")
def leheküljest():
    return render_template('leheküljest.html')


@app.route("/ristsõna")
def ristsõna():
    return render_template('ristsõna.html')

if __name__ == '__main__':
    app.run()

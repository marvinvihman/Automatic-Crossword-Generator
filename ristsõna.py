import andmestikuEeltöötleja as ae
import estnltk
from estnltk.wordnet import Wordnet

andmestikuEeltöötleja = ae.AndmestikuEeltöötleja("https://www.cl.ut.ee/ressursid/sagedused/tabel1.txt")
sagedus_sõnastik = andmestikuEeltöötleja.looDataFrame()
andmestikuEeltöötleja.sorteeriDataFrame(sagedus_sõnastik)

top100Sõna = sagedus_sõnastik[:100]

print(top100Sõna)

lahendus = []
lahendamisel = []


import andmestikuEeltöötleja as ae
import random
#import estnltk
#from estnltk.wordnet import Wordnet

LAUA_SUURUSED = [15, 21, 23, 25]
SUURUS = 0
LAUD = [['-' for i in range(LAUA_SUURUSED[SUURUS])] for j in range(LAUA_SUURUSED[SUURUS])]

def prooviHorisontaali(sõna):
    global LAUD
    lauaKoopia = LAUD.copy()
    sõnaIdx = 0
    for i in range(len(LAUD)):
        for j in range(len(LAUD[i])):
            if LAUD[i][j] == '-':
                if LAUD[i][j-1] != '-' and sõnaIdx == 0:
                    continue
                # Kui terve sõna saab lisatud, jäta meelde sõna ning algus/lõpp koordinaadid
                if sõnaIdx == len(sõna):
                    lahendus.append([sõna, (i, j-len(sõna)), (i, j)])
                    break
                # Kontrollib, et sõna ruudustikust välja ei läheks
                if (len(LAUD[i]) - j - (len(sõna) - sõnaIdx)) >= 0:
                    #print(len(LAUD[i]), j, len(sõna) - sõnaIdx)
                    lauaKoopia[i][j] = sõna[sõnaIdx]
                    sõnaIdx += 1

    LAUD = lauaKoopia

def prooviVertikaali(sõna):
    global LAUD
    lauaKoopia = LAUD.copy()
    sõnaIdx = 0
    for i in range(len(LAUD)):
        for j in range(len(LAUD[i])):
            if LAUD[j][i] == '-':
                if LAUD[j-1][i] != '-' and sõnaIdx == 0:
                    continue
                # Kui terve sõna saab lisatud, jäta meelde sõna ning algus/lõpp koordinaadid
                if sõnaIdx == len(sõna):
                    lahendus.append([sõna, (j, i-len(sõna)), (j, i)])
                    break
                # Kontrollib, et sõna ruudustikust välja ei läheks
                if (len(LAUD[i]) - j - (len(sõna) - sõnaIdx)) >= 0:
                    #print(len(LAUD[i]), j, len(sõna) - sõnaIdx)
                    lauaKoopia[j][i] = sõna[sõnaIdx]
                    sõnaIdx += 1

    LAUD = lauaKoopia

andmestikuEeltöötleja = ae.AndmestikuEeltöötleja("https://www.cl.ut.ee/ressursid/sagedused/tabel1.txt")
sagedus_sõnastik = andmestikuEeltöötleja.looDataFrame()
andmestikuEeltöötleja.sorteeriDataFrame(sagedus_sõnastik)

sõnad = sagedus_sõnastik[6000:7000]

lahendus = []

for i in range(10):
    sample = sõnad.sample()
    sõna = sample['sõna'].values[0]
    print(sõna, len(sõna))

    prooviVertikaali(sõna)

for i in LAUD:
    print(i)
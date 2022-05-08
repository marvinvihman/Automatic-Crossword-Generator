import andmestikuEeltöötleja as ae
import random
import re
from estnltk.wordnet import Wordnet

wd = Wordnet()

LAUA_SUURUSED = [15, 21, 23, 25]
SUURUS = 0
LAUD = [['.' for i in range(LAUA_SUURUSED[SUURUS])] for j in range(LAUA_SUURUSED[SUURUS])]

"""
Algoritm:
    1. Aseta sõna lauale horisontaalselt
    2. Kui mahub, aseta teine sõna samuti horisontaalselt
    3. Võta 0 rea ja 2n veeru algustäht, otsi hulgast sama algustähega, list.sample() ning aseta vertikaalselt.
    4. Korda 2. aga vertikaalselt
    5. 
      
"""


def leiaValikud(reg, sonastik):
    loendur = 0
    cutoff = 0
    cutoff_lisa = 0
    uuesti = False
    for i in range(len(reg)):
        if reg[i] == '.':
            loendur += 1
        else:
            loendur = 0

        if loendur > 1:
            cutoff = i
            break

    #print(r"^(" + reg[:cutoff] + "*?)")
    if reg[:cutoff] != '':
        valikud = []
        while not valikud:
            for val in sonastik:

                if re.search(r"^" + reg[:cutoff - cutoff_lisa] + "*?", val):
                    valikud.append(val)
            #print(reg[:cutoff - cutoff_lisa])
            cutoff_lisa += 1
            if len(reg) == cutoff_lisa:
                uuesti = True

            if uuesti:
                for val in sonastik:

                    if re.search(r"^" + reg[cutoff_lisa:cutoff] + "*?", val):
                        valikud.append(val)
                #print(reg[:cutoff - cutoff_lisa])
                cutoff_lisa += 1

        if len(reg) < len(min(valikud)):
            return []
        return valikud
    return []


def asetaLauale(sonastik, laud, asetatud):
    ridaIdx = 0
    veergIdx = 0
    loendur = 0

    # Asetab lauale horisontaalselt
    while loendur <= 20:
        #print(loendur)
        #print(ridaIdx, veergIdx)
        if ridaIdx >= len(laud):
            if loendur == 16:
                break
            else:
                ridaIdx = loendur
        rida = ''.join(laud[ridaIdx][veergIdx:])
        #print(rida)
        while len(rida) > 2:
            if ridaIdx <= len(laud) and veergIdx <= len(laud):
                rida = ''.join(laud[ridaIdx][veergIdx:])
            else:
                break

            valikud = leiaValikud(str(rida), sonastik)
            if not valikud:
                break

            sona = random.choice(valikud)
            while sona in asetatud and len(sona) <= len(rida):
                sona = random.choice(valikud)
            if len(sona) <= len(rida):
                for jrk, taht in enumerate(sona):
                    # Mõne puhul annab Errori list index out of range, seega vaja else plokis for-tsüklit
                    if jrk == 0:
                        if len(wd[sona]) > 1:
                            if wd[sona][0].definition is None:
                                asetatud[sona] = ((ridaIdx, veergIdx), '-', len(asetatud) + 1, 'wd[sona][0].definition')
                            else:
                                asetatud[sona] = ((ridaIdx, veergIdx), '-', len(asetatud) + 1, wd[sona][0].definition)
                        else:
                            for i in wd[sona]:
                                if i.definition is None:
                                    asetatud[sona] = ((ridaIdx, veergIdx), '-', len(asetatud) + 1, 'i.definition')
                                else:
                                    asetatud[sona] = ((ridaIdx, veergIdx), '-', len(asetatud) + 1, i.definition)

                    laud[ridaIdx][veergIdx] = taht
                    veergIdx += 1
                veergIdx += 1

        veergIdx = 0
        veerg = ''.join([i[veergIdx] for i in laud][ridaIdx:])
        while len(veerg) > 2:
            if ridaIdx <= len(laud) and veergIdx <= len(laud):
                veerg = ''.join([i[veergIdx] for i in laud][ridaIdx:])
            else:
                break
            valikud = leiaValikud(str(veerg), sonastik)

            if not valikud:
                break

            sona = random.choice(valikud)
            while sona in asetatud:
                sona = random.choice(valikud)
            if len(sona) <= len(veerg):
                for jrk, taht in enumerate(sona):
                    # Mõne puhul annab Errori list index out of range, seega vaja else plokis for-tsüklit
                    if jrk == 0:
                        if len(wd[sona]) > 1:
                            if wd[sona][0].definition is None:
                                asetatud[sona] = ((ridaIdx, veergIdx), '|', len(asetatud) + 1, 'wd[sona][0].definition')
                            else:
                                asetatud[sona] = ((ridaIdx, veergIdx), '|', len(asetatud) + 1, wd[sona][0].definition)
                        else:
                            for i in wd[sona]:
                                if i.definition is None:
                                    asetatud[sona] = ((ridaIdx, veergIdx), '|', len(asetatud) + 1, 'i.definition')
                                else:
                                    asetatud[sona] = ((ridaIdx, veergIdx), '|', len(asetatud) + 1, i.definition)


                    laud[ridaIdx][veergIdx] = taht
                    ridaIdx += 1
                ridaIdx += 1

        loendur += 2
        ridaIdx += 2

    loendur = 0
    ridaIdx = 0
    veergIdx = 2
    # Asetab lauale vertikaalselt
    while loendur <= 20:
        if veergIdx >= len(laud):
            if loendur == 16:
                break
            else:
                ridaIdx = loendur
                veergIdx -= 2

        veerg = ''.join([i[veergIdx] for i in laud][ridaIdx:])

        while len(veerg) > 2:
            if ridaIdx <= len(laud) and veergIdx <= len(laud):
                veerg = ''.join([i[veergIdx] for i in laud][ridaIdx:])
            else:
                break
            valikud = leiaValikud(str(veerg), sonastik)

            if not valikud:
                break

            sona = random.choice(valikud)
            while sona in asetatud:
                sona = random.choice(valikud)
            if len(sona) <= len(veerg):
                for jrk, taht in enumerate(sona):
                    if jrk == 0:
                        if len(wd[sona]) > 1:
                            if wd[sona][0].definition is None:
                                asetatud[sona] = ((ridaIdx, veergIdx), '|', len(asetatud) + 1, 'wd[sona][0].definition')
                            else:
                                asetatud[sona] = ((ridaIdx, veergIdx), '|', len(asetatud)+1, wd[sona][0].definition)
                        else:
                            for i in wd[sona]:
                                if i.definition is None:
                                    asetatud[sona] = ((ridaIdx, veergIdx), '|', len(asetatud)+1, 'i.definition')
                                else:
                                    asetatud[sona] = ((ridaIdx, veergIdx), '|', len(asetatud) + 1, i.definition)

                    laud[ridaIdx][veergIdx] = taht
                    ridaIdx += 1
                ridaIdx += 1

        loendur += 2
        veergIdx += 2
        ridaIdx = 0

andmestikuEeltöötleja = ae.AndmestikuEeltöötleja("https://www.cl.ut.ee/ressursid/sagedused/tabel1.txt")
sagedus_sõnastik = andmestikuEeltöötleja.looDataFrame()
andmestikuEeltöötleja.sorteeriDataFrame(sagedus_sõnastik)

sagedus_sõnastik = sagedus_sõnastik.dropna()
sonad = sagedus_sõnastik['sõna'].tolist()

lahendus = dict()
asetaLauale(sonad, LAUD, lahendus)

for i in LAUD:
    print(i)

print(lahendus)
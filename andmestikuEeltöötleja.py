import pandas as pd

class AndmestikuEeltöötleja:

    def __init__(self, tee_failini):
        self.url = tee_failini
        self.sõnaliigid = {
            "S": "nimisõna",
            "A": "omadussõna",
            "V": "tegusõna",
            "P": "asesõna",
            "D": "muutumatu"}

    def looDataFrame(self):
        dataFrame = pd.read_csv(self.url, delimiter="\t")
        # Veerud 'ilu' ja 'aja' ei ole vajalikud, kuna tunneme huvi kogu sagedus arvust
        dataFrame.drop('ilu', axis=1, inplace=True)
        dataFrame.drop('aja', axis=1, inplace=True)

        return dataFrame

    def sorteeriDataFrame(self, dataFrame):
        dataFrame.sort_values(by="kokku", ascending=False, inplace=True)

        return dataFrame

    def tagastaLühendiNimetus(self, lühend):
        if '/' in lühend:
            lühendid = lühend.split('/')

            return [self.sõnaliigid[i] if i in self.sõnaliigid else 'Tundmatu lühend' for i in lühendid]
        else:
            try:

                return self.sõnaliigid[lühend]
            except:

                return 'Tundmatu lühend'

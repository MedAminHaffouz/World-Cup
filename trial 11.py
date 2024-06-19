from random import randint
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

Euro = ['Albania', 'Austria', 'Belgium', 'Bosnia & Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'England', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Montenegro', 'Netherlands', 'North Macedonia', 'Northern Ireland', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Scotland', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'Wales']

Afro = ['Algeria', 'Angola', 'Benin', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'Comoros', 'Congo Rep.', 'DRC', 'Egypt', 'Equatorial Guinea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Morocco', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']

SA = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']

NA = ['Bahamas', 'Barbados', 'Belize', 'Bermuda', 'Canada', 'Costa Rica', 'Cuba', 'Curaçao', 'Dominica', 'Dominican Republic', 'El Salvador', 'French Guiana', 'Grenada', 'Guadeloupe', 'Guatemala', 'Guyana', 'Haiti', 'Haiti', 'Honduras', 'Jamaica', 'Martinique', 'Mexico', 'Nicaragua', 'Panama', 'Saint Lucia', 'Snt Vincent & Gren.', 'Suriname', 'Trinidad and Tobago', 'USA']

Asia = ['Australia', 'Bahrain', 'Brunei', 'Cambodia', 'China', 'India', 'Indonesia', 'Iran', 'Iraq', 'Japan', 'Jordan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar (Burma)', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkmenistan', 'UAE', 'Uzbekistan', 'Vietnam', 'Yemen']

Oceania = ['Fiji', 'New Zealand', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Vanuatu']


def find(Country):
    if Country in Euro:
        return 1
    elif Country in Afro:
        return 2
    elif Country in SA:
        return 3
    elif Country in NA:
        return 4
    elif Country in Asia:
        return 5
    elif Country in Oceania:
        return 6


def check(T):
    EuroNum, AfroNum, AsiaNum, SANum, NANum, OceaniaNum = 0, 0, 0, 0, 0, 0
    for i in range(4):
        A = find(T[i])
        match A:
            case 1:
                EuroNum += 1
            case 2:
                AfroNum += 1
            case 3:
                SANum += 1
            case 4:
                NANum += 1
            case 5:
                AsiaNum += 1
            case 6:
                OceaniaNum += 1
    return EuroNum <= 2 and AfroNum <= 1 and AsiaNum <= 1 and NANum <= 1 and SANum <= 1


def main():
    Test=False
    while not(Test):
        try:
            Countries = Euro + Afro + SA + NA + Asia + Oceania
            Host = Countries[randint(0, len(Countries) - 1)]
            A = find(Host)

            QEuro = []
            while len(QEuro) < 16:
                x = randint(0, len(Euro) - 1)
                while Euro[x] in QEuro or Euro[x] == Host:
                    x = randint(0, len(Euro) - 1)
                (QEuro).append(Euro[x])

            MaxAfro,iMaxAfro=9,9
            MaxAsia,iMaxAsia=8,8
            MaxNA,iMaxNA=6,6
            MaxSA,iMaxSA=6,6
            MaxOce,iMaxOce=1,1


            Choice1=randint(1,5)
            match Choice1:
                case 1:
                    MaxAfro+=1
                case 2:
                    MaxAsia+=1
                case 3:
                    MaxNA+=1
                case 4:
                    MaxSA+=1
                case 5:
                    MaxOce+=1

            Choice2=randint(1,5)
            Test=False
            while not(Test):
                Test=True
                match Choice2:
                    case 1:
                        if MaxAfro==iMaxAfro:
                            MaxAfro+=1
                        else :
                            Test=False
                    case 2:
                        if MaxAsia==iMaxAsia:
                            MaxAsia+=1
                        else :
                            Test=False
                    case 3:
                        if MaxNA==iMaxNA:
                            MaxNA+=1
                        else :
                            Test=False
                    case 4:
                        if MaxSA==iMaxSA:
                            MaxSA+=1
                        else :
                            Test=False
                    case 5:
                        if MaxOce==iMaxOce:
                            MaxOce+=1
                        else :
                            Test=False

            QAfro = []
            while len(QAfro) < MaxAfro:
                x = randint(0, len(Afro) - 1)
                while Afro[x] in QAfro or Afro[x] == Host:
                    x = randint(0, len(Afro) - 1)
                (QAfro).append(Afro[x])

            QOceania = []
            while len(QOceania) < MaxOce:
                x = randint(0, len(Oceania) - 1)
                while Oceania[x] in QOceania or Oceania[x] == Host:
                    x = randint(0, len(Oceania) - 1)
                (QOceania).append(Oceania[x])


            QSA = []
            while len(QSA) < MaxSA:
                x = randint(0, len(SA) - 1)
                while SA[x] in QSA or SA[x] == Host:
                    x = randint(0, len(SA) - 1)
                (QSA).append(SA[x])


            QNA = []
            while len(QNA) < MaxNA:
                x = randint(0, len(NA) - 1)
                while NA[x] in QNA or NA[x] == Host:
                    x = randint(0, len(NA) - 1)
                (QNA).append(NA[x])

            QAsia = []
            while len(QAsia) < MaxAsia:
                x = randint(0, len(Asia) - 1)
                while Asia[x] in QAsia or Asia[x] == Host:
                    x = randint(0, len(Asia) - 1)
                (QAsia).append(Asia[x])

            QCountries = []
            QCountries.append(Host)
            QCountries += QEuro
            QCountries += QAfro
            QCountries += QNA
            QCountries += QSA
            QCountries += QAsia

            End = False
            P = []
            P.append(Host)
            while len(P) < 48:
                a = randint(1, 47)
                while QCountries[a] in P:
                    a = randint(1, 47)
                P.append(QCountries[a])

            P1 = P[0:12]
            P2 = P[12:24]
            P3 = P[24:36]
            P4 = P[36:48]

            G = []
            G.append(Host)
            A2 = randint(0, 11)
            G.append(P2[A2])
            A3 = randint(0, 11)
            G.append(P3[A3])
            A4 = randint(0, 11)
            G.append(P4[A4])
            while len(G) < 48:
                A1 = randint(0, 11)
                while P1[A1] in G:
                    A1 = randint(0, 11)
                G.append(P1[A1])
                A2 = randint(0, 7)
                while P2[A2] in G:
                    A2 = randint(0, 11)
                G.append(P2[A2])
                A3 = randint(0, 7)
                while P3[A3] in G:
                    A3 = randint(0,11)
                G.append(P3[A3])
                A4 = randint(0, 7)
                while P4[A4] in G:
                    A4 = randint(0, 11)
                G.append(P4[A4])

            global G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G11,G12

            G1 = G[0:4]
            G2 = G[4:8]
            G3 = G[8:12]
            G4 = G[12:16]
            G5 = G[16:20]
            G6 = G[20:24]
            G7 = G[24:28]
            G8 = G[28:32]
            G9=G[32:36]
            G10=G[36:40]
            G11=G[40:44]
            G12=G[44:48]


            Test = (check(G1) and check(G2) and check(G3) and check(G4) and check(G4) and check(G5) and check(G6) and check(G7) and check(G8)) and check(G9) and check(G10) and check(G11) and check(G12)


            AffG1 = G1[0] + "\n"
            for i in range(1, 4):
                AffG1 += G1[i] + "\n"
            AffG2 = G2[0] + "\n"
            for i in range(1, 4):
                AffG2 += G2[i] + "\n"
            AffG3 = G3[0] + "\n"
            for i in range(1, 4):
                AffG3 += G3[i] + "\n"
            AffG4 = G4[0] + "\n"
            for i in range(1, 4):
                AffG4 += G4[i] + "\n"
            AffG5 = G5[0] + "\n"
            for i in range(1, 4):
                AffG5 += G5[i] + "\n"
            AffG6 = G6[0] + "\n"
            for i in range(1, 4):
                AffG6 += G6[i] + "\n"
            AffG7 = G7[0] + "\n"
            for i in range(1, 4):
                AffG7 += G7[i] + "\n"
            AffG8 = G8[0] + "\n"
            for i in range(1, 4):
                AffG8 += G8[i] + "\n"
            AffG9 = G9[0] + "\n"
            for i in range(1, 4):
                AffG9 += G9[i] + "\n"
            AffG10 = G10[0] + "\n"
            for i in range(1, 4):
                AffG10 += G10[i] + "\n"
            AffG11 = G11[0] + "\n"
            for i in range(1, 4):
                AffG11 += G11[i] + "\n"
            AffG12 = G12[0] + "\n"
            for i in range(1, 4):
                AffG12 += G12[i] + "\n"
        
            G1show.insert(tk.END, AffG1)
            G2show.insert(tk.END, AffG2)
            G3show.insert(tk.END, AffG3)
            G4show.insert(tk.END, AffG4)
            G5show.insert(tk.END, AffG5)
            G6show.insert(tk.END, AffG6)
            G7show.insert(tk.END, AffG7)
            G8show.insert(tk.END, AffG8)
            G9show.insert(tk.END, AffG9)
            G10show.insert(tk.END, AffG10)
            G11show.insert(tk.END, AffG11)
            G12show.insert(tk.END, AffG12)

            generate.grid_forget()
            delete.grid(row=8, column=1, columnspan=4, pady=5)
            matches.grid(row=9, column=1, columnspan=4, pady=5)

        except Exception as e:
            main()


def execute():
    if __name__ == "__main__":
        main()


def treat(G, Result, i, j, Score, GS, GC, GT):
    Teamigoals = int(Result[:Result.find("-")])
    Teamjgoals = int(Result[Result.find("-") + 1:])
    if Teamigoals > Teamjgoals:
        Score[i] = Score[i] + 3
    elif Teamjgoals > Teamigoals:
        Score[j] = Score[j] + 3
    elif Teamigoals == Teamjgoals:
        Score[i] = Score[i] + 1
        Score[j] = Score[j] + 1
    GS[i] += Teamigoals
    GS[j] += Teamjgoals
    GC[i] -= Teamjgoals
    GC[j] -= Teamigoals
    GT[i] = GS[i] + GC[i]
    GT[j] = GS[j] + GC[j]


def sort(G, Score, GS, GC, GT):
    Test = False
    while not(Test):
        Test = True
        for x in range(1, 4):
            if Score[x - 1] < Score[x]:
                Score[x - 1], Score[x] = Score[x], Score[x - 1]
                G[x - 1], G[x] = G[x], G[x - 1]
                GS[x - 1], GS[x] = GS[x], GS[x - 1]
                GC[x - 1], GC[x] = GC[x], GC[x - 1]
                GT[x - 1], GT[x] = GT[x], GT[x - 1]
                Test = False
            elif Score[x - 1] == Score[x] and GT[x - 1] < GT[x]:
                Score[x - 1], Score[x] = Score[x], Score[x - 1]
                G[x - 1], G[x] = G[x], G[x - 1]
                GS[x - 1], GS[x] = GS[x], GS[x - 1]
                GC[x - 1], GC[x] = GC[x], GC[x - 1]
                GT[x - 1], GT[x] = GT[x], GT[x - 1]
                Test = False


def gotoround2():
    if match1entry.get() != "" and match2entry.get() != "" and match3entry.get() != "" and match4entry.get() != "" and match5entry.get() != "" and match6entry.get() != "" and match7entry.get() != "" and match8entry.get() != "" and match9entry.get() != "" and match10entry.get() != "" and match11entry.get() != "" and match12entry.get() != "" and match13entry.get() != "" and match14entry.get() != "" and match15entry.get() != "" and match16entry.get() != "" and match17entry.get() != "" and match18entry.get() != "" and match19entry.get() != "" and match20entry.get() != "" and match21entry.get() != "" and match22entry.get() != "" and match23entry.get() != "" and match24entry.get() != "" :
        Result = match1entry.get()
        treat(G1, Result, 0, 1, Score1, GS1, GC1, GT1)
        Result = match2entry.get()
        treat(G1, Result, 2, 3, Score1, GS1, GC1, GT1)
        Result = match3entry.get()
        treat(G2, Result, 0, 1, Score2, GS2, GC2, GT2)
        Result = match4entry.get()
        treat(G2, Result, 2, 3, Score2, GS2, GC2, GT2)
        Result = match5entry.get()
        treat(G3, Result, 0, 1, Score3, GS3, GC3, GT3)
        Result = match6entry.get()
        treat(G3, Result, 2, 3, Score3, GS3, GC3, GT3)
        Result = match7entry.get()
        treat(G4, Result, 0, 1, Score4, GS4, GC4, GT4)
        Result = match8entry.get()
        treat(G4, Result, 2, 3, Score4, GS4, GC4, GT4)
        Result = match9entry.get()
        treat(G5, Result, 0, 1, Score5, GS5, GC5, GT5)
        Result = match10entry.get()
        treat(G5, Result, 2, 3, Score5, GS5, GC5, GT5)
        Result = match11entry.get()
        treat(G6, Result, 0, 1, Score6, GS6, GC6, GT6)
        Result = match12entry.get()
        treat(G6, Result, 2, 3, Score6, GS6, GC6, GT6)
        Result = match13entry.get()
        treat(G7, Result, 0, 1, Score7, GS7, GC7, GT7)
        Result = match14entry.get()
        treat(G7, Result, 2, 3, Score7, GS7, GC7, GT7)
        Result = match15entry.get()
        treat(G8, Result, 0, 1, Score8, GS8, GC8, GT8)
        Result = match16entry.get()
        treat(G8, Result, 2, 3, Score8, GS8, GC8, GT8)
        Result = match17entry.get()
        treat(G9, Result, 0, 1, Score9, GS9, GC9, GT9)
        Result = match18entry.get()
        treat(G9, Result, 2, 3, Score9, GS9, GC9, GT9)
        Result = match19entry.get()
        treat(G10, Result, 0, 1, Score10, GS10, GC10, GT10)
        Result = match20entry.get()
        treat(G10, Result, 2, 3, Score10, GS10, GC10, GT10)
        Result = match21entry.get()
        treat(G11, Result, 0, 1, Score11, GS11, GC11, GT11)
        Result = match22entry.get()
        treat(G11, Result, 2, 3, Score11, GS11, GC11, GT11)
        Result = match23entry.get()
        treat(G12, Result, 0, 1, Score12, GS12, GC12, GT12)
        Result = match24entry.get()
        treat(G12, Result, 2, 3, Score12, GS12, GC12, GT12)



        match1entry.delete(0, tk.END)
        match2entry.delete(0, tk.END)
        match3entry.delete(0, tk.END)
        match4entry.delete(0, tk.END)
        match5entry.delete(0, tk.END)
        match6entry.delete(0, tk.END)
        match7entry.delete(0, tk.END)
        match8entry.delete(0, tk.END)
        match9entry.delete(0, tk.END)
        match10entry.delete(0, tk.END)
        match11entry.delete(0, tk.END)
        match12entry.delete(0, tk.END)
        match13entry.delete(0, tk.END)
        match14entry.delete(0, tk.END)
        match15entry.delete(0, tk.END)
        match16entry.delete(0, tk.END)
        match17entry.delete(0, tk.END)
        match18entry.delete(0, tk.END)
        match19entry.delete(0, tk.END)
        match20entry.delete(0, tk.END)
        match21entry.delete(0, tk.END)
        match22entry.delete(0, tk.END)
        match23entry.delete(0, tk.END)
        match24entry.delete(0, tk.END)

        match1.config(text=round2_matches[0])
        match2.config(text=round2_matches[1])
        match3.config(text=round2_matches[2])
        match4.config(text=round2_matches[3])
        match5.config(text=round2_matches[4])
        match6.config(text=round2_matches[5])
        match7.config(text=round2_matches[6])
        match8.config(text=round2_matches[7])
        match9.config(text=round2_matches[8])
        match10.config(text=round2_matches[9])
        match11.config(text=round2_matches[10])
        match12.config(text=round2_matches[11])
        match13.config(text=round2_matches[12])
        match14.config(text=round2_matches[13])
        match15.config(text=round2_matches[14])
        match16.config(text=round2_matches[15])
        match17.config(text=round2_matches[16])
        match18.config(text=round2_matches[17])
        match19.config(text=round2_matches[18])
        match20.config(text=round2_matches[19])
        match21.config(text=round2_matches[20])
        match22.config(text=round2_matches[21])
        match23.config(text=round2_matches[22])
        match24.config(text=round2_matches[23])
        roundtitle.config(text="Round 2")
        round2.grid_forget()
        round3.grid(row=9, column=4, padx=5)


def gotoround3():
    if match1entry.get() != "" and match2entry.get() != "" and match3entry.get() != "" and match4entry.get() != "" and match5entry.get() != "" and match6entry.get() != "" and match7entry.get() != "" and match8entry.get() != "" and match9entry.get() != "" and match10entry.get() != "" and match11entry.get() != "" and match12entry.get() != "" and match13entry.get() != "" and match14entry.get() != "" and match15entry.get() != "" and match16entry.get() != "" and match17entry.get() != "" and match18entry.get() != "" and match19entry.get() != "" and match20entry.get() != "" and match21entry.get() != "" and match22entry.get() != "" and match23entry.get() != "" and match24entry.get() != "" :
        Result = match1entry.get()
        treat(G1, Result, 0, 2, Score1, GS1, GC1, GT1)
        Result = match2entry.get()
        treat(G1, Result, 1, 3, Score1, GS1, GC1, GT1)
        Result = match3entry.get()
        treat(G2, Result, 0, 2, Score2, GS2, GC2, GT2)
        Result = match4entry.get()
        treat(G2, Result, 1, 3, Score2, GS2, GC2, GT2)
        Result = match5entry.get()
        treat(G3, Result, 0, 2, Score3, GS3, GC3, GT3)
        Result = match6entry.get()
        treat(G3, Result, 1, 3, Score3, GS3, GC3, GT3)
        Result = match7entry.get()
        treat(G4, Result, 0, 2, Score4, GS4, GC4, GT4)
        Result = match8entry.get()
        treat(G4, Result, 1, 3, Score4, GS4, GC4, GT4)
        Result = match9entry.get()
        treat(G5, Result, 0, 2, Score5, GS5, GC5, GT5)
        Result = match10entry.get()
        treat(G5, Result, 1, 3, Score5, GS5, GC5, GT5)
        Result = match11entry.get()
        treat(G6, Result, 0, 2, Score6, GS6, GC6, GT6)
        Result = match12entry.get()
        treat(G6, Result, 1, 3, Score6, GS6, GC6, GT6)
        Result = match13entry.get()
        treat(G7, Result, 0, 2, Score7, GS7, GC7, GT7)
        Result = match14entry.get()
        treat(G7, Result, 1, 3, Score7, GS7, GC7, GT7)
        Result = match15entry.get()
        treat(G8, Result, 0, 2, Score8, GS8, GC8, GT8)
        Result = match16entry.get()
        treat(G8, Result, 1, 3, Score8, GS8, GC8, GT8)
        Result = match17entry.get()
        treat(G9, Result, 0, 2, Score9, GS9, GC9, GT9)
        Result = match18entry.get()
        treat(G9, Result, 1, 3, Score9, GS9, GC9, GT9)
        Result = match19entry.get()
        treat(G10, Result, 0, 2, Score10, GS10, GC10, GT10)
        Result = match20entry.get()
        treat(G10, Result, 1, 3, Score10, GS10, GC10, GT10)
        Result = match21entry.get()
        treat(G11, Result, 0, 2, Score11, GS11, GC11, GT11)
        Result = match22entry.get()
        treat(G11, Result, 1, 3, Score11, GS11, GC11, GT11)
        Result = match23entry.get()
        treat(G12, Result, 0, 2, Score12, GS12, GC12, GT12)
        Result = match24entry.get()
        treat(G12, Result, 1, 3, Score12, GS12, GC12, GT12)
        


        match1entry.delete(0, tk.END)
        match2entry.delete(0, tk.END)
        match3entry.delete(0, tk.END)
        match4entry.delete(0, tk.END)
        match5entry.delete(0, tk.END)
        match6entry.delete(0, tk.END)
        match7entry.delete(0, tk.END)
        match8entry.delete(0, tk.END)
        match9entry.delete(0, tk.END)
        match10entry.delete(0, tk.END)
        match11entry.delete(0, tk.END)
        match12entry.delete(0, tk.END)
        match13entry.delete(0, tk.END)
        match14entry.delete(0, tk.END)
        match15entry.delete(0, tk.END)
        match16entry.delete(0, tk.END)
        match17entry.delete(0, tk.END)
        match18entry.delete(0, tk.END)
        match19entry.delete(0, tk.END)
        match20entry.delete(0, tk.END)
        match21entry.delete(0, tk.END)
        match22entry.delete(0, tk.END)
        match23entry.delete(0, tk.END)
        match24entry.delete(0, tk.END)


        match1.config(text=round3_matches[0])
        match2.config(text=round3_matches[1])
        match3.config(text=round3_matches[2])
        match4.config(text=round3_matches[3])
        match5.config(text=round3_matches[4])
        match6.config(text=round3_matches[5])
        match7.config(text=round3_matches[6])
        match8.config(text=round3_matches[7])
        match9.config(text=round3_matches[8])
        match10.config(text=round3_matches[9])
        match11.config(text=round3_matches[10])
        match12.config(text=round3_matches[11])
        match13.config(text=round3_matches[12])
        match14.config(text=round3_matches[13])
        match15.config(text=round3_matches[14])
        match16.config(text=round3_matches[15])
        match17.config(text=round3_matches[16])
        match18.config(text=round3_matches[17])
        match19.config(text=round3_matches[18])
        match20.config(text=round3_matches[19])
        match21.config(text=round3_matches[20])
        match22.config(text=round3_matches[21])
        match23.config(text=round3_matches[22])
        match24.config(text=round3_matches[23])



        roundtitle.config(text="Round 3")
        round3.grid_forget()
        finalbutton.grid(row=9, column=4, padx=5)


def filltable(table, G, Score, GS, GC, GT):
    for i in range(4):
        table.insert('', 'end', text=f'Item {i}', values=(i + 1, G[i], Score[i], GS[i], GC[i], GT[i]))


def gotofinals():
    if match1entry.get() != "" and match2entry.get() != "" and match3entry.get() != "" and match4entry.get() != "" and match5entry.get() != "" and match6entry.get() != "" and match7entry.get() != "" and match8entry.get() != "" and match9entry.get() != "" and match10entry.get() != "" and match11entry.get() != "" and match12entry.get() != "" and match13entry.get() != "" and match14entry.get() != "" and match15entry.get() != "" and match16entry.get() != "" and match17entry.get() != "" and match18entry.get() != "" and match19entry.get() != "" and match20entry.get() != "" and match21entry.get() != "" and match22entry.get() != "" and match23entry.get() != "" and match24entry.get() != "" :
        Result = match1entry.get()
        treat(G1, Result, 0, 3, Score1, GS1, GC1, GT1)
        Result = match2entry.get()
        treat(G1, Result, 1, 2, Score1, GS1, GC1, GT1)
        Result = match3entry.get()
        treat(G2, Result, 0, 3, Score2, GS2, GC2, GT2)
        Result = match4entry.get()
        treat(G2, Result, 1, 2, Score2, GS2, GC2, GT2)
        Result = match5entry.get()
        treat(G3, Result, 0, 3, Score3, GS3, GC3, GT3)
        Result = match6entry.get()
        treat(G3, Result, 1, 2, Score3, GS3, GC3, GT3)
        Result = match7entry.get()
        treat(G4, Result, 0, 3, Score4, GS4, GC4, GT4)
        Result = match8entry.get()
        treat(G4, Result, 1, 2, Score4, GS4, GC4, GT4)
        Result = match9entry.get()
        treat(G5, Result, 0, 3, Score5, GS5, GC5, GT5)
        Result = match10entry.get()
        treat(G5, Result, 1, 2, Score5, GS5, GC5, GT5)
        Result = match11entry.get()
        treat(G6, Result, 0, 3, Score6, GS6, GC6, GT6)
        Result = match12entry.get()
        treat(G6, Result, 1, 2, Score6, GS6, GC6, GT6)
        Result = match13entry.get()
        treat(G7, Result, 0, 3, Score7, GS7, GC7, GT7)
        Result = match14entry.get()
        treat(G7, Result, 1, 2, Score7, GS7, GC7, GT7)
        Result = match15entry.get()
        treat(G8, Result, 0, 3, Score8, GS8, GC8, GT8)
        Result = match16entry.get()
        treat(G8, Result, 1, 2, Score8, GS8, GC8, GT8)
        Result = match17entry.get()
        treat(G9, Result, 0, 3, Score9, GS9, GC9, GT9)
        Result = match18entry.get()
        treat(G9, Result, 1, 2, Score9, GS9, GC9, GT9)
        Result = match19entry.get()
        treat(G10, Result, 0, 3, Score10, GS10, GC10, GT10)
        Result = match20entry.get()
        treat(G10, Result, 1, 2, Score10, GS10, GC10, GT10)
        Result = match21entry.get()
        treat(G10, Result, 0, 3, Score7, GS7, GC7, GT7)
        Result = match14entry.get()
        treat(G7, Result, 1, 2, Score7, GS7, GC7, GT7)
        Result = match15entry.get()
        treat(G8, Result, 0, 3, Score8, GS8, GC8, GT8)
        Result = match16entry.get()
        treat(G8, Result, 1, 2, Score8, GS8, GC8, GT8)



        match1entry.grid_forget()
        match2entry.grid_forget()
        match3entry.grid_forget()
        match4entry.grid_forget()
        match5entry.grid_forget()
        match6entry.grid_forget()
        match7entry.grid_forget()
        match8entry.grid_forget()
        match9entry.grid_forget()
        match10entry.grid_forget()
        match11entry.grid_forget()
        match12entry.grid_forget()
        match13entry.grid_forget()
        match14entry.grid_forget()
        match15entry.grid_forget()
        match16entry.grid_forget()
        match1.grid_forget()
        match2.grid_forget()
        match3.grid_forget()
        match4.grid_forget()
        match5.grid_forget()
        match6.grid_forget()
        match7.grid_forget()
        match8.grid_forget()
        match9.grid_forget()
        match10.grid_forget()
        match11.grid_forget()
        match12.grid_forget()
        match13.grid_forget()
        match14.grid_forget()
        match15.grid_forget()
        match16.grid_forget()
        roundtitle.config(text="Finals")
        round3.grid_forget()
        finalbutton.grid_forget()
        G1name.grid_forget()
        G2name.grid_forget()
        G3name.grid_forget()
        G4name.grid_forget()
        G5name.grid_forget()
        G6name.grid_forget()
        G7name.grid_forget()
        G8name.grid_forget()
        sort(G1, Score1, GS1, GC1, GT1)
        sort(G2, Score2, GS2, GC2, GT2)
        sort(G3, Score3, GS3, GC3, GT3)
        sort(G4, Score4, GS4, GC4, GT4)
        sort(G5, Score5, GS5, GC5, GT5)
        sort(G6, Score6, GS6, GC6, GT6)
        sort(G7, Score7, GS7, GC7, GT7)
        sort(G8, Score8, GS8, GC8, GT8)

        global table1, table2, table3, table4, table5, table6, table7, table8

        table1 = ttk.Treeview(scheduleshow, height=5, columns=(
            "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
        table1.heading('#1', text="Rank")
        table1.heading('#2', text="Country")
        table1.heading('#3', text="Score")
        table1.heading('#4', text="GS")
        table1.heading('#5', text="GC")
        table1.heading('#6', text="GT")
        table1.column('#1', width=30)
        table1.column('#2', width=70)
        table1.column('#3', width=30)
        table1.column('#4', width=30)
        table1.column('#5', width=30)
        table1.column('#6', width=30)

        filltable(table1, G1, Score1, GS1, GC1, GT1)

        G1name.grid(row=2, column=1)
        table1.grid(row=3, column=1)

        table2 = ttk.Treeview(scheduleshow, height=5, columns=(
            "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
        table2.heading('#1', text="Rank")
        table2.heading('#2', text="Country")
        table2.heading('#3', text="Score")
        table2.heading('#4', text="GS")
        table2.heading('#5', text="GC")
        table2.heading('#6', text="GT")
        table2.column('#1', width=30)
        table2.column('#2', width=70)
        table2.column('#3', width=30)
        table2.column('#4', width=30)
        table2.column('#5', width=30)
        table2.column('#6', width=30)

        filltable(table2, G2, Score2, GS2, GC2, GT2)

        G2name.grid(row=2, column=2)
        table2.grid(row=3, column=2)

        table3 = ttk.Treeview(scheduleshow, height=5, columns=(
            "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
        table3.heading('#1', text="Rank")
        table3.heading('#2', text="Country")
        table3.heading('#3', text="Score")
        table3.heading('#4', text="GS")
        table3.heading('#5', text="GC")
        table3.heading('#6', text="GT")
        table3.column('#1', width=30)
        table3.column('#2', width=70)
        table3.column('#3', width=30)
        table3.column('#4', width=30)
        table3.column('#5', width=30)
        table3.column('#6', width=30)

        filltable(table3, G3, Score3, GS3, GC3, GT3)

        G3name.grid(row=2, column=3)
        table3.grid(row=3, column=3)

        table4 = ttk.Treeview(scheduleshow, height=5, columns=(
            "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
        table4.heading('#1', text="Rank")
        table4.heading('#2', text="Country")
        table4.heading('#3', text="Score")
        table4.heading('#4', text="GS")
        table4.heading('#5', text="GC")
        table4.heading('#6', text="GT")
        table4.column('#1', width=30)
        table4.column('#2', width=70)
        table4.column('#3', width=30)
        table4.column('#4', width=30)
        table4.column('#5', width=30)
        table4.column('#6', width=30)

        filltable(table4, G4, Score4, GS4, GC4, GT4)

        G4name.grid(row=2, column=4)
        table4.grid(row=3, column=4)

        table5 = ttk.Treeview(scheduleshow, height=5, columns=(
            "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
        table5.heading('#1', text="Rank")
        table5.heading('#2', text="Country")
        table5.heading('#3', text="Score")
        table5.heading('#4', text="GS")
        table5.heading('#5', text="GC")
        table5.heading('#6', text="GT")
        table5.column('#1', width=30)
        table5.column('#2', width=70)
        table5.column('#3', width=30)
        table5.column('#4', width=30)
        table5.column('#5', width=30)
        table5.column('#6', width=30)

        filltable(table5, G5, Score5, GS5, GC5, GT5)

        G5name.grid(row=4, column=1)
        table5.grid(row=5, column=1)

        table6 = ttk.Treeview(scheduleshow, height=5, columns=(
            "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
        table6.heading('#1', text="Rank")
        table6.heading('#2', text="Country")
        table6.heading('#3', text="Score")
        table6.heading('#4', text="GS")
        table6.heading('#5', text="GC")
        table6.heading('#6', text="GT")
        table6.column('#1', width=30)
        table6.column('#2', width=70)
        table6.column('#3', width=30)
        table6.column('#4', width=30)
        table6.column('#5', width=30)
        table6.column('#6', width=30)

        filltable(table6, G6, Score6, GS6, GC6, GT6)

        G6name.grid(row=4, column=2)
        table6.grid(row=5, column=2)

        table7 = ttk.Treeview(scheduleshow, height=5, columns=(
            "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
        table7.heading('#1', text="Rank")
        table7.heading('#2', text="Country")
        table7.heading('#3', text="Score")
        table7.heading('#4', text="GS")
        table7.heading('#5', text="GC")
        table7.heading('#6', text="GT")
        table7.column('#1', width=30)
        table7.column('#2', width=70)
        table7.column('#3', width=30)
        table7.column('#4', width=30)
        table7.column('#5', width=30)
        table7.column('#6', width=30)

        filltable(table7, G7, Score7, GC7, GC7, GT7)

        G7name.grid(row=4, column=3)
        table7.grid(row=5, column=3)

        table8 = ttk.Treeview(scheduleshow, height=5, columns=(
            "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
        table8.heading('#1', text="Rank")
        table8.heading('#2', text="Country")
        table8.heading('#3', text="Score")
        table8.heading('#4', text="GS")
        table8.heading('#5', text="GC")
        table8.heading('#6', text="GT")
        table8.column('#1', width=30)
        table8.column('#2', width=70)
        table8.column('#3', width=30)
        table8.column('#4', width=30)
        table8.column('#5', width=30)
        table8.column('#6', width=30)

        filltable(table8, G8, Score8, GS8, GC8, GT8)

        G8name.grid(row=4, column=4)
        table8.grid(row=5, column=4)

        round16.grid(row=6, column=1, columnspan=4)

        global Qround16

        Qround16 = [G1[0], G2[1], G3[0], G4[1], G5[0], G6[1], G7[0],
                    G8[1], G1[1], G2[0], G3[1], G4[0], G5[1], G6[0], G7[1], G8[0]]

def gotoround32():
    print("32")

def gotoround16():
    global Test,tableroot
    Test= True
    tableroot = tk.Toplevel()
    tableroot.config(bg="green")
    tableroot.title("Groups stage tables")

    G1_name = tk.Label(tableroot, text="G1")
    G2_name = tk.Label(tableroot, text="G2")
    G3_name = tk.Label(tableroot, text="G3")
    G4_name = tk.Label(tableroot, text="G4")
    G5_name = tk.Label(tableroot, text="G5")
    G6_name = tk.Label(tableroot, text="G6")
    G7_name = tk.Label(tableroot, text="G7")
    G8_name = tk.Label(tableroot, text="G8")

    table_1 = ttk.Treeview(tableroot, height=5, columns=(
        "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
    table_1.heading('#1', text="Rank")
    table_1.heading('#2', text="Country")
    table_1.heading('#3', text="Score")
    table_1.heading('#4', text="GS")
    table_1.heading('#5', text="GC")
    table_1.heading('#6', text="GT")
    table_1.column('#1', width=30)
    table_1.column('#2', width=70)
    table_1.column('#3', width=30)
    table_1.column('#4', width=30)
    table_1.column('#5', width=30)
    table_1.column('#6', width=30)

    filltable(table_1, G1, Score1, GS1, GC1, GT1)

    G1_name.grid(row=2, column=1)
    table_1.grid(row=3, column=1)

    table_2 = ttk.Treeview(tableroot, height=5, columns=(
        "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
    table_2.heading('#1', text="Rank")
    table_2.heading('#2', text="Country")
    table_2.heading('#3', text="Score")
    table_2.heading('#4', text="GS")
    table_2.heading('#5', text="GC")
    table_2.heading('#6', text="GT")
    table_2.column('#1', width=30)
    table_2.column('#2', width=70)
    table_2.column('#3', width=30)
    table_2.column('#4', width=30)
    table_2.column('#5', width=30)
    table_2.column('#6', width=30)

    filltable(table_2, G2, Score2, GS2, GC2, GT2)

    G2_name.grid(row=2, column=2)
    table_2.grid(row=3, column=2)

    table_3 = ttk.Treeview(tableroot, height=5, columns=(
        "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
    table_3.heading('#1', text="Rank")
    table_3.heading('#2', text="Country")
    table_3.heading('#3', text="Score")
    table_3.heading('#4', text="GS")
    table_3.heading('#5', text="GC")
    table_3.heading('#6', text="GT")
    table_3.column('#1', width=30)
    table_3.column('#2', width=70)
    table_3.column('#3', width=30)
    table_3.column('#4', width=30)
    table_3.column('#5', width=30)
    table_3.column('#6', width=30)

    filltable(table_3, G3, Score3, GS3, GC3, GT3)

    G3_name.grid(row=2, column=3)
    table_3.grid(row=3, column=3)

    table_4 = ttk.Treeview(tableroot, height=5, columns=(
        "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
    table_4.heading('#1', text="Rank")
    table_4.heading('#2', text="Country")
    table_4.heading('#3', text="Score")
    table_4.heading('#4', text="GS")
    table_4.heading('#5', text="GC")
    table_4.heading('#6', text="GT")
    table_4.column('#1', width=30)
    table_4.column('#2', width=70)
    table_4.column('#3', width=30)
    table_4.column('#4', width=30)
    table_4.column('#5', width=30)
    table_4.column('#6', width=30)

    filltable(table_4, G4, Score4, GS4, GC4, GT4)

    G4_name.grid(row=2, column=4)
    table_4.grid(row=3, column=4)

    table_5 = ttk.Treeview(tableroot, height=5, columns=(
        "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
    table_5.heading('#1', text="Rank")
    table_5.heading('#2', text="Country")
    table_5.heading('#3', text="Score")
    table_5.heading('#4', text="GS")
    table_5.heading('#5', text="GC")
    table_5.heading('#6', text="GT")
    table_5.column('#1', width=30)
    table_5.column('#2', width=70)
    table_5.column('#3', width=30)
    table_5.column('#4', width=30)
    table_5.column('#5', width=30)
    table_5.column('#6', width=30)

    filltable(table_5, G5, Score5, GS5, GC5, GT5)

    G5_name.grid(row=4, column=1)
    table_5.grid(row=5, column=1)

    table_6 = ttk.Treeview(tableroot, height=5, columns=(
        "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
    table_6.heading('#1', text="Rank")
    table_6.heading('#2', text="Country")
    table_6.heading('#3', text="Score")
    table_6.heading('#4', text="GS")
    table_6.heading('#5', text="GC")
    table_6.heading('#6', text="GT")
    table_6.column('#1', width=30)
    table_6.column('#2', width=70)
    table_6.column('#3', width=30)
    table_6.column('#4', width=30)
    table_6.column('#5', width=30)
    table_6.column('#6', width=30)

    filltable(table_6, G6, Score6, GS6, GC6, GT6)

    G6_name.grid(row=4, column=2)
    table_6.grid(row=5, column=2)

    table_7 = ttk.Treeview(tableroot, height=5, columns=(
        "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
    table_7.heading('#1', text="Rank")
    table_7.heading('#2', text="Country")
    table_7.heading('#3', text="Score")
    table_7.heading('#4', text="GS")
    table_7.heading('#5', text="GC")
    table_7.heading('#6', text="GT")
    table_7.column('#1', width=30)
    table_7.column('#2', width=70)
    table_7.column('#3', width=30)
    table_7.column('#4', width=30)
    table_7.column('#5', width=30)
    table_7.column('#6', width=30)

    filltable(table_7, G7, Score7, GC7, GC7, GT7)

    G7_name.grid(row=4, column=3)
    table_7.grid(row=5, column=3)

    table_8 = ttk.Treeview(tableroot, height=5, columns=(
        "Rank", "Country", "Score", "GS", "GC", "GT"), show='headings')
    table_8.heading('#1', text="Rank")
    table_8.heading('#2', text="Country")
    table_8.heading('#3', text="Score")
    table_8.heading('#4', text="GS")
    table_8.heading('#5', text="GC")
    table_8.heading('#6', text="GT")
    table_8.column('#1', width=30)
    table_8.column('#2', width=70)
    table_8.column('#3', width=30)
    table_8.column('#4', width=30)
    table_8.column('#5', width=30)
    table_8.column('#6', width=30)

    filltable(table_8, G8, Score8, GS8, GC8, GT8)

    G8_name.grid(row=4, column=4)
    table_8.grid(row=5, column=4)

    round16_matches = [
        G1[0] + " vs " + G2[1],
        G3[0] + " vs " + G4[1],
        G5[0] + " vs " + G6[1],
        G7[0] + " vs " + G8[1],
        G1[1] + " vs " + G2[0],
        G3[1] + " vs " + G4[0],
        G5[1] + " vs " + G6[0],
        G7[1] + " vs " + G8[0],
    ]

    G1name.grid_forget()
    G2name.grid_forget()
    G3name.grid_forget()
    G4name.grid_forget()
    G5name.grid_forget()
    G6name.grid_forget()
    G7name.grid_forget()
    G8name.grid_forget()

    table1.grid_forget()
    table2.grid_forget()
    table3.grid_forget()
    table4.grid_forget()
    table5.grid_forget()
    table6.grid_forget()
    table7.grid_forget()
    table8.grid_forget()

    global countriesframe, matchesframe

    countriesframe = tk.Frame(scheduleshow)
    country1_16 = tk.Label(countriesframe, text=Qround16[0])
    country2_16 = tk.Label(countriesframe, text=Qround16[1])
    country3_16 = tk.Label(countriesframe, text=Qround16[2])
    country4_16 = tk.Label(countriesframe, text=Qround16[3])
    country5_16 = tk.Label(countriesframe, text=Qround16[4])
    country6_16 = tk.Label(countriesframe, text=Qround16[5])
    country7_16 = tk.Label(countriesframe, text=Qround16[6])
    country8_16 = tk.Label(countriesframe, text=Qround16[7])
    country9_16 = tk.Label(countriesframe, text=Qround16[8])
    country10_16 = tk.Label(countriesframe, text=Qround16[9])
    country11_16 = tk.Label(countriesframe, text=Qround16[10])
    country12_16 = tk.Label(countriesframe, text=Qround16[11])
    country13_16 = tk.Label(countriesframe, text=Qround16[12])
    country14_16 = tk.Label(countriesframe, text=Qround16[13])
    country15_16 = tk.Label(countriesframe, text=Qround16[14])
    country16_16 = tk.Label(countriesframe, text=Qround16[15])

    country1_16.grid(row=1, column=1)
    country2_16.grid(row=2, column=1)
    country3_16.grid(row=3, column=1)
    country4_16.grid(row=4, column=1)
    country5_16.grid(row=5, column=1)
    country6_16.grid(row=6, column=1)
    country7_16.grid(row=7, column=1)
    country8_16.grid(row=8, column=1)
    country9_16.grid(row=1, column=8)
    country10_16.grid(row=2, column=8)
    country11_16.grid(row=3, column=8)
    country12_16.grid(row=4, column=8)
    country13_16.grid(row=5, column=8)
    country14_16.grid(row=6, column=8)
    country15_16.grid(row=7, column=8)
    country16_16.grid(row=8, column=8)

    global match1_16entry, match2_16entry, match3_16entry, match4_16entry, match5_16entry, match6_16entry, match7_16entry, match8_16entry,match1_16,match2_16,match3_16,match4_16,match5_16,match6_16,match7_16,match8_16

    matchesframe = tk.Frame(scheduleshow)
    match1_16 = tk.Label(matchesframe, text=round16_matches[0])
    match2_16 = tk.Label(matchesframe, text=round16_matches[1])
    match3_16 = tk.Label(matchesframe, text=round16_matches[2])
    match4_16 = tk.Label(matchesframe, text=round16_matches[3])
    match5_16 = tk.Label(matchesframe, text=round16_matches[4])
    match6_16 = tk.Label(matchesframe, text=round16_matches[5])
    match7_16 = tk.Label(matchesframe, text=round16_matches[6])
    match8_16 = tk.Label(matchesframe, text=round16_matches[7])
    match1_16entry = tk.Entry(matchesframe, width=10)
    match2_16entry = tk.Entry(matchesframe, width=10)
    match3_16entry = tk.Entry(matchesframe, width=10)
    match4_16entry = tk.Entry(matchesframe, width=10)
    match5_16entry = tk.Entry(matchesframe, width=10)
    match6_16entry = tk.Entry(matchesframe, width=10)
    match7_16entry = tk.Entry(matchesframe, width=10)
    match8_16entry = tk.Entry(matchesframe, width=10)

    match1_16.grid(row=1, column=1)
    match1_16entry.grid(row=1, column=2)
    match2_16.grid(row=2, column=1)
    match2_16entry.grid(row=2, column=2)
    match3_16.grid(row=3, column=1)
    match3_16entry.grid(row=3, column=2)
    match4_16.grid(row=4, column=1)
    match4_16entry.grid(row=4, column=2)
    match5_16.grid(row=5, column=1)
    match5_16entry.grid(row=5, column=2)
    match6_16.grid(row=6, column=1)
    match6_16entry.grid(row=6, column=2)
    match7_16.grid(row=7, column=1)
    match7_16entry.grid(row=7, column=2)
    match8_16.grid(row=8, column=1)
    match8_16entry.grid(row=8, column=2)

    countriesframe.grid(row=2, column=1)
    matchesframe.grid(row=2, column=2)
    round16.grid_forget()
    round8.grid(row=3, column=1, columnspan=2)


def treatfinals(Result, Qinit, i, j, Qfinal):
    teamigoals = int(Result[:Result.find("-")])
    teamjgoals = int(Result[Result.find("-") + 1:])
    if teamigoals < teamjgoals:
        Qfinal.append(Qinit[j])
    elif teamigoals > teamjgoals:
        Qfinal.append(Qinit[i])
    elif teamigoals==teamjgoals:
        Choice=randint(0,1)
        if Choice==0:
            Qfinal.append(Qinit[i])
        else :
            Qfinal.append(Qinit[j])


def gotoround8():
    round8.grid_forget()
    round4.grid(row=3, column=1, columnspan=2)
    global Qround8
    Qround8 = []
    Result = match1_16entry.get()
    treatfinals(Result, Qround16, 0, 1, Qround8)
    Result = match2_16entry.get()
    treatfinals(Result, Qround16, 2, 3, Qround8)
    Result = match3_16entry.get()
    treatfinals(Result, Qround16, 4, 5, Qround8)
    Result = match4_16entry.get()
    treatfinals(Result, Qround16, 6, 7, Qround8)
    Result = match5_16entry.get()
    treatfinals(Result, Qround16, 8, 9, Qround8)
    Result = match6_16entry.get()
    treatfinals(Result, Qround16, 10, 11, Qround8)
    Result = match7_16entry.get()
    treatfinals(Result, Qround16, 12, 13, Qround8)
    Result = match8_16entry.get()
    treatfinals(Result, Qround16, 14, 15, Qround8)

    match1_16.grid_forget()
    match2_16.grid_forget()
    match3_16.grid_forget()
    match4_16.grid_forget()
    match5_16.grid_forget()
    match6_16.grid_forget()
    match7_16.grid_forget()
    match8_16.grid_forget()
    match1_16entry.grid_forget()
    match2_16entry.grid_forget()
    match3_16entry.grid_forget()
    match4_16entry.grid_forget()
    match5_16entry.grid_forget()
    match6_16entry.grid_forget()
    match7_16entry.grid_forget()
    match8_16entry.grid_forget()
    

    round8_matches = [
        Qround8[0] + " vs " + Qround8[1],
        Qround8[2] + " vs " + Qround8[3],
        Qround8[4] + " vs " + Qround8[5],
        Qround8[6] + " vs " + Qround8[7]
    ]

    country1_8 = tk.Label(countriesframe, width=25, text=Qround8[0])
    country1_8.grid(row=1, column=2, rowspan=2)
    country2_8 = tk.Label(countriesframe, width=25, text=Qround8[1])
    country2_8.grid(row=3, column=2, rowspan=2)
    country3_8 = tk.Label(countriesframe, width=25, text=Qround8[2])
    country3_8.grid(row=5, column=2, rowspan=2)
    country4_8 = tk.Label(countriesframe, width=25, text=Qround8[3])
    country4_8.grid(row=7, column=2, rowspan=2)
    country5_8 = tk.Label(countriesframe, width=25, text=Qround8[4])
    country5_8.grid(row=1, column=7, rowspan=2)
    country6_8 = tk.Label(countriesframe, width=25, text=Qround8[5])
    country6_8.grid(row=3, column=7, rowspan=2)
    country7_8 = tk.Label(countriesframe, width=25, text=Qround8[6])
    country7_8.grid(row=5, column=7, rowspan=2)
    country8_8 = tk.Label(countriesframe, width=25, text=Qround8[7])
    country8_8.grid(row=7, column=7, rowspan=2)

    global match1_8,match2_8,match3_8,match4_8,match1_8entry,match2_8entry,match3_8entry,match4_8entry


    match1_8 = tk.Label(matchesframe, text=round8_matches[0])
    match1_8entry = tk.Entry(matchesframe, width=10)
    match2_8 = tk.Label(matchesframe, text=round8_matches[1])
    match2_8entry = tk.Entry(matchesframe, width=10)
    match3_8 = tk.Label(matchesframe, text=round8_matches[2])
    match3_8entry = tk.Entry(matchesframe, width=10)
    match4_8 = tk.Label(matchesframe, text=round8_matches[3])
    match4_8entry = tk.Entry(matchesframe, width=10)

    match1_8.grid(row=1, column=1)
    match2_8.grid(row=2, column=1)
    match3_8.grid(row=3, column=1)
    match4_8.grid(row=4, column=1)
    match1_8entry.grid(row=1, column=2)
    match2_8entry.grid(row=2, column=2)
    match3_8entry.grid(row=3, column=2)
    match4_8entry.grid(row=4, column=2)

def gotoround4():
    round4.grid_forget()
    roundf.grid(row=3, column=1, columnspan=2)
    global Qround4
    Qround4 = []
    Result = match1_8entry.get()
    treatfinals(Result, Qround8, 0, 1, Qround4)
    Result = match2_8entry.get()
    treatfinals(Result, Qround8, 2, 3, Qround4)
    Result = match3_8entry.get()
    treatfinals(Result, Qround8, 4, 5, Qround4)
    Result = match4_8entry.get()
    treatfinals(Result, Qround8, 6, 7, Qround4)

    match1_8.grid_forget()
    match2_8.grid_forget()
    match3_8.grid_forget()
    match4_8.grid_forget()

    match1_8entry.grid_forget()
    match2_8entry.grid_forget()
    match3_8entry.grid_forget()
    match4_8entry.grid_forget()
    
    

    round4_matches = [
        Qround4[0] + " vs " + Qround4[1],
        Qround4[2] + " vs " + Qround4[3],
    ]

    country1_4 = tk.Label(countriesframe, width=25, text=Qround4[0])
    country1_4.grid(row=1, column=3, rowspan=4)
    country2_4 = tk.Label(countriesframe, width=25, text=Qround4[1])
    country2_4.grid(row=5, column=3, rowspan=4)
    country3_4 = tk.Label(countriesframe, width=25, text=Qround4[2])
    country3_4.grid(row=1, column=6, rowspan=4)
    country4_8 = tk.Label(countriesframe, width=25, text=Qround4[3])
    country4_8.grid(row=5, column=6, rowspan=4)

    global match1_4,match2_4,match1_4entry,match2_4entry

    match1_4 = tk.Label(matchesframe, text=round4_matches[0])
    match1_4entry = tk.Entry(matchesframe, width=10)
    match2_4= tk.Label(matchesframe, text=round4_matches[1])
    match2_4entry = tk.Entry(matchesframe, width=10)

    match1_4.grid(row=1, column=1)
    match2_4.grid(row=2, column=1)
    match1_4entry.grid(row=1, column=2)
    match2_4entry.grid(row=2, column=2)

def gotoroundf():
    roundf.grid_forget()
    finish.grid(row=3, column=1, columnspan=2)
    global Qroundf
    Qroundf = []
    Result = match1_4entry.get()
    treatfinals(Result, Qround4, 0, 1, Qroundf)
    Result = match2_4entry.get()
    treatfinals(Result, Qround4, 2, 3, Qroundf)

    match1_4.grid_forget()
    match2_4.grid_forget()

    match1_4entry.grid_forget()
    match2_4entry.grid_forget()
    
    

    roundf_matches = [
        Qroundf[0] + " vs " + Qroundf[1]
    ]

    country1_f = tk.Label(countriesframe, width=25, text=Qroundf[0])
    country1_f.grid(row=1, column=4, rowspan=8)
    country2_f = tk.Label(countriesframe, width=25, text=Qroundf[1])
    country2_f.grid(row=1, column=5, rowspan=8)

    global match1_f,match1_fentry

    match1_f = tk.Label(matchesframe, text=roundf_matches[0])
    match1_fentry = tk.Entry(matchesframe, width=10)

    match1_f.grid(row=1, column=1)
    match1_fentry.grid(row=1, column=2)

def finishwc():
    finish.grid_forget()
    Winner=[]
    Result=match1_fentry.get()
    treatfinals(Result, Qroundf, 0, 1, Winner)

    match1_f.grid_forget()
    match1_fentry.grid_forget()
    matchesframe.grid_forget()

    countrywinner=tk.Label(countriesframe,text=Winner[0])
    countrywinner.grid(row=2,column=4,columnspan=2)

def clear():
    G1show.delete(1.0, tk.END)
    G2show.delete(1.0, tk.END)
    G3show.delete(1.0, tk.END)
    G4show.delete(1.0, tk.END)
    G5show.delete(1.0, tk.END)
    G6show.delete(1.0, tk.END)
    G7show.delete(1.0, tk.END)
    G8show.delete(1.0, tk.END)
    G9show.delete(1.0, tk.END)
    G10show.delete(1.0, tk.END)
    G11show.delete(1.0, tk.END)
    G12show.delete(1.0, tk.END)
    delete.grid_forget()
    generate.grid(row=8, column=1, columnspan=4, pady=5)
    matches.grid_forget()



def schedule():
    global scheduleshow

    scheduleshow = tk.Toplevel()
    scheduleshow.config(bg="green")
    scheduleshow.title("Matches Schedule")

    global roundtitle

    roundtitle = tk.Label(scheduleshow, text="Round 1")
    roundtitle.grid(row=1, column=1, columnspan=4)

    global match1, match2, match3, match4, match5, match5, match6, match7, match8, match9, match10, match11, match12, match13, match14, match15, match16, match17, match18, match19, match20, match21, match22, match23, match24, G1name, G2name, G3name, G4name, G5name, G6name, G7name, G8name, G9name, G10name, G11name, G12name

    G1name = tk.Label(scheduleshow, text="G1")
    match1 = tk.Label(scheduleshow)
    match2 = tk.Label(scheduleshow)

    G2name = tk.Label(scheduleshow, text="G2")
    match3 = tk.Label(scheduleshow)
    match4 = tk.Label(scheduleshow)

    G3name = tk.Label(scheduleshow, text="G3")
    match5 = tk.Label(scheduleshow)
    match6 = tk.Label(scheduleshow)

    G4name = tk.Label(scheduleshow, text="G4")
    match7 = tk.Label(scheduleshow)
    match8 = tk.Label(scheduleshow)

    G5name = tk.Label(scheduleshow, text="G5")
    match9 = tk.Label(scheduleshow)
    match10 = tk.Label(scheduleshow)

    G6name = tk.Label(scheduleshow, text="G6")
    match11 = tk.Label(scheduleshow)
    match12 = tk.Label(scheduleshow)

    G7name = tk.Label(scheduleshow, text="G7")
    match13 = tk.Label(scheduleshow)
    match14 = tk.Label(scheduleshow)

    G8name = tk.Label(scheduleshow, text="G8")
    match15 = tk.Label(scheduleshow)
    match16 = tk.Label(scheduleshow)

    G9name = tk.Label(scheduleshow, text="G9")
    match17 = tk.Label(scheduleshow)
    match18 = tk.Label(scheduleshow)

    G10name = tk.Label(scheduleshow, text="G10")
    match19 = tk.Label(scheduleshow)
    match20 = tk.Label(scheduleshow)

    G11name = tk.Label(scheduleshow, text="G11")
    match21 = tk.Label(scheduleshow)
    match22 = tk.Label(scheduleshow)

    G12name = tk.Label(scheduleshow, text="G12")
    match23 = tk.Label(scheduleshow)
    match24 = tk.Label(scheduleshow)

    global match1entry, match2entry, match3entry, match4entry, match5entry, match6entry, match7entry, match8entry, match9entry, match10entry, match11entry, match12entry, match13entry, match14entry, match15entry, match16entry,match17entry, match18entry, match19entry, match20entry, match21entry, match22entry, match23entry, match24entry

    match1entry = tk.Entry(scheduleshow, width=10)
    match2entry = tk.Entry(scheduleshow, width=10)
    match3entry = tk.Entry(scheduleshow, width=10)
    match4entry = tk.Entry(scheduleshow, width=10)
    match5entry = tk.Entry(scheduleshow, width=10)
    match6entry = tk.Entry(scheduleshow, width=10)
    match7entry = tk.Entry(scheduleshow, width=10)
    match8entry = tk.Entry(scheduleshow, width=10)
    match9entry = tk.Entry(scheduleshow, width=10)
    match10entry = tk.Entry(scheduleshow, width=10)
    match11entry = tk.Entry(scheduleshow, width=10)
    match12entry = tk.Entry(scheduleshow, width=10)
    match13entry = tk.Entry(scheduleshow, width=10)
    match14entry = tk.Entry(scheduleshow, width=10)
    match15entry = tk.Entry(scheduleshow, width=10)
    match16entry = tk.Entry(scheduleshow, width=10)
    match17entry = tk.Entry(scheduleshow, width=10)
    match18entry = tk.Entry(scheduleshow, width=10)
    match19entry = tk.Entry(scheduleshow, width=10)
    match20entry = tk.Entry(scheduleshow, width=10)
    match21entry = tk.Entry(scheduleshow, width=10)
    match22entry = tk.Entry(scheduleshow, width=10)
    match23entry = tk.Entry(scheduleshow, width=10)
    match24entry = tk.Entry(scheduleshow, width=10)

    global Score1, Score2, Score3, Score4, Score5, Score6, Score7, Score8, Score9, Score10, Score11, Score12, GS1, GS2, GS3, GS4, GS5, GS6, GS7, GS8, GS9, GS10, GS11, GS12, GC1, GC2, GC3, GC4, GC5, GC6, GC7, GC8,GC9, GC10, GC11, GC12, GT1, GT2, GT3, GT4, GT5, GT6, GT7, GT8, GT9, GT10, GT11, GT12

    Score1, Score2, Score3, Score4, Score5, Score6, Score7, Score8,Score9, Score10, Score11, Score12 = [0, 0, 0, 0], [0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
    GS1, GS2, GS3, GS4, GS5, GS6, GS7, GS8, GS9, GS10, GS11, GS12 = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
    GC1, GC2, GC3, GC4, GC5, GC6, GC7, GC8, GC9, GC10, GC11, GC12 = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
    GT1, GT2, GT3, GT4, GT5, GT6, GT7, GT8,GT9, GT10, GT11, GT12 = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]

    global round2, round3, finalbutton,round32, round16, round8,round4,roundf,finish

    round2 = tk.Button(scheduleshow, text="Round 2", command=gotoround2)
    round3 = tk.Button(scheduleshow, text="Round 3", command=gotoround3)
    finalbutton = tk.Button(scheduleshow, text="Finals", command=gotofinals)
    round32=tk.Button(scheduleshow, text="Finals", command=gotoround32)
    round16 = tk.Button(scheduleshow, text="1/8 final", command=gotoround16)
    round8 = tk.Button(scheduleshow, text="1/4 final", command=gotoround8)
    round4 = tk.Button(scheduleshow, text="1/2 final", command=gotoround4)
    roundf = tk.Button(scheduleshow, text="final", command=gotoroundf)
    finish=tk.Button(scheduleshow,text="Finish this world cup",command=finishwc)

    global round1_matches, round2_matches, round3_matches

    round1_matches = [
        G1[0] + " vs " + G1[1],
        G1[2] + " vs " + G1[3],
        G2[0] + " vs " + G2[1],
        G2[2] + " vs " + G2[3],
        G3[0] + " vs " + G3[1],
        G3[2] + " vs " + G3[3],
        G4[0] + " vs " + G4[1],
        G4[2] + " vs " + G4[3],
        G5[0] + " vs " + G5[1],
        G5[2] + " vs " + G5[3],
        G6[0] + " vs " + G6[1],
        G6[2] + " vs " + G6[3],
        G7[0] + " vs " + G7[1],
        G7[2] + " vs " + G7[3],
        G8[0] + " vs " + G8[1],
        G8[2] + " vs " + G8[3],
        G9[0] + " vs " + G9[1],
        G9[2] + " vs " + G9[3],
        G10[0] + " vs " + G10[1],
        G10[2] + " vs " + G10[3],
        G11[0] + " vs " + G11[1],
        G11[2] + " vs " + G11[3],
        G12[0] + " vs " + G12[1],
        G12[2] + " vs " + G12[3]
    ]

    round2_matches = [
        G1[0] + " vs " + G1[2],
        G1[1] + " vs " + G1[3],
        G2[0] + " vs " + G2[2],
        G2[1] + " vs " + G2[3],
        G3[0] + " vs " + G3[2],
        G3[1] + " vs " + G3[3],
        G4[0] + " vs " + G4[2],
        G4[1] + " vs " + G4[3],
        G5[0] + " vs " + G5[2],
        G5[1] + " vs " + G5[3],
        G6[0] + " vs " + G6[2],
        G6[1] + " vs " + G6[3],
        G7[0] + " vs " + G7[2],
        G7[1] + " vs " + G7[3],
        G8[0] + " vs " + G8[2],
        G8[1] + " vs " + G8[3],
        G9[0] + " vs " + G9[2],
        G9[1] + " vs " + G9[3],
        G10[0] + " vs " + G10[2],
        G10[1] + " vs " + G10[3],
        G11[0] + " vs " + G11[2],
        G11[1] + " vs " + G11[3],
        G12[0] + " vs " + G12[2],
        G12[1] + " vs " + G12[3]
    ]

    round3_matches = [
        G1[0] + " vs " + G1[3],
        G1[1] + " vs " + G1[2],
        G2[0] + " vs " + G2[3],
        G2[1] + " vs " + G2[2],
        G3[0] + " vs " + G3[3],
        G3[1] + " vs " + G3[2],
        G4[0] + " vs " + G4[3],
        G4[1] + " vs " + G4[2],
        G5[0] + " vs " + G5[3],
        G5[1] + " vs " + G5[2],
        G6[0] + " vs " + G6[3],
        G6[1] + " vs " + G6[2],
        G7[0] + " vs " + G7[3],
        G7[1] + " vs " + G7[2],
        G8[0] + " vs " + G8[3],
        G8[1] + " vs " + G8[2],
        G9[0] + " vs " + G9[3],
        G9[1] + " vs " + G9[2],
        G10[0] + " vs " + G10[3],
        G10[1] + " vs " + G10[2],
        G11[0] + " vs " + G11[3],
        G11[1] + " vs " + G11[2],
        G12[0] + " vs " + G12[3],
        G12[1] + " vs " + G12[2]
    ]

    match1.config(text=round1_matches[0])
    match2.config(text=round1_matches[1])
    match3.config(text=round1_matches[2])
    match4.config(text=round1_matches[3])
    match5.config(text=round1_matches[4])
    match6.config(text=round1_matches[5])
    match7.config(text=round1_matches[6])
    match8.config(text=round1_matches[7])
    match9.config(text=round1_matches[8])
    match10.config(text=round1_matches[9])
    match11.config(text=round1_matches[10])
    match12.config(text=round1_matches[11])
    match13.config(text=round1_matches[12])
    match14.config(text=round1_matches[13])
    match15.config(text=round1_matches[14])
    match16.config(text=round1_matches[15])
    match17.config(text=round1_matches[16])
    match18.config(text=round1_matches[17])
    match19.config(text=round1_matches[18])
    match20.config(text=round1_matches[19])
    match21.config(text=round1_matches[20])
    match22.config(text=round1_matches[21])
    match23.config(text=round1_matches[22])
    match24.config(text=round1_matches[23])

    G1name.grid(row=2, column=1, rowspan=2, pady=5)
    match1.grid(row=2, column=2)
    match1entry.grid(row=2, column=3)
    match2.grid(row=3, column=2)
    match2entry.grid(row=3, column=3)
    G2name.grid(row=4, column=1, rowspan=2, pady=5)
    match3.grid(row=4, column=2)
    match3entry.grid(row=4, column=3)
    match4.grid(row=5, column=2)
    match4entry.grid(row=5, column=3)
    G3name.grid(row=6, column=1, rowspan=2, pady=5)
    match5.grid(row=6, column=2)
    match5entry.grid(row=6, column=3)
    match6.grid(row=7, column=2)
    match6entry.grid(row=7, column=3)
    G4name.grid(row=8, column=1, rowspan=2, pady=5)
    match7.grid(row=8, column=2)
    match7entry.grid(row=8, column=3)
    match8.grid(row=9, column=2)
    match8entry.grid(row=9, column=3)
    G5name.grid(row=10, column=1, rowspan=2, pady=5)
    match9.grid(row=10, column=2)
    match9entry.grid(row=10, column=3)
    match10.grid(row=11, column=2)
    match10entry.grid(row=11, column=3)
    G6name.grid(row=12, column=1, rowspan=2, pady=5)
    match11.grid(row=12, column=2)
    match11entry.grid(row=12, column=3)
    match12.grid(row=13, column=2)
    match12entry.grid(row=13, column=3)
    G7name.grid(row=14, column=1, rowspan=2, pady=5)
    match13.grid(row=14, column=2)
    match13entry.grid(row=14, column=3)
    match14.grid(row=15, column=2)
    match14entry.grid(row=15, column=3)
    G8name.grid(row=16, column=1, rowspan=2, pady=5)
    match15.grid(row=16, column=2)
    match15entry.grid(row=16, column=3)
    match16.grid(row=17, column=2)
    match16entry.grid(row=17, column=3)

    G9name.grid(row=18, column=1, rowspan=2, pady=5)
    match17.grid(row=18, column=2)
    match17entry.grid(row=18, column=3)
    match18.grid(row=19, column=2)
    match18entry.grid(row=19, column=3)
    G10name.grid(row=20, column=1, rowspan=2, pady=5)
    match19.grid(row=20, column=2)
    match19entry.grid(row=20, column=3)
    match20.grid(row=21, column=2)
    match20entry.grid(row=21, column=3)
    G11name.grid(row=22, column=1, rowspan=2, pady=5)
    match21.grid(row=22, column=2)
    match21entry.grid(row=22, column=3)
    match22.grid(row=23, column=2)
    match22entry.grid(row=23, column=3)
    G12name.grid(row=24, column=1, rowspan=2, pady=5)
    match23.grid(row=24, column=2)
    match23entry.grid(row=24, column=3)
    match24.grid(row=25, column=2)
    match24entry.grid(row=25, column=3)


    round2.grid(row=9, column=4, padx=5)
    


def show():
    cont = tk.Toplevel()
    cont.title("Countries list")
    cont.config(bg="green")

    conttitle = tk.Label(cont, text="Countries")
    conttitle.grid(row=1, column=1, columnspan=6)

    eurotitle = tk.Label(cont, text="Europe")
    eurotitle.grid(row=2, column=1)
    afrotitle = tk.Label(cont, text="Africa")
    afrotitle.grid(row=2, column=2)
    asiatitle = tk.Label(cont, text="Asia")
    asiatitle.grid(row=2, column=3)
    satitle = tk.Label(cont, text="South America")
    satitle.grid(row=2, column=4)
    natitle = tk.Label(cont, text="North America")
    natitle.grid(row=2, column=5)
    oceantitle = tk.Label(cont, text="Oceania")
    oceantitle.grid(row=2, column=6)

    Eurolist = scrolledtext.ScrolledText(cont, width=20, height=20)
    Euroelements = Euro[0]
    for i in range(1, len(Euro)):
        Euroelements += "\n" + Euro[i]
    Eurolist.insert(tk.END, Euroelements)

    Afrolist = scrolledtext.ScrolledText(cont, width=20, height=20)
    Afroelements = Afro[0]
    for i in range(1, len(Afro)):
        Afroelements += "\n" + Afro[i]
    Afrolist.insert(tk.END, Afroelements)

    Asialist = scrolledtext.ScrolledText(cont, width=20, height=20)
    Asiaelements = Asia[0]
    for i in range(1, len(Asia)):
        Asiaelements += "\n" + Asia[i]
    Asialist.insert(tk.END, Asiaelements)

    NAlist = scrolledtext.ScrolledText(cont, width=20, height=20)
    NAelements = NA[0]
    for i in range(1, len(NA)):
        NAelements += "\n" + NA[i]
    NAlist.insert(tk.END, NAelements)

    SAlist = scrolledtext.ScrolledText(cont, width=20, height=20)
    SAelements = SA[0]
    for i in range(1, len(SA)):
        SAelements += "\n" + SA[i]
    SAlist.insert(tk.END, SAelements)

    Oceanialist = scrolledtext.ScrolledText(cont, width=20, height=20)
    Oceaniaelements = Oceania[0]
    for i in range(1, len(Oceania)):
        Oceaniaelements += "\n" + Oceania[i]
    Oceanialist.insert(tk.END, Oceaniaelements)

    Eurolist.grid(row=3, column=1)
    Afrolist.grid(row=3, column=2)
    Asialist.grid(row=3, column=3)
    NAlist.grid(row=3, column=4)
    SAlist.grid(row=3, column=5)
    Oceanialist.grid(row=3, column=6)

    hint = tk.Label(cont, text="Only countries with this synthax will be accepted")
    hint.grid(row=4, column=1, columnspan=6)

Test=False
root = tk.Tk()
root.title("World Cup")
root.config(bg="green")
root.geometry("770x450")
title = tk.Label(root, text="World Cup Bild")
G1title = tk.Label(root, text="G1")
G2title = tk.Label(root, text="G2")
G3title = tk.Label(root, text="G3")
G4title = tk.Label(root, text="G4")
G5title = tk.Label(root, text="G5")
G6title = tk.Label(root, text="G6")
G7title = tk.Label(root, text="G7")
G8title = tk.Label(root, text="G8")
G9title = tk.Label(root, text="G9")
G10title = tk.Label(root, text="G10")
G11title = tk.Label(root, text="G11")
G12title = tk.Label(root, text="G12")
G1show = scrolledtext.ScrolledText(root, width=20, height=5)
G2show = scrolledtext.ScrolledText(root, width=20, height=5)
G3show = scrolledtext.ScrolledText(root, width=20, height=5)
G4show = scrolledtext.ScrolledText(root, width=20, height=5)
G5show = scrolledtext.ScrolledText(root, width=20, height=5)
G6show = scrolledtext.ScrolledText(root, width=20, height=5)
G7show = scrolledtext.ScrolledText(root, width=20, height=5)
G8show = scrolledtext.ScrolledText(root, width=20, height=5)
G9show = scrolledtext.ScrolledText(root, width=20, height=5)
G10show = scrolledtext.ScrolledText(root, width=20, height=5)
G11show = scrolledtext.ScrolledText(root, width=20, height=5)
G12show = scrolledtext.ScrolledText(root, width=20, height=5)
generate = tk.Button(root, text="Generate", command=execute)
delete = tk.Button(root, text="Clear", command=clear)
matches = tk.Button(root, text="Show matches schedule", command=schedule)

def about():
    aboutwindow=tk.Toplevel()
    aboutwindow.config(bg="green")

    aboutframe = tk.Frame(aboutwindow,bg="#0E96CC")

    Name = tk.Label(aboutframe, text=("Professor Xenon"), fg="#0E96CC", font=("Arial", 20))
    image = tk.PhotoImage(file="C:/My files/Coding/programming_main/New projects/World Cup/Me.png")
    infos = tk.Label(aboutframe, font=("Arial", 10))
    infos.config(text="Real name: Med Amin Haffouz \nEmail:aminhfz01@gmail.com\nStudies at : Tunis National Institute of Applied Sciences and Technology (INSAT)")

    Name.grid(row=1, column=1, columnspan=2)
    image_label = tk.Label(aboutframe, image=image)
    image_label.grid(row=2, column=1)
    infos.grid(row=2, column=2)

    aboutframe.pack(padx=5,pady=5)

menu=tk.Menu(root)

menu.add_command(label="Show countries lists", command=show)
menu.add_command(label="About",command=about)
menu.add_command(label="Exit",command=root.destroy)

root.config(menu=menu)

title.grid(row=1, column=1, columnspan=4)
G1title.grid(row=2, column=1)
G2title.grid(row=2, column=2)
G3title.grid(row=2, column=3)
G4title.grid(row=2, column=4)
G1show.grid(row=3, column=1, padx=5)
G2show.grid(row=3, column=2, padx=5)
G3show.grid(row=3, column=3, padx=5)
G4show.grid(row=3, column=4, padx=5)
G5title.grid(row=4, column=1)
G6title.grid(row=4, column=2)
G7title.grid(row=4, column=3)
G8title.grid(row=4, column=4)
G5show.grid(row=5, column=1, padx=5)
G6show.grid(row=5, column=2, padx=5)
G7show.grid(row=5, column=3, padx=5)
G8show.grid(row=5, column=4, padx=5)
G9title.grid(row=6, column=1)
G10title.grid(row=6, column=2)
G11title.grid(row=6, column=3)
G12title.grid(row=6, column=4)
G9show.grid(row=7, column=1, padx=5)
G10show.grid(row=7, column=2, padx=5)
G11show.grid(row=7, column=3, padx=5)
G12show.grid(row=7, column=4, padx=5)
generate.grid(row=8, column=1, columnspan=4, pady=5)



root.mainloop()

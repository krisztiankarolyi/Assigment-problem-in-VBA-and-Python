from myfunctions import *
from tkinter import *
from tkinter.ttk import Combobox
import random

import numpy as np
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit


def openNewWindow(ablak, eredmeny, maximalizalas: bool, atlag_min: float, atlag_max: float,
                  kapottenegyest: bool, jegymatrix: list, binarismatrix: list):
    """
    a kiiratasert felelos fuggveny.
    """
    newWindow = Toplevel(ablak)
    newWindow.title("Eredmény")
    newWindow.geometry("1200x400")
    newWindow.resizable(False, False)
    blokk = Frame(newWindow)

    if maximalizalas:
        Label(blokk, text='A lehető legjobb átlag (megoldás): ', font=7).grid(row=0, column=0)
        Label(blokk, text='Átlag, ha mindenki a lehető legkedvezőbb tételt húzná: ', font=7).grid(row=1, column=0)
        Label(blokk, text="{:.2f}".format(atlag_max), font=7).grid(row=1, column=1)
        if atlag_max == eredmeny:
            Label(blokk, text='A tételhúzás során mindenki a számára legkedvezőbb tételt tudta kihúzni. ', justify=LEFT,
                  font=7).grid(row=2, column=0, sticky='w')
        else:
            Label(blokk, text='A tételhúzás során nem mindenki tudta kihúzni a számára legkedvezőbb tételt. ',
                  justify=LEFT, font=7).grid(row=2, column=0, sticky='w')
    else:
        Label(blokk, text='A lehető legrosszabb átlag (megoldás): ', font=7).grid(row=0, column=0)
        Label(blokk, text='Átlag, ha mindenki a lehető legrosszabb tételt húzná: ', font=7).grid(row=1, column=0)
        Label(blokk, text="{:.2f}".format(atlag_min), font=7).grid(row=1, column=1)
        if kapottenegyest:
            Label(blokk, text='A tételhúzás során volt legalább egy hallgató, aki 4-est kapott. ', justify=LEFT,
                  font=7).grid(row=2, column=0, sticky='w')
        else:
            Label(blokk, text='A tételhúzás során NEM volt olyan hallgató, aki 4-est kapott. ', justify=LEFT,
                  font=7).grid(row=2, column=0, sticky='w')

    Label(blokk, text="{:.2f}".format(eredmeny), font=7, fg='green').grid(row=0, column=1)
    er = Text(blokk, font="Courier 10", wrap=NONE)
    er.config(width=100, height=3)

    er.grid(row=4, column=0)

    vsbar = Scrollbar(blokk, orient="vertical", command=er.yview)
    vsbar.grid(row=4, column=1, rowspan=2, sticky="nse")
    hsbar = Scrollbar(blokk, orient="horizontal", command=er.xview)
    hsbar.grid(row=5, column=0, columnspan=2, sticky="nsew")
    Button(blokk, text="Előrejelzés", command=mozgo_atlag).grid(row=6, column=0, padx=1, pady=1)
    blokk.pack()

    szoveg = ""  # fejlec
    for i in range(n):
        index = i + 1
        szoveg += "H" + str(index) + "\t"
    er.insert("1.0", szoveg)

    szoveg = "\n"  # kapott jegy
    teteleknevei = "\n"
    for i in range(n):
        for j in range(m):
            if jegymatrix[i][j] * binarismatrix[i][j] > 0:
                szoveg += str(jegymatrix[i][j]) + "\t"
                teteleknevei += "T" + str((j + 1)) + "\t"
    er.insert("2.0", szoveg)
    er.insert("3.0", teteleknevei)
    er.config(state=DISABLED)
    mainloop()


def checkText(text: str):
    """
    ha szám és 1-10 között -> True; egyébként -> False
    :param text:
    :return: Boolean
    """
    text = str(text).strip()
    if text.isnumeric():
        if 0 < int(text) < 100:
            return True
    return False


def Hide(gridElement):
    gridElement.grid_forget()


def ujfel():
    global n, m, t
    if checkText(tsz.get()) and checkText(hsz.get()):
        n = int(hsz.get())
        m = int(tsz.get())
        s = "    "  # s = " " * 4
        if n < 100 and m < 100:
            s += " "
            for i in range(m):
                s = s + "T" + str(i + 1)
                if i + 1 < 10:
                    for j in range(4 - len(str(i))):
                        s = s + " "
                else:
                    for j in range(4 - len(str(i + 1))):
                        s = s + " "
            s = s + "\n"

            for i in range(n):  # Koltseg matrix(jegyek generalasa)
                if i + 1 < 10:
                    s = s + "H" + str(i + 1) + ":  "
                else:
                    s = s + "H" + str(i + 1) + ": "
                for j in range(m):
                    rand = random.randint(4, 10)
                    if rand == 10:
                        s = s + str(rand) + "   "
                    else:
                        s = s + str(rand) + "    "
                s += "\n"

            if n < 20:
                if m < 26:
                    ce.config(width=m * 5 + 5, height=n + 1, padx=1, pady=1)
                    Hide(vsbar)
                    Hide(hsbar)
                else:
                    ce.config(width=130, height=n + 1, padx=1, pady=1)
                    hsbar.grid(row=2, column=0, columnspan=2, sticky="nsew")
                    Hide(vsbar)
            else:
                if m < 26:
                    ce.config(width=m * 5 + 5, height=21, padx=1, pady=1)
                    vsbar.grid(row=1, column=1, rowspan=2, sticky="nse")
                    Hide(hsbar)
                else:
                    ce.config(width=130, height=21, padx=1, pady=1)
                    vsbar.grid(row=1, column=1, rowspan=2, sticky="nse")
                    hsbar.grid(row=2, column=0, columnspan=2, sticky="nsew")

            ce.delete('1.0', END)
            ce.insert("1.0", s)
            s = " " * 4
            blok2.pack()
        else:
            #  print("Túl sok hallgató / tétel!")
            messagebox.showwarning(title="Hiba",
                                   message="Túl sok hallgató vagy tétel! lett beállÍtva! MAX 100 - 100 lehet.")
    else:
        # print("Helytelen adat lett megadva! N = "+str(hsz.get())+"  M = "+str(tsz.get()))
        messagebox.showwarning(title="Hiba", message="Helytelen adat lett megadva!")


def linp():
    global n, m, t, e, cf, jegyek_matrix
    n = int(hsz.get())
    m = int(tsz.get())

    jegyek_matrix = []
    binaris_matrix = []

    allcorrect = True  # a program nem engedi a rossz adat bevitelet
    tomb = ce.get("1.0", END).split("\n")

    szamokTomb = []
    for i in range(1, len(tomb)):  # a fejlecet es az ozlopjelolot kihagyom
        sorIn = tomb[i].split(" ")
        sorOut = []
        for j in range(1, len(sorIn)):
            if sorIn[j].isnumeric():
                sorOut.append(int(sorIn[j]))
            elif sorIn[j] != " " and sorIn[j] != "":
                allcorrect = False
                msg = "Hibás adat a jegyeknél: [" + sorIn[j] + "]"
                messagebox.showerror(title="Hiba", message=msg)
        if len(sorOut) == m:
            szamokTomb.append(sorOut)

    if len(szamokTomb) != n:
        allcorrect = False

    if allcorrect:  # ha minden adat ok, akkor mehet tovabb a megoldasban majd

        jegyek_matrix = szamokTomb
        feltolt0(matrix=binaris_matrix, n=n, m=m)

        print("n=", n, "\nm=", m)
        print("jegymatrix:", jegyek_matrix)
        print("binarismatrix:", binaris_matrix)

        if t.get() == "max":
            maximalizalas = True
        else:
            maximalizalas = False

        atlag_max = sorMaxAvg(n=n, matrix=jegyek_matrix)
        atlag_min = sorMinAvg(n=n, matrix=jegyek_matrix)

        # print("mehet tovabb, az adatok helyesek")

        if n == m:
            cost_matrix = np.array(jegyek_matrix)
            row_ind, col_ind = linear_sum_assignment(cost_matrix, maximalizalas)
            print("row_ind=", row_ind)
            print("col_ind=", col_ind)

            for i in range(n):
                binaris_matrix[row_ind[i]][col_ind[i]] = 1
                # binaris matrix feltoltese

            eredmeny = cfEredmenyGeneralas(jegyek_matrix, binaris_matrix) / n
            if maximalizalas:
                kapottenegyest = False
            else:
                kapottenegyest = legrosszabb_huzas(jegyek_matrix, binaris_matrix)

            print(cost_matrix[row_ind, col_ind].sum())

        elif n < m:

            if maximalizalas:
                cf = -1 * np.array(convert_1D(jegyek_matrix))
                res = lp(n=n, m=m, cf=cf, binarismatrix=binaris_matrix)
                print(-res.fun)
                print(res.x)
                eredmeny = cfEredmenyGeneralas(jegyek_matrix, binaris_matrix) / n
                print("eredmeny - atlag_max: " + str(eredmeny) + " - " + str(atlag_max))
                legjobb_huzas(n=n, result=-res.fun, maxatlag=atlag_max)
                kapottenegyest = False
            else:
                cf = convert_1D(jegyek_matrix)
                res = lp(n=n, m=m, cf=cf, binarismatrix=binaris_matrix)
                print(res.fun)
                print(res.x)
                eredmeny = cfEredmenyGeneralas(jegyek_matrix, binaris_matrix) / n
                print("eredmeny - atlag_min: " + str(eredmeny) + " - " + str(atlag_min))
                kapottenegyest = legrosszabb_huzas(jegyek_matrix, binaris_matrix)

        else:
            if maximalizalas:
                cf = -1 * np.array(convert_1D(jegyek_matrix))
                res = lp(n=n, m=m, cf=cf, binarismatrix=binaris_matrix)
                print(-res.fun)
                print(res.x)
                eredmeny = cfEredmenyGeneralas(jegyek_matrix, binaris_matrix) / n
                print("eredmeny - atlag_max: " + str(eredmeny) + " - " + str(atlag_max))
                legjobb_huzas(n=n, result=-res.fun, maxatlag=atlag_max)
                kapottenegyest = False

            else:
                cf = convert_1D(jegyek_matrix)
                res = lp(n=n, m=m, cf=cf, binarismatrix=binaris_matrix)
                print(res.fun)
                print(res.x)
                eredmeny = cfEredmenyGeneralas(jegyek_matrix, binaris_matrix) / n
                print("eredmeny - atlag_min: " + str(eredmeny) + " - " + str(atlag_min))
                kapottenegyest = legrosszabb_huzas(jegyek_matrix, binaris_matrix)

        print("n=", n, "m=", m)
        print("maximalizalas:", maximalizalas)
        print("jegymatrix:    ", jegyek_matrix)
        print("binarismatrix: ", binaris_matrix)
        openNewWindow(ablak, eredmeny, maximalizalas, atlag_min, atlag_max, kapottenegyest, jegyek_matrix,
                      binaris_matrix)
    else:
        # print("Helytelen adat lett megadva a jegyekhez!")
        messagebox.showerror(title="Hibás adatok",
                             message="valószínúleg valamelyik hallgatónál nem lett helyes jegy beállítva! (space vagy üres karakter okozhatja)")


def mozgo_atlag():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filenev = filedialog.askopenfilename(initialdir=dir_path, title="Select file",
                                         filetypes=(("text files", "*.txt"), ("all files", "*.*")))

    try:
        with open(filenev) as f:
            lines = f.read()
        lista = lines.split("\n")
        i = 0
        while i < len(lista):
            if lista[i] == '':
                lista.remove(lista[i])
                i -= 1
            else:
                lista[i] = float(lista[i])
            i += 1
        print("Vizsgaatlagok: ", lista)
        vizsga_atlagok = lista
        n = len(vizsga_atlagok)
        AE = []
        for i in range(2, n):
            ertek = []
            for j in range(n - i):
                osszeg = 0
                k = len(ertek)
                hatar = i + len(ertek)
                while k < hatar:
                    osszeg += vizsga_atlagok[k]
                    k += 1
                atlag = osszeg / i  # (x1+x2)/2 pl
                ertek.append(abs(vizsga_atlagok[j + i] - atlag))  # abs(x3 - (x1+x2)/2) pl
            ae = sum(ertek[l] for l in range(len(ertek))) / (n - i)
            AE.append(ae)

        hatar = 5
        if len(vizsga_atlagok) < 5:
            hatar = len(vizsga_atlagok)

        AE = AE[:hatar]

        print("AE: ", AE)
        print("AE legkisebb értéke: ", min(AE))
        for i in range(len(AE)):
            if AE[i] == min(AE):
                index = i
                print("Optimális periódus:", index + 2)

        elorejelzes_lista = []
        for i in range(n):
            if i < (index+2):
                elorejelzes_lista.append(0)
            else:
                ertek = 0
                for j in range(i-(index+2), i, 1): # i=5 , index+2 =4 -> j = {1,2,3,4}
                    ertek += vizsga_atlagok[j]
                atlag = round(ertek / (index+2), 2)
                elorejelzes_lista.append(atlag)

        print("Elorejelzes:")
        elorejelzes = round(sum(vizsga_atlagok[i] for i in range(n - 1, n - index - 3, -1)) / (index + 2), 2)
        print(elorejelzes)

        print(elorejelzes_lista)
        elorejelzes_lista.append(elorejelzes)
        for i in range(len(elorejelzes_lista)):
            if elorejelzes_lista[i] == 0:
                elorejelzes_lista[i] = None
        print(elorejelzes_lista)

        plt.figure("Előrejelzés")
        plt.plot(elorejelzes_lista, color='green', marker='o', mfc='red')  # plot the data
        plt.plot(vizsga_atlagok, linestyle='', marker='*', color='blue', markersize=10)

        plt.xticks(np.arange(len(elorejelzes_lista)), np.arange(1, len(elorejelzes_lista) + 1))

        plt.ylabel('jegy')  # set the label for y-axis
        plt.xlabel('index')  # set the label for x-axis
        plt.title("Jegyek - előrejelzés")  # set the title of the graph
        plt.show()  # display the graph

    except:
        messagebox.showwarning("Állomány nyitása", "Nem lehet megnyitni \n(%s)" % filenev)


ablak = Tk()
ablak.configure(bg='#555')
ablak.resizable(True, True)
w, h = ablak.winfo_screenwidth(), ablak.winfo_screenheight()
ablak.geometry("1250x800")

blok1 = Frame(ablak)
blok1.configure(bg='#555')
ablak.eval('tk::PlaceWindow . center')
Label(blok1, text='Hallgatok száma:', bg="#555", fg="white", font=10).grid(row=0, column=0, ipadx=2, ipady=1)
hsz = Entry(blok1, font=10)  # n
hsz.grid(row=0, column=1, pady=5, ipadx=1, ipady=1)
Label(blok1, text='Tetelek száma:', bg="#555", fg="white", font=10).grid(row=1, column=0, ipadx=2, ipady=1)
tsz = Entry(blok1, font=10)  # m
tsz.insert(0, "1")  # default ertek
hsz.insert(0, "1")
tsz.grid(row=1, column=1, pady=5, ipadx=1, ipady=1)

# megvan: n, m
Label(blok1, text='Feladat típusa:', bg="#555", fg="white", font=10).grid(row=2, column=0, ipadx=2, ipady=1)
adat1 = ("max", "min")
t = StringVar()
t.set("min")  # kombobox erteket tarolja es vlasztja ki alapbol az elsot
mm = Combobox(blok1, values=adat1, textvariable=t, state="readonly", font=10, width=19)
mm.set("max")
mm.grid(row=2, column=1, pady=5, ipadx=1, ipady=1)

# megvan: n, m, maximalizalas

Button(blok1, text="Új feladat", command=ujfel, width=25).grid(row=3, column=1, columnspan=2, ipadx=2, ipady=2)
blok1.pack()

blok2 = Frame(ablak)
Label(blok2, text="Hallgatók felkészültsége: ").grid(row=0, column=0)
ce = Text(blok2, font="Courier 11", wrap=NONE, spacing3=5)
ce.grid(row=1, column=0, pady=5)

vsbar = Scrollbar(blok2, orient="vertical", command=ce.yview)
hsbar = Scrollbar(blok2, orient="horizontal", command=ce.xview)

Button(blok2, text="Megold", command=linp, pady=1, font=3, width=20, bg='green', fg='white').grid(row=4, column=0,
                                                                                                  ipadx=2, ipady=2)
ablak.eval('tk::PlaceWindow . center')
ablak.title('Tételhúzásos hozzárendelési feladat V1.0 (Beta)')
ablak.mainloop()
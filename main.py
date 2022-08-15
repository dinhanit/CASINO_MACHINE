from lib2to3.pgen2.token import OP
import sys,random
from PyQt5.QtWidgets import QApplication,QMainWindow
from casino import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QMovie
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
import time
from tkinter import ttk
from tkinter import *



def ListToString(list:list)->str:
    result=""
    for i in range(0,len(list)):
        result+=list[i]+"+"
    return  result

def Notification(s):
    label1 = tk.Label(
        text=s,
        font="Arial",
        width=30,
        height=2,
        foreground="black",  # Set the text color to white
        background="white"  # Set the background color to black
    )
    label1.pack()
    #label1.after(1000, lambda: label1.destroy())
    tk.mainloop()

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.money=1000
        self.chip=0
        self.slot=1
        self.oldSum=0
        self.sum=0
        self.mode=0
        self.Random_Dice1=0
        self.Random_Dice2=0
        self.ID = self.uic.ID_SignUp.toPlainText()
        self.one_point= QtGui.QPixmap("../CASINO_MACHINE/background/1.png")
        self.two_point= QtGui.QPixmap("../CASINO_MACHINE/background/2.png")
        self.three_point= QtGui.QPixmap("../CASINO_MACHINE/background/3.png")
        self.four_point= QtGui.QPixmap("../CASINO_MACHINE/background/4.png")
        self.five_point= QtGui.QPixmap("../CASINO_MACHINE/background/5.png")
        self.six_point= QtGui.QPixmap("../CASINO_MACHINE/background/6.png")
        self.uic.Button_Stop.clicked.connect(self.ShowDice)
        self.uic.Button_Roll.clicked.connect(self.Roll)
        self.uic.Button_SignIn.clicked.connect(self.SignIn)
        self.uic.Button_SignUp.clicked.connect(self.SignUp)
        self.uic.Button_BuyChip.clicked.connect(self.BuyChip)
        self.uic.Button_SellChip.clicked.connect(self.SellChips)
        self.uic.Button_Exit.clicked.connect(self.main_win.close)
        self.uic.Button_StatusReport.clicked.connect(self.StatusReport)
        self.uic.Button_Menu_3.clicked.connect(self.BackMenu)
        self.uic.Button_Craps.clicked.connect(self.PlayCraps)
        self.uic.Button_Arups.clicked.connect(self.PlayArups)
        self.uic.Button_Menu_4.clicked.connect(self.BackMenu)



    def StatusReport(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Page_StatusReport)
        self.uic.lable_money.setText("$"+str(self.money))
        self.uic.lable_chips.setText("Chips: "+str(self.chip))

    def ChangeMoney10(self):
        if self.money-10*11 >= 0:
            self.chip+=10
            self.money-=10*11
            self.uic.screen_Money.setText("$"+str(self.money))
            self.uic.screen_Chips.setText("Chips:"+str(self.chip))
        else:
            Notification("Not enough money")
    def ChangeMoney50(self):
        if self.money-50*11 >= 0:
            self.chip+=50
            self.money-=50*11
            self.uic.screen_Money.setText("$"+str(self.money))
            self.uic.screen_Chips.setText("Chips:"+str(self.chip))
        else:
            Notification("Not enough money")

    def ChangeMoney100(self):
        if self.money-100*11 >= 0:
            self.chip+=100
            self.money-=100*11
            self.uic.screen_Money.setText("$"+str(self.money))
            self.uic.screen_Chips.setText("Chips:"+str(self.chip))
        else:
            Notification("Not enough money")

    def ChangeMoney500(self):
        if self.money-500*11 >= 0:
            self.chip+=500
            self.money-=500*11
            self.uic.screen_Money.setText("$"+str(self.money))
            self.uic.screen_Chips.setText("Chips:"+str(self.chip))
        else:
            Notification("Not enough money")

    def SellChips(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Page_SellChips)
        self.uic.Button_Sell.clicked.connect(self.SolveSell)
        self.uic.Button_Menu_2.clicked.connect(self.BackMenu)

        self.uic.money.setText("$" + str(self.money))
        self.uic.chip.setText("Chips:" + str(self.chip))

    def Reset(self):
        self.slot=1
        self.oldSum=0
        self.sum=0

    def SolveSell(self):
        try:
            sell=int(self.uic.lineEdit.displayText())
            if sell <= self.chip:
                self.money += sell * 10
                self.chip -= sell
                self.uic.money.setText("$"+str(self.money))
                self.uic.chip.setText("Chips:"+str(self.chip))
            else:
                Notification("Invalid amount")
        except:
            Notification("Invalid amount")

    def Roll(self):
        self.uic.Dice1.setText(" ")
        self.uic.Dice2.setText(" ")
        movie= QMovie("ClearCanineBasilisk-size_restricted.gif")
        self.uic.ScreenRoll.setMovie(movie)
        movie.start()
        self.uic.ScreenRoll.setScaledContents(True)

    def PlayCraps(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Page_RollDice)
        self.mode=1
        self.Reset()
        self.Roll()

    def PlayArups(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Page_RollDice)
        self.mode=2
        self.Reset()
        self.Roll()

    def BuyChip(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Page_BuyChips)
        self.uic.Button_Menu.clicked.connect(self.BackMenu)
        self.uic.Button_10chips.clicked.connect(self.ChangeMoney10)
        self.uic.Button_50chips.clicked.connect(self.ChangeMoney50)
        self.uic.Button_100chips.clicked.connect(self.ChangeMoney100)
        self.uic.Button_500chips.clicked.connect(self.ChangeMoney500)

        self.uic.screen_Money.setText("$" + str(self.money))
        self.uic.screen_Chips.setText("Chips:" + str(self.chip))


    def BackMenu(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Page_MainScreen)
        self.SaveData()


    def ShowDice(self):
        if self.chip>0:
            self.Random_Dice1=random.randint(1,6)
            if self.Random_Dice1 == 1:
                self.uic.Dice1.setPixmap(self.one_point)
                self.uic.Dice1.setScaledContents(True)
            elif self.Random_Dice1 == 2:
                self.uic.Dice1.setPixmap(self.two_point)
                self.uic.Dice1.setScaledContents(True)
            elif self.Random_Dice1 == 3:
                self.uic.Dice1.setPixmap(self.three_point)
                self.uic.Dice1.setScaledContents(True)
            elif self.Random_Dice1 == 4:
                self.uic.Dice1.setPixmap(self.four_point)
                self.uic.Dice1.setScaledContents(True)
            elif self.Random_Dice1 == 5:
                self.uic.Dice1.setPixmap(self.five_point)
                self.uic.Dice1.setScaledContents(True)
            elif self.Random_Dice1 == 6:
                self.uic.Dice1.setPixmap(self.six_point)
                self.uic.Dice1.setScaledContents(True)

            self.Random_Dice2=random.randint(1,6)
            self.uic.Dice2.setPixmap(self.two_point)
            self.uic.Dice2.setScaledContents(True)
            if self.Random_Dice2 == 1:
                self.uic.Dice2.setPixmap(self.one_point)
                self.uic.Dice2.setScaledContents(True)
            elif self.Random_Dice2 == 2:
                self.uic.Dice2.setPixmap(self.two_point)
                self.uic.Dice2.setScaledContents(True)
            elif self.Random_Dice2 == 3:
                self.uic.Dice2.setPixmap(self.three_point)
                self.uic.Dice2.setScaledContents(True)
            elif self.Random_Dice2 == 4:
                self.uic.Dice2.setPixmap(self.four_point)
                self.uic.Dice2.setScaledContents(True)
            elif self.Random_Dice2 == 5:
                self.uic.Dice2.setPixmap(self.five_point)
                self.uic.Dice2.setScaledContents(True)
            elif self.Random_Dice2 == 6:
                self.uic.Dice2.setPixmap(self.six_point)
                self.uic.Dice2.setScaledContents(True)

            self.sum=self.Random_Dice1+self.Random_Dice2
            if self.mode==1:
                if self.slot==1:
                    if (self.sum==7) or (self.sum==11):
                        self.Win()
                    elif (self.sum==2) or (self.sum==3) or (self.sum==12):
                        self.Loss()
                    else:
                        self.oldSum=self.sum
                        self.slot=2
                        Notification(str(self.Random_Dice1) + "+" + str(self.Random_Dice2)+" Continous")
                else:
                    if self.sum==self.oldSum:
                        self.Win()
                    elif self.sum==7:
                        self.Loss()
                    else:
                        Notification(str(self.Random_Dice1) + "+" + str(self.Random_Dice2)+" Continous")
            else:
                if self.slot==1:
                    if (self.sum==11) or (self.sum==12):
                        self.Win()
                    elif self.sum==2:
                        self.Loss()
                    else:
                        self.oldSum=self.sum
                        self.slot=2
                        Notification(str(self.Random_Dice1) + "+" + str(self.Random_Dice2)+" Continous")
                else:
                    if self.sum>self.oldSum:
                        self.Win()
                    else:
                        self.Loss()
        else: Notification("Not enough Chips")




    def SignIn(self):
        ID = self.uic.ID_SignIn.toPlainText()
        Pass = self.uic.Pass_SignIn.toPlainText()
        Confirm = self.uic.Confirm_SignIn.toPlainText()
        try:
            Account = open("Account.txt", "r")
            Check_Acount = Account.read().split("+")
        except:
            Account = open("Account.txt","w")
        try:
            Check_Acount.index(ID)
            Notification("Account already exists")
        except:
            Account = open("Account.txt", "a")
            Account.write("+"+"ID"+ID+"+"+Pass+"+"+"1000"+"+"+"0")
            Account.close()
            if Pass==Confirm:
                Notification("Sign in successfully")
            else:
                Notification("Check again password")
    def Win(self):
        self.chip+=2
        self.Reset()
        Notification(str(self.Random_Dice1) + "+" + str(self.Random_Dice2) + "Win +2 chip")


    def Loss(self):
        self.chip-=1
        self.Reset()
        Notification(str(self.Random_Dice1) + "+" + str(self.Random_Dice2) + "Loss -1 chip")


    def SignUp(self):
        self.ID = self.uic.ID_SignUp.toPlainText()
        Pass = self.uic.Pass_SignUp.toPlainText()
        Account=open("Account.txt","r")
        Check_Acount=Account.read().split("+")
        if "ID"+self.ID in Check_Acount:
            pos=Check_Acount.index("ID"+self.ID)
            if Pass==Check_Acount[pos+1]:
                self.money=int(Check_Acount[pos+2])
                self.chip=int(Check_Acount[pos+3])
                self.Play()
            else:
                Notification("Wrong account or not registered yet")
        else:  Notification("Wrong account or not registered yet")

    def SaveData(self):
        Account = open("Account.txt", "r")
        Check_Acount = Account.read().split("+")
        pos=Check_Acount.index("ID"+self.ID)
        Check_Acount[pos+2]=str(self.money)
        Check_Acount[pos+3]=str(self.chip)
        joined= "+".join(Check_Acount)
        Account = open("Account.txt", "w")
        Account.write(joined)

    def Play(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Page_MainScreen)
        self.uic.BackGround_1.setText("")
        movie = QMovie("BVDZ.gif")
        self.uic.BackGround_1.setMovie(movie)
        movie.start()
        self.uic.BackGround_1.setScaledContents(True)

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
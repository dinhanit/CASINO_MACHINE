# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'casino.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 574)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 791, 521))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setAutoFillBackground(True)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.tabWidget = QtWidgets.QTabWidget(self.page)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 661, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tab.setFont(font)
        self.tab.setAutoFillBackground(True)
        self.tab.setObjectName("tab")
        self.ID_SignUp = QtWidgets.QTextEdit(self.tab)
        self.ID_SignUp.setGeometry(QtCore.QRect(230, 170, 211, 41))
        self.ID_SignUp.setObjectName("ID_SignUp")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(180, 170, 71, 41))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(70, 230, 161, 41))
        self.label_12.setObjectName("label_12")
        self.Pass_SignUp = QtWidgets.QTextEdit(self.tab)
        self.Pass_SignUp.setGeometry(QtCore.QRect(230, 230, 211, 41))
        self.Pass_SignUp.setObjectName("Pass_SignUp")
        self.Button_SignUp = QtWidgets.QPushButton(self.tab)
        self.Button_SignUp.setGeometry(QtCore.QRect(260, 290, 131, 51))
        self.Button_SignUp.setObjectName("Button_SignUp")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(240, 110, 231, 31))
        self.label_13.setObjectName("label_13")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(0, 0, 661, 491))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("background/poker-background-with-playing-cards-and-chips-on-green-casino-background-modern-poker-widescreen-wallpaper-vector.jpg"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.label_20.raise_()
        self.ID_SignUp.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.Pass_SignUp.raise_()
        self.Button_SignUp.raise_()
        self.label_13.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Pass_SignIn = QtWidgets.QTextEdit(self.tab_2)
        self.Pass_SignIn.setGeometry(QtCore.QRect(240, 210, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Pass_SignIn.setFont(font)
        self.Pass_SignIn.setObjectName("Pass_SignIn")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(190, 150, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(70, 210, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.ID_SignIn = QtWidgets.QTextEdit(self.tab_2)
        self.ID_SignIn.setGeometry(QtCore.QRect(240, 150, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ID_SignIn.setFont(font)
        self.ID_SignIn.setObjectName("ID_SignIn")
        self.Confirm_SignIn = QtWidgets.QTextEdit(self.tab_2)
        self.Confirm_SignIn.setGeometry(QtCore.QRect(240, 270, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Confirm_SignIn.setFont(font)
        self.Confirm_SignIn.setObjectName("Confirm_SignIn")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(90, 270, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.Button_SignIn = QtWidgets.QPushButton(self.tab_2)
        self.Button_SignIn.setGeometry(QtCore.QRect(280, 320, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Button_SignIn.setFont(font)
        self.Button_SignIn.setObjectName("Button_SignIn")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(250, 100, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(0, 0, 661, 501))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("background/poker-background-with-playing-cards-and-chips-on-green-casino-background-modern-poker-widescreen-wallpaper-vector.jpg"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.label_19.raise_()
        self.Pass_SignIn.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.ID_SignIn.raise_()
        self.Confirm_SignIn.raise_()
        self.label_16.raise_()
        self.Button_SignIn.raise_()
        self.label_17.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.stackedWidget.addWidget(self.page)
        self.Page_MainScreen = QtWidgets.QWidget()
        self.Page_MainScreen.setObjectName("Page_MainScreen")
        self.BackGround_1 = QtWidgets.QLabel(self.Page_MainScreen)
        self.BackGround_1.setGeometry(QtCore.QRect(0, 0, 661, 521))
        self.BackGround_1.setText("")
        self.BackGround_1.setPixmap(QtGui.QPixmap("../Casino/background/109764-rdlnnfwoyl-1546592968.jpg"))
        self.BackGround_1.setScaledContents(True)
        self.BackGround_1.setObjectName("BackGround_1")
        self.Button_BuyChip = QtWidgets.QPushButton(self.Page_MainScreen)
        self.Button_BuyChip.setGeometry(QtCore.QRect(0, 470, 111, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Button_BuyChip.setFont(font)
        self.Button_BuyChip.setAutoFillBackground(True)
        self.Button_BuyChip.setAutoDefault(False)
        self.Button_BuyChip.setDefault(True)
        self.Button_BuyChip.setFlat(False)
        self.Button_BuyChip.setObjectName("Button_BuyChip")
        self.Button_SellChip = QtWidgets.QPushButton(self.Page_MainScreen)
        self.Button_SellChip.setGeometry(QtCore.QRect(110, 470, 111, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Button_SellChip.setFont(font)
        self.Button_SellChip.setAutoFillBackground(True)
        self.Button_SellChip.setAutoDefault(False)
        self.Button_SellChip.setDefault(True)
        self.Button_SellChip.setFlat(False)
        self.Button_SellChip.setObjectName("Button_SellChip")
        self.Button_Craps = QtWidgets.QPushButton(self.Page_MainScreen)
        self.Button_Craps.setGeometry(QtCore.QRect(220, 470, 111, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Button_Craps.setFont(font)
        self.Button_Craps.setAutoFillBackground(True)
        self.Button_Craps.setAutoDefault(False)
        self.Button_Craps.setDefault(True)
        self.Button_Craps.setFlat(False)
        self.Button_Craps.setObjectName("Button_Craps")
        self.Button_Arups = QtWidgets.QPushButton(self.Page_MainScreen)
        self.Button_Arups.setGeometry(QtCore.QRect(330, 470, 111, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Button_Arups.setFont(font)
        self.Button_Arups.setAutoFillBackground(True)
        self.Button_Arups.setAutoDefault(False)
        self.Button_Arups.setDefault(True)
        self.Button_Arups.setFlat(False)
        self.Button_Arups.setObjectName("Button_Arups")
        self.Button_StatusReport = QtWidgets.QPushButton(self.Page_MainScreen)
        self.Button_StatusReport.setGeometry(QtCore.QRect(440, 470, 111, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Button_StatusReport.setFont(font)
        self.Button_StatusReport.setAutoFillBackground(True)
        self.Button_StatusReport.setAutoDefault(False)
        self.Button_StatusReport.setDefault(True)
        self.Button_StatusReport.setFlat(False)
        self.Button_StatusReport.setObjectName("Button_StatusReport")
        self.Button_Exit = QtWidgets.QPushButton(self.Page_MainScreen)
        self.Button_Exit.setGeometry(QtCore.QRect(550, 470, 111, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Button_Exit.setFont(font)
        self.Button_Exit.setAutoFillBackground(True)
        self.Button_Exit.setAutoDefault(False)
        self.Button_Exit.setDefault(True)
        self.Button_Exit.setFlat(False)
        self.Button_Exit.setObjectName("Button_Exit")
        self.stackedWidget.addWidget(self.Page_MainScreen)
        self.Page_RollDice = QtWidgets.QWidget()
        self.Page_RollDice.setObjectName("Page_RollDice")
        self.Dice1 = QtWidgets.QLabel(self.Page_RollDice)
        self.Dice1.setGeometry(QtCore.QRect(160, 120, 151, 151))
        self.Dice1.setText("")
        self.Dice1.setPixmap(QtGui.QPixmap("../Casino/background/1.jpg"))
        self.Dice1.setScaledContents(True)
        self.Dice1.setObjectName("Dice1")
        self.Dice2 = QtWidgets.QLabel(self.Page_RollDice)
        self.Dice2.setGeometry(QtCore.QRect(330, 120, 161, 151))
        self.Dice2.setText("")
        self.Dice2.setPixmap(QtGui.QPixmap("../Casino/background/1.jpg"))
        self.Dice2.setScaledContents(True)
        self.Dice2.setObjectName("Dice2")
        self.Button_Stop = QtWidgets.QPushButton(self.Page_RollDice)
        self.Button_Stop.setGeometry(QtCore.QRect(340, 330, 111, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Button_Stop.setFont(font)
        self.Button_Stop.setAutoFillBackground(True)
        self.Button_Stop.setAutoDefault(False)
        self.Button_Stop.setDefault(True)
        self.Button_Stop.setFlat(False)
        self.Button_Stop.setObjectName("Button_Stop")
        self.label_7 = QtWidgets.QLabel(self.Page_RollDice)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 651, 511))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("background/istockphoto-672556284-612x612.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.ScreenRoll = QtWidgets.QLabel(self.Page_RollDice)
        self.ScreenRoll.setGeometry(QtCore.QRect(160, 120, 331, 151))
        self.ScreenRoll.setText("")
        self.ScreenRoll.setPixmap(QtGui.QPixmap("../Casino/background/1.jpg"))
        self.ScreenRoll.setScaledContents(True)
        self.ScreenRoll.setObjectName("ScreenRoll")
        self.Button_Roll = QtWidgets.QPushButton(self.Page_RollDice)
        self.Button_Roll.setGeometry(QtCore.QRect(200, 330, 111, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Button_Roll.setFont(font)
        self.Button_Roll.setAutoFillBackground(True)
        self.Button_Roll.setAutoDefault(False)
        self.Button_Roll.setDefault(True)
        self.Button_Roll.setFlat(False)
        self.Button_Roll.setObjectName("Button_Roll")
        self.Button_Menu_4 = QtWidgets.QPushButton(self.Page_RollDice)
        self.Button_Menu_4.setGeometry(QtCore.QRect(560, 480, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Button_Menu_4.setFont(font)
        self.Button_Menu_4.setObjectName("Button_Menu_4")
        self.label_7.raise_()
        self.Button_Stop.raise_()
        self.ScreenRoll.raise_()
        self.Dice1.raise_()
        self.Dice2.raise_()
        self.Button_Roll.raise_()
        self.Button_Menu_4.raise_()
        self.stackedWidget.addWidget(self.Page_RollDice)
        self.Page_BuyChips = QtWidgets.QWidget()
        self.Page_BuyChips.setObjectName("Page_BuyChips")
        self.label_2 = QtWidgets.QLabel(self.Page_BuyChips)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 761, 531))
        self.label_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_2.setStyleSheet("back-ground.rgb(255, 255, 127)")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("background/Background.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.Button_10chips = QtWidgets.QPushButton(self.Page_BuyChips)
        self.Button_10chips.setGeometry(QtCore.QRect(290, 160, 100, 100))
        self.Button_10chips.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("background/10 chip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_10chips.setIcon(icon)
        self.Button_10chips.setIconSize(QtCore.QSize(100, 100))
        self.Button_10chips.setObjectName("Button_10chips")
        self.Button_100chips = QtWidgets.QPushButton(self.Page_BuyChips)
        self.Button_100chips.setGeometry(QtCore.QRect(290, 280, 100, 100))
        self.Button_100chips.setAutoFillBackground(False)
        self.Button_100chips.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("background/100 chip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_100chips.setIcon(icon1)
        self.Button_100chips.setIconSize(QtCore.QSize(100, 100))
        self.Button_100chips.setCheckable(False)
        self.Button_100chips.setObjectName("Button_100chips")
        self.Button_50chips = QtWidgets.QPushButton(self.Page_BuyChips)
        self.Button_50chips.setGeometry(QtCore.QRect(410, 160, 100, 100))
        self.Button_50chips.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("background/50 chip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_50chips.setIcon(icon2)
        self.Button_50chips.setIconSize(QtCore.QSize(100, 100))
        self.Button_50chips.setObjectName("Button_50chips")
        self.Button_500chips = QtWidgets.QPushButton(self.Page_BuyChips)
        self.Button_500chips.setGeometry(QtCore.QRect(410, 280, 100, 100))
        self.Button_500chips.setAutoFillBackground(False)
        self.Button_500chips.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("background/500 chip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_500chips.setIcon(icon3)
        self.Button_500chips.setIconSize(QtCore.QSize(100, 100))
        self.Button_500chips.setCheckable(False)
        self.Button_500chips.setObjectName("Button_500chips")
        self.label = QtWidgets.QLabel(self.Page_BuyChips)
        self.label.setGeometry(QtCore.QRect(280, 80, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.screen_Money = QtWidgets.QLabel(self.Page_BuyChips)
        self.screen_Money.setGeometry(QtCore.QRect(290, 30, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.screen_Money.setFont(font)
        self.screen_Money.setObjectName("screen_Money")
        self.screen_Chips = QtWidgets.QLabel(self.Page_BuyChips)
        self.screen_Chips.setGeometry(QtCore.QRect(480, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.screen_Chips.setFont(font)
        self.screen_Chips.setObjectName("screen_Chips")
        self.Button_Menu = QtWidgets.QPushButton(self.Page_BuyChips)
        self.Button_Menu.setGeometry(QtCore.QRect(560, 480, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Button_Menu.setFont(font)
        self.Button_Menu.setObjectName("Button_Menu")
        self.stackedWidget.addWidget(self.Page_BuyChips)
        self.Page_StatusReport = QtWidgets.QWidget()
        self.Page_StatusReport.setObjectName("Page_StatusReport")
        self.label_8 = QtWidgets.QLabel(self.Page_StatusReport)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 661, 521))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(True)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("background/e9cfb196-5685-4b26-ac4a-982fdad49358_DESIGNS-74876_PP-Live_Casino_LHS_Paddy_Power_Live_Roulette_flat.jpeg"))
        self.label_8.setScaledContents(True)
        self.label_8.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_8.setObjectName("label_8")
        self.lable_money = QtWidgets.QLabel(self.Page_StatusReport)
        self.lable_money.setGeometry(QtCore.QRect(70, 220, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lable_money.setFont(font)
        self.lable_money.setAutoFillBackground(True)
        self.lable_money.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.lable_money.setObjectName("lable_money")
        self.lable_chips = QtWidgets.QLabel(self.Page_StatusReport)
        self.lable_chips.setGeometry(QtCore.QRect(70, 260, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lable_chips.setFont(font)
        self.lable_chips.setAutoFillBackground(True)
        self.lable_chips.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.lable_chips.setObjectName("lable_chips")
        self.label_3 = QtWidgets.QLabel(self.Page_StatusReport)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName("label_3")
        self.Button_Menu_3 = QtWidgets.QPushButton(self.Page_StatusReport)
        self.Button_Menu_3.setGeometry(QtCore.QRect(560, 490, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Button_Menu_3.setFont(font)
        self.Button_Menu_3.setObjectName("Button_Menu_3")
        self.stackedWidget.addWidget(self.Page_StatusReport)
        self.Page_SellChips = QtWidgets.QWidget()
        self.Page_SellChips.setObjectName("Page_SellChips")
        self.bgr = QtWidgets.QLabel(self.Page_SellChips)
        self.bgr.setGeometry(QtCore.QRect(0, 0, 671, 521))
        self.bgr.setText("")
        self.bgr.setPixmap(QtGui.QPixmap("background/360_F_76611410_eyrT8oAz2zON4oi0L3392J3FGJyzZW13.jpg"))
        self.bgr.setScaledContents(True)
        self.bgr.setWordWrap(False)
        self.bgr.setObjectName("bgr")
        self.label_5 = QtWidgets.QLabel(self.Page_SellChips)
        self.label_5.setGeometry(QtCore.QRect(260, 250, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.Page_SellChips)
        self.lineEdit.setGeometry(QtCore.QRect(280, 320, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.Button_Sell = QtWidgets.QPushButton(self.Page_SellChips)
        self.Button_Sell.setGeometry(QtCore.QRect(290, 350, 93, 28))
        self.Button_Sell.setObjectName("Button_Sell")
        self.money = QtWidgets.QLabel(self.Page_SellChips)
        self.money.setGeometry(QtCore.QRect(260, 220, 55, 16))
        self.money.setObjectName("money")
        self.chip = QtWidgets.QLabel(self.Page_SellChips)
        self.chip.setGeometry(QtCore.QRect(340, 220, 55, 16))
        self.chip.setObjectName("chip")
        self.Button_Menu_2 = QtWidgets.QPushButton(self.Page_SellChips)
        self.Button_Menu_2.setGeometry(QtCore.QRect(560, 490, 93, 28))
        self.Button_Menu_2.setObjectName("Button_Menu_2")
        self.stackedWidget.addWidget(self.Page_SellChips)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 663, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_11.setText(_translate("MainWindow", "ID:"))
        self.label_12.setText(_translate("MainWindow", "PASSWORD:"))
        self.Button_SignUp.setText(_translate("MainWindow", "Sign Up"))
        self.label_13.setText(_translate("MainWindow", "CASINO GAME"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "SIGN UP"))
        self.label_14.setText(_translate("MainWindow", "ID:"))
        self.label_15.setText(_translate("MainWindow", "PASSWORD:"))
        self.label_16.setText(_translate("MainWindow", "CONFIRM:"))
        self.Button_SignIn.setText(_translate("MainWindow", "Sign In"))
        self.label_17.setText(_translate("MainWindow", "CASINO GAME"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "SIGN IN"))
        self.Button_BuyChip.setText(_translate("MainWindow", "BUY CHIPS"))
        self.Button_SellChip.setText(_translate("MainWindow", "SELL CHIPS"))
        self.Button_Craps.setText(_translate("MainWindow", "Craps"))
        self.Button_Arups.setText(_translate("MainWindow", "Arups"))
        self.Button_StatusReport.setText(_translate("MainWindow", "Status Report"))
        self.Button_Exit.setText(_translate("MainWindow", "Exit"))
        self.Button_Stop.setText(_translate("MainWindow", "STOP"))
        self.Button_Roll.setText(_translate("MainWindow", "ROLL"))
        self.Button_Menu_4.setText(_translate("MainWindow", "MENU"))
        self.label.setText(_translate("MainWindow", "CLICK TO BUY CHIP"))
        self.screen_Money.setText(_translate("MainWindow", "$"))
        self.screen_Chips.setText(_translate("MainWindow", "Chips:"))
        self.Button_Menu.setText(_translate("MainWindow", "MENU"))
        self.lable_money.setText(_translate("MainWindow", "$"))
        self.lable_chips.setText(_translate("MainWindow", "Chip"))
        self.label_3.setText(_translate("MainWindow", "STATUS REPORT"))
        self.Button_Menu_3.setText(_translate("MainWindow", "MENU"))
        self.label_5.setText(_translate("MainWindow", "SELL CHIPS"))
        self.Button_Sell.setText(_translate("MainWindow", "SELL"))
        self.money.setText(_translate("MainWindow", "$"))
        self.chip.setText(_translate("MainWindow", "Chips:"))
        self.Button_Menu_2.setText(_translate("MainWindow", "MENU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
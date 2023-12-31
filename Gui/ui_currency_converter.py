from PyQt5 import QtCore, QtGui, QtWidgets
import Gui.Images.currency_rc as currency_rc


class Ui_Currency(object):
    def setupUi(self, Currency):
        Currency.setObjectName("Currency")
        Currency.resize(710, 660)
        Currency.setMinimumSize(QtCore.QSize(710, 660))
        Currency.setMaximumSize(QtCore.QSize(710, 660))
        Currency.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Currency.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frm_back = QtWidgets.QFrame(Currency)
        self.frm_back.setGeometry(QtCore.QRect(10, 10, 691, 641))
        self.frm_back.setStyleSheet("background-color:#2596be;\n"
                                    "border-radius:20px;\n"
                                    "")
        self.frm_back.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_back.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_back.setObjectName("frm_back")
        self.frm_mid = QtWidgets.QFrame(self.frm_back)
        self.frm_mid.setGeometry(QtCore.QRect(10, 10, 671, 631))
        self.frm_mid.setStyleSheet(
            "background-color:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:0.715909,stop:0 rgba(0,0,0,9), stop:0.375 rgba(0,0,0,50),stop:0.835227 rgba(0,0,0,75));\n"
            "border-radius:20px;\n"
            "")
        self.frm_mid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_mid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_mid.setObjectName("frm_mid")
        self.frm_front = QtWidgets.QFrame(self.frm_mid)
        self.frm_front.setGeometry(QtCore.QRect(9, 10, 651, 621))
        self.frm_front.setStyleSheet("/* FRAME STYLE */\n"
                                     "QFrame{\n"
                                     "    background-color: rgba(0,0,0,100);\n"
                                     "    border-radius: 20px;\n"
                                     "}\n"
                                     "\n"
                                     "/* LABEL STYLE */\n"
                                     "QLabel{\n"
                                     "    color: #2596be;\n"
                                     "    background-color: #0b1e3b;\n"
                                     "    border-radius: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "/* LINE EDIT STYLE */\n"
                                     "QLineEdit{\n"
                                     "    color: rgba(255,255,255,210);\n"
                                     "    background-color: #0b1e3b;\n"
                                     "    border-radius: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "/* COMBO BOX STYLE */\n"
                                     "QComboBox{\n"
                                     "    color: rgba(255,255,255,210);\n"
                                     "    background-color: #0b1e3b;\n"
                                     "    border-radius: 5px;\n"
                                     "    padding: 5px;\n"
                                     "    text-align: center;\n"
                                     "}\n"
                                     "QComboBox QAbstractItemView {\n"
                                     "     color: rgba(255,255,255,210);\n"
                                     "     background-color: #0b1e3b;\n"
                                     "     text-align: center;\n"
                                     "}\n"
                                     "\n"
                                     "/* BUTTON STYLE */\n"
                                     "QPushButton{\n"
                                     "    background-color: #0b1e3b;\n"
                                     "    color: #2596be;\n"
                                     "    border-radius: 5px;\n"
                                     "    padding: 8px 10px; /* Adjust the padding for the pop-up effect */\n"
                                     "    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Add a box shadow for the pop-up effect */\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 150, 190, 200), stop:1 rgba(85, 98, 112, 226));\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "    padding-left: 8px;\n"
                                     "    padding-top: 10px;\n"
                                     "    background-color: rgba(105, 118, 132, 200);\n"
                                     "    box-shadow: none; /* Remove the box shadow when pressed */\n"
                                     "}\n"
                                     "")
        self.frm_front.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_front.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_front.setObjectName("frm_front")
        self.frm_header = QtWidgets.QFrame(self.frm_front)
        self.frm_header.setGeometry(QtCore.QRect(0, 0, 651, 58))
        self.frm_header.setMinimumSize(QtCore.QSize(0, 50))
        self.frm_header.setStyleSheet("/* FRAME STYLE */\n"
                                      "\n"
                                      "QFrame{\n"
                                      "background-color:#0b1e3b;\n"
                                      "border-radius:15px;\n"
                                      "}\n"
                                      "\n"
                                      "/* BUTTON STYLE */\n"
                                      "QPushButton{\n"
                                      "    background-color: #0b1e3b;\n"
                                      "    color: #2596be;\n"
                                      "    border-radius: 5px;\n"
                                      "    padding: 8px 10px; /* Adjust the padding for the pop-up effect */\n"
                                      "    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Add a box shadow for the pop-up effect */\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 150, 190, 200), stop:1 rgba(85, 98, 112, 226));\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "    padding-left: 8px;\n"
                                      "    padding-top: 10px;\n"
                                      "    background-color: rgba(105, 118, 132, 200);\n"
                                      "    box-shadow: none; /* Remove the box shadow when pressed */\n"
                                      "}\n"
                                      "")
        self.frm_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_header.setObjectName("frm_header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frm_header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frm_contact_info = QtWidgets.QFrame(self.frm_header)
        self.frm_contact_info.setStyleSheet("")
        self.frm_contact_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_contact_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_contact_info.setObjectName("frm_contact_info")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frm_contact_info)
        self.horizontalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_github = QtWidgets.QPushButton(self.frm_contact_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_github.sizePolicy().hasHeightForWidth())
        self.btn_github.setSizePolicy(sizePolicy)
        self.btn_github.setMinimumSize(QtCore.QSize(65, 45))
        self.btn_github.setMaximumSize(QtCore.QSize(65, 45))
        self.btn_github.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_github.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/icons/github.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_github.setIcon(icon)
        self.btn_github.setIconSize(QtCore.QSize(40, 40))
        self.btn_github.setObjectName("btn_github")
        self.horizontalLayout_3.addWidget(self.btn_github)
        self.btn_linkedin = QtWidgets.QPushButton(self.frm_contact_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_linkedin.sizePolicy().hasHeightForWidth())
        self.btn_linkedin.setSizePolicy(sizePolicy)
        self.btn_linkedin.setMinimumSize(QtCore.QSize(65, 45))
        self.btn_linkedin.setMaximumSize(QtCore.QSize(65, 45))
        self.btn_linkedin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_linkedin.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/icons/linkedin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_linkedin.setIcon(icon1)
        self.btn_linkedin.setIconSize(QtCore.QSize(40, 40))
        self.btn_linkedin.setObjectName("btn_linkedin")
        self.horizontalLayout_3.addWidget(self.btn_linkedin)
        self.btn_cv = QtWidgets.QPushButton(self.frm_contact_info)
        self.btn_cv.setMinimumSize(QtCore.QSize(65, 45))
        self.btn_cv.setMaximumSize(QtCore.QSize(65, 45))
        self.btn_cv.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cv.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/icons/paperclip.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cv.setIcon(icon2)
        self.btn_cv.setIconSize(QtCore.QSize(40, 40))
        self.btn_cv.setObjectName("btn_cv")
        self.horizontalLayout_3.addWidget(self.btn_cv)
        self.btn_email = QtWidgets.QPushButton(self.frm_contact_info)
        self.btn_email.setMinimumSize(QtCore.QSize(65, 45))
        self.btn_email.setMaximumSize(QtCore.QSize(65, 45))
        self.btn_email.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_email.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/icons/mail.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_email.setIcon(icon3)
        self.btn_email.setIconSize(QtCore.QSize(40, 40))
        self.btn_email.setObjectName("btn_email")
        self.horizontalLayout_3.addWidget(self.btn_email)
        self.horizontalLayout.addWidget(self.frm_contact_info, 0, QtCore.Qt.AlignLeft)
        self.frm_utility = QtWidgets.QFrame(self.frm_header)
        self.frm_utility.setStyleSheet("")
        self.frm_utility.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_utility.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_utility.setObjectName("frm_utility")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frm_utility)
        self.horizontalLayout_2.setContentsMargins(0, 0, 5, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_minimize = QtWidgets.QPushButton(self.frm_utility)
        self.btn_minimize.setMinimumSize(QtCore.QSize(65, 45))
        self.btn_minimize.setMaximumSize(QtCore.QSize(65, 45))
        self.btn_minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimize.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/icons/chevron-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon4)
        self.btn_minimize.setIconSize(QtCore.QSize(40, 40))
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_2.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.frm_utility)
        self.btn_close.setMinimumSize(QtCore.QSize(65, 45))
        self.btn_close.setMaximumSize(QtCore.QSize(65, 45))
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon5)
        self.btn_close.setIconSize(QtCore.QSize(40, 40))
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.frm_utility, 0, QtCore.Qt.AlignRight)
        self.btn_reset = QtWidgets.QPushButton(self.frm_front)
        self.btn_reset.setGeometry(QtCore.QRect(490, 62, 150, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reset.setFont(font)
        self.btn_reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_reset.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/icons/exchange.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reset.setIcon(icon6)
        self.btn_reset.setIconSize(QtCore.QSize(30, 60))
        self.btn_reset.setObjectName("btn_reset")
        self.lbl_icon_eur = QtWidgets.QLabel(self.frm_front)
        self.lbl_icon_eur.setGeometry(QtCore.QRect(10, 200, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_icon_eur.setFont(font)
        self.lbl_icon_eur.setText("")
        self.lbl_icon_eur.setPixmap(QtGui.QPixmap(":/flags/flags/eur.png"))
        self.lbl_icon_eur.setScaledContents(True)
        self.lbl_icon_eur.setObjectName("lbl_icon_eur")
        self.lbl_icon_usd = QtWidgets.QLabel(self.frm_front)
        self.lbl_icon_usd.setGeometry(QtCore.QRect(10, 260, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_icon_usd.setFont(font)
        self.lbl_icon_usd.setText("")
        self.lbl_icon_usd.setPixmap(QtGui.QPixmap(":/flags/flags/usd.png"))
        self.lbl_icon_usd.setScaledContents(True)
        self.lbl_icon_usd.setObjectName("lbl_icon_usd")
        self.lbl_icon_gbp = QtWidgets.QLabel(self.frm_front)
        self.lbl_icon_gbp.setGeometry(QtCore.QRect(10, 320, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_icon_gbp.setFont(font)
        self.lbl_icon_gbp.setText("")
        self.lbl_icon_gbp.setPixmap(QtGui.QPixmap(":/flags/flags/gbp.png"))
        self.lbl_icon_gbp.setScaledContents(True)
        self.lbl_icon_gbp.setObjectName("lbl_icon_gbp")
        self.lbl_icon_cad = QtWidgets.QLabel(self.frm_front)
        self.lbl_icon_cad.setGeometry(QtCore.QRect(10, 380, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_icon_cad.setFont(font)
        self.lbl_icon_cad.setText("")
        self.lbl_icon_cad.setPixmap(QtGui.QPixmap(":/flags/flags/cad.png"))
        self.lbl_icon_cad.setScaledContents(True)
        self.lbl_icon_cad.setObjectName("lbl_icon_cad")
        self.lbl_icon_chf = QtWidgets.QLabel(self.frm_front)
        self.lbl_icon_chf.setGeometry(QtCore.QRect(10, 440, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_icon_chf.setFont(font)
        self.lbl_icon_chf.setText("")
        self.lbl_icon_chf.setPixmap(QtGui.QPixmap(":/flags/flags/chf.png"))
        self.lbl_icon_chf.setScaledContents(True)
        self.lbl_icon_chf.setObjectName("lbl_icon_chf")
        self.lbl_icon_rub = QtWidgets.QLabel(self.frm_front)
        self.lbl_icon_rub.setGeometry(QtCore.QRect(10, 500, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_icon_rub.setFont(font)
        self.lbl_icon_rub.setText("")
        self.lbl_icon_rub.setPixmap(QtGui.QPixmap(":/flags/flags/rub.png"))
        self.lbl_icon_rub.setScaledContents(True)
        self.lbl_icon_rub.setObjectName("lbl_icon_rub")
        self.lbl_icon_jpy = QtWidgets.QLabel(self.frm_front)
        self.lbl_icon_jpy.setGeometry(QtCore.QRect(10, 560, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_icon_jpy.setFont(font)
        self.lbl_icon_jpy.setText("")
        self.lbl_icon_jpy.setPixmap(QtGui.QPixmap(":/flags/flags/jpy.png"))
        self.lbl_icon_jpy.setScaledContents(True)
        self.lbl_icon_jpy.setObjectName("lbl_icon_jpy")
        self.lbl_currency_rub = QtWidgets.QLabel(self.frm_front)
        self.lbl_currency_rub.setGeometry(QtCore.QRect(90, 500, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_currency_rub.setFont(font)
        self.lbl_currency_rub.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_currency_rub.setObjectName("lbl_currency_rub")
        self.lbl_currency_gbp = QtWidgets.QLabel(self.frm_front)
        self.lbl_currency_gbp.setGeometry(QtCore.QRect(90, 320, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_currency_gbp.setFont(font)
        self.lbl_currency_gbp.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_currency_gbp.setObjectName("lbl_currency_gbp")
        self.lbl_currency_usd = QtWidgets.QLabel(self.frm_front)
        self.lbl_currency_usd.setGeometry(QtCore.QRect(90, 260, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_currency_usd.setFont(font)
        self.lbl_currency_usd.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_currency_usd.setObjectName("lbl_currency_usd")
        self.lbl_currency_cad = QtWidgets.QLabel(self.frm_front)
        self.lbl_currency_cad.setGeometry(QtCore.QRect(90, 380, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_currency_cad.setFont(font)
        self.lbl_currency_cad.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_currency_cad.setObjectName("lbl_currency_cad")
        self.lbl_currency_chf = QtWidgets.QLabel(self.frm_front)
        self.lbl_currency_chf.setGeometry(QtCore.QRect(90, 440, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_currency_chf.setFont(font)
        self.lbl_currency_chf.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_currency_chf.setObjectName("lbl_currency_chf")
        self.lbl_currency_eur = QtWidgets.QLabel(self.frm_front)
        self.lbl_currency_eur.setGeometry(QtCore.QRect(90, 200, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_currency_eur.setFont(font)
        self.lbl_currency_eur.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_currency_eur.setObjectName("lbl_currency_eur")
        self.lbl_currency_jpy = QtWidgets.QLabel(self.frm_front)
        self.lbl_currency_jpy.setGeometry(QtCore.QRect(90, 560, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_currency_jpy.setFont(font)
        self.lbl_currency_jpy.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_currency_jpy.setObjectName("lbl_currency_jpy")
        self.lbl_title_currency = QtWidgets.QLabel(self.frm_front)
        self.lbl_title_currency.setGeometry(QtCore.QRect(10, 140, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title_currency.setFont(font)
        self.lbl_title_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title_currency.setObjectName("lbl_title_currency")
        self.lbl_title_rate = QtWidgets.QLabel(self.frm_front)
        self.lbl_title_rate.setGeometry(QtCore.QRect(170, 140, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title_rate.setFont(font)
        self.lbl_title_rate.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title_rate.setObjectName("lbl_title_rate")
        self.lbl_title_amount = QtWidgets.QLabel(self.frm_front)
        self.lbl_title_amount.setGeometry(QtCore.QRect(330, 140, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title_amount.setFont(font)
        self.lbl_title_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title_amount.setObjectName("lbl_title_amount")
        self.lbl_title_buy = QtWidgets.QLabel(self.frm_front)
        self.lbl_title_buy.setGeometry(QtCore.QRect(490, 140, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title_buy.setFont(font)
        self.lbl_title_buy.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title_buy.setObjectName("lbl_title_buy")
        self.btn_clear = QtWidgets.QPushButton(self.frm_front)
        self.btn_clear.setGeometry(QtCore.QRect(330, 62, 150, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear.setStyleSheet("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Icons/icons/rotate-cw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_clear.setIcon(icon7)
        self.btn_clear.setIconSize(QtCore.QSize(30, 60))
        self.btn_clear.setObjectName("btn_clear")
        self.lbl_rate_eur = QtWidgets.QLabel(self.frm_front)
        self.lbl_rate_eur.setGeometry(QtCore.QRect(170, 200, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_rate_eur.setFont(font)
        self.lbl_rate_eur.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rate_eur.setObjectName("lbl_rate_eur")
        self.lbl_rate_usd = QtWidgets.QLabel(self.frm_front)
        self.lbl_rate_usd.setGeometry(QtCore.QRect(170, 260, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_rate_usd.setFont(font)
        self.lbl_rate_usd.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rate_usd.setObjectName("lbl_rate_usd")
        self.lbl_rate_gbp = QtWidgets.QLabel(self.frm_front)
        self.lbl_rate_gbp.setGeometry(QtCore.QRect(170, 320, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_rate_gbp.setFont(font)
        self.lbl_rate_gbp.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rate_gbp.setObjectName("lbl_rate_gbp")
        self.lbl_rate_chf = QtWidgets.QLabel(self.frm_front)
        self.lbl_rate_chf.setGeometry(QtCore.QRect(170, 440, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_rate_chf.setFont(font)
        self.lbl_rate_chf.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rate_chf.setObjectName("lbl_rate_chf")
        self.lbl_rate_cad = QtWidgets.QLabel(self.frm_front)
        self.lbl_rate_cad.setGeometry(QtCore.QRect(170, 380, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_rate_cad.setFont(font)
        self.lbl_rate_cad.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rate_cad.setObjectName("lbl_rate_cad")
        self.lbl_rate_rub = QtWidgets.QLabel(self.frm_front)
        self.lbl_rate_rub.setGeometry(QtCore.QRect(170, 500, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_rate_rub.setFont(font)
        self.lbl_rate_rub.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rate_rub.setObjectName("lbl_rate_rub")
        self.lbl_rate_jpy = QtWidgets.QLabel(self.frm_front)
        self.lbl_rate_jpy.setGeometry(QtCore.QRect(170, 560, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_rate_jpy.setFont(font)
        self.lbl_rate_jpy.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rate_jpy.setObjectName("lbl_rate_jpy")
        self.lbl_buy_cad = QtWidgets.QLabel(self.frm_front)
        self.lbl_buy_cad.setGeometry(QtCore.QRect(490, 380, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_buy_cad.setFont(font)
        self.lbl_buy_cad.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_buy_cad.setObjectName("lbl_buy_cad")
        self.lbl_buy_rub = QtWidgets.QLabel(self.frm_front)
        self.lbl_buy_rub.setGeometry(QtCore.QRect(490, 500, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_buy_rub.setFont(font)
        self.lbl_buy_rub.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_buy_rub.setObjectName("lbl_buy_rub")
        self.lbl_buy_usd = QtWidgets.QLabel(self.frm_front)
        self.lbl_buy_usd.setGeometry(QtCore.QRect(490, 260, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_buy_usd.setFont(font)
        self.lbl_buy_usd.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_buy_usd.setObjectName("lbl_buy_usd")
        self.lbl_buy_chf = QtWidgets.QLabel(self.frm_front)
        self.lbl_buy_chf.setGeometry(QtCore.QRect(490, 440, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_buy_chf.setFont(font)
        self.lbl_buy_chf.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_buy_chf.setObjectName("lbl_buy_chf")
        self.lbl_buy_gbp = QtWidgets.QLabel(self.frm_front)
        self.lbl_buy_gbp.setGeometry(QtCore.QRect(490, 320, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_buy_gbp.setFont(font)
        self.lbl_buy_gbp.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_buy_gbp.setObjectName("lbl_buy_gbp")
        self.lbl_buy_jpy = QtWidgets.QLabel(self.frm_front)
        self.lbl_buy_jpy.setGeometry(QtCore.QRect(490, 560, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_buy_jpy.setFont(font)
        self.lbl_buy_jpy.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_buy_jpy.setObjectName("lbl_buy_jpy")
        self.lbl_buy_eur = QtWidgets.QLabel(self.frm_front)
        self.lbl_buy_eur.setGeometry(QtCore.QRect(490, 200, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_buy_eur.setFont(font)
        self.lbl_buy_eur.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_buy_eur.setObjectName("lbl_buy_eur")
        self.lineEdit_amount_eur = QtWidgets.QLineEdit(self.frm_front)
        self.lineEdit_amount_eur.setGeometry(QtCore.QRect(330, 200, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_amount_eur.setFont(font)
        self.lineEdit_amount_eur.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_amount_eur.setObjectName("lineEdit_amount_eur")
        self.lineEdit_amount_usd = QtWidgets.QLineEdit(self.frm_front)
        self.lineEdit_amount_usd.setGeometry(QtCore.QRect(330, 260, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_amount_usd.setFont(font)
        self.lineEdit_amount_usd.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_amount_usd.setObjectName("lineEdit_amount_usd")
        self.lineEdit_amount_cad = QtWidgets.QLineEdit(self.frm_front)
        self.lineEdit_amount_cad.setGeometry(QtCore.QRect(330, 380, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_amount_cad.setFont(font)
        self.lineEdit_amount_cad.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_amount_cad.setObjectName("lineEdit_amount_cad")
        self.lineEdit_amount_gbp = QtWidgets.QLineEdit(self.frm_front)
        self.lineEdit_amount_gbp.setGeometry(QtCore.QRect(330, 320, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_amount_gbp.setFont(font)
        self.lineEdit_amount_gbp.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_amount_gbp.setObjectName("lineEdit_amount_gbp")
        self.lineEdit_amount_rub = QtWidgets.QLineEdit(self.frm_front)
        self.lineEdit_amount_rub.setGeometry(QtCore.QRect(330, 500, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_amount_rub.setFont(font)
        self.lineEdit_amount_rub.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_amount_rub.setObjectName("lineEdit_amount_rub")
        self.lineEdit_amount_chf = QtWidgets.QLineEdit(self.frm_front)
        self.lineEdit_amount_chf.setGeometry(QtCore.QRect(330, 440, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_amount_chf.setFont(font)
        self.lineEdit_amount_chf.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_amount_chf.setObjectName("lineEdit_amount_chf")
        self.lineEdit_amount_jpy = QtWidgets.QLineEdit(self.frm_front)
        self.lineEdit_amount_jpy.setGeometry(QtCore.QRect(330, 560, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_amount_jpy.setFont(font)
        self.lineEdit_amount_jpy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_amount_jpy.setObjectName("lineEdit_amount_jpy")
        self.lineEdit_currency_01 = QtWidgets.QLineEdit(self.frm_front)
        self.lineEdit_currency_01.setGeometry(QtCore.QRect(10, 62, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_currency_01.setFont(font)
        self.lineEdit_currency_01.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_currency_01.setObjectName("lineEdit_currency_01")
        self.lineEdit_currency_02 = QtWidgets.QLineEdit(self.frm_front)
        self.lineEdit_currency_02.setGeometry(QtCore.QRect(170, 62, 150, 33))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_currency_02.setFont(font)
        self.lineEdit_currency_02.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_currency_02.setReadOnly(True)
        self.lineEdit_currency_02.setObjectName("lineEdit_currency_02")
        self.cmb_currency_01 = QtWidgets.QComboBox(self.frm_front)
        self.cmb_currency_01.setGeometry(QtCore.QRect(10, 100, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cmb_currency_01.setFont(font)
        self.cmb_currency_01.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmb_currency_01.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.cmb_currency_01.setCurrentText("")
        self.cmb_currency_01.setPlaceholderText("")
        self.cmb_currency_01.setObjectName("cmb_currency_01")
        self.cmb_currency_02 = QtWidgets.QComboBox(self.frm_front)
        self.cmb_currency_02.setGeometry(QtCore.QRect(170, 100, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cmb_currency_02.setFont(font)
        self.cmb_currency_02.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmb_currency_02.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.cmb_currency_02.setObjectName("cmb_currency_02")

        # Setting Validator to LineEdit objects

        int_validator = QtGui.QIntValidator()
        self.lineEdit_currency_01.setValidator(int_validator)
        self.lineEdit_currency_02.setValidator(int_validator)
        self.lineEdit_amount_eur.setValidator(int_validator)
        self.lineEdit_amount_chf.setValidator(int_validator)
        self.lineEdit_amount_jpy.setValidator(int_validator)
        self.lineEdit_amount_cad.setValidator(int_validator)
        self.lineEdit_amount_gbp.setValidator(int_validator)
        self.lineEdit_amount_rub.setValidator(int_validator)
        self.lineEdit_amount_usd.setValidator(int_validator)
        self.retranslateUi(Currency)
        QtCore.QMetaObject.connectSlotsByName(Currency)

    def retranslateUi(self, Currency):
        _translate = QtCore.QCoreApplication.translate
        Currency.setWindowTitle(_translate("Currency", "Currency"))
        self.btn_reset.setText(_translate("Currency", "Reload"))
        self.lbl_currency_rub.setText(_translate("Currency", "RUB"))
        self.lbl_currency_gbp.setText(_translate("Currency", "GBP"))
        self.lbl_currency_usd.setText(_translate("Currency", "USD"))
        self.lbl_currency_cad.setText(_translate("Currency", "CAD"))
        self.lbl_currency_chf.setText(_translate("Currency", "CHF"))
        self.lbl_currency_eur.setText(_translate("Currency", "EUR"))
        self.lbl_currency_jpy.setText(_translate("Currency", "JPY"))
        self.lbl_title_currency.setText(_translate("Currency", "CURRENCY"))
        self.lbl_title_rate.setText(_translate("Currency", "RATE"))
        self.lbl_title_amount.setText(_translate("Currency", "AMOUNT"))
        self.lbl_title_buy.setText(_translate("Currency", "BUY"))
        self.btn_clear.setText(_translate("Currency", "Clear"))
        self.lineEdit_amount_eur.setText(_translate("Currency", "1"))
        self.lineEdit_amount_usd.setText(_translate("Currency", "1"))
        self.lineEdit_amount_cad.setText(_translate("Currency", "1"))
        self.lineEdit_amount_gbp.setText(_translate("Currency", "1"))
        self.lineEdit_amount_rub.setText(_translate("Currency", "1"))
        self.lineEdit_amount_chf.setText(_translate("Currency", "1"))
        self.lineEdit_amount_jpy.setText(_translate("Currency", "1"))
        self.lineEdit_currency_01.setText(_translate("Currency", "1"))
        self.lineEdit_currency_02.setText(_translate("Currency", "1"))
        self.cmb_currency_01.setWindowTitle(_translate("Currency", "Currency"))
        self.cmb_currency_02.setWindowTitle(_translate("Currency", "Currency"))

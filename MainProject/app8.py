from PyQt4 import QtCore, QtGui
import sys
from newfor import namcty,houtem,houtim,houpre,houhumi,curtem,curpre,curhumi,curusm,curpri,housum,houpri
from graph import grapy
from emailerqw import mainio
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WeatherForcast(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    
    def setupUi(self, WeatherForcast):
        WeatherForcast.setObjectName(_fromUtf8("WeatherForcast"))
        WeatherForcast.resize(572, 570)
        font = QtGui.QFont()
        font.setUnderline(True)
        WeatherForcast.setFont(font)
        WeatherForcast.setStyleSheet(_fromUtf8(""))
        
         # TOP_MIDDLE FRAME
        self.MIDDLE_FRAME = QtGui.QFrame(WeatherForcast)
        self.MIDDLE_FRAME.setGeometry(QtCore.QRect(0, 0, 571, 411))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.MIDDLE_FRAME.setFont(font)
        self.MIDDLE_FRAME.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/BACKGROUND_TOP.jpg)"))
        self.MIDDLE_FRAME.setFrameShape(QtGui.QFrame.StyledPanel)
        self.MIDDLE_FRAME.setFrameShadow(QtGui.QFrame.Raised)
        self.MIDDLE_FRAME.setObjectName(_fromUtf8("MIDDLE_FRAME"))
        
         # PLACE LABEL
        self.PLACE_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.PLACE_LABEL.setGeometry(QtCore.QRect(140, 80, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.PLACE_LABEL.setFont(font)
        self.PLACE_LABEL.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.PLACE_LABEL.setObjectName(_fromUtf8("PLACE_LABEL"))
        self.DATE_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.DATE_LABEL.setGeometry(QtCore.QRect(140, 120, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        
        # DATA LABEL
        self.DATE_LABEL.setFont(font)
        self.DATE_LABEL.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.DATE_LABEL.setObjectName(_fromUtf8("DATE_LABEL"))
        
        # DATE EDIT
        self.DATE_EDIT = QtGui.QDateEdit(self.MIDDLE_FRAME)
        self.DATE_EDIT.setGeometry(QtCore.QRect(250, 120, 211, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.DATE_EDIT.setFont(font)
        self.DATE_EDIT.setCalendarPopup(True)
        self.DATE_EDIT.setObjectName(_fromUtf8("DATE_EDIT"))
        
        # OK BUTTON
        self.OK_BUTTON = QtGui.QPushButton(self.MIDDLE_FRAME)
        self.OK_BUTTON.setGeometry(QtCore.QRect(254, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.OK_BUTTON.setFont(font)
        self.OK_BUTTON.setObjectName(_fromUtf8("OK_BUTTON"))
        
        # E-MAILBUTTOM
        self.EMAIL_BUTTON = QtGui.QPushButton(self.MIDDLE_FRAME)
        self.EMAIL_BUTTON.setGeometry(QtCore.QRect(350, 160, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.EMAIL_BUTTON.setFont(font)
        self.EMAIL_BUTTON.setObjectName(_fromUtf8("EMAIL_BUTTON"))
        
        # WEATHER LABEL
        self.WEATHER_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.WEATHER_LABEL.setGeometry(QtCore.QRect(200, -10, 371, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(24)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.WEATHER_LABEL.setFont(font)
        self.WEATHER_LABEL.setAutoFillBackground(False)
        self.WEATHER_LABEL.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.WEATHER_LABEL.setObjectName(_fromUtf8("WEATHER_LABEL"))
        
        # FORCAST LABEL
        self.FORCAST_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.FORCAST_LABEL.setGeometry(QtCore.QRect(370, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Brush Script MT"))
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        
        
        self.FORCAST_LABEL.setFont(font)
        self.FORCAST_LABEL.setStyleSheet(_fromUtf8("Background:\n"
"url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.FORCAST_LABEL.setObjectName(_fromUtf8("FORCAST_LABEL"))
        self.label = QtGui.QLabel(self.MIDDLE_FRAME)
        self.label.setGeometry(QtCore.QRect(10, 60, 551, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Algerian"))
        font.setPointSize(36)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        
        # GRAPHIC BUTTON
        self.GRAPH_BUTTON = QtGui.QPushButton(self.MIDDLE_FRAME)
        self.GRAPH_BUTTON.setGeometry(QtCore.QRect(440, 160, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.GRAPH_BUTTON.setFont(font)
        self.GRAPH_BUTTON.setObjectName(_fromUtf8("GRAPH_BUTTON"))
        
        # CURRENT TEMPERATURE LABEL
        self.CURRENT_TEMPERATURE_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.CURRENT_TEMPERATURE_LABEL.setGeometry(QtCore.QRect(10, 210, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.CURRENT_TEMPERATURE_LABEL.setFont(font)
        self.CURRENT_TEMPERATURE_LABEL.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.CURRENT_TEMPERATURE_LABEL.setObjectName(_fromUtf8("CURRENT_TEMPERATURE_LABEL"))
        self.label_2 = QtGui.QLabel(self.MIDDLE_FRAME)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 551, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Algerian"))
        font.setPointSize(36)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        # CURRENT DATA LABEL
        self.CURRENT_DATA_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.CURRENT_DATA_LABEL.setGeometry(QtCore.QRect(10, 170, 181, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.CURRENT_DATA_LABEL.setFont(font)
        self.CURRENT_DATA_LABEL.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.CURRENT_DATA_LABEL.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CURRENT_DATA_LABEL.setObjectName(_fromUtf8("CURRENT_DATA_LABEL"))
        
        # CURRENT PRESSURE LABEL
        self.CURRENT_PRESSURE_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.CURRENT_PRESSURE_LABEL.setGeometry(QtCore.QRect(10, 250, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.CURRENT_PRESSURE_LABEL.setFont(font)
        self.CURRENT_PRESSURE_LABEL.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.CURRENT_PRESSURE_LABEL.setObjectName(_fromUtf8("CURRENT_PRESSURE_LABEL"))
        
        # CURRENT PRECIPITATION LABEL
        self.CURRENT_PRECIPITATION_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.CURRENT_PRECIPITATION_LABEL.setGeometry(QtCore.QRect(10, 290, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.CURRENT_PRECIPITATION_LABEL.setFont(font)
        self.CURRENT_PRECIPITATION_LABEL.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.CURRENT_PRECIPITATION_LABEL.setObjectName(_fromUtf8("CURRENT_PRECIPITATION_LABEL"))
        
        # CURRENT SUMMARY LABEL
        self.CURRENT_SUMMARY_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.CURRENT_SUMMARY_LABEL.setGeometry(QtCore.QRect(300, 250, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.CURRENT_SUMMARY_LABEL.setFont(font)
        self.CURRENT_SUMMARY_LABEL.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.CURRENT_SUMMARY_LABEL.setObjectName(_fromUtf8("CURRENT_SUMMARY_LABEL"))
        
        # CURRENT HUMIDITY LABEL
        self.CURRENT_HUMIDITY_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.CURRENT_HUMIDITY_LABEL.setGeometry(QtCore.QRect(300, 210, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.CURRENT_HUMIDITY_LABEL.setFont(font)
        self.CURRENT_HUMIDITY_LABEL.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.CURRENT_HUMIDITY_LABEL.setObjectName(_fromUtf8("CURRENT_HUMIDITY_LABEL"))
        self.label_5 = QtGui.QLabel(self.MIDDLE_FRAME)
        self.label_5.setGeometry(QtCore.QRect(10, 350, 551, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Algerian"))
        font.setPointSize(36)
        font.setUnderline(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        
        # HOURLY DATA LABEL
        self.HOURLY_DATA_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.HOURLY_DATA_LABEL.setGeometry(QtCore.QRect(10, 330, 181, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.HOURLY_DATA_LABEL.setFont(font)
        self.HOURLY_DATA_LABEL.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.HOURLY_DATA_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.HOURLY_DATA_LABEL.setObjectName(_fromUtf8("HOURLY_DATA_LABEL"))
        
        # HOURLY TEMPERATURE LABEL
        self.HOURLY_TEMP_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.HOURLY_TEMP_LABEL.setGeometry(QtCore.QRect(0, 370, 131, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.HOURLY_TEMP_LABEL.setFont(font)
        self.HOURLY_TEMP_LABEL.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.HOURLY_TEMP_LABEL.setObjectName(_fromUtf8("HOURLY_TEMP_LABEL"))
        
        # HOURLY PRESSURE LABEL
        self.HOURLY_PRESSURE_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.HOURLY_PRESSURE_LABEL.setGeometry(QtCore.QRect(140, 370, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.HOURLY_PRESSURE_LABEL.setFont(font)
        self.HOURLY_PRESSURE_LABEL.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.HOURLY_PRESSURE_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.HOURLY_PRESSURE_LABEL.setObjectName(_fromUtf8("HOURLY_PRESSURE_LABEL"))
        
        # HOURLY PRECIPITATION LABEL
        self.HOURLY_PRECIPITATION_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.HOURLY_PRECIPITATION_LABEL.setGeometry(QtCore.QRect(260, 370, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.HOURLY_PRECIPITATION_LABEL.setFont(font)
        self.HOURLY_PRECIPITATION_LABEL.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.HOURLY_PRECIPITATION_LABEL.setObjectName(_fromUtf8("HOURLY_PRECIPITATION_LABEL"))
        
        # HOURLY HUMIDITY LABEL
        self.HOURLY_HUMIDTY_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.HOURLY_HUMIDTY_LABEL.setGeometry(QtCore.QRect(380, 370, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.HOURLY_HUMIDTY_LABEL.setFont(font)
        self.HOURLY_HUMIDTY_LABEL.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.HOURLY_HUMIDTY_LABEL.setObjectName(_fromUtf8("HOURLY_HUMIDTY_LABEL"))
        
        #HOURLY SUMMARY LABEL
        self.HOURLY_SUMMARY_LABEL = QtGui.QLabel(self.MIDDLE_FRAME)
        self.HOURLY_SUMMARY_LABEL.setGeometry(QtCore.QRect(470, 370, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.HOURLY_SUMMARY_LABEL.setFont(font)
        self.HOURLY_SUMMARY_LABEL.setStyleSheet(_fromUtf8("Background:url(:/BG_PIC/SMALL_BACKGROUND.png)"))
        self.HOURLY_SUMMARY_LABEL.setObjectName(_fromUtf8("HOURLY_SUMMARY_LABEL"))
        
        # PLACE TEXT EDIT
        self.PLACE_TEXTEDIT = QtGui.QTextEdit(self.MIDDLE_FRAME)
        self.PLACE_TEXTEDIT.setGeometry(QtCore.QRect(250, 80, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PLACE_TEXTEDIT.setFont(font)
        self.PLACE_TEXTEDIT.setStyleSheet(_fromUtf8("background:\n""rgb(255, 255, 255)"))
        self.PLACE_TEXTEDIT.setObjectName(_fromUtf8("PLACE_TEXTEDIT"))
        
        # CURRENT TEMPURATURE TEXTEDIT
        self.CURRENT_TEMP_LINE_EDIT_BOX = QtGui.QTextEdit(self.MIDDLE_FRAME)
        self.CURRENT_TEMP_LINE_EDIT_BOX.setGeometry(QtCore.QRect(150, 210, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.CURRENT_TEMP_LINE_EDIT_BOX.setFont(font)
        self.CURRENT_TEMP_LINE_EDIT_BOX.setStyleSheet(_fromUtf8("BACKGROUND: rgb(255, 255, 255)"))
        self.CURRENT_TEMP_LINE_EDIT_BOX.setObjectName(_fromUtf8("CURRENT_TEMP_LINE_EDIT_BOX"))
        
        # CURRENT PRESSURE TEXTEDIT
        self.CURRENT_PRESSURE_LINE_EDIT_BOX_2 = QtGui.QTextEdit(self.MIDDLE_FRAME)
        self.CURRENT_PRESSURE_LINE_EDIT_BOX_2.setGeometry(QtCore.QRect(150, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.CURRENT_PRESSURE_LINE_EDIT_BOX_2.setFont(font)
        self.CURRENT_PRESSURE_LINE_EDIT_BOX_2.setStyleSheet(_fromUtf8("BACKGROUND: rgb(255, 255, 255)"))
        self.CURRENT_PRESSURE_LINE_EDIT_BOX_2.setObjectName(_fromUtf8("CURRENT_PRESSURE_LINE_EDIT_BOX_2"))
        
        # CURRENT PRECIPITATION TEXTEDIT
        self.CURRENT_PRECIPITATION_EDIT_BOX_2 = QtGui.QTextEdit(self.MIDDLE_FRAME)
        self.CURRENT_PRECIPITATION_EDIT_BOX_2.setGeometry(QtCore.QRect(150, 290, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.CURRENT_PRECIPITATION_EDIT_BOX_2.setFont(font)
        self.CURRENT_PRECIPITATION_EDIT_BOX_2.setStyleSheet(_fromUtf8("BACKGROUND: rgb(255, 255, 255)"))
        self.CURRENT_PRECIPITATION_EDIT_BOX_2.setObjectName(_fromUtf8("CURRENT_PRECIPITATION_EDIT_BOX_2"))
        
        # CURRENT HUMIDITY TEXTEDIT
        self.CURRENT_HUMIDITY_LINE_EDIT_BOX_3 = QtGui.QTextEdit(self.MIDDLE_FRAME)
        self.CURRENT_HUMIDITY_LINE_EDIT_BOX_3.setGeometry(QtCore.QRect(410, 210, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.CURRENT_HUMIDITY_LINE_EDIT_BOX_3.setFont(font)
        self.CURRENT_HUMIDITY_LINE_EDIT_BOX_3.setStyleSheet(_fromUtf8("BACKGROUND: rgb(255, 255, 255)"))
        self.CURRENT_HUMIDITY_LINE_EDIT_BOX_3.setObjectName(_fromUtf8("CURRENT_HUMIDITY_LINE_EDIT_BOX_3"))
        
        # CURRENT SUMMARY TEXTEDIT
        self.CURRENT_SUMMARY_LINE_EDIT_BOX_3 = QtGui.QTextEdit(self.MIDDLE_FRAME)
        self.CURRENT_SUMMARY_LINE_EDIT_BOX_3.setGeometry(QtCore.QRect(410, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.CURRENT_SUMMARY_LINE_EDIT_BOX_3.setFont(font)
        self.CURRENT_SUMMARY_LINE_EDIT_BOX_3.setStyleSheet(_fromUtf8("BACKGROUND: rgb(255, 255, 255)"))
        self.CURRENT_SUMMARY_LINE_EDIT_BOX_3.setObjectName(_fromUtf8("CURRENT_SUMMARY_LINE_EDIT_BOX_3"))
        
        # HOURLY DATA TEXTEDIT
        self.HOURLY_DATA_TEXTEDIT = QtGui.QTextEdit(WeatherForcast)
        self.HOURLY_DATA_TEXTEDIT.setGeometry(QtCore.QRect(0, 390, 571, 181))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(10)
        font.setUnderline(False)
        self.HOURLY_DATA_TEXTEDIT.setFont(font)
        self.HOURLY_DATA_TEXTEDIT.setStyleSheet(_fromUtf8("BACKGROUND:url(:/BG_PIC/RESULT_TEXTBOX_BG.jpg)"))
        self.HOURLY_DATA_TEXTEDIT.setObjectName(_fromUtf8("HOURLY_DATA_TEXTEDIT"))

        self.retranslateUi(WeatherForcast)
        QtCore.QMetaObject.connectSlotsByName(WeatherForcast)

    def retranslateUi(self, WeatherForcast):
        WeatherForcast.setWindowTitle(_translate("WeatherForcast", "WeatherForcast", None))
        self.PLACE_LABEL.setText(_translate("WeatherForcast", "PLACE :", None))
        self.DATE_LABEL.setText(_translate("WeatherForcast", "DATE :", None))
        self.OK_BUTTON.setText(_translate("WeatherForcast", "OK", None))
        self.OK_BUTTON.clicked.connect(self.forcst)
        self.EMAIL_BUTTON.setText(_translate("WeatherForcast", "E-MAIL", None))
        self.EMAIL_BUTTON.clicked.connect(self.emlr)
        self.WEATHER_LABEL.setText(_translate("WeatherForcast", "WEATHER", None))
        self.FORCAST_LABEL.setText(_translate("WeatherForcast", "forcast", None))
        self.label.setText(_translate("WeatherForcast", "---------------------------------------------------------------------------------------------------------------------------------------------", None))
        self.GRAPH_BUTTON.setText(_translate("WeatherForcast", "GRAPH", None))
        self.GRAPH_BUTTON.clicked.connect(self.grapu)
        self.CURRENT_TEMPERATURE_LABEL.setText(_translate("WeatherForcast", "TEMPERATURE:", None))
        self.label_2.setText(_translate("WeatherForcast", "---------------------------------------------------------------------------------------------------------------------------------------------", None))
        self.CURRENT_DATA_LABEL.setText(_translate("WeatherForcast", "      CURRENT DATA:", None))
        self.CURRENT_PRESSURE_LABEL.setText(_translate("WeatherForcast", "PRESSURE :", None))
        self.CURRENT_PRECIPITATION_LABEL.setText(_translate("WeatherForcast", "PRECIPITATION:", None))
        self.CURRENT_SUMMARY_LABEL.setText(_translate("WeatherForcast", "SUMMARY:", None))
        self.CURRENT_HUMIDITY_LABEL.setText(_translate("WeatherForcast", "HUMIDITY :", None))
        self.label_5.setText(_translate("WeatherForcast", "---------------------------------------------------------------------------------------------------------------------------------------------", None))
        self.HOURLY_DATA_LABEL.setText(_translate("WeatherForcast", "HOURLY DATA:", None))
        self.HOURLY_TEMP_LABEL.setText(_translate("WeatherForcast", "     TEMPERATURE", None))
        self.HOURLY_PRESSURE_LABEL.setText(_translate("WeatherForcast", "PRESSURE ", None))
        self.HOURLY_PRECIPITATION_LABEL.setText(_translate("WeatherForcast", "PRECIPITATION", None))
        self.HOURLY_HUMIDTY_LABEL.setText(_translate("WeatherForcast", "HUMIDITY ", None))
        self.HOURLY_SUMMARY_LABEL.setText(_translate("WeatherForcast", "SUMMARY", None))

    def emlr(self):
        mainio()
    
    def grapu(self):
        x=str(self.DATE_EDIT.date().toPyDate())
        
        print (x[0:4],x[5:7],x[8:10],type(int(x[0:4])))
        grapy(str(self.PLACE_TEXTEDIT.toPlainText()),int(x[0:4]),int(x[5:7]),int(x[8:10]))
    def forcst(self):
        #print(str(self.PLACE_TEXTBOX.toPlainText()))
        #self.HOURLY_DATA_TEXTEDIT.setText(self.PLACE_TEXTEDIT.toPlainText())
        namcty(str(self.PLACE_TEXTEDIT.toPlainText()))
        curtm=curtem()
        d = degree_sign= u'\N{DEGREE SIGN}'
        self.CURRENT_TEMP_LINE_EDIT_BOX.setText(str(curtm)+str(d)+'C')
        curpr=curpre()
        self.CURRENT_PRESSURE_LINE_EDIT_BOX_2.setText(str(curpr)+' hpa')
        
        self.CURRENT_HUMIDITY_LINE_EDIT_BOX_3.setText(str(curhumi()))
        self.CURRENT_SUMMARY_LINE_EDIT_BOX_3.setText(str(curusm()))
        self.CURRENT_PRECIPITATION_EDIT_BOX_2.setText(str(curpri()))
        x=str(self.DATE_EDIT.date().toPyDate())
        #print(x[0:4],x[5:7],x[8:10])
        temp=houtem(int(x[0:4]),int(x[5:7]),int(x[8:10]))
        time=houtim(int(x[0:4]),int(x[5:7]),int(x[8:10]))
        pres=houpre(int(x[0:4]),int(x[5:7]),int(x[8:10]))
        humi=houhumi(int(x[0:4]),int(x[5:7]),int(x[8:10]))
        summ=housum(int(x[0:4]),int(x[5:7]),int(x[8:10]))
        pric=houpri(int(x[0:4]),int(x[5:7]),int(x[8:10]))
        i=0
        self.HOURLY_DATA_TEXTEDIT.setText(str('\t')+str(temp[0])+str('\t')+str(pres[0])+str('\t\t')+str(pric[0])+str('\t')+str(humi[0])+str('        ')+str(summ[0]) \
                                          
                                          +('\n')+str('\t')+str(temp[1])+str('\t')+str(pres[1])+str('\t\t')+str(pric[1])+str('\t')+str(humi[1])+str('        ')+str(summ[1]) \
                                          +('\n')+str('\t')+str(temp[2])+str('\t')+str(pres[2])+str('\t\t')+str(pric[2])+str('\t')+str(humi[2])+str('        ')+str(summ[2]) \
                                          +('\n')+str('\t')+str(temp[3])+str('\t')+str(pres[3])+str('\t\t')+str(pric[3])+str('\t')+str(humi[3])+str('        ')+str(summ[3]) \
                                          +('\n')+str('\t')+str(temp[4])+str('\t')+str(pres[4])+str('\t\t')+str(pric[4])+str('\t')+str(humi[4])+str('        ')+str(summ[4]) \
                                          +('\n')+str('\t')+str(temp[5])+str('\t')+str(pres[5])+str('\t\t')+str(pric[5])+str('\t')+str(humi[5])+str('        ')+str(summ[5]) \
                                          +('\n')+str('\t')+str(temp[6])+str('\t')+str(pres[6])+str('\t\t')+str(pric[6])+str('\t')+str(humi[6])+str('        ')+str(summ[6]) \
                                          +('\n')+str('\t')+str(temp[7])+str('\t')+str(pres[7])+str('\t\t')+str(pric[7])+str('\t')+str(humi[7])+str('        ')+str(summ[7]) \
                                          +('\n')+str('\t')+str(temp[8])+str('\t')+str(pres[8])+str('\t\t')+str(pric[8])+str('\t')+str(humi[8])+str('        ')+str(summ[8]) \
                                          +('\n')+str('\t')+str(temp[9])+str('\t')+str(pres[9])+str('\t\t')+str(pric[9])+str('\t')+str(humi[9])+str('        ')+str(summ[9]) \
                                          +('\n')+str('\t')+str(temp[10])+str('\t')+str(pres[10])+str('\t\t')+str(pric[10])+str('\t')+str(humi[10])+str('        ')+str(summ[10]) \
                                          +('\n')+str('\t')+str(temp[11])+str('\t')+str(pres[11])+str('\t\t')+str(pric[11])+str('\t')+str(humi[11])+str('        ')+str(summ[11]) \
                                          +('\n')+str('\t')+str(temp[12])+str('\t')+str(pres[12])+str('\t\t')+str(pric[12])+str('\t')+str(humi[12])+str('        ')+str(summ[12]) \
                                          +('\n')+str('\t')+str(temp[13])+str('\t')+str(pres[13])+str('\t\t')+str(pric[13])+str('\t')+str(humi[13])+str('        '))+str(summ[13]) \
                                          +('\n')+str('\t')+str(temp[14])+str('\t')+str(pres[14])+str('\t\t')+str(pric[14])+str('\t')+str(humi[14])+str('        ')+str(summ[14]) \
                                          +('\n')+str('\t')+str(temp[15])+str('\t')+str(pres[15])+str('\t\t')+str(pric[15])+str('\t')+str(humi[15])+str('        ')+str(summ[15]) \
                                          +('\n')+str('\t')+str(temp[16])+str('\t')+str(pres[16])+str('\t\t')+str(pric[16])+str('\t')+str(humi[16])+str('        ')+str(summ[16]) \
                                          +('\n')+str('\t')+str(temp[17])+str('\t')+str(pres[17])+str('\t\t')+str(pric[17])+str('\t')+str(humi[17])+str('        ')+str(summ[17]) \
                                          +('\n')+str('\t')+str(temp[18])+str('\t')+str(pres[18])+str('\t\t')+str(pric[18])+str('\t')+str(humi[18])+str('        ')+str(summ[18]) \
                                          +('\n')+str('\t')+str(temp[19])+str('\t')+str(pres[19])+str('\t\t')+str(pric[19])+str('\t')+str(humi[19])+str('        ')+str(summ[19]) \
                                          +('\n')+str('\t')+str(temp[20])+str('\t')+str(pres[20])+str('\t\t')+str(pric[20])+str('\t')+str(humi[20])+str('        ')+str(summ[20]) \
                                          +('\n')+str('\t')+str(temp[21])+str('\t')+str(pres[21])+str('\t\t')+str(pric[21])+str('\t')+str(humi[21])+str('        ')+str(summ[21]) \
                                          +('\n')+str('\t')+str(temp[22])+str('\t')+str(pres[22])+str('\t\t')+str(pric[22])+str('\t')+str(humi[22])+str('        ')+str(summ[22]) \
                                          +('\n')+str('\t')+str(temp[23])+str('\t')+str(pres[23])+str('\t\t')+str(pric[23])+str('\t')+str(humi[23])+str('        ')+str(summ[23]) 
                                          

        
    
        #namcty(str(self.PLACE_TEXTBOX.toPlainText()))
        

#import FRAME_BG_rc

if __name__ == "__main__": 
     app = QtGui.QApplication(sys.argv)
     ex = Ui_WeatherForcast()
     ex.show()
     sys.exit(app.exec_()) 

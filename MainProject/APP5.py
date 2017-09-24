from PyQt4 import QtCore, QtGui
import sys
from newfor import namcty,houtem,houtim,houpre,houhumi
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

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)    
     
        
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Fo ';/.;[prm"))
        Form.resize(600, 599)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 571, 81))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        # label for BIRLA WEATHER FORCAST
        self.BIRLA_WEATHER_FORCAST_LABEL = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        
        
        self.BIRLA_WEATHER_FORCAST_LABEL.setFont(font)
        self.BIRLA_WEATHER_FORCAST_LABEL.setAutoFillBackground(False)
        self.BIRLA_WEATHER_FORCAST_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.BIRLA_WEATHER_FORCAST_LABEL.setObjectName(_fromUtf8("BIRLA_WEATHER_FORCAST_LABEL"))
        self.verticalLayout.addWidget(self.BIRLA_WEATHER_FORCAST_LABEL)
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 110, 201, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        
        # LABEL FOR PLACE 
        self.PLACE_LABEL = QtGui.QLabel(self.horizontalLayoutWidget)

        
        
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PLACE_LABEL.setFont(font)
        self.PLACE_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.PLACE_LABEL.setObjectName(_fromUtf8("PLACE_LABEL"))
        self.horizontalLayout.addWidget(self.PLACE_LABEL)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(210, 160, 371, 51))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        
        # DATE SET CONTROL PANEL
        self.DATE_SET = QtGui.QDateEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.DATE_SET.setFont(font)
        self.DATE_SET.setAccelerated(False)
        self.DATE_SET.setProperty("showGroupSeparator", False)
        self.DATE_SET.setCalendarPopup(True)
        self.DATE_SET.setObjectName(_fromUtf8("DATE_SET"))
        self.verticalLayout_2.addWidget(self.DATE_SET)
        self.verticalLayoutWidget_3 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 160, 201, 51))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.DATE = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.DATE.setFont(font)
        self.DATE.setAlignment(QtCore.Qt.AlignCenter)
        self.DATE.setObjectName(_fromUtf8("DATE"))
        self.verticalLayout_3.addWidget(self.DATE)
        self.verticalLayoutWidget_5 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 290, 571, 31))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.RESULT_LABEL = QtGui.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        
        # RESULT LABEL
        self.RESULT_LABEL.setFont(font)
        self.RESULT_LABEL.setObjectName(_fromUtf8("RESULT_LABEL"))
        self.verticalLayout_5.addWidget(self.RESULT_LABEL)
        self.verticalLayoutWidget_6 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 330, 571, 241))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        
        
        # RESULT TEXTBOX
        self.RESULT_TEXTBOX = QtGui.QTextEdit(self.verticalLayoutWidget_6)
        self.RESULT_TEXTBOX.setObjectName(_fromUtf8("RESULT_TEXTBOX"))
        self.verticalLayout_6.addWidget(self.RESULT_TEXTBOX)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 230, 571, 43))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        
        # SUBMIT BUTTON
        self.SUBMIT_BUTTON = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.SUBMIT_BUTTON.setMaximumSize(QtCore.QSize(16777169, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SUBMIT_BUTTON.setFont(font)
        self.SUBMIT_BUTTON.setObjectName(_fromUtf8("SUBMIT_BUTTON"))
        self.horizontalLayout_3.addWidget(self.SUBMIT_BUTTON)
        
        # SEND E-MAIL BUTTON
        self.SEND_EMAIL_BUTTON = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SEND_EMAIL_BUTTON.setFont(font)
        self.SEND_EMAIL_BUTTON.setObjectName(_fromUtf8("SEND_EMAIL_BUTTON"))
        self.horizontalLayout_3.addWidget(self.SEND_EMAIL_BUTTON)
        
        # PLACE TEXTBOX 
        self.PLACE_TEXTBOX = QtGui.QTextEdit(Form)
        self.PLACE_TEXTBOX.setGeometry(QtCore.QRect(210, 110, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PLACE_TEXTBOX.setFont(font)
        self.PLACE_TEXTBOX.setAutoFillBackground(False)
        self.PLACE_TEXTBOX.setObjectName(_fromUtf8("PLACE_TEXTBOX"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.BIRLA_WEATHER_FORCAST_LABEL.setText(_translate("Form", "BIRLA WEATHER FORCAST", None))
        self.PLACE_LABEL.setText(_translate("Form", "PLACE :", None))
        self.DATE.setText(_translate("Form", "DATE :", None))
        self.RESULT_LABEL.setText(_translate("Form", "RESULTS :", None))
        self.SUBMIT_BUTTON.setText(_translate("Form", "SUBMIT", None))
        self.SUBMIT_BUTTON.clicked.connect(self.forcst)
        self.SEND_EMAIL_BUTTON.setText(_translate("Form", "SEND  E-MAIL", None))

    def forcst(self):
        #print(str(self.PLACE_TEXTBOX.toPlainText()))
        self.RESULT_TEXTBOX.setText(self.PLACE_TEXTBOX.toPlainText())
        #x=str(self.DATE_SET.date().toPyDate())
        #print(x)
        
        #namcty(str(self.PLACE_TEXTBOX.toPlainText()))
        
        
        
                
        
        
if __name__ == "__main__": 
     app = QtGui.QApplication(sys.argv)
     ex = Ui_Form()
     ex.show()
     sys.exit(app.exec_())

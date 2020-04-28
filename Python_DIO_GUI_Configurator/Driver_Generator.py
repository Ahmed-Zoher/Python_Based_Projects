# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Driver_Generator.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

def QString(x):
  return x

config=[[['PORTA','PIN0',1,0],['PORTA','PIN1',1,0],['PORTA','PIN2',1,0],['PORTA','PIN3',1,0],\
        [ 'PORTA','PIN4',1,0],['PORTA','PIN5',1,0],['PORTA','PIN6',1,0],['PORTA','PIN7',1,0]],\
        [['PORTB','PIN0',1,0],['PORTB','PIN1',1,0],['PORTB','PIN2',1,0],['PORTB','PIN3',1,0],\
        [ 'PORTB','PIN4',1,0],['PORTB','PIN5',1,0],['PORTB','PIN6',1,0],['PORTB','PIN7',1,0]],\
        [['PORTC','PIN0',1,0],['PORTC','PIN1',1,0],['PORTC','PIN2',1,0],['PORTC','PIN3',1,0],\
        [ 'PORTC','PIN4',1,0],['PORTC','PIN5',1,0],['PORTC','PIN6',1,0],['PORTC','PIN7',1,0]],\
        [['PORTD','PIN0',1,0],['PORTD','PIN1',1,0],['PORTD','PIN2',1,0],['PORTD','PIN3',1,0],\
        [ 'PORTD','PIN4',1,0],['PORTD','PIN5',1,0],['PORTD','PIN6',1,0],['PORTD','PIN7',1,0]]]

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(449, 302)
        self.Pin_GroupBox = QGroupBox(Form)
        self.Pin_GroupBox.setObjectName(u"Pin_GroupBox")
        self.Pin_GroupBox.setGeometry(QRect(0, 50, 441, 201))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75);
        self.Pin_GroupBox.setFont(font)
        self.Output_RadioButton = QRadioButton(self.Pin_GroupBox)
        self.Output_RadioButton.setObjectName(u"Output_RadioButton")
        self.Output_RadioButton.setGeometry(QRect(10, 50, 111, 31))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75);
        self.Output_RadioButton.setFont(font1)
        self.Output_RadioButton.setChecked(True)
        self.Input_RadioButton = QRadioButton(self.Pin_GroupBox)
        self.Input_RadioButton.setObjectName(u"Input_RadioButton")
        self.Input_RadioButton.setGeometry(QRect(10, 110, 111, 31))
        self.Input_RadioButton.setFont(font1)
        self.OutputLevel_GroupBox = QGroupBox(self.Pin_GroupBox)
        self.OutputLevel_GroupBox.setObjectName(u"OutputLevel_GroupBox")
        self.OutputLevel_GroupBox.setGeometry(QRect(140, 40, 291, 51))
        self.OutputLevel_GroupBox.setFont(font)
        self.High_RadioButton = QRadioButton(self.OutputLevel_GroupBox)
        self.High_RadioButton.setObjectName(u"High_RadioButton")
        self.High_RadioButton.setGeometry(QRect(10, 20, 97, 20))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setWeight(50);
        self.High_RadioButton.setFont(font2)
        self.Low_RadioButton = QRadioButton(self.OutputLevel_GroupBox)
        self.Low_RadioButton.setObjectName(u"Low_RadioButton")
        self.Low_RadioButton.setGeometry(QRect(140, 20, 97, 20))
        self.Low_RadioButton.setFont(font2)
        self.Low_RadioButton.setChecked(True)
        self.InputConfigurations_GroupBox = QGroupBox(self.Pin_GroupBox)
        self.InputConfigurations_GroupBox.setObjectName(u"InputConfigurations_GroupBox")
        self.InputConfigurations_GroupBox.setEnabled(False)
        self.InputConfigurations_GroupBox.setGeometry(QRect(140, 100, 291, 51))
        self.InputConfigurations_GroupBox.setFont(font)
        self.PullUp_RadioButton = QRadioButton(self.InputConfigurations_GroupBox)
        self.PullUp_RadioButton.setObjectName(u"PullUp_RadioButton")
        self.PullUp_RadioButton.setGeometry(QRect(10, 20, 97, 20))
        self.PullUp_RadioButton.setFont(font2)
        self.HighImpeadance_RadioButton = QRadioButton(self.InputConfigurations_GroupBox)
        self.HighImpeadance_RadioButton.setObjectName(u"HighImpeadance_RadioButton")
        self.HighImpeadance_RadioButton.setGeometry(QRect(136, 20, 131, 20))
        self.HighImpeadance_RadioButton.setFont(font2)
        self.HighImpeadance_RadioButton.setChecked(True)
        self.SubmitConfiguration_PushButton = QPushButton(self.Pin_GroupBox)
        self.SubmitConfiguration_PushButton.setObjectName(u"SubmitConfiguration_PushButton")
        self.SubmitConfiguration_PushButton.setGeometry(QRect(280, 160, 151, 28))
        self.Port_ComboBox = QComboBox(Form)
        self.Port_ComboBox.addItem(QString(''))
        self.Port_ComboBox.addItem(QString(''))
        self.Port_ComboBox.addItem(QString(''))
        self.Port_ComboBox.addItem(QString(''))
        self.Port_ComboBox.setObjectName(u"Port_ComboBox")
        self.Port_ComboBox.setGeometry(QRect(70, 10, 101, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.Port_ComboBox.setFont(font3)
        self.Pin_ComboBox = QComboBox(Form)
        self.Pin_ComboBox.addItem(QString(''))
        self.Pin_ComboBox.addItem(QString(''))
        self.Pin_ComboBox.addItem(QString(''))
        self.Pin_ComboBox.addItem(QString(''))
        self.Pin_ComboBox.addItem(QString(''))
        self.Pin_ComboBox.addItem(QString(''))
        self.Pin_ComboBox.addItem(QString(''))
        self.Pin_ComboBox.addItem(QString(''))
        self.Pin_ComboBox.setObjectName(u"Pin_ComboBox")
        self.Pin_ComboBox.setGeometry(QRect(180, 10, 91, 31))
        self.Pin_ComboBox.setFont(font3)
        self.Save_PushButton = QPushButton(Form)
        self.Save_PushButton.setObjectName(u"Save_PushButton")
        self.Save_PushButton.setGeometry(QRect(340, 260, 93, 31))
        self.Save_PushButton.setFont(font1)
        self.Load_PushButton = QPushButton(Form)
        self.Load_PushButton.setObjectName(u"Load_PushButton")
        self.Load_PushButton.setGeometry(QRect(240, 260, 93, 31))
        self.Load_PushButton.setFont(font1)

        self.retranslateUi(Form)
        self.Output_RadioButton.toggled.connect(self.InputConfigurations_GroupBox.setDisabled)
        self.Input_RadioButton.toggled.connect(self.OutputLevel_GroupBox.setDisabled)

        self.SubmitConfiguration_PushButton.clicked.connect(self.Sumbit_MyHandler)
        self.Save_PushButton.clicked.connect(self.Save_MyHandler)
        self.Load_PushButton.clicked.connect(self.Load_MyHandler)
        self.Port_ComboBox.currentTextChanged.connect(self.Setup_MyHandler)
        self.Pin_ComboBox.currentTextChanged.connect(self.Setup_MyHandler)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def Sumbit_MyHandler(self):
      x=self.Pin_GroupBox.title() 
      config[int(ord(x[4]))-int(ord('A'))][int(x[-1])]
      if self.Output_RadioButton.isChecked():
        config[int(ord(x[4]))-int(ord('A'))][int(x[-1])][2]=1
        if self.High_RadioButton.isChecked():
          config[int(ord(x[4]))-int(ord('A'))][int(x[-1])][3]=1
        else:
          config[int(ord(x[4]))-int(ord('A'))][int(x[-1])][3]=0
      else:
        config[int(ord(x[4]))-int(ord('A'))][int(x[-1])][2]=0
        if self.PullUp_RadioButton.isChecked():
          config[int(ord(x[4]))-int(ord('A'))][int(x[-1])][3]=1
        else:
          config[int(ord(x[4]))-int(ord('A'))][int(x[-1])][3]=0


    def Setup_MyHandler(self):
      x=self.Port_ComboBox.currentText()
      y=self.Pin_ComboBox.currentText()
      z=config[int(ord(x[-1]))-int(ord('A'))][int(y[-1])]
      if z[2]:
        self.Output_RadioButton.setChecked(True)
        if z[3]:
          self.High_RadioButton.setChecked(True)
        else:
          self.Low_RadioButton.setChecked(True)
      else:
        self.Input_RadioButton.setChecked(True)
        if z[3]:
          self.PullUp_RadioButton.setChecked(True)
        else:
          self.HighImpeadance_RadioButton.setChecked(True)
      self.Pin_GroupBox.setTitle(x+'_'+y)


    def Save_MyHandler(self):
      f=open('PORT_CONFIG.h','a+')
      f.truncate(0)
      for i in range(0,4,1):
        x=config[i]
        for j in range (0,8,1):
          y=config[i][j]
          f.write('#define    '+'DIO_'+y[0]+'_'+y[1]+'_'+'DIR'+'    '+str(y[2])+'\n')
          f.write('#define    '+'DIO_'+y[0]+'_'+y[1]+'_'+'INITIAL_VALUE'+'    '+str(y[3])+'\n\n')
      f.close()

    def Load_MyHandler(self):
      f=open('PORT_CONFIG.h','r+')
      lines=f.readlines()
      j=0
      for i in range(0,24,3):
        config[0][j][2]=int(lines[i][33])
        config[0][j][3]=int(lines[i+1][43])
        j=j+1
      j=0
      for i in range(24,48,3):
        config[1][j][2]=int(lines[i][33])
        config[1][j][3]=int(lines[i+1][43])
        j=j+1
      j=0
      for i in range(48,72,3):
        config[2][j][2]=int(lines[i][33])
        config[2][j][3]=int(lines[i+1][43])
        j=j+1
      j=0
      for i in range(72,96,3):
        config[3][j][2]=int(lines[i][33])
        config[3][j][3]=int(lines[i+1][43])
        j=j+1
      f.close()
      self.Setup_MyHandler()


    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Pin_GroupBox.setTitle(QCoreApplication.translate("Form", u"PORTA_PIN0", None))
        self.Output_RadioButton.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_RadioButton.setText(QCoreApplication.translate("Form", u"Input", None))
        self.OutputLevel_GroupBox.setTitle(QCoreApplication.translate("Form", u"Output Level", None))
        self.High_RadioButton.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_RadioButton.setText(QCoreApplication.translate("Form", u"Low", None))
        self.InputConfigurations_GroupBox.setTitle(QCoreApplication.translate("Form", u"Input Configurations", None))
        self.PullUp_RadioButton.setText(QCoreApplication.translate("Form", u"Pull Up", None))
        self.HighImpeadance_RadioButton.setText(QCoreApplication.translate("Form", u"High Impeadance", None))
        self.SubmitConfiguration_PushButton.setText(QCoreApplication.translate("Form", u"Submit Configuration", None))
        self.Port_ComboBox.setItemText(0, QCoreApplication.translate("Form", u"PORTA", None))
        self.Port_ComboBox.setItemText(1, QCoreApplication.translate("Form", u"PORTB", None))
        self.Port_ComboBox.setItemText(2, QCoreApplication.translate("Form", u"PORTC", None))
        self.Port_ComboBox.setItemText(3, QCoreApplication.translate("Form", u"PORTD", None))

        self.Pin_ComboBox.setItemText(0, QCoreApplication.translate("Form", u"PIN0", None))
        self.Pin_ComboBox.setItemText(1, QCoreApplication.translate("Form", u"PIN1", None))
        self.Pin_ComboBox.setItemText(2, QCoreApplication.translate("Form", u"PIN2", None))
        self.Pin_ComboBox.setItemText(3, QCoreApplication.translate("Form", u"PIN3", None))
        self.Pin_ComboBox.setItemText(4, QCoreApplication.translate("Form", u"PIN4", None))
        self.Pin_ComboBox.setItemText(5, QCoreApplication.translate("Form", u"PIN5", None))
        self.Pin_ComboBox.setItemText(6, QCoreApplication.translate("Form", u"PIN6", None))
        self.Pin_ComboBox.setItemText(7, QCoreApplication.translate("Form", u"PIN7", None))

        self.Save_PushButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.Load_PushButton.setText(QCoreApplication.translate("Form", u"Load", None))
    # retranslateUi

app = QApplication(sys.argv)
Widget = QWidget()
Form=Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())
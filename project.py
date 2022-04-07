from PyQt5 import QtWidgets
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
from reshintegral import simpson
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import matplotlib.patches as mpatches
 
init_printing()
x = Symbol('x')
 
class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.btnClicked)
		self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
 

	def btnClicked(self):
		lineeditvalue = self.ui.lineEdit.text()
		upvalue = (self.ui.lineEdit_2.text())
		downvalue = (self.ui.lineEdit_3.text())
		if lineeditvalue == "":
			error_dialog.showMessage( "Ошибка! Введите интеграл")
		elif upvalue == "":
			error_dialog.showMessage( "Ошибка! Введите верхнюю границу интегрирования")
		elif downvalue == "":
			error_dialog.showMessage( "Ошибка! Введите нижнюю границу интегрирования")
		else:
			upvalue = float(upvalue)
			downvalue = float(downvalue)
			result = simpson(lineeditvalue, upvalue, downvalue, 1000)
			otvet = str(result[0]) + " +- " + str(result[1])
			self.ui.label_4.setText(otvet)

			
	def btnClicked_2(self):
		lineeditvalue = self.ui.lineEdit.text()
		upvalue = (self.ui.lineEdit_2.text())
		downvalue = (self.ui.lineEdit_3.text())
		if lineeditvalue == "":
			error_dialog.showMessage( "Ошибка! Введите интеграл")
		elif upvalue == "":
			error_dialog.showMessage( "Ошибка! Введите верхнюю границу интегрирования")
		elif downvalue == "":
			error_dialog.showMessage( "Ошибка! Введите нижнюю границу интегрирования")
		else:
			upvalue = float(upvalue)
			downvalue = float(downvalue)
			integral = parse_expr(lineeditvalue)
			plot(integral,(x,downvalue,upvalue))
			
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
error_dialog = QtWidgets.QErrorMessage()
 
sys.exit(app.exec())

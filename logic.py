import PyQt6.QtWidgets as pyqt
import gui
import csv

class Logic(pyqt.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
  

        self.button_submitEntry.clicked.connect(lambda: self.submit())

    def submit(self):
        try:
            day = int(self.input_day.text())
            month = int(self.input_month.text())
            year = int(self.input_year.text())
            phone_hours = int(self.input_phone_hours.text())
            phone_minutes = int(self.input_phone_minutes.text())

            #check input
            if day >31 or day < 0:
                raise Exception("invalid day [{day}]")
            if month < 1 or month > 12:
                raise Exception("invalid month")
            if year < 2026 or year > 2150:
                raise Exception("invalid year")
            if phone_hours < 0 or phone_hours > 23:
                raise Exception("invalid phone hours")
            if phone_minutes < 0 or phone_minutes >59:
                raise Exception("invalid phone minutes")
        except Exception as e:
            print(e)

        

        
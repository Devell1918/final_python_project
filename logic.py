import PyQt6.QtWidgets as pyqt
import gui
import csv
from datetime import date
import pandas as pd

class Logic(pyqt.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label_message.setText("")
        self.dateEdit.setDate(date(2026, 1, 1))
        # when submit is clicked it calls sumit function
        self.button_submitEntry.clicked.connect(lambda: self.submit())

        #when the combo box is changed it calls the on_dropwon_change function
        self.combo_box.currentIndexChanged.connect(self.on_dropdown_change)

    def submit(self):
        """
        This method checks the data and then stores it into a csv
        """
        try:
            qt_date = self.dateEdit.date()
            python_date = qt_date.toPyDate()
            phone_hours = int(self.input_phone_hours.text())
            phone_minutes = int(self.input_phone_minutes.text())
            total_phone_minutes = phone_minutes + (phone_hours * 60)

            #check input
            if python_date < date(2026, 1, 1) or python_date > date.today():
                raise Exception("invalid date")
            if phone_hours < 0 or phone_hours > 23:
                raise Exception("invalid phone hours")
            if phone_minutes < 0 or phone_minutes >59:
                raise Exception("invalid phone minutes")
        except ValueError:
            self.label_message.setText("Enter valid phone time")
            return
        except Exception as e:
            print(e)
            self.label_message.setText("Enter valid phone time")
            return


        selected_caffeine = self.button_group_caffeine.checkedButton()
        selected_workout = self.button_group_workout.checkedButton()
        selected_read = self.button_group_read.checkedButton()
        selected_gamedev = self.button_group_gamedev.checkedButton()
        selected_nap = self.button_group_nap.checkedButton()
        selected_wellbeing = self.button_group_wellbeing.checkedButton()

        if selected_caffeine and selected_workout and selected_read and selected_gamedev and selected_nap and selected_wellbeing:
            caffeine_value, workout_value, read_value, gamedev_value, nap_value, wellbeing_value = self.get_values(selected_caffeine, selected_workout, selected_read, selected_gamedev, selected_nap, selected_wellbeing)
            print(python_date, phone_hours, phone_minutes, caffeine_value, workout_value, read_value, gamedev_value, nap_value, wellbeing_value)
            self.write_values(python_date, total_phone_minutes, caffeine_value, workout_value, read_value, gamedev_value, nap_value, wellbeing_value)
            #TODO write logic/ submission entered to message box
        else:
            print("Make sure each topic has a selection")
            self.label_message.setText("Make sure each topic has a selection")
            #TODO display message to user
        


            
    def on_dropdown_change(self):
        """
        this method runs when the dropdown is changed, and displays the correct data
        """
        pass

    def get_values(self, selected_caffeine: int, selected_workout: int, selected_read: int, selected_gamedev: int, selected_nap: int, selected_wellbeing: int):
        """
        takes in the selected buttons and returns their corresponding values
        """
        match selected_caffeine:
            case self.radio_caffeine_0:
                caffeine_value = 0
            case self.radio_caffeine_1:
                caffeine_value = 1
            case self.radio_caffeine_2:
                caffeine_value = 2
            case self.radio_caffeine_3:
                caffeine_value = 3
            case self.radio_caffeine_4:
                caffeine_value = 4
            case self.radio_caffeine_5:
                caffeine_value = 5
            case self.radio_caffeine_6:
                caffeine_value = 6
            case self.radio_caffeine_7:
                caffeine_value = 7
            case self.radio_caffeine_8:
                caffeine_value = 8
            case self.radio_caffeine_9:
                caffeine_value = 9
        match selected_workout:
            case self.radio_workout_no:
                workout_value = 0
            case self.radio_workout_yes:
                workout_value = 1
        match selected_read:
            case self.radio_read_no:
                read_value = 0
            case self.radio_read_yes:
                read_value = 1
        match selected_gamedev:
            case self.radio_game_no:
                gamedev_value = 0
            case self.radio_game_yes:
                gamedev_value = 1
        match selected_nap:
            case self.radio_nap_no:
                nap_value = 0
            case self.radio_nap_yes:
                nap_value = 1
        match selected_wellbeing:
            case self.radio_wellbeing_1:
                wellbeing_value = 1
            case self.radio_wellbeing_2:
                wellbeing_value = 2
            case self.radio_wellbeing_3:
                wellbeing_value = 3
            case self.radio_wellbeing_4:
                wellbeing_value = 4
            case self.radio_wellbeing_5:
                wellbeing_value = 5
            case self.radio_wellbeing_6:
                wellbeing_value = 6
            case self.radio_wellbeing_7:
                wellbeing_value = 7
            case self.radio_wellbeing_8:
                wellbeing_value = 8
            case self.radio_wellbeing_9:
                wellbeing_value = 9
            case self.radio_wellbeing_10:
                wellbeing_value = 10
        return caffeine_value, workout_value, read_value, gamedev_value, nap_value, wellbeing_value
    def write_values(self, date: date, total_phone_minutes: int, caffeine_value: int, workout_value: int, read_value: int, gamedev_value: int, nap_value: int, wellbeing_value: int):
        new_data_frame = pd.DataFrame([{"Date": date, "Phone": 0, "Caffeine": caffeine_value, "Workout": workout_value, "Read": read_value, "GameDev": gamedev_value, "Nap": nap_value, "Wellbeing": wellbeing_value}])
        data_frame = pd.read_csv("personal_stats_data.csv")


        data_frame.at[data_frame.index[-1], 'Phone'] = total_phone_minutes

        data_frame.to_csv("personal_stats_data.csv", mode='w', header=True, index=False)

        new_data_frame.to_csv("personal_stats_data.csv", mode='a', header=False, index=False)

        # code used befor switching to pandas library for easier csv manipulation
        # with open("personal_stats_data.csv", mode="r") as stat_file_r:
        #     reader = csv.reader(stat_file_r)

        #     with open("personal_stats_data.csv", mode="a", newline="") as stat_file_w:
        #         writer = csv.writer(stat_file_w)
        #         writer.writerow([date, total_phone_minutes, caffeine_value, workout_value, 0, gamedev_value, nap_value, wellbeing_value])
        #         for row in reader:
        #             print (row)
                
        self.label_message.setText("Submission Entered")

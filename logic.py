import PyQt6.QtWidgets as pyqt
import gui
from datetime import date
import pandas as pd

class Logic(pyqt.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current_stat = "Phone"
        #default values
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
            #get date and phone time
            qt_date = self.dateEdit.date()
            python_date = qt_date.toPyDate()
            phone_hours = int(self.input_phone_hours.text())
            phone_minutes = int(self.input_phone_minutes.text())
            total_phone_minutes = phone_minutes + (phone_hours * 60)
            #TODO seperate date and time try blocks
            #check input
            data_frame = pd.read_csv("personal_stats_data.csv", parse_dates=["Date"])
            if (data_frame["Date"].dt.date == python_date).any():
                raise Exception("invalid date (duplicate)")
            if python_date < date(2026, 1, 1) or python_date > date.today():
                raise Exception("invalid date")
            if phone_hours < 0 or phone_hours > 23:
                raise Exception("invalid phone hours")
            if phone_minutes < 0 or phone_minutes >59:
                raise Exception("invalid phone minutes")
        except ValueError as e:
            self.label_message.setText("Enter valid phone time")
            print(e)
            return
        except Exception as e:
            print(e)
            self.label_message.setText("Enter valid phone time")
            return

        #get selections
        selected_caffeine = self.button_group_caffeine.checkedButton()
        selected_workout = self.button_group_workout.checkedButton()
        selected_read = self.button_group_read.checkedButton()
        selected_gamedev = self.button_group_gamedev.checkedButton()
        selected_nap = self.button_group_nap.checkedButton()
        selected_wellbeing = self.button_group_wellbeing.checkedButton()

        #I know I should have used a list, but this works okay because I don't have a ton of values
        if selected_caffeine and selected_workout and selected_read and selected_gamedev and selected_nap and selected_wellbeing:
            caffeine_value, workout_value, read_value, gamedev_value, nap_value, wellbeing_value = self.get_values(selected_caffeine, selected_workout, selected_read, selected_gamedev, selected_nap, selected_wellbeing)
            print(python_date, phone_hours, phone_minutes, caffeine_value, workout_value, read_value, gamedev_value, nap_value, wellbeing_value)
            self.write_values(python_date, total_phone_minutes, caffeine_value, workout_value, read_value, gamedev_value, nap_value, wellbeing_value)
        else:
            print("Make sure each topic has a selection")
            self.label_message.setText("Make sure each topic has a selection")
            
        


            
    def on_dropdown_change(self):
        """
        this method runs when the dropdown is changed, and displays the correct data
        """
        data_frame = pd.read_csv("personal_stats_data.csv", parse_dates=["Date"])
        if self.combo_box.currentIndex() == 0:
            print("Phone Time Selected")
            self.calculate_and_set_averages("Phone", data_frame)
        if self.combo_box.currentIndex() == 1:
            print("Caffeine Selected")    
            self.calculate_and_set_averages("Caffeine", data_frame)    
        if self.combo_box.currentIndex() == 2:
            print("Workout Selected")
            self.calculate_and_set_averages("Workout", data_frame)  
        if self.combo_box.currentIndex() == 3:
            print("Read Selected")
            self.calculate_and_set_averages("Read", data_frame)  
        if self.combo_box.currentIndex() == 4:
            print("Game Dev Selected")
            self.calculate_and_set_averages("GameDev", data_frame)  
        if self.combo_box.currentIndex() == 5:
            print("Nap Selected")      
            self.calculate_and_set_averages("Nap", data_frame)    
        if self.combo_box.currentIndex() == 6:
            print("Wellbeing Selected")
            self.calculate_and_set_averages("Wellbeing", data_frame)  


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
        """
        takes values and writes them to a csv file
        """
        new_data_frame = pd.DataFrame([{"Date": date, "Phone": 0, "Caffeine": caffeine_value, "Workout": workout_value, "Read": read_value, "GameDev": gamedev_value, "Nap": nap_value, "Wellbeing": wellbeing_value}])
        data_frame = pd.read_csv("personal_stats_data.csv", parse_dates=["Date"])


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
        data_frame
        #refresh averages
        data_frame = pd.read_csv("personal_stats_data.csv", parse_dates=["Date"])
        self.calculate_and_set_averages(self.current_stat, data_frame)

    def calculate_and_set_averages(self, column: str, data_frame):
            """
            calculates the averages and then sets the labels accordingly

            :param column: the column to be averaged
            :param data_frame: the csv data
            """

            if column == "Phone":
                week_av = data_frame[column].iloc[-7:-1].mean()
                rounded_week_av = f'{week_av: .2f}'
                self.label_weekly_output.setText(rounded_week_av)

                month_av = data_frame[column].iloc[-31:-1].mean()
                rounded_month_av = f'{month_av: .2f}'
                self.label_monthly_output.setText(rounded_month_av)

                start_av = data_frame[column].iloc[0:-1].mean()
                rounded_start_av = f'{start_av: .2f}'
                self.label_start_ouput.setText(rounded_start_av)
            else:
                week_av = data_frame[column].iloc[-6:].mean()
                rounded_week_av = f'{week_av: .2f}'
                self.label_weekly_output.setText(rounded_week_av)

                month_av = data_frame[column].iloc[-30:].mean()
                rounded_month_av = f'{month_av: .2f}'
                self.label_monthly_output.setText(rounded_month_av)

                start_av = data_frame[column].iloc[0:].mean()
                rounded_start_av = f'{start_av: .2f}'
                self.label_start_ouput.setText(rounded_start_av)

            #value used to refresh values when submit is pressed
            self.current_stat = column



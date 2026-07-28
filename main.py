from logic import *
def main():
    application = pyqt.QApplication([])
    window = Logic()
    window.show()
    window.setWindowTitle("Test 10")
    application.exec()

if __name__ == '__main__':
    main()
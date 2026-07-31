from logic import *
def main():
    application = pyqt.QApplication([])
    window = Logic()
    window.show()
    window.setWindowTitle("Final Project")
    application.exec()

if __name__ == '__main__':
    main()
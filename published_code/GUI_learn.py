import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QCheckBox, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MY First GUI")
        self.setGeometry(1200, 200, 600, 500)
        self.setWindowIcon(QIcon("icon_image.png"))
        self.label = QLabel("Are you sure want to submit?", self)
        self.checkbox = QCheckBox("Are you okay with sharing your data?", self)
        self.radio1 = QRadioButton("Mark if you have interest in python?", self)
        self.radio2 = QRadioButton("Mark if you live in U.S?", self)
        self.radio3 = QRadioButton("Mark if you have experience?", self)
        self.radio4 = QRadioButton("Mark if have a degree?", self)
        self.radio5 = QRadioButton("Mark if you are fluent in english?", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.button_group3 = QButtonGroup(self)
        self.button_group4 = QButtonGroup(self)
        self.button_group5 = QButtonGroup(self)
        self.button1 = QPushButton("submit", self)
        self.line_edit = QLineEdit(self)
        self.initUI()

    def initUI(self):

        # LABEL HEADER
        self.label.setGeometry(80, 350, 400, 150)
        self.label.setStyleSheet("Font-size: 30px;")

        label = QLabel("Hello, Welcome", self)
        label.setFont(QFont("Arial", 20))
        label.setGeometry(0, 0, 600, 50)
        label.setStyleSheet("color: Black;"
                            "Background-color: yellow;")
        label.setAlignment(Qt.AlignCenter)


        # CHECKBOX 
        self.checkbox.setGeometry(10, 100, 400, 50)
        self.checkbox.setStyleSheet("Font-size: 20px;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)



        # BUTTON 
        self.button = QPushButton("submit", self)
        self.button.setGeometry(200, 450, 150, 50)
        self.button.setStyleSheet("Font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        # RADIOBUTTON 
        self.radio1.setGeometry(10, 150, 300, 50)
        self.radio2.setGeometry(10, 200, 300, 50)
        self.radio3.setGeometry(10, 250, 300, 50)
        self.radio4.setGeometry(10, 300, 300, 50)
        self.radio5.setGeometry(10, 350, 300, 50)

        self.setStyleSheet("QradioButton {"
                           "Font-size: 20px;"
                           "Font-family: Arial;" 
                           "padding: 10px;"
                           "}")
        
        self.button_group1.addButton(self.radio1)
        self.button_group2.addButton(self.radio2)
        self.button_group3.addButton(self.radio3)
        self.button_group4.addButton(self.radio4)
        self.button_group5.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)


        # NAME TAG ON THE TOP 
        self.line_edit.setGeometry(0, 60, 150, 40)
        self.line_edit.setStyleSheet("{"
                                     "font-size: 30px;"
                                     "font-family: arial;"
                                     "}")
        self.button1.setGeometry(160, 60, 100, 40)
        self.line_edit.setPlaceholderText("Enter your name")
        self.button1.clicked.connect(self.submit_name)




    def on_click(self):
        print("The Form is submitted")
        self.button.setText("Submitted")


    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("Yes I am okay with sharing my data.")
        else:
            print("No, I am not okay with it.")

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():\
        print(f"{radio_button.text()} is Marked.")

    def submit_name(self):
        text = self.line_edit.text()
        print(f"Hello {text}, welcome to my GUI APP!")




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



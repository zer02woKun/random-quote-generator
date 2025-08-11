from PyQt5.QtWidgets import QMainWindow, QGridLayout, QHBoxLayout, QVBoxLayout, QApplication, QWidget, QLineEdit, QTextEdit, QPushButton
from PyQt5.QtCore import Qt
import sys
import requests
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0, 300, 300)
        self.setWindowTitle("Random Quote Generator")
        
        self.textBox = QTextEdit()
        self.textBox.setObjectName("TextScreen")
        self.textBox.setAlignment(Qt.AlignCenter)
        self.button = QPushButton("Generate")
        self.button.setObjectName("Ok")
        self.button.clicked.connect(self.getRandomQuote)

        self.button1 = QPushButton("Copy")
        self.button1.clicked.connect(self.copyToClipboard)
        
        

        self.initUI()






    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        mainLayout = QVBoxLayout()


        
        hBox = QHBoxLayout()
        hBox.addWidget(self.textBox)
        
        self.textBox.setReadOnly(True)
        

        hBox1 = QHBoxLayout()
        self.button.setMaximumSize(300, 100)
        self.button1.setMaximumSize(150,100)
        hBox1.addWidget(self.button1,0)
        hBox1.addWidget(self.button,1)
        

        mainLayout.addLayout(hBox)
        mainLayout.addSpacing(50)
        mainLayout.addLayout(hBox1)

        
        


        


        central_widget.setLayout(mainLayout)

        self.setStyleSheet("""QPushButton#Ok{ padding: 20px;}QTextEdit{ font-size: 20px;}


""")

    #get a random quote on the zenquotes website, then update the textbox
    def getRandomQuote(self)-> None:
        url = "https://zenquotes.io/api/random"
        response = requests.get(url)

        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']

        self.textBox.setPlainText(f"{quote} -{author}")
        self.randomizeStyles()
        print(quote)

    #copies the quote then add it to the clipboard
    def copyToClipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.textBox.toPlainText())
        print("copied")
    #gives the quote a random styles
    def randomizeStyles(self)-> None:
        fonts = ["Courier New","Georgia", "Papyrus"]
        font = random.choice(fonts)
        print(font)
        self.textBox.setStyleSheet(f"font-family:{font};")
        


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())





main()

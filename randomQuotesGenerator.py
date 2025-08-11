from PyQt5.QtWidgets import QMainWindow, QGridLayout, QHBoxLayout, QVBoxLayout, QApplication, QWidget, QLineEdit, QTextEdit, QPushButton
from PyQt5.QtCore import Qt
import sys
import requests



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0, 300, 300)
        self.setWindowTitle("Random Quote Generator")
        
        self.textBox = QTextEdit()
        self.button = QPushButton("Generate")
        self.button.setObjectName("Ok")
        self.button.clicked.connect(self.getRandomQuote)
        
        

        self.initUI()






    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        mainLayout = QVBoxLayout()


        
        hBox = QHBoxLayout()
        hBox.addWidget(self.textBox)
        
        self.textBox.setReadOnly(True)
        self.textBox.setAlignment(Qt.AlignCenter)

        hBox1 = QHBoxLayout()
        hBox1.addWidget(self.button)
    

        


        mainLayout.addLayout(hBox)
        mainLayout.addLayout(hBox1)

        
        


        


        central_widget.setLayout(mainLayout)

        self.setStyleSheet("""QPushButton#Ok{ padding: 20px; max-width: 200px}QTextEdit{ font-size: 20px}


""")

    #get a random quote on the zenquotes website, then update the textbox
    def getRandomQuote(self):
        url = "https://zenquotes.io/api/random"
        response = requests.get(url)

        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        self.textBox.setPlainText(f"{quote} -{author}")
        print(quote)






def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())





main()

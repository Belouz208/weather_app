import sys
import requests
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout)
from PyQt5.QtCore import Qt


# f414e56e7e94d1f6ea12a2ec435a3cbd
class WeatherApp(QWidget):

    def __init__(self):
        super().__init__( )
        self.city_label = QLabel("Enter city name :",self)
        self.city_input =QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather",self)
        self.temperature_label = QLabel("70°F",self)
        self.emoji_label=QLabel( "☀️",self)
        self.description_label = QLabel("sunny",self)

        self.initUI()



    def initUI(self):
        self.setWindowTitle("weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_input)
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_label.setAlignment(Qt.AlignCenter)

#bonjour












        pass







if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())




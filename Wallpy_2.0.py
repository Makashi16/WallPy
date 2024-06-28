import sys
import random
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QInputDialog, QMessageBox, QComboBox
class WallPy(QWidget):
    def __init__(self):
        super().__init__()
        self.running = True
        self.money = 100
        self.round = 0
        self.item = {
            'none': "none",
            'petrol':0,
            'iron':0,
            'water':0,
        }
        self.prices = {
            'petrol': 0, 
            'iron': 0,
            'water':0,
            }
        self.possessed = {
            'petrol': 0, 
            'iron': 0,
            'water': 0,
            }
        self.products = {
            'petrol': 0, 
            'iron': 0,
            'water': 0,
        }
        self.mission ={
            'Earn 1 million $': False,
            'Earn 156 petrol stock': False,
            'Be alive at the round 100': False

        }
        QMessageBox.information(self, "Intro", "Hello young biusnessman. Today you will practice in WallPy 2.0, the new simplified stock exchange simulator by Makashi_16. It's very easy to use so don't be shy. I'm WallPy Guard. I will call you if you make trouble. You can see your missions on the button clear mission. GOOD LUCK !!!")
        self.initUI()
    def initUI(self):
        self.setWindowTitle("WallPy 2.0")
        self.info_label = QLabel("Bienvenue dans WallPy 2.0", self)
        self.info2_label = QLabel("Welcome to the Lobby, what do you wand to do ?", self)
        self.money_label = QLabel(f"${self.money}", self)
        self.round_label = QLabel(f"Round: {self.round}", self)
        self.petrol_price_label = QLabel(f"Price: petrol : {self.prices['petrol']}", self)
        self.iron_price_label = QLabel(f"Price: iron : {self.prices['iron']}", self)
        self.water_price_label = QLabel(f"Price: water : {self.prices['water']}", self)
        self.petrol_possessed_label = QLabel(f"Owned : petrol : {self.possessed['petrol']}", self)
        self.iron_possessed_label = QLabel(f"Owned: iron : {self.possessed['iron']}", self)
        self.water_possessed_label = QLabel(f"Owned: water : {self.possessed['water']}", self)
        self.buy_button = QPushButton("Buy", self)
        self.sell_button = QPushButton("Sell", self)
        self.pass_button = QPushButton("Pass", self)
        self.mission_button = QPushButton("Clear a mission", self)
        self.exit_button = QPushButton("Exit", self)

        self.buy_button.clicked.connect(self.on_buy)
        self.sell_button.clicked.connect(self.on_sell)
        self.pass_button.clicked.connect(self.on_pass)
        self.mission_button.clicked.connect(self.on_mission)
        self.exit_button.clicked.connect(self.on_exit)

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addWidget(self.info2_label)
        layout.addWidget(self.round_label)
        layout.addWidget(self.money_label)
        layout.addWidget(self.petrol_price_label)
        layout.addWidget(self.iron_price_label)
        layout.addWidget(self.water_price_label)
        layout.addWidget(self.petrol_possessed_label)
        layout.addWidget(self.iron_possessed_label)
        layout.addWidget(self.water_possessed_label)
        layout.addWidget(self.buy_button)
        layout.addWidget(self.sell_button)
        layout.addWidget(self.pass_button)
        layout.addWidget(self.mission_button)
        layout.addWidget(self.exit_button)
        self.setLayout(layout)
    ans2 = 0
    def buy_combo_selected(self):
        global ans2
        ans2 = self.combo.currentText()
        ans3, ok = QInputDialog.getInt(self, "Buy", f"How much {ans2} do you want to buy?")
        if ok and (ans3*self.prices[ans2]) <= self.money:
            self.possessed[ans2] += ans3
            self.money -= ans3 * self.prices[ans2]
            self.round += 1
            self.mixPrice()
            self.updateLabels()
            if ans2 != "---none---":
                self.combo.deleteLater()
        else:
            self.error()
            self.combo.deleteLater()
    def on_buy(self):       
        global ans2
        layout = QVBoxLayout()
        self.combo = QComboBox()
        self.combo.addItem("---none---")
        self.combo.addItem("petrol")
        self.combo.addItem("iron")
        self.combo.addItem("water")
        self.combo.currentIndexChanged.connect(self.buy_combo_selected)
        layout.addWidget(self.combo)
        self.combo.show()
    def sell_combo_selected(self):
        ans2 = self.combo.currentText()
        if ans2 in self.prices:
            ans3, ok = QInputDialog.getInt(self, "Sell", f"How much {ans2} do you want to sell?")
            k = self.possessed.get(ans2)
            if ok and ans3 <= k:
                self.possessed[ans2] -= ans3
                self.money += ans3 * self.prices[ans2]
                self.round += 1
                self.mixPrice()
                self.updateLabels()
                if ans2 != "---none---":
                    self.combo.deleteLater()
            else:
                self.error()
                self.combo.deleteLater()
        else:
            self.error()
    def on_sell(self):
        layout = QVBoxLayout()
        self.combo = QComboBox()
        self.combo.addItem("---none---")
        self.combo.addItem("petrol")
        self.combo.addItem("iron")
        self.combo.addItem("water")
        self.combo.currentIndexChanged.connect(self.sell_combo_selected)
        layout.addWidget(self.combo)
        self.setLayout(layout)
        self.combo.show()
    def on_pass(self):
        if self.money >= 10:
            self.money -= 10
            QMessageBox.information(self, "Pass", "You waited for a better price, you lose $10.")
            self.round += 1
            self.mixPrice()
            self.updateLabels()
        else:
            self.error()
    def on_mission(self):
        layout = QVBoxLayout()
        self.combo = QComboBox()
        self.combo.addItem("---none---")
        if self.mission['Earn 1 million $'] == True and self.mission['Earn 156 petrol stock'] == True and self.mission['Be alive at the round 100'] == True: 
            QMessageBox.information(self, "Mission", "Conglurations, Yout last mission is to share this game to 2 friends")
        else:
            if self.mission['Earn 1 million $'] == False:
                self.combo.addItem("Earn 1 million $")
            if self.mission['Earn 156 petrol stock'] == False:
                self.combo.addItem("Earn 156 petrol stock")
            if self.mission['Be alive at the round 100'] == False:
                self.combo.addItem("Be alive at the round 100")
            self.combo.currentIndexChanged.connect(self.mission_combo_selected)
            layout.addWidget(self.combo)
            self.combo.show()
    def mission_combo_selected(self):
        ans2 = self.combo.currentText()
        if ans2 in self.mission:
            if ans2 == "Earn 1 million $":
                if self.money >= 1000000:
                    self.money -= 1000000
                    self.mission['Earn 1 million $'] = True
                    QMessageBox.information(self, "Mission", "Conglurations, you have completed succesfully this mission !!!")
                    self.possessed["petrol"] += random.randint(1, 50)
                    self.possessed["iron"] += random.randint(1, 50)
                    self.possessed["water"] += random.randint(1, 50)
                    if ans2 != "---none---":
                        self.combo.deleteLater()
                else:
                    self.error()
                    self.combo.deleteLater()
            elif ans2 == "Earn 156 petrol stock":
                if self.possessed["petrol"] >= 156:
                    self.possessed["petrol"] -= 156
                    self.mission['Earn 156 petrol stock'] = True
                    QMessageBox.information(self, "Mission", "Conglurations, you have completed succesfully this mission !!!")
                    self.money += random.randint(10000, 100000)
                    if ans2 != "---none---":
                        self.combo.deleteLater()
                else:
                    self.error()
                    self.combo.deleteLater()
            elif ans2 == "Be alive at the round 100":
                if round >= 100:
                    self.mission['Be alive at the round 100'] = True
                    QMessageBox.information(self, "Mission", "Conglurations, you have completed succesfully this mission !!! Now you are a professianal buisnessman")
                    self.possessed["petrol"] += random.randint(1, 50)
                    self.possessed["iron"] += random.randint(1, 50)
                    self.possessed["water"] += random.randint(1, 50)
                    self.money += random.randint(100000, 1000000)
                    if ans2 != "---none---":
                        self.combo.deleteLater()
                else:
                    self.error()
                    self.combo.deleteLater()
    def on_exit(self):
        self.running = False
        self.close()
    def updateLabels(self):
        self.money_label.setText(f"${self.money}")
        self.round_label.setText(f"Round: {self.round}")
        self.petrol_possessed_label.setText(f"Owned : petrol : {self.possessed['petrol']}")
        self.iron_possessed_label.setText(f"Owned: iron : {self.possessed['iron']}")
        self.water_possessed_label.setText(f"Owned: water : {self.possessed['water']}")
        self.petrol_price_label.setText(f"Price: petrol : {self.prices['petrol']}")
        self.iron_price_label.setText(f"Price: iron : {self.prices['iron']}")
        self.water_price_label.setText(f"Price: water : {self.prices['water']}")
    def error(self):
        QMessageBox.warning(self, "Error", "WallPy guard : Please don't make trouble, I will guide you to the lobby")
    def mixPrice(self):
        self.prices['petrol'] = random.randint(1, 50)
        self.prices['iron'] = random.randint(1, 50)
        self.prices['water'] = random.randint(1, 50)
if __name__ == "__main__":
    app = QApplication([])
    window = WallPy()
    window.mixPrice()
    window.updateLabels()
    window.show()
    sys.exit(app.exec_())
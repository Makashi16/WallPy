import sys
import random
import os
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QInputDialog, QMessageBox, QComboBox
class WallPy(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wallpy")
        self.running = True
        self.money = 100
        self.round = 0
        self.q = False
        self.item = {
            'none': "none",
            'petrol':0,
            'iron':0,
            'water':0,
            'wood':0,
            'coffee':0,
            'wheat':0,
        }
        self.prices = {
            'petrol': 0, 
            'iron': 0,
            'water':0,
            'wood':0,
            'coffee':0,
            'wheat':0,
            }
        self.possessed = {
            'petrol': 0, 
            'iron': 0,
            'water': 0,
            'wood':0,
            'coffee':0,
            'wheat':0,
            }
        self.products = {
            'petrol': 0, 
            'iron': 0,
            'water': 0,
            'wood':0,
            'coffee':0,
            'wheat':0,
        }
        self.mission ={
            'Millionaire : Earn 1 million $': False,
            'Petrol King : Earn 500 petrol stock': False,
            'Always awake : Earn 500 coffee stock':False,
            'Never thirst : Earn 500 water stock':False,
            'Country guy : Earn 500 wheat stock':False,
            'Iron man : Earn 500 iron stock':False,
            'Lumberjack : Earn 500 wood stock':False,
            'Survivor : Be alive at the round 100': False

        }
        file_path = '/home/baptiste/python/qt/WallPy2.2_save.txt'
        if os.path.exists(file_path):
            ok = QMessageBox.question(self,"Save", "WallPy Guard has detected a save file, do you want to load the save")
            if ok  == 16384:
                f = open("WallPy2.2_save.txt", "r")
                self.money = int(f.readline())
                self.round = int(f.readline())
                self.json_prices = f.readline()
                self.prices = json.loads(self.json_prices)
                self.json_possessed = f.readline()
                self.possessed = json.loads(self.json_possessed)
                self.json_missions = f.readline()
                self.mission = json.loads(self.json_missions)
            else:
                QMessageBox.information(self, "Intro", "Hello young biusnessman. Today you will practice in WallPy, the new simplified stock exchange simulator by Makashi_16. It's very easy to use so don't be shy. I'm WallPy Guard. I will call you if you make trouble. You can see your missions on the button clear mission. GOOD LUCK !!!")
                QMessageBox.warning(self, '/!\ WARNING /!\ ', 'For save you game use save and exit buttun. if you use the X in the top of the window it will be dont work')
                self.mixPrice()
        else:
            QMessageBox.information(self, "Intro", "Hello young biusnessman. Today you will practice in WallPy, the new simplified stock exchange simulator by Makashi_16. It's very easy to use so don't be shy. I'm WallPy Guard. I will call you if you make trouble. You can see your missions on the button clear mission. GOOD LUCK !!!")
            QMessageBox.warning(self, '/!\ WARNING /!\ ', 'For save you progression, use save and exit buttun. If you use the X in the top of the main window, it will be dont save your progression.')        
            self.mixPrice()

        self.initUI()
    def initUI(self):
        self.setWindowTitle("WallPy")
        self.info_label = QLabel("Bienvenue dans WallPy", self)
        self.info2_label = QLabel("Welcome to the Lobby, what do you wand to do ?", self)
        self.money_label = QLabel(f"${self.money}", self)
        self.round_label = QLabel(f"Round: {self.round}", self)
        self.petrol_price_label = QLabel(f"Price: petrol : {self.prices['petrol']}", self)
        self.iron_price_label = QLabel(f"Price: iron : {self.prices['iron']}", self)
        self.water_price_label = QLabel(f"Price: water : {self.prices['water']}", self)
        self.wood_price_label = QLabel(f"Price: wood : {self.prices['wood']}", self)
        self.coffee_price_label = QLabel(f"Price: coffee : {self.prices['coffee']}", self)
        self.wheat_price_label = QLabel(f"Price: wheat : {self.prices['wheat']}", self)
        self.petrol_possessed_label = QLabel(f"Owned : petrol : {self.possessed['petrol']}", self)
        self.iron_possessed_label = QLabel(f"Owned: iron : {self.possessed['iron']}", self)
        self.water_possessed_label = QLabel(f"Owned: water : {self.possessed['water']}", self)
        self.wood_possessed_label = QLabel(f"Owned: wood : {self.possessed['wood']}", self)
        self.coffee_possessed_label = QLabel(f"Owned: coffee : {self.possessed['coffee']}", self)
        self.wheat_possessed_label = QLabel(f"Owned: wheat : {self.possessed['wheat']}", self)
        self.buy_button = QPushButton("Buy", self)
        self.sell_button = QPushButton("Sell", self)
        self.pass_button = QPushButton("Pass", self)
        self.mission_button = QPushButton("Clear a mission", self)
        self.exit_button = QPushButton("Save and exit", self)

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
        layout.addWidget(self.wood_price_label)
        layout.addWidget(self.coffee_price_label)
        layout.addWidget(self.wheat_price_label)
        layout.addWidget(self.petrol_possessed_label)
        layout.addWidget(self.iron_possessed_label)
        layout.addWidget(self.water_possessed_label)
        layout.addWidget(self.wood_possessed_label)
        layout.addWidget(self.coffee_possessed_label)
        layout.addWidget(self.wheat_possessed_label)
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
            self.save()
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
        self.combo.addItem("wood")
        self.combo.addItem("coffee")
        self.combo.addItem("wheat")
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
                self.save()
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
        self.combo.addItem("wood")
        self.combo.addItem("coffee")
        self.combo.addItem("wheat")
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
            self.save()
        else:
            self.error()
    def missionC(self):
        a = 0
        for k in self.mission:
            if  self.mission.keys() == True:
                    a += 1
                    if a == 8:
                        QMessageBox.information(self, 'Mission completed', "Congluration you have done all missions !!! So your last mission is to share this game to 2 friends or more.")
                        self.q = True
    def on_mission(self):
        self.missionC()
        print(self.mission)
        if self.q == False:
            layout = QVBoxLayout()
            self.combo = QComboBox()
            self.combo.addItem("---none---")
            if self.mission['Millionaire : Earn 1 million $'] == False:
                self.combo.addItem("Millionaire : Earn 1 million $")
            if self.mission['Petrol King : Earn 500 petrol stock'] == False:
                self.combo.addItem("Petrol King : Earn 500 petrol stock")
            if self.mission['Always awake : Earn 500 coffee stock'] == False:
                self.combo.addItem("Always awake : Earn 500 coffee stock")
            if self.mission['Never thirst : Earn 500 water stock'] == False:
                self.combo.addItem("Never thirst : Earn 500 water stock")
            if self.mission['Country guy : Earn 500 wheat stock'] == False:
                self.combo.addItem("Country guy : Earn 500 wheat stock")
            if self.mission['Iron man : Earn 500 iron stock'] == False:
                self.combo.addItem("Iron man : Earn 500 iron stock")
            if self.mission['Lumberjack : Earn 500 wood stock'] == False:
                self.combo.addItem("Lumberjack : Earn 500 wood stock")
            if self.mission['Survivor : Be alive at the round 100'] == False:
                self.combo.addItem("Survivor : Be alive at the round 100")
                
            self.combo.currentIndexChanged.connect(self.mission_combo_selected)
            layout.addWidget(self.combo)
            self.combo.show()
    def mission_combo_selected(self):
        ans2 = self.combo.currentText()
        if ans2 == "Millionaire : Earn 1 million $":
            if self.money >= 1000000:
                self.money -= 1000000
                self.mission['Millionaire : Earn 1 million $'] = True
                QMessageBox.information(self, "Mission", "Conglurations, you have completed succesfully this mission !!!")
                self.possessed["petrol"] += random.randint(1, 50)
                self.possessed["iron"] += random.randint(1, 50)
                self.possessed["water"] += random.randint(1, 50)
                self.possessed["wood"] += random.randint(1, 50)
                self.possessed["coffee"] += random.randint(1, 50)
                self.possessed["wheat"] += random.randint(1, 50)
                self.updateLabels()
                self.save()
                if ans2 != "---none---":
                    self.combo.deleteLater()
            else:
                self.error()
                self.combo.deleteLater()
        elif ans2 == "Petrol King : Earn 500 petrol stock":
            if self.possessed["petrol"] >= 500:
                self.possessed["petrol"] -= 500
                self.mission['Petrol King : Earn 500 petrol stock'] = True
                QMessageBox.information(self, "Mission", "Conglurations, you have completed succesfully this mission !!!")
                self.money += random.randint(10000, 100000)
                self.updateLabels()
                self.save()
                if ans2 != "---none---":
                    self.combo.deleteLater()
            else:
                self.error()
                self.combo.deleteLater()
        elif ans2 == "Always awake : Earn 500 coffee stock":
            if self.possessed["coffee"] >= 500:
                self.possessed["coffee"] -= 500
                self.mission['Always awake : Earn 500 coffee stock'] = True
                QMessageBox.information(self, "Mission", "Conglurations, you have completed succesfully this mission !!!")
                self.money += random.randint(10000, 100000)
                self.updateLabels()
                self.save()
                if ans2 != "---none---":
                    self.combo.deleteLater()
            else:
                self.error()
                self.combo.deleteLater()
        elif ans2 == "Never thirst : Earn 500 water stock":
            if self.possessed["water"] >= 500:
                self.possessed["water"] -= 500
                self.mission['Never thirst : Earn 500 water stock'] = True
                QMessageBox.information(self, "Mission", "Conglurations, you have completed succesfully this mission !!!")
                self.money += random.randint(10000, 100000)
                self.updateLabels()
                self.save()
                if ans2 != "---none---":
                    self.combo.deleteLater()
            else:
                self.error()
                self.combo.deleteLater()
        elif ans2 == "Country guy : Earn 500 wheat stock":
            if self.possessed["wheat"] >= 500:
                self.possessed["wheat"] -= 500
                self.mission['Country guy : Earn 500 wheat stock'] = True
                QMessageBox.information(self, "Mission", "Conglurations, you have completed succesfully this mission !!!")
                self.money += random.randint(10000, 100000)
                self.updateLabels()
                self.save()
                if ans2 != "---none---":
                    self.combo.deleteLater()
            else:
                self.error()
                self.combo.deleteLater()
        elif ans2 == "Iron man : Earn 500 iron stock":
            if self.possessed["iron"] >= 500:
                self.possessed["iron"] -= 500
                self.mission['Iron man : Earn 500 iron stock'] = True
                QMessageBox.information(self, "Mission", "Conglurations, you have completed succesfully this mission !!!")
                self.money += random.randint(10000, 100000)
                self.updateLabels()
                self.save()
                if ans2 != "---none---":
                    self.combo.deleteLater()
            else:
                self.error()
                self.combo.deleteLater()
        elif ans2 == "Lumberjack : Earn 500 wood stock":
                if self.possessed["wood"] >= 500:
                    self.possessed["wood"] -= 500
                    self.mission['Lumberjack : Earn 500 wood stock'] = True
                    QMessageBox.information(self, "Mission", "Conglurations, you have completed succesfully this mission !!!")
                    self.money += random.randint(10000, 100000)
                    self.updateLabels()
                    self.save()
                    if ans2 != "---none---":
                        self.combo.deleteLater()
                else:
                    self.error()
                    self.combo.deleteLater()
        elif ans2 == "Survivor : Be alive at the round 100":
            if self.round >= 100:
                self.mission['Survivor : Be alive at the round 100'] = True
                QMessageBox.information(self, "Mission", "Conglurations, you have completed succesfully this mission !!! Now you are a professianal buisnessman")
                self.possessed["petrol"] += random.randint(1, 50)
                self.possessed["iron"] += random.randint(1, 50)
                self.possessed["water"] += random.randint(1, 50)
                self.possessed["wood"] += random.randint(1, 50)
                self.possessed["coffee"] += random.randint(1, 50)
                self.possessed["wheat"] += random.randint(1, 50)
                self.money += random.randint(100000, 1000000)
                self.updateLabels()
                self.save()
                if ans2 != "---none---":
                    self.combo.deleteLater()
            else:
                self.error()
                self.combo.deleteLater()
    def on_exit(self):
        self.running = False
        self.save()
        self.close()
    def updateLabels(self):
        self.money_label.setText(f"${self.money}")
        self.round_label.setText(f"Round: {self.round}")
        self.petrol_possessed_label.setText(f"Owned : petrol : {self.possessed['petrol']}")
        self.iron_possessed_label.setText(f"Owned: iron : {self.possessed['iron']}")
        self.water_possessed_label.setText(f"Owned: water : {self.possessed['water']}")
        self.wood_possessed_label.setText(f"Owned: wood : {self.possessed['wood']}")
        self.coffee_possessed_label.setText(f"Owned: coffee : {self.possessed['coffee']}")
        self.wheat_possessed_label.setText(f"Owned: wheat : {self.possessed['wheat']}")
        self.petrol_price_label.setText(f"Price: petrol : {self.prices['petrol']}")
        self.iron_price_label.setText(f"Price: iron : {self.prices['iron']}")
        self.water_price_label.setText(f"Price: water : {self.prices['water']}")
        self.wood_price_label.setText(f"Price: wood : {self.prices['wood']}")
        self.coffee_price_label.setText(f"Price: coffee : {self.prices['coffee']}")
        self.wheat_price_label.setText(f"Price: wheat : {self.prices['wheat']}")
        if self.money <= 10 and self.possessed['petrol'] == 0 and self.possessed['iron'] == 0 and self.possessed['water'] == 0 and self.possessed['wood'] == 0 and self.possessed['coffee'] == 0 and self.possessed['wheat'] == 0 :
            QMessageBox.information(self, "Looser", "Wallpy Guard : Oh my God !!! Return to school you need it !")
            self.close()
    def error(self):
        QMessageBox.warning(self, "Error", "WallPy guard : Please don't make trouble, I will guide you to the lobby")
    def mixPrice(self):
        self.prices['petrol'] = random.randint(1, 50)
        self.prices['iron'] = random.randint(1, 50)
        self.prices['water'] = random.randint(1, 50)
        self.prices['wood'] = random.randint(1, 50)
        self.prices['coffee'] = random.randint(1, 50)
        self.prices['wheat'] = random.randint(1, 50)
    def save(self):
        f = open("WallPy2.2_save.txt", "w")
        f.write(f"{self.money}\n")
        f.write(f"{self.round}\n")
        f.write(f"{json.dumps(self.prices)}\n")
        f.write(f"{json.dumps(self.possessed)}\n")
        f.write(f"{json.dumps(self.mission)}\n")
        f.close()
if __name__ == "__main__":

    app = QApplication([])
    window = WallPy()
    window.updateLabels()
    window.show()
    sys.exit(app.exec_())
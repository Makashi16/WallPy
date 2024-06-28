import random
money = 100
petrol_price = 0
iron_price = 0
water_price = 0
my_petrol = 0
my_iron = 0
my_water = 0
ans = 0
ans2 = 0
ans3 = 0
mission1 = 0
round = 0

prices = {
    'iron': 0,
    'petrol':0,
    'water': 0,
    'wood' : 0,
    'coffee': 0,
    'wheat':0,
}
possessed = {
    'iron': 0,
    'petrol':0,
    'water': 0,
    'wood' : 0,
    'coffee': 0,
    'wheat':0,
}
def showValue():
    print("money: $", money)
    print("petrol_price:", prices["petrol"])
    print("iron_price:", prices["iron"])
    print("water_price:", prices["water"])
    print("wood_price:", prices["wood"])
    print("coffee_price:", prices["coffee"])
    print("wheat_price:", prices["wheat"])
    print("my_petrol:", possessed["petrol"])
    print("my_iron", possessed["iron"])
    print("my_water", possessed["water"])
    print("my_wood:", possessed["wood"])
    print("my_coffee:", possessed["coffee"])
    print("my_wheat:", possessed["wheat"])
def mixPrice():
    global prices
    prices["petrol"] = random.randint(1,50)
    prices["iron"] = random.randint(1,50)
    prices["water"] = random.randint(1,50)
    prices["wood"] = random.randint(1,50)
    prices["coffee"] = random.randint(1,50)
    prices["wheat"] = random.randint(1,50)
def showMission():
    print("Mission:")
    if mission1 == 0:
        print("1. Earn $1,000")
    else: 
        print("No task ;) ")
def error():
    print("It's not possible try again")

print(" Hello young entrepreneur. Welcome to WallPy, the new stock exchange simulator by Makashi_16. You must earn money by buy and sell petrol,iron and water. For communicate with WallPy, answer questions with, for the 1st question: buy, sell, pass or mission; for the 2nd question: petrol, iron, water or the number of the mission you want to complete; and for the third question : you must to answer the number of action you want to buy. If you pass the turn, prices change but you lose 10$. Good luck !!!")
print(" I foget to say if you want to stop, write exit but you will don't need it ;)")
mixPrice()
running = True
while running == True:
    ans = 0
    ans2 = 0
    ans3 = 0
    showValue()
    print("Do you want to buy ,sell or pass ?")
    ans = str(input())
    if ans == "buy":
        print("What do you want to buy ?")
        ans2 = str(input())
        if ans2 in prices.keys():
            print(f"how much {ans2} do you wanna buy ?")
            ans3 = int(input())
            if  ans3*prices[ans2] <= money:
                possessed[ans2] += ans3
                money -= ans3*prices[ans2]
                round+=1
                mixPrice()
            else:
                error()

        else: 
            error()
    elif ans == "sell":
        print("What do you want to sell ?")
        ans2 = str(input())
        if ans2 in prices.keys():
            print(f"how much {ans2} do you wanna sell ?")
            ans3 = int(input())
            if ans3 <= possessed[ans2]:
                possessed[ans2] -= ans3
                money += ans3*prices[ans2]
                round+=1
                mixPrice()
            else:
                error()

        else: 
            error()
    elif ans == "pass":
        if money >= 10:
            money = money - 10
            print("You was waiting for better price, you lose $10.")
            round = round + 1 
            mixPrice()
        else:
            error()
    elif ans == "exit":
        running = False
    elif ans == "mission":
        showMission()
        print("Witch mission do you want to complete ? (write the number of the mission")
        ans2 = int(input())
        if ans2 == 1:
            if money >= 1000:
                print("Conglurations, mission completed succesfully")
                money = money -1000
            else: 
                error()
    elif ans == "round":
        print("round :", round)
    else:
        error()
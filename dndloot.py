import sqlite3
import random

def rand(x, y):
    number = random.randint(x, y)
    return number

def money_calc(money):
    if money==1:
        copper = random.randint(1, 100)
        money = ("copper", copper)
        return money
    
    elif money==2:
        silver = random.randint(1, 100)
        money = ("silver", silver)
        return money

    elif money==3:
        gold = random.randint(1, 100)
        money = ("gold", gold)
        return money

    else:
        money = "nothing"
        return money

def item_calc(items):
    if items==1:
        weapon = random.randint(1, 100)
        items = ("weapon", weapon)
        return items
    
    elif items==2:
        armour = random.randint(1, 100)
        items = ("armour", armour)
        return items

    elif items==3:
        randomitem = random.randint(1, 100)
        items = ("randomitem", randomitem)
        return items

    else:
        items = "nothing"
        return items
    

def uncommon_calc(uncommon):
    name = "uncommon: "
    if uncommon==1:
        uncommonitem = rand(1, 100)
        uncommon = (name, uncommonitem)
        return uncommon 
        
    elif uncommon==2:
        uncommonitem = rand(1, 100)
        uncommon = (name, uncommonitem)
        return uncommon
    
    elif uncommon==3:
        uncommonitem = rand(1, 100)
        uncommon = (name, uncommonitem)
        return uncommon

    else:
        uncommon = "nothing"
        return uncommon

def loot_table(difficulty):
    if difficulty == 'e':
        money = random.randint(1, 4)
        items = random.randint(1, 4)
        money = money_calc(money)
        items = item_calc(items)
        
        print("money: ", money, "\n")
        print("items: ", items)
        
    elif difficulty=='m':
        money = random.randint(1, 4)
        items = random.randint(1, 4)
        uncommon = random.randint(1, 4)
        money = money_calc(money)
        items = item_calc(items)
        uncommon = uncommon_calc(uncommon)
        print("money: ", money, "\n")
        print("items: ", items, "\n")
        print("uncommon: ", uncommon)




def main():
    while True:

        difficulty = input("What level difficulty is the encounter? ")
        if difficulty=='e':
            print("loot table for easy difficulty: ")
            loot_table(difficulty)

        elif difficulty=='m':
            print("loot table for medium difficulty: ")
            loot_table(difficulty)
            
        elif difficulty=='h':
            print("loot table for hard difficulty: ")
            loot_table(difficulty)
            
        elif difficulty=='d':
            print("loot table for deadly difficulty: ")
            loot_table(difficulty)
        
        elif difficulty=='exit':
            print("Closing the loot table app....")
            break

        else:
            print("Please select a difficulty \n")
            print("e = easy\n")
            print("m = medium \n")
            print("h = hard \n")
            print("d = deadly \n")
            print("exit = exit \n")


main()
      
  


print("DnD Initiative tracker\n")
number_of_enemies = input("Add the number of enemies ")

players = ["Onyx", "Varic", "Thorgar", "Chadwick", "BlackThorn", "Dellora", "Alarik"]

def get_player_initiative(players):
    initiative_order = {}
    for p in players:
        initiative = input("Add initiative for player " + p + " ")
        initiative_order.update({p : initiative})

    return initiative_order

def get_monsters_initiative(initiative_order):
    for n in range(int(number_of_enemies)):
        initiative = input("Add initiative for monster ")
        initiative_order.update({"monster " + str(n): initiative})
    
    return initiative_order

def sort_initiative_order(initiative_order):
    sorted_initiative_order = dict(sorted(initiative_order.items(), key=lambda key_val: int(key_val[1]), reverse=True))
    
    return sorted_initiative_order

initiative_order = get_player_initiative(players)
initiative_order = get_monsters_initiative(initiative_order)
sorted_initiative_order = sort_initiative_order(initiative_order)
print(sorted_initiative_order)

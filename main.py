from collections import Counter

class card:
    def __init__(self,id,name):
        self.id = id
        self.name = name

class player:
    def __init__(self,id,hand=[],stack=[]):
        self.id = id
        self.hand = hand
        self.stack = stack

def stack_checker(players_list):
    for i in players_list:
        for j in Counter(i.stack).values():
            if j >= 8:
                return 0
    return -1


def dis_card(choose_card,dec_card,turn_player,choosed_player,players_list):
    print("0:False")
    print("1:True")
    a = int(input())
    if a ==(choose_card==dec_card):
        players_list[turn_player].stack.append(choose_card)
    else:
        players_list[choosed_player].stack.append(choose_card)
        turn_player == choosed_player

def choose_player(can_choose_player):
    while True:
        print(can_choose_player)
        a = int(input())
        if a in can_choose_player:
            break
    return a

def hand_choosing(player):
    cards = set(player.hand)
    while True:
        print("choose_your_card")
        for i in cards:
            print(i.id,i.name)
        x = int(input())
        if x in cards:
            return x


import json

a = open("card.json")
b = json.load(a)
cards = []
for i in b["card"]:
    cards.append(card(i["id"],i["name"]))



import random

p = 4
players_list = [player(i) for i in range(p)]
data = []
for i in cards:
    data.extend([i for j in range(8)])


c = 0
while len(data) > 0:
    players_list[c].hand.append(data.pop(random.randint(0,len(data)-1)))
    c = (c+1)%p


over = -1
turn_player = random.randint(0,p-1)
choosed_player = -1
can_choose_player = [i for i in range(4) if not(turn_player==i)]

while over == -1:
    end = False
    while not end:
        choosed_player = choose_player(can_choose_player)
        choose_card = 0 #choose
        dec_card = 0 #choose
        print("action")
        action = int(input()) #choose
        if action == 0:
            can_choose_player.remove(choosed_player)
            turn_player = choosed_player
            choosed_player = can_choose_player[random.randint(0,len(can_choose_player)-1)]
            continue
        else:
            dis_card(choose_card,dec_card,turn_player,choosed_player,players_list)
            can_choose_player = [i for i in range(4) if not(turn_player==i)]
            end = True
    over = stack_checker(players_list)

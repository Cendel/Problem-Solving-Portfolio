import sys
import math

"""This program simulates a simplified card game where two players, p1 and p2, draw cards from their 
respective decks and compare the values of the top cards. If the values match, the game proceeds with 
a special set of rules for tie scenarios. The game continues until one of the players runs out of cards, 
and the program then determines the winner or declares a tie (PAT) based on the game's outcome."""


p1=["10D", "9S", "8D", "KH", "7D", "5H", "6S"]
p2= ["10H", "7H", "5C", "QC", "2C", "4H", "6D"]
reserved = []
round = 0

pat = False


def deal_cards(p1cards, p2cards, p1, p2):
    a = []
    for card in p1cards:
        a.append(card)
        p1.remove(card)
    for card in p2cards:
        a.append(card)
        p2.remove(card)
    return a

def num(symbol):
    J, Q, K, A = 11,12,13,14
    if symbol == "J":
        return J
    if symbol == "Q":
        return Q
    if symbol == "K":
        return K
    if symbol == "A":
        return A
    else:
        return int(symbol)


while True:
    if not p1 or not p2:
        break
    else:
        if num(p1[0][:-1]) == num(p2[0][:-1]):
            if len(p1) == 1 or len(p2) == 1:
                if len(p1) > len(p2):
                    reserved.extend(deal_cards([p1[0]], [p2[0]], p1, p2))
                    p1.extend(reserved)
                else:
                    reserved.extend(deal_cards([p1[0]], [p2[0]], p1, p2))
                    p2.extend(reserved)
                continue

            if len(p1) < 5 or len(p2) < 5:
                pat = True
                break
            else:
                reserved.extend(deal_cards(p1[0:4], p2[0:4], p1, p2))
                continue
        else:
            if num(p1[0][:-1]) > num(p2[0][:-1]):
                reserved.extend(deal_cards([p1[0]], [p2[0]], p1, p2))
                p1.extend(reserved)
            else:
                reserved.extend(deal_cards([p1[0]], [p2[0]], p1, p2))
                p2.extend(reserved)
            reserved = []
            round += 1
            continue

if pat:
    print("PAT")
    print(p1)
    print(p2)
elif p1:
    print(f"1 {round}")
elif p2:
    print(f"2 {round}")









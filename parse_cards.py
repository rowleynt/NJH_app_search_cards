from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity


def searchQ(uinput):
    """not used yet in main.py but this will print card data neatly"""
    q = Card.where(q=f"name:*{uinput}*")
    for i in range(len(q)):
        print(f"Card {i}:")
        temp = {
            "id": q[i].id,
            "name": q[i].name,
            "supertype": q[i].supertype,
            "subtypes": q[i].subtypes,
            # "level": q[i].level,
            "hp": q[i].hp,
            "types": q[i].types,
            "evolvesFrom": q[i].evolvesFrom,
            "rules": q[i].rules,
            "ancientTrait": q[i].ancientTrait,
            "abilities": q[i].abilities,
            "attacks": q[i].attacks,
            "weaknesses": q[i].weaknesses,
            "resistances": q[i].resistances,
            "retreatCost": q[i].retreatCost,
            "convertedRetreatCost": q[i].convertedRetreatCost,
            "set": q[i].set,
            "number": q[i].number,
            "artist": q[i].artist,
            "rarity": q[i].rarity,
            "flavorText": q[i].flavorText,
            "nationalPokedexNumbers": q[i].nationalPokedexNumbers,
            "legalities": q[i].legalities,
            "regulationMark": q[i].regulationMark,
            "image": q[i].images.large
            # "tcgplayer": q[i].tcgplayer,
            # "cardmarket": q[i].cardmarket.prices
        }
        for key in temp:
            print(key, ":", temp[key])
        print()


def temp_sch(uinput):
    """returns a list of images from cards found from search query"""
    q = Card.where(q=f"name:*{uinput}*")
    img_list = []
    for card in q:
        img_list.append(card.images.large)
    # print(q[0].images.large)
    return img_list

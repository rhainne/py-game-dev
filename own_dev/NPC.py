
# This will hold a dictionary with NPCs and their respective information to make
# calls to their constructors. Im not sure yet if I need objects for NPCs of its enough
# with just static information
#
# "greetings", "farewells" and "not_enough_money"
# will be sentences NPCs will use in different situations

#
# Item lists Data. It will contain lists of items common to many NPCs
# Unique items related to one or few specific NPCs will be added in NPCs_data[npc]["items_to_sell"]
#
# Items to sell
dict_items_to_sell = {
    "trader_lvl_1": [],
    "trader_lvl_2": [],
    "trader_lvl_3": [],
    "trader_lvl_4": [],
    "traveler_lvl_1": [],
    "traveler_lvl_2": [],
    "traveler_lvl_3": [],
    "traveler_lvl_4": []
}
# Items to buy
dict_items_to_buy = {
    "trader_lvl_1": [],
    "trader_lvl_2": [],
    "trader_lvl_3": [],
    "trader_lvl_4": [],
    "traveler_lvl_1": [],
    "traveler_lvl_2": [],
    "traveler_lvl_3": [],
    "traveler_lvl_4": []
}

# NPC Data
NPCs_data = {
    "barbas": {
        "name": "barbas", "display_name": "Barbas, Mercader Oscuro",
        "items_to_sell": [], "items_to_buy": [], "greetings": [], "farewells": [],
        "not_enough_money": []
    },
    "rakanishai": {
        "name": "rakanishiai", "display_name": "Rakanishiai",
        "items_to_sell": [], "items_to_buy": [], "greetings": [], "farewells": [],
        "not_enough_money": []
    },
    "ender_naro": {
        "name": "ender_naro", "display_name": "Ender Naro",
        "items_to_sell": [], "items_to_buy": [], "greetings": [], "farewells": [],
        "not_enough_money": []
    }
}
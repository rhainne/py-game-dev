from Map import *

# List of contructors
# Should apply here the same approach as with Ememy data, Region data, or NPCs data
Map_constructors = {
        "rohan": Map("rohan", "../assets/maps/rohan_map.jpg", "simon"),
        "middle_earth": Map("middle_earth", "../assets/maps/middle_earth_map.jpg", "simon"),
        "simon": Map("simon", "../assets/maps/map_2x2.png", None, ["rohan", "middle_earth"]
                     , [[(0, 0), (206.5, 409)]
                     , [(206.5, 0), (413, 409)]
                        ])
}

Maps_data = {
    "rohan": {
        "name": "rohan", "img": "../assets/maps/rohan_map.jpg", "outside_map": "simon"
    },
    "middle_earth": {
        "name": "middle_earth", "img": "../assets/maps/middle_earth_map.jpg", "outside_map": "simon"
    },
    "simon": {
        "name": "simon", "img": "../assets/maps/map_2x2.png", "outside_map": None
        , "inside_maps": ["rohan", "middle_earth"]
        , "frontier_list": [
            [(0, 0), (206.5, 409)]
            , [(206.5, 0), (413, 409)]
        ]
    }
}

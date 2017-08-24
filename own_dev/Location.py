from own_dev.Stage import *

# This class will hold information about the Location.
# all the enemies that could appear in the area,
# weather information, shops information etc


class Location(Stage):
    def __init__(self, **kwargs):
        Stage.__init__(self, kwargs.get("background_img"))
        attributes = {
            "name": "default_name",
            "display_name": "Default Name",
            "fauna_list": [],
            "crowdness": 0,
            "shop_list": [],
            "weather": "",
            "dominion_faction": "",
            "political_tendency": "",
            "people_political_tendency": ""
        }

        for (prop, default) in list(attributes.items()):
            setattr(self, prop, kwargs.get(prop, default))

    def __str__(self):
        return "Name: {0}" \
               "\nWeather: {1}" \
               "\nDominion faction: {2}" \
               "\nPolitical tendency: {3}" \
               "\nPeople's political tendency: {4}".format(self.display_name
                                                           , self.weather
                                                           , self.dominion_faction
                                                           , self.political_tendency
                                                           , self.people_political_tendency)

    __repr__ = __str__

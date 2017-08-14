# This class will hold information about the Location.
# all the enemies that could appear in the area,
# weather information, shops information etc


class Location(object):
    def __init__(self, fauna_list=None, shop_list=None):
        self.fauna_list = fauna_list
        self.shop_list = shop_list
        self.weather = ""

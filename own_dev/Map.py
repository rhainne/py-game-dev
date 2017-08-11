class Map:
    def __init__(self, name, img=None, outside_map=None, inside_map_list=None, frontier_list=None):
        self.name = name
        self.img = img
        self.outside_map = outside_map
        self.inside_maps = inside_map_list
        #
        # All the frontier stuff should be implemented with rects or other kind of form.
        # Should be more portable and modulable
        #
        self.frontiers = frontier_list

    def __str__(self):
        return self.name

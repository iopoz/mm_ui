from models.enter_to_application import EnterToApplication
from models.navigate import Navigate
from models.place_info import PlaceInfo
from models.search_place import SearchPlace


class Application(object):
    def __init__(self):
        #-----global classes-----#
        self.enter_2_app = EnterToApplication(self)
        self.search = SearchPlace(self)
        self.navigate = Navigate(self)
        self.place_details = PlaceInfo(self)

        # -----global variables-----#
        self.first_enter = True
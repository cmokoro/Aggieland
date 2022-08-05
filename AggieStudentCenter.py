import AggieBuildings as AB
#This is a derrived class for Aggie land application with methods for Student Centers.
class AggieStuCenter(AB.Buildings):

    def __init__(self, building_name, building_adress, building_rooms,num_Resturants, num_StudyRooms,  num_stuBathrooms, num_Lounge) -> None:
        super().__init__(building_name, building_adress, building_rooms)
        self.resturants = num_Resturants
        self.studyRooms = num_StudyRooms
        self.stuBathrooms = num_stuBathrooms
        self.stuLounge = num_Lounge

    def getResturants(self):
        return self.resturants

    def setResturants(self, num_Resturants):
       self.resturants = num_Resturants


    def getStudyrooms(self):
        return self.studyRooms

    def setStudyrooms(self,num_StudyRooms ):
       self.studyRooms = num_StudyRooms
    

    def getStuLounge(self):
        return self.stuLounge

    def setStuLounge(self, num_Lounge):
        self.stuLounge = num_Lounge 
    

    def getStuBathrooms(self):
        return self.stuBathrooms

    def setStuBathrooms(self, num_stuBathrooms):
        self.stuBathrooms = num_stuBathrooms
      
    def __str__(self):
        return (f'{AB.Buildings.getName(self)}:\nAdress: {AB.Buildings.getAdress(self)} \nTotal Rooms: {AB.Buildings.getRooms(self)}\nnumber of study roooms: {AggieStuCenter.getStudyrooms(self)}  \nnumber of resturants: {AggieStuCenter.getResturants(self)}  \nnumber of lounges: {AggieStuCenter.getStuLounge(self)}\nnumber of Bathrooms: {AggieStuCenter.getStuBathrooms(self)}  ')
        
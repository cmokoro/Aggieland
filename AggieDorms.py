import AggieBuildings as AB
#This is a derrived class for Aggie land application with methods for Dorm.
class AggieDorms(AB.Buildings):

    def __init__(self, building_name, building_adress, building_rooms,num_Dormrooms ,num_bathrooms,num_lounge, num_landry) -> None:
        super().__init__(building_name, building_adress, building_rooms)
        self.dormRooms = num_Dormrooms
        self.dormBathrooms = num_bathrooms
        self.dormLounge = num_lounge
        self.dormlandry = num_landry
    def getDormRooms(self):
        return self.dormRooms

    def setDormRooms(self, num_Dormrooms):
       self.dormRooms = num_Dormrooms
    
    def getDormBathrooms(self):
        return self.dormBathrooms

    def setDormBathrooms(self,num_bathrooms ):
       self.dormBathrooms = num_bathrooms
    

    def getDormLounge(self):
        return self.dormLounge

    def setDormLounge(self, num_Lounge):
        self.dormLounge = num_Lounge 
    
    def getDormLandry(self):
        return self.dormlandry

    def setDormLandry(self, num_landry):
        self.dormlandry = num_landry 
      
    def __str__(self):
        return (f'{AB.Buildings.getName(self)}: {AB.Buildings.getAdress(self)} \nTotal Rooms: {AB.Buildings.getRooms(self)}\nnumber of dorm roooms: {AggieDorms.getDormRooms(self)}  \nnumber of Bathrooms: {AggieDorms.getDormBathrooms(self)}  \nnumber of lounges: {AggieDorms.getDormLounge(self)}\nnumbers of landry rooms: {AggieDorms.getDormLandry(self)} ')
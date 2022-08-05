import AggieBuildings as AB
#This is a derrived class for Aggie land application with methods for Research buildings.

class Aggieresearch(AB.Buildings):

    def __init__(self, building_name, building_adress, building_rooms, num_offices,num_bathrooms, num_TestingCenters) -> None:
        super().__init__(building_name, building_adress, building_rooms)
        self.ResearchOffices = num_offices
        self.researchBathrooms = num_bathrooms
        self.TCenter = num_TestingCenters


    def getLabs(self):
        return self.Labs

    def setLabs(self, num_Labs):
       self.Labs = num_Labs


    def getOffices(self):
        return self.ResearchOffices

    def setOffices(self,num_offices ):
       self.ResearchOffices = num_offices
    

    def getTestingCenters(self):
        return self.TCenter

    def setTestingCenter(self, num_TestingCenters):
        self.TCenter = num_TestingCenters 

    def getResearchBathrooms(self):
        return self.researchBathrooms

    def setResearchBathrooms(self, num_bathrooms):
        self.researchBathrooms = num_bathrooms
      
    def __str__(self):
        return (f'{AB.Buildings.getName(self)}:\nAdress: {AB.Buildings.getAdress(self)} \nTotal Rooms: {AB.Buildings.getRooms(self)}\nnumber of Labs: {Aggieresearch.getLabs(self)}  \nnumber of offices : {Aggieresearch.getOffices(self)}  \nnumber of Testing Centers: {Aggieresearch.getTestingCenters(self)}\nnumber of Bathrooms: {Aggieresearch.getResearchBathrooms (self)}  ')
        
        
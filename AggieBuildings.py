

print("In this program it will allow users to create ")
#This is the base class for Aggie land application with methods for buildings.
class Buildings:
    def __init__(self,building_name = "N/A",building_adress = "N/A",building_rooms = "N/A"):
        self.name = building_name
        self.adress = building_adress
        self.rooms = building_rooms
    def __str__(self):

        return (f'{self.name}: {self.adress} \nNumber of Rooms: {self.rooms}')

    def getName(self):
        return self.name

    def setname(self,building_name):
        self.name = building_name
        
    def getAdress(self):
        return self.adress

    def setAdress(self,building_adress):
        self.adress = building_adress
    
    def getRooms(self):
        return self.rooms

    def setRooms(self,building_rooms):
        self.adress = building_rooms
    

    
    




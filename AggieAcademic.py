import AggieBuildings as AB
#This is a derrived class for Aggie land application with methods for Academic Buildings.
class AggieAcademic(AB.Buildings):

    def __init__(self, building_name, building_adress, building_rooms,num_ClassRooms,num_Offices, num_Bathrooms) -> None:
        super().__init__(building_name, building_adress, building_rooms)
        self.classrooms = num_ClassRooms
        self.offices = num_Offices
        self.AcademicBathrooms = num_Bathrooms
    
    def getClassrooms(self):
        return self.classrooms

    def setClassrooms(self, num_ClassRooms):
       self.classrooms = num_ClassRooms


    def getOffices(self):
        return self.offices

    def setOffices(self,num_Offices ):
       self.offices = num_Offices
   

    def getAcademicBathrooms(self):
        return self.AcademicBathrooms

    def setAcademicBathrooms(self, num_Bathrooms):
        self.AcademicBathrooms = num_Bathrooms
      
    def __str__(self):
        return (f'{AB.Buildings.getName(self)}:\nAdress: {AB.Buildings.getAdress(self)} \nTotal Rooms: {AB.Buildings.getRooms(self)}\nnumber of classroooms: {AggieAcademic.getClassrooms(self)}  \nnumber of Offices: {AggieAcademic.getOffices(self)}  \nnumber of Bathrooms: {AggieAcademic.getAcademicBathrooms(self)} ')
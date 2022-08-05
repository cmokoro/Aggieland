# Chidi Okoro
# August 2 2022
# Comp 163-001

from typing import List
import Menu
import AggieBuildings  as AB
import AggieDorms as AD
import AggieStudentCenter as AS
import AggieAcademic as AA
import AggieResearch as AR

print("Welcome to AGGIELAND application!")
print("This program uses inheritance, abstraction and encapsalation.")
print("In this application it allows you to create and add new NCAT Building concepts Through the menu selection :")


#This program list buildings and building in a certain type of building
def listbuildings():
    for building in buildingList:
        print(building)

def listdorms():
    for dorm in dormList:
        print(dorm)

def listStuCenter():
    for center in stuCenterList:
        print(center)

def listAcademic():
    for building in academicList:
        print(building)

def listresearch():
    for building in researchList:
        print(building)

#This program is a set off funtions to create a building and other type of buildings
def createBuilding():
    building_name = input("Enter Building name : ")
    building_adress = input("Enter Building adress : ")
    building_rooms = int(input("Enter number of rooms in building :"))
    buildingList.append(AB.Buildings(building_name,building_adress, building_rooms))
   
def createDorm():
    building_name = input("Enter Building name : ")
    building_adress = input("Enter Building adress : ")
    building_rooms = int(input("Enter number of rooms in building :"))

    num_Dormrooms =  int(input("Enter number of Dorm rooms in building :")) 
    num_bathrooms = int(input("Enter number of Dorm bathrooms in building :")) 
    num_lounge = int(input("Enter number of Dorm lounges in building :")) 
    num_landry = int(input("Enter number of Dorm landry rooms in building :")) 

    buildingList.append(AB.Buildings(building_name,building_adress, building_rooms))
    dormList.append(AD.AggieDorms(building_name,building_adress,building_rooms, num_Dormrooms ,num_bathrooms,num_lounge, num_landry))

def createStudentCenter():
    building_name = input("Enter Student Center name : ")
    building_adress = input("Enter Student Center adress : ")
    building_rooms = int(input("Enter number of rooms in Student Center:"))

    
    num_Resturants = int(input("Enter number of Resturants in Student Center:")) 
    num_StudyRooms =  int(input("Enter number of Dorm rooms in Student Center:")) 
    num_stuBathrooms = int(input("Enter number of Dorm bathrooms in Student Center:")) 
    num_Lounge = int(input("Enter number of Dorm lounges in Student Center :")) 


    buildingList.append(AB.Buildings(building_name,building_adress, building_rooms))
    stuCenterList.append(AS.AggieStuCenter(building_name,building_adress, building_rooms,num_Resturants, num_StudyRooms,  num_stuBathrooms, num_Lounge))

def createAcademicBuilding():
    building_name = input("Enter Building name : ")
    building_adress = input("Enter Building adress : ")
    building_rooms = int(input("Enter number of rooms in building :"))

    num_ClassRooms = int(input("Enter number of classrooms in Academic building :"))
    num_Offices =  int(input("Enter number of offices in Academic building :"))
    num_Bathrooms = int(input("Enter number of bathrooms in Academic building :"))

    buildingList.append(AB.Buildings(building_name,building_adress, building_rooms))
    academicList.append(AA.AggieAcademic(building_name,building_adress, building_rooms,num_ClassRooms,num_Offices, num_Bathrooms))


def createReasearchbuilding():
    building_name = input("Enter Building name : ")
    building_adress = input("Enter Building adress : ")
    building_rooms = int(input("Enter number of rooms in building :"))

    num_Labs = int(input("Enter number of Labs in Research building :"))
    num_offices = int(input("Enter number of offices in Research building :"))
    num_bathrooms = int(input("Enter number of bathrooms in Research building :"))
    num_TestingCenters = int(input("Enter number of Testing Center in Academic building :"))
    


    buildingList.append(AB.Buildings(building_name,building_adress, building_rooms))
    researchList.append(AR.Aggieresearch(building_name,building_adress, building_rooms,num_Labs,num_offices,num_bathrooms, num_TestingCenters))

 
#container for all buildings and Building types
buildingList = []
researchList = []
dormList = []
stuCenterList = []
academicList = []

def __str__(self):
    return(dormList)

# This code is a while loop for menu selection
while True:
    Menu.displayMenu()
    menuItem = input("Enter Selection : ").upper()
    if menuItem == "1":
       listbuildings()
    elif menuItem == "2":
        listdorms()
    elif menuItem == "3":
        listStuCenter()
    elif menuItem == "4":
        listAcademic()
    elif menuItem == "5":
        print(researchList)
    elif menuItem == "A":
        createBuilding()
    elif menuItem == "B":
        createDorm()
    elif menuItem == "C":
        createReasearchbuilding()
    elif menuItem == "D":
        createAcademicBuilding()     
    elif menuItem == "E":
        createReasearchbuilding()      
    elif menuItem == "Q":
        Menu.aggieExit()
    else:
        Menu.invalidMenuSelection()      




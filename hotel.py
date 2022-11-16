class Hotel:
     def __init__(self,numRooms,parkinLot,spa,insurance) :
          self.__numRooms = numRooms
          self.__spa = True
          self.__parkingLot = parkinLot
          self.__insurance = insurance
          #get data
     def getNRooms(self):
          return self.__numRooms
     def getSpa(self):
          return self.__spa
     def getParkingLot(self):
          return self.__parkingLot
     def getInsurance(self):
          return self.__insurance
          #set data
     def setNRooms(self,numRooms):
          self.__numRooms =  numRooms
     def setSpa(self,spa):
          self.__spa =  spa
     def getParkingLot(self,parkingLot):
          self.__parkingLot =  parkingLot
  

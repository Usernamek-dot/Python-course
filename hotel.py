class Hotel:
     def __init__(self,numRooms,parkinLot,spa,insurance) :
          self.__numRooms = numRooms
          self.__spa = True
          self.__parkingLot = parkinLot
          self.__insurance = insurance
     def getNRooms(self):
          return self.__numRooms
     def getSpa(self):
          return self.__spa
     def getParkingLot(self):
          return self.__parkingLot
     def getInsurance(self):
          return self.__insurance
class Hotel:
     def __init__(self,numRooms,parkingLot,spa) :
          self.__numRooms = numRooms
          self.__spa = spa
          self.__parkingLot = parkingLot
          self.__insurance = True 
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
     def getParkingLot(self):
          return self.__parkingLot 
        #delete
     def delNRooms (self):
          del self.__numRooms
     def delSpa (self):
          del self.__spa
     def delParkingLot (self):
          del self.__parkingLot  
class HotelVIP (Hotel):
     pass
class HotelTurist(Hotel):
     def __init__(self, numRooms, parkingLot, spa,jaccuzzi):
          super().__init__(numRooms, parkingLot, spa,jaccuzzi)
          self.jaccuzzi = jaccuzzi
     pass
intercontinental = Hotel(850,False,"Two")
miHotelito = Hotel(300,2,5) 
hotelL = HotelVIP()
hotelHL= HotelTurist()
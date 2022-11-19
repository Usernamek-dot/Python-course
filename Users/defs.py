import re
import datetime
import pytz

@property
def idd(self):
     return self._id

@idd.setter
def idd(self,value):
     if  value.isnumeric():
          self._id = value
     raise ValueError("Id must be number.")


@property
def name(self):
     return self._name

@name.setter
def name(self, value):
     if len(value) > 20:
          raise ValueError("Name cannot exceed 20 characters.")
     if  isinstance(value, str):
          raise ValueError("Name must not have numbers or characters.")
     self._name = value


@property
def age(self):
     return self._age

@age.setter
def age(self, value):
     if  value.isnumeric():
          self._id = value
     raise ValueError("Age must be number.")
     

@property
def country(self):
     return self._country

@country.setter
def country(self, value):
     if len(value) > 20:
          raise ValueError("Country cannot exceed 20 characters.")
     self._country = value


@property
def phone(self):
     return self._phone

@phone.setter
def phone(self, value):
     if len(value) > 10:
          raise ValueError("phone cannot exceed 10 characters.")
     if value is not value.isnumeric():
          raise ValueError("phone must be numbers.")
     self._phone = value


@property
def date(self):
     return self._date
     
@date.setter
def date(self,value):
     # date_format = '%Y-%m-%d'
     date_format = pytz.timezone('America/Bogota')
     try:
          dateObject = datetime.datetime.strptime(value, date_format)
          print(dateObject)
     except ValueError:
          print("Incorrect data format, should be YYYY-MM-DD")
     self._date = value


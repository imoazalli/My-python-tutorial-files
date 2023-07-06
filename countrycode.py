import phonenumbers
import openpyxl
from phonenumbers import geocoder



f=open("Country-codes.xls",'r')
data=f.read()
print(data)
f.close()
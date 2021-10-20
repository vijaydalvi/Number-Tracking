import phonenumbers
from phonenumbers import geocoder
phone1=phonenumbers.parse("+917620199209")
phone2=phonenumbers.parse("+4930801820")
phone3=phonenumbers.parse("+13475439904")
print(geocoder.description_for_number(phone1,"en"))
print(geocoder.description_for_number(phone2, "en"))
print(geocoder.description_for_number(phone3, "en"))

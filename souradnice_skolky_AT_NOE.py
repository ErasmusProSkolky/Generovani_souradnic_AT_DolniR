# import modulu geopy
from geopy.geocoders import Nominatim
 
# načtení Nominatim
loc = Nominatim(user_agent="GetLoc")

with open('NOE_Kindergarten.txt', encoding='utf-8') as vstup:
    radky = vstup.readlines()

jeden_radek = [radek.split('\n') for radek in radky]

for cast_radku in jeden_radek:
    try:
        cast = cast_radku[0].split(",")  
        getLoc = loc.geocode(cast[0]+' '+cast[1])

        skolka = ""
        with open('AT_NOE.csv', mode='a', encoding='utf-8') as vystup:
            skolka = cast_radku[0] + "," + str(getLoc.latitude) + "," + str(getLoc.longitude) + "\n"
            vystup.writelines(skolka)
    
    except Exception as A:
        with open('nezname_adresy_AT_NOE.csv', mode='a',encoding='utf-8') as vystup_nezname:
            skolka_nezname = cast_radku[0] + "\n"
            vystup_nezname.writelines(skolka_nezname)
        pass


  






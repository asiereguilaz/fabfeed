
# coding: utf-8

# In[8]:

geoponics = [310.34, 1,2,3,4,5]
hydroponics = [0,1,2,3,4,5]
aquaponics = [642.5,228.5,291.5,310.5]
aeroponics = [291.5,310.5,512.5,552.0]
spirulina = [0,1,2,3,4,5]
foodcomputer = [0,1,2,3,4,5]


print "You are about to start developing your own FabFeedLab."
print " "
print "Let's start defining each food production systems' required areas"
print " "
answer = input("is it going to be based on LEDS?")
if (answer == "yes" or answer == "YES" or answer == "Yes"):
    print " "
    print "GEOPONICS? (sqm)"
    geo = raw_input()
    print " "
    print "HYDROPONICS? (sqm)"
    hydro = raw_input()
    print " "
    print "AQUAPONICS? (sqm)"
    aqua = raw_input()
    print " "
    print "AEROPONICS? (sqm)"
    aero = raw_input()
    print " "
    print "SPIRULINA? (sqm)"
    spiru = raw_input()
    print " "
    print "FOOD COMPUTER? (sqm)"
    foodco = raw_input()
    print " "

else:
    print " "
    print "GEOPONICS? (sqm)"
    geo = raw_input()
    print " "
    print "HYDROPONICS? (sqm)"
    hydro = raw_input()
    print " "
    print "AQUAPONICS? (sqm)"
    aqua = raw_input()
    print " "
    print "AEROPONICS? (sqm)"
    aero = raw_input()
    print " "
    print "SPIRULINA? (sqm)"
    spiru = raw_input()
    print " "
    print "FOOD COMPUTER? (sqm)"
    foodco = raw_input()
    print " "

    
geototal1 = int(geo) * geoponics[0]
hydtotal1 = int(hydro) * hydroponics[0]
aqutotal1 = int(aqua) * aquaponics[0]
aertotal1 = int(aero) * aeroponics[0]
spitotal1 = int(spiru) * spirulina[0] 
foototal1 = int(foodco)* foodcomputer[0]

geototal2 = int(geo) * geoponics[1]
hydtotal2 = int(hydro) * hydroponics[1]
aqutotal2 = int(aqua) * aquaponics[1]
aertotal2 = int(aero) * aeroponics[1]
spitotal2 = int(spiru) * spirulina[1]
foototal2 = int(foodco) * foodcomputer[1]

geogasto1 = int(geo) * geoponics[2]
hydgasto1 = int(hydro) * hydroponics[2]
aqugasto1 = int(aqua) * aquaponics[2]
aergasto1 = int(aero) * aeroponics[2]
spigasto1 = int(spiru) * spirulina[2] 
foogasto1 = int(foodco)* foodcomputer[2]

geogasto2 = int(geo) * geoponics[3]
hydgasto2 = int(hydro) * hydroponics[3]
aqugasto2 = int(aqua) * aquaponics[3]
aergasto2 = int(aero) * aeroponics[3]
spigasto2 = int(spiru) * spirulina[3]
foogasto2 = int(foodco) * foodcomputer[3]

geobene1 = geototal1 - geogasto1
hydbene1 = hydtotal1 - hydgasto1
aqubene1 = aqutotal1 - aqugasto1
aerbene1 = aertotal1 - aergasto1
spibene1 = spitotal1 - spigasto1
foobene1 = foototal1 - foogasto1

geobene2 = geototal2 - geogasto2
hydbene2 = hydtotal2 - hydgasto2
aqubene2 = aqutotal2 - aqugasto2
aerbene2 = aertotal2 - aergasto2
spibene2 = spitotal2 - spigasto2
foobene2 = foototal2 - foogasto2

totaltotal1 = geototal1 + hydtotal1 + aqutotal1 + aertotal1 + spitotal1 + foototal1
totalgasto1 = geogasto1 + hydgasto1 + aqugasto1 + aergasto1 + spigasto1 + foogasto1
totalbene1 = geobene1 + hydbene1 + aqubene1 + aerbene1 + spibene1 + foobene1

totaltotal2 = geototal2 + hydtotal2 + aqutotal2 + aertotal2 + spitotal2 + foototal2
totalgasto2 = geogasto2 + hydgasto2 + aqugasto2 + aergasto2 + spigasto2 + foogasto2
totalbene2 = geobene2 + hydbene2 + aqubene2 + aerbene2 + spibene2 + foobene2

if (answer == "yes" or answer == "YES" or answer == "Yes"):
    print " "
    print " "
    print "RESULTS:"
    print " "
    print "income", totaltotal1, "€"
    print "expenses", totalgasto1, "€"
    print "profit", totalbene1, "€" 
    
else:
    print "income", totaltotal2, "€"
    print "expenses", totalgasto2, "€"
    print "profit", totalbene2, "€"


# In[ ]:




print ("This generator was created by Joey Nadol. It randomly and realistically generates planets based\
 on the planets we see in our solar system and the ones we have found outside of it.")
import random
startype = random.randint (1,4)
if (startype == 1):
    startype = "Yellow Dwarf"
if (startype == 2):
    startype = "Red Giant"
if (startype == 3):
    startype = "Red Dwarf"
if (startype == 4):
    startype = "Blue Supergiant"
binary = random.randint (1, 4)
if (binary == 1):
    binary = random.randint (1, 4)
    if (binary == 1):
        binary = "Yellow Dwarf"
    if (binary == 2):
        binary = "Red Giant"
    if (binary == 3):
        binary = "Red Dwarf"
    if (binary == 4):
        binary = "Blue Supergiant"
    print ("Star Type: Binary", startype, "And", binary, "System")
else:
    print ("Star Type:", startype, "System")
atmosphere = 0
planetnum = random.randint (1, 15)
currentnum = 1
print ("Number of Planets In System:", planetnum)
while (currentnum < planetnum + 1):
    print ("*")
    print ("*")
    print ("*")
    print ("Planet #", currentnum)
    #This section determines size
    powerraisedto = random.randint (22, 30)
    nummultipliedby = random.randint (1000, 9999) / 1000
    if (powerraisedto == 22):
        if (nummultipliedby > 3):
            planetsize = "(Moon-sized)"
        else:
            planetsize = "(Dwarf planet)"
    elif (powerraisedto == 23):
        if (nummultipliedby > 5):
            planetsize = "(Mars-sized)"
        else:
            planetsize = "(Mercury-sized)"
    elif (powerraisedto == 24):
        planetsize = "(Earth-sized)"
    elif (powerraisedto == 25):
        planetsize = "(Small gas giant)"
    elif (powerraisedto == 26):
        planetsize = "(Average size gas giant)"
    elif (powerraisedto == 27):
        planetsize = "(Jupiter-sized gas giant)"
    else:
        planetsize = "(Bigger than Jupiter)"
    print ("Mass:", nummultipliedby, " * 10^", powerraisedto, planetsize)
    #This section determines atmospheric composition
    if (powerraisedto > 24):
        atmosphere1 = random.randint(1, 10)
        atmosphere2 = random.randint(1, 10)
        if (atmosphere1 < 5):
            atmosphere1 = "% Hydrogen"
        elif (atmosphere1 > 4 and atmosphere1 < 8):
            atmosphere1 = "% Helium"
        elif (atmosphere1 == 8):
            atmosphere1 = "% Methane"
        elif (atmosphere1 == 9):
            atmosphere1 = "% Ammonia"
        elif (atmosphere1 == 10):
            atmosphere1 = "% Water Vapor"
        if (atmosphere2 < 5):
            atmosphere2 = "% Hydrogen"
        elif (atmosphere2 > 4 and atmosphere2 < 8):
            atmosphere2 = "% Helium"
        elif (atmosphere2 == 8):
            atmosphere2 = "% Methane"
        elif (atmosphere2 == 9):
            atmosphere2 = "% Ammonia"
        elif (atmosphere2 == 10):
            atmosphere2 = "% Water Vapor"
        if (atmosphere1 == atmosphere2):
            if (atmosphere1 == "% Hydrogen"):
                atmosphere = "100% Hydrogen"
            elif (atmosphere1 == "% Helium"):
                atmosphere = "100% Helium"
            elif (atmosphere1 == "% Methane"):
                atmosphere = "100% Methane"
            elif (atmosphere1 == "% Ammonia"):
                atmosphere = "100% Ammonia"
            elif (atmosphere1 == "% Water Vapor"):
                atmosphere = "100% Water Vapor"
            print (atmosphere)
        else:
            percent1 = random.randint (50, 99)
            percent2 = (100 - percent1)
            print ("Atmosphere: ", percent1, atmosphere1, percent2, atmosphere2)
    elif (powerraisedto < 25):
        atmosphere1 = random.randint(1, 10)
        atmosphere2 = random.randint(1, 10)
        if (atmosphere1 == atmosphere2):
            if (atmosphere1 == 1):
                atmosphere = "100% Nitrogen"
            elif (atmosphere1 == 2):
                atmosphere = "100% Sodium"
            elif (atmosphere1 == 3):
                atmosphere = "100% Methane"
            elif (atmosphere1 == 4):
                atmosphere = "100% Hydrogen"
            elif (atmosphere1 == 5 or atmosphere1 == 9):
                atmosphere = "100% Carbon Dioxide"
            elif (atmosphere1 == 6 or atmosphere1 == 10):
                atmosphere1 = "None"
            elif (atmosphere1 == 7):
                atmosphere = "100% Oxygen"
            elif (atmosphere1 == 8):
                atmosphere = "100% Helium"
            print (atmosphere)
        else:
            if (atmosphere1 == 1):
                atmosphere1 = "% Nitrogen, "
            elif (atmosphere1 == 2):
                atmosphere1 = "% Sodium, "
            elif (atmosphere1 == 3):
                atmosphere1 = "% Methane, "
            elif (atmosphere1 == 4):
                atmosphere1 = "% Hydrogen, "
            elif (atmosphere1 == 5 or atmosphere1 == 9):
                atmosphere1 = "% Carbon Dioxide, "
            elif (atmosphere1 == 7):
                atmosphere1 = "% Oxygen, "
            elif (atmosphere1 == 8):
                atmosphere1 = "% Helium, "
            if (atmosphere2 == 1):
                atmosphere2 = "% Nitrogen"
            elif (atmosphere2 == 2):
                atmosphere2 = "% Sodium"
            elif (atmosphere2 == 3):
                atmosphere2 = "% Methane"
            elif (atmosphere2 == 4):
                atmosphere2 = "% Hydrogen"
            elif (atmosphere2 == 5 or atmosphere2 == 9):
                atmosphere2 = "% Carbon Dioxide"
            elif (atmosphere2 == 6 or atmosphere1 == 6 or atmosphere2 == 10 or atmosphere1 == 6):
                atmosphere = "None"
            elif (atmosphere2 == 7):
                atmosphere2 = "% Oxygen"
            elif (atmosphere2 == 8):
                atmosphere2 = "% Helium"
            percent1 = random.randint (50, 99)
            percent2 = (100 - percent1)
            if (atmosphere1 == "None" or atmosphere2 == "None" or atmosphere == "None"):
                print ("Atmosphere: None")
            else:
                print ("Atmosphere: ", percent1, atmosphere1, percent2, atmosphere2)
#This section determines atmospheric pressure
    thickness = random.randint (0, 1)
    if (atmosphere == "None"):
        thickness1 = "N/A"
        thickness2 = 0
        thickness3 = 0
        print ("No atmospheric pressure")
    elif (thickness == 0 and powerraisedto < 25):
        thickness2 = random.randint (0, 9)
        thickness3 = 0
        print ("Atmospheric Pressure: ", thickness3, ".", thickness2, " atm")
    elif (thickness == 1 and powerraisedto < 25):
        thickness2 = random.randint (0, 9)
        thickness3 = random.randint(1, 9)
        print ("Atmospheric Pressure: ", thickness3, ".", thickness2, " atm")
    else:
        print ("Atmospheric pressure is irrelevant due to planet being a gas giant.")
        thickness1 = 0
        thickness2 = 0
        thickness3 = 0
    #This section determines distance from the star
    if (currentnum == 1):
        distancefromstar = random.randint (1, 200)
        aufromstar = distancefromstar / 93
        prevdist = distancefromstar
    else:
        if (prevdist > 998):
            distancefromstar = prevdist + random.randint (30,60)
        else:
            distancefromstar = random.randint (prevdist, 999)
        aufromstar = distancefromstar / 93
        prevdist = distancefromstar
    print ("Distance from star: ", distancefromstar, "million miles (", round (aufromstar, 2), "AU)")
    #This following equation determines the surface temperature
    if (powerraisedto > 24):
        surfacetemp = (1 - round (aufromstar, 2) ) * 40 + 75
    else:
        surfacetemp = (1 - round (aufromstar, 2) * 10) / (1 + (thickness3 + (thickness2 / 10))) - round (aufromstar, 2) * 10 + (thickness3 * 20) + 60
    print ("Surface Temperature:", round (surfacetemp, 2), "C, ", round (surfacetemp * 9 / 5 + 32, 2), " F")
    #This section of code labels the planets accordingly
    if (powerraisedto > 24):
        if (distancefromstar < 500):
            planettype = "Gas Giant"
        else:
            planettype = "Ice Giant"
    else:
        if (thickness3 < 1 and thickness2 < 5):
            planettype = "Dead Planet"
        else:
            if (surfacetemp > 0 and surfacetemp < 100):
                planettype = random.randint (1, 2)
                if (planettype == 1):
                    planettype = "Oceanic Planet"
                else:
                    planettype = "Terran Planet"
            else:
                if (surfacetemp < 0):
                    planettype = "Ice Planet"
                else:
                    planettype = "Desert Planet"
    if (surfacetemp < -200):
        templabel = "Frozen"
    elif (surfacetemp < -100):
        templabel = "Cold"
    elif (surfacetemp < 0):
        templabel = "Cool"
    elif (surfacetemp < 100):
        templabel = "Temperate"
    elif (surfacetemp < 200):
        templabel = "Warm"
    elif (surfacetemp < 300):
        templabel = "Hot"
    else:
        templabel = "Scorching"
    print ("Planet Type:", templabel, planettype)
    #This section determines if the planet has life, and if so, what type
    if (planettype == "Oceanic Planet"):
        life = random.randint (1, 7)
        if (life == 1):
            lifeanswer = "Yes"
            lifetype = "Marine"
        else:
            lifeanswer = "No"
    elif (planettype == "Terran Planet"):
        life = random.randint (1, 6)
        if (life == 1):
            lifeanswer = "Yes"
            lifetype = random.randint (1, 3)
            if (lifetype == 1):
                lifetype = "Marine"
            elif (lifetype == 2):
                lifetype = "Terrestrial"
            elif (lifetype == 3):
                lifetype = "Marine and Terrestrial"
        else:
            lifeanswer = "No"
    elif (planettype == "Ice Planet"):
        life = random.randint (1, 16)
        if (life == 1):
            lifeanswer = "Yes"
            lifetype = "Subglacial"
        else:
            lifeanswer = "No"
    elif (planettype == "Desert Planet"):
        life = random.randint (1, 16)
        if (life == 1):
            lifeanswer = "Yes"
            lifetype = "Terrestrial"
        else:
            lifeanswer = "No"
    if (planettype == "Dead Planet"):
        lifeanswer = "No"
    elif (planettype == "Gas Giant" or planettype == "Ice Giant"):
        life = random.randint (1, 25)
        if (life == 1):
            lifeanswer = "Yes"
            lifetype = "Aerial"
        else:
            lifeanswer = "No"
    lifecells = random.randint (1, 3)
    if (lifecells == 1):
        lifecells = "Multicellular"
    else:
        lifecells = "Unicellular"
    if (lifeanswer == "Yes"):
        print ("Life:", lifecells, lifetype)
    else:
        print ("Life: None")
    currentnum += 1
    #That's All Folks. Version 1.0 SOLAR SYSTEM GENERATOR

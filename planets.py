#Initialize list with two planets
planet_list = ["Mercury", "Mars"]

#Add jupiter and Saturn
planet_list.append("Jupiter")
planet_list.append("Saturn")

#Create list of last two planets and add them to planet_list
last_two_planets = ["Uranus", "Neptune"]
planet_list.extend(last_two_planets)

#Insert Venus and Earth at popper positions
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

#Remove Pluto
planet_list.append("Pluto")

#Create list of rocky planets
rocky_planets = planet_list[0:4]

#Delete Pluto
del planet_list[-1]


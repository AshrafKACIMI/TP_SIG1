import re

pattern = """(-?[0-9]{1,3})°?[\s]*([0-9]{1,2})'?[\s]*([0-9]{1,2})"?"""

def lecture_cordonnee(nom, type_entree):
    m = None
    while m == None:
        coordonees = raw_input("Entrer la"+type_entree+" de "+nom+""" sous la forme DMS: <degré>° <minute>', <seconde>"\n""")
        m = re.search(pattern, coordonees)
        if m != None:
            coord =  m.groups()
            if verifier_coord(coord, type_entree):
            	break
            else:
            	print "la synthaxe est bonne, mais les valeurs sont erronnées"
            	continue
        print "La synthaxe n'a pas été respectée"
    
def verifier_coord(coord, type):
	if type == "longitude":
		return (-180 <= coord[0] <= 180) and (0 <= coord[1] < 60) (0 < coord[2] < 60)
	elif type == "latitude":
		return (-90 <= coord[0] <= 90) and (0 <= coord[1] < 60) (0 < coord[2] < 60)

def coord_sec(coordonnees):
	return coordonnees[0]*3600 + coordonnees[1]*60 + coordonnees[2]

def distance_metres((long_A, lat_A), (long_B, lat_B)):
	return ((coord_sec(long_A)-coord_sec(long_B))**2 + (coord_sec(lat_A)-coord_sec(lat_B))**2) ** 0.5 * 30

#pattern = "-".join([pattern] * 2)
longitude_A = lecture_cordonnee("A", "longitude")
latitude_A = lecture_cordonnee("A", "latitude")
longitude_B = lecture_cordonnee("B", "longitude")
latitude_B = lecture_cordonnee("B", "latitude")
d = distance_metres((longitude_A, latitude_A), (longitude_B, latitude_B))
print "La distance entre les deux points est : ",
print str(d/1000)+" km" if d/1000 >=1 else str(d)+" m"


import re
from math import sin, cos, atan,  sqrt

pattern = """(-?[0-9]{1,3})�?[\s]*([0-9]{1,2})'?[\s]*([0-9]{1,2})"?"""

def lecture_cordonnee(nom, type_entree):
    m = None     #objet qui contient le r�sultat de la v�rification d'expression r�guli�re
    while m == None:    #tant qu'on n'a pas d'entr�e valide
        coordonees = raw_input("Entrer la "+type_entree+" de "+nom+""" sous la forme DMS: <degr�>� <minute>' <seconde>" \n""") 
        #on v�rifie si l'entree v�rifie l'expression r�guli�re
        m = re.search(pattern, coordonees)
        if m != None:   #dans le cas o� elle la v�rifie
            coord =  map(int, m.groups()) #on r�cup�re les �lements DMS: degr�, minute, seconde sous forme de triplet
            if verifier_coord(coord, type_entree):    #si les valeurs des entr�es sont valides on quitte la boucle de lecture
            	break
            else:     #si les valeurs DMS d�passent leur intervalle
            	print "la synthaxe est bonne, mais les valeurs sont erronn�es"
            	m = None
        else:
            print "La synthaxe n'a pas �t� respect�e"
    return coord

def verifier_coord(coord, type_entree):
	if type_entree == "longitude":
		return (-180 <= coord[0] <= 180) and (0 <= coord[1] < 60) and (0 <= coord[2] < 60)
	elif type_entree == "latitude":
		return (-90 <= coord[0] <= 90) and (0 <= coord[1] < 60) and (0 <= coord[2] < 60)

def distance_km((long_A, lat_A), (long_B, lat_B)):
        R_long_A = long_A * pi / 180
        R_lat_A = lat_A * pi / 180
        R_long_B = long_B * pi / 180
        R_lat_B = lat_B * pi / 180
        delta_long = abs(R_long_A - R_long_B)
        delta_lat = abs(R_lat_A - R_lat_B)
        tmp = (sin(delta_lat/2)**2 + cos(R_lat_A)) * cos(R_lat_B) * sin(delta_long / 2) **2
        tmp2 = 2 * atan(sqrt( tmp / (1-tmp) ))
        return tmp2 * 6371 						#6371 est le rayon de la terre

#pattern = "-".join([pattern] * 2)
longitude_A = lecture_cordonnee("A", "longitude")
latitude_A = lecture_cordonnee("A", "latitude")
longitude_B = lecture_cordonnee("B", "longitude")
latitude_B = lecture_cordonnee("B", "latitude")
d = distance_metres((longitude_A, latitude_A), (longitude_B, latitude_B))
print "La distance entre les deux points est : ",
print str(d*1000)+" m" if d < 1 else str(d)+"km"


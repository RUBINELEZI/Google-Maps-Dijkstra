# A = Astir, Starting point
# B = Pallati me shigjeta
# C = Sheshi shqiponja 
# D = Zogu i zi 
# E = 21 dhjetori 
# F = Vasil Shanto 
# G = Qender
# H = Spitalet
# I = AliDem
# J = CIT, Final Destination


import requests
import networkx as nx

#API key
api_file = open('api-key.txt', 'r')
api_key = api_file.read()
api_file.close()

#codrdintes
A = '41.331989, 19.783476'
B = '41.322117, 19.791662'
C = '41.339077, 19.786791'
D = '41.333257, 19.804112'
E = '41.325707, 19.803352'
F = '41.321443, 19.805987'
G = '41.327817, 19.816265'
H = '41.344953, 19.838455'
I = '41.330143, 19.834251'
J = '41.341990, 19.845664'

#basse url
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

#response

AB = requests.get(url + "origins=" + A + "&destinations=" + B + "&key=" + api_key).json()["rows"][0]["elements"][0]["duration"]["value"]
BE = requests.get(url + "origins=" + B + "&destinations=" + E + "&key=" + api_key).json()["rows"][0]["elements"][0]["duration"]["value"]
BF = requests.get(url + "origins=" + B + "&destinations=" + F + "&key=" + api_key).json()["rows"][0]["elements"][0]["duration"]["value"]
EG = requests.get(url + "origins=" + E + "&destinations=" + G + "&key=" + api_key).json()["rows"][0]["elements"][0]["duration"]["value"]
GJ = requests.get(url + "origins=" + G + "&destinations=" + J + "&key=" + api_key).json()["rows"][0]["elements"][0]["duration"]["value"]
FI = requests.get(url + "origins=" + F + "&destinations=" + I + "&key=" + api_key).json()["rows"][0]["elements"][0]["duration"]["value"]
IJ = requests.get(url + "origins=" + I + "&destinations=" + J + "&key=" + api_key).json()["rows"][0]["elements"][0]["duration"]["value"]
DG = requests.get(url + "origins=" + D + "&destinations=" + G + "&key=" + api_key).json()["rows"][0]["elements"][0]["duration"]["value"]
DH = requests.get(url + "origins=" + D + "&destinations=" + H + "&key=" + api_key).json()["rows"][0]["elements"][0]["duration"]["value"]
AC = requests.get(url + "origins=" + A + "&destinations=" + C + "&key=" + api_key).json()["rows"][0]["elements"][0]["duration"]["value"]
CD = requests.get(url + "origins=" + C + "&destinations=" + D + "&key=" + api_key).json()["rows"][0]["elements"][0]["duration"]["value"]
HJ = requests.get(url + "origins=" + H + "&destinations=" + J + "&key=" + api_key).json()["rows"][0]["elements"][0]["duration"]["value"]


G = nx.Graph()
e = [('A','B',AB),('B','E',BE),('B','F',BF),('E','G',EG),('G','J',GJ),('F','I',FI),('I','J',IJ),('D','G',DG),('D','H',DH),('A','C',AC),('C','D',CD),('H','J',HJ),]
G.add_weighted_edges_from(e)
print(nx.dijkstra_path(G,'J','A'))


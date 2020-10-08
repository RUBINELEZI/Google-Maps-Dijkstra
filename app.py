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

#codrdintes from google
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
FE = requests.get(url + "origins=" + F + "&destinations=" + E + "&key=" + api_key).json()["rows"][0]["elements"][0]["duration"]["value"] 
IG = requests.get(url + "origins=" + I + "&destinations=" + G + "&key=" + api_key).json()["rows"][0]["elements"][0]["duration"]["value"]

# IMPLEMENT DIJKSTRA ALGORITHM

inf = float('inf')
# starting point
start = 'J'
stop = 'A'

# BUILD THE GRAPH
graph = {}

graph['A'] = {}
graph['A']['B'] = AB
graph['A']['C'] = AC

graph['B'] = {}
graph['B']['E'] = BE
graph['B']['F'] = BF
graph['B']['A'] = AB

graph['E'] = {}
graph['E']['G'] = EG
# NOTE I AM USING THE SAME VALUE FROM E TO F AS F TO E
graph['E']['F'] = FE 

graph['G'] = {}
graph['G']['J'] = GJ
graph['G']['D'] = DG
graph['G']['I'] = IG

graph['F'] = {}
graph['F']['E'] = FE
graph['F']['I'] = FI
graph['F']['B'] = BF

graph['I'] = {}
graph['I']['J'] = IJ
graph['I']['G'] = IG
graph['I']['F'] = FI

graph['C'] = {}
graph['C']['D'] = CD
graph['C']['A'] = AC

graph['D'] = {}
graph['D']['G'] = DG
graph['D']['H'] = DH
graph['D']['C'] = CD

graph['H'] = {}
graph['H']['J'] = HJ
graph['H']['D'] = DH

graph['J'] = {}
graph['J']['G'] = GJ
graph['J']['H'] = HJ
graph['J']['I'] = IJ

costs = {}
parents = {}
for node in graph:
    # we assume that costs is infinite until we go to that node
    costs[node] = inf
    parents[node] = {}
costs[start] = 0

def find_cheapest_node(costs, not_checked):
    cheapest_node = None
    lowest_cost = inf
    for node in not_checked:
        if costs[node] <= lowest_cost:
            lowest_cost = costs[node]
            cheapest_node = node
    return cheapest_node

if __name__ == '__main__':
    not_checked = [node for node in costs]
    node = find_cheapest_node(costs, not_checked)
    while not_checked:
        print(f'Not checked: {not_checked}')
        cost = costs[node]
        child_cost = graph[node]
        for c in child_cost:
            if costs[c] > cost + child_cost[c]:
                costs[c] = cost + child_cost[c]
                parents[c] = node
        
        not_checked.pop(not_checked.index(node))
        node = find_cheapest_node(costs, not_checked)

print(f'Costs: {costs}')
print(f'The time to go from {start} to {stop} is {costs[stop]} SECONDS ')

if costs[stop] < inf:
    path = [stop]
    i = 0
    while start not in path:
        path.append(parents[path[i]])
        i += 1
    print(f'The Shortest path is {path[::-1]}')
else:
    print('A path could not be found')






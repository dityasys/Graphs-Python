from graph import Graph
G = Graph()

A = G.addVertex('A')
B = G.addVertex('B')
C = G.addVertex('C')
D = G.addVertex('D')
E = G.addVertex('E')

A.addEdge('D', 7)
A.addEdge('E', 15)
B.addEdge('A', 5)
B.addEdge('E', 10)
C.addEdge('D', 15)
D.addEdge('E', 5)
E.addEdge('C', 20)

'''SO, THE GRAPHS LOOKS LIKE THIS:

LVertex-|
        | 
        |-> [A] ----> [[D, 7], [E, 15]]
            [B] ----> [[A, 5], [E, 10]]
            [C] ----> [[D, 15]]
            [D] ----> [[E, 5]]
            [E] ----> [[C, 20]]'''

string1 = 'A'
string2 = 'C'

x = G.Dijkstra(string1, string2)
if x is not None:
    print ('The Shortest Path from: ' + string1 + ' to ' + string2 + ' is: ' + str(x))




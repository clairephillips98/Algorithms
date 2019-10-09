
# Name: Claire Phillips
# NetID: 15cvp2
# student number: 20010910
# Date: September 21st 2019
# I certify that this submission contains my own work, except as noted.

from collections import namedtuple
from os import path

class Graph():
    City = namedtuple('City', [ 'arrive', 'candidate', 'estimate', 'reached', 'predecessor', 'path'])

    def __init__(self, file, start, end):

        with open(file, 'r') as f:
            vertices = [line.split() for line in f]
            cities = int(vertices[0][0])
            self.flights = []

            for x in range(len(vertices) - 1):
                self.flights.append(vertices[x + 1])

            for x in range(len(self.flights)):
                for y in range(len(self.flights[x])):
                    # iterate for 4 columns
                    self.flights[x][y] = int(self.flights[x][y])
        self.node = list(range(0, cities))
        self.start = int(start)
        self.end = int(end)
        print("Optimal Route from %s to %s " %(str(self.start),str(self.end)))
        self.currentNode = start #the new closest node
        self.node[start] = Graph.City( arrive = -1, candidate = False, estimate = 0, reached = True, predecessor = " ", path = " ")
        self.found = [start] #integers of reached cities
        self.unfound = [] #integer of all cities not reached
        self.candidates = [] #integers of all cities which have been marked as candidate
        for i  in range(0, cities):
            if i not in self.found:
                self.unfound.append(i) # add city to list of unfound cities
                self.node[i] = Graph.City( arrive = float('inf'), candidate = False, estimate = float('inf'), reached = False, predecessor = float('inf'), path = "undefined")
                self.nextFlight(i)
        Graph.dijkstras(self)

    def nextFlight(self,  destination): # find if there is a possible flight from selected node to destination node
        for flight in self.flights:
            if flight[0] == self.currentNode and flight[1] == destination and flight[2] > self.node[self.currentNode].arrive:
                if flight[3] < self.node[destination].estimate:
                    self.node[destination] = Graph.City(float('inf'), True, flight[3], False, self.currentNode, "undefined")
                    if destination not in self.candidates: self.candidates.append(destination) #add city to list of candidate cities

    def findClosestCandidate(self): #find the next closest node and make its estimate cost, make it reached and make it new current node
        lowest = float('inf')
        nextClosest = self.currentNode
        for candid in self.candidates: #for each integer in the list of integer cities
            if self.node[candid].estimate < lowest:
                lowest = self.node[candid].estimate
                nextClosest = candid
        self.currentNode = nextClosest
        predecessor = self.node[nextClosest].predecessor
        path = ("%s\n%s to %s" % (self.node[predecessor].path, predecessor, nextClosest))
        self.node[nextClosest] = Graph.City(lowest, False, lowest, True, predecessor, path)
        if nextClosest in self.candidates: self.candidates.remove(nextClosest)
        self.found.append(nextClosest)
        if nextClosest in self.unfound: self.unfound.remove(nextClosest)


    def dijkstras(self):
        while self.end in self.unfound and self.candidates:
            Graph.findClosestCandidate(self)
            for i in self.unfound:
                Graph.nextFlight(self, i)
        print ("%s\n\nArrive at %s at time %s" % (self.node[self.end].path, self.end, self.node[self.end].arrive))


if __name__ == "__main__":
    try:
        start = 20
        end = 9
        file = "2019_Lab_2_flights_real_data.txt"
        path.exists(file)
        Graph(file, start, end)
    except:
        print("couldn't find files.")




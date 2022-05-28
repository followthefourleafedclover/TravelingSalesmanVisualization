import turtle
import random
import math

#Distance Function
def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2) + ((y2 - x1)**2) ** 0.5

#Swap Function, allows us to change the position of the elements in the array
def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp
    return l

#Randomizes the coordinates for cites 
cities = []
sums = []
n = int(input())
for i in range(n):
    cities.append([random.randint(-240, 240), random.randint(-240, 240)])

#Initializes Turtle and Appearance     
salesman = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('black')
wn.colormode(255)
salesman.pencolor(255, 255, 255)
record = []

#Turtle draws the cities
for i in range(n):
    salesman.penup()
    salesman.setpos(cities[i][0], cities[i][1])
    salesman.pendown()
    salesman.dot(5, 'white')

#Turtle draws every possible path 
salesman.penup()
for i in range(math.factorial(len(cities))):
    print(cities)
    for j in range((len(cities))):
        distances = []
        salesman.pendown()
        salesman.setpos(cities[j][0], cities[j][1])
        for h in range(len(cities) - 1):
            distances.append(distance(cities[h][0], cities[h][1],cities[h+1][0], cities[h+1][1]))
    
    #Total Distance of path is recorded
    s = sum(distances)
    record.append([s, cities])
    
    #Order of the cities is randomized 
    k = random.randint(0, n - 1)
    l = random.randint(0, n - 1)

    cities = swap(cities, k, l)
    
#Shortest path is calculated, displayed, and drawn in red
shortest_path = min(record)
print("This is the shortest path:", shortest_path[0], shortest_path[1])

for i in range(n):
    salesman.pencolor(255, 0, 0)
    salesman.pendown()
    salesman.setpos(shortest_path[1][i][0], shortest_path[1][i][1])

salesman.write(str(shortest_path[0]), font=('Arial', 30))

turtle.done()
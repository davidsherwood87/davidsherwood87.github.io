"""
This model is designed to assign 10 agents to a set of random coordinates
and thenget them to eat the environment before checking where their
nearest neighbour is and then moving to another random point.
"""

import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv

environment = []
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:  #a list is created for each row
            rowlist.append(value) 
        environment.append(rowlist)  #puts all row lists into one super list

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()  #will show the environment as a raster image

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

agents = []
agents.append(agentframework.Agent(environment, agents))
print (agents[0])  #test to see if one agent has been suvvessfully placed

fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1])                 

#ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

def update(frame_number):
    """ Takes in our Agent class, then plots the data and iterates 100 times""" 
    fig.clear()   
    for j in range(num_of_iterations):
        random.shuffle(agents)  #shuffles the agents every iteration
        for i in range(num_of_agents):
            agents[i].move()  #moves the agents randomly
            agents[i].eat()  #agents eat away the environment
            agents[i].share_with_neighbours(neighbourhood)    
      
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        #print(agents[i].x, agents[i].y)
        
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)        
    
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
matplotlib.pyplot.show()  #will show the agents moving arounf the environment
    


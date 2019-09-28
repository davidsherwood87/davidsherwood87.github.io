"""
This file contains one class comprising of a move, eat and share function
"""
#agentframework.py
import random
class Agent():   
    def __init__(self, environment, agents):
        self.environment = environment
        self.store = 0
        self.agents = agents
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)

    def __str__(self):
        """
        Returns:
        A description of the agent detailing it's location and store.
        """
        return "Location x = " + str(self.x) + ", y = " + str(self.y) + ", store = " + str(self.store)

                   
    def move(self): 
        """
        Using the random function, both y and x axis are given a random
        number
        """
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
   
    def eat(self): 
        """
        Each agent will eat part of the environment it is in
        """        
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
    
    def share_with_neighbours (self, neighbourhood):
        """
        The agents will communicate with eachother so that they know
        eachothers location
        """
        
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave            
    
    def distance_between(self, agent):
        """ 
        Uses calculation to determine the distance between a y and
        and x agent in the environment
        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
                               
                        
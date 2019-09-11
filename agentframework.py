# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 12:27:20 2019

@author: david
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
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
   
    def eat(self): # Each agent will eat part of the environment
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
    
    def share_with_neighbours (self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
            
    
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
                               
                        
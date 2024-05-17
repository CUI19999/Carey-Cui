#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 09:08:16 2024

@author: zhengcui
"""
import random

class Agent:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def __repr__(self):
        return f"Agent({self.id}, {self.x}, {self.y})"


class World:
    def __init__(self, width, height, num_agents):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.agents = []
        self.initialize_agents(num_agents)

    def initialize_agents(self, num_agents):
        for i in range(num_agents):
            while True:
                x, y = random.randint(0, self.width-1), random.randint(0, self.height-1)
                if self.grid[y][x] is None:
                    agent = Agent(i, x, y)
                    self.grid[y][x] = agent
                    self.agents.append(agent)
                    break

    def find_empty_patch(self):
        empty_patches = [(x, y) for x in range(self.width) for y in range(self.height) if self.grid[y][x] is None]
        return random.choice(empty_patches) if empty_patches else None

    def move_agent(self, agent):
        new_pos = self.find_empty_patch()
        if new_pos:
            self.grid[agent.y][agent.x] = None  
            new_x, new_y = new_pos
            agent.move(new_x, new_y)
            self.grid[new_y][new_x] = agent 

world = World(width=5, height=10, num_agents=10)
world2 = World(width=100, height=200, num_agents=300)


for _ in range(5):  
    for agent in world.agents:
        world.move_agent(agent)
    print(world.grid)  

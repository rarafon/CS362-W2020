# -*- coding: utf-8 -*-
"""
Fri Jan 17 2020

@author: situa
set number of victory cards to 0
also modified the number of victory cards to other values
"""

import Dominion
import testUtility
import random
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
numVictCards=100
numCurses = -10 + 10 * len(player_names)

#Define box, # Victory Cards is for Gardens
box = testUtility.GetBoxes(numVictCards)

supply_order = testUtility.MakeSupplyOrder()

supply = testUtility.MakeSupply(player_names, box, numCurses, numVictCards)

players = testUtility.CreatePlayers(player_names)

#Play the game
testUtility.PlayGame(players, supply, supply_order)

testUtility.WriteFinalMessage(players)
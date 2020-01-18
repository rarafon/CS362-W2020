# -*- coding: utf-8 -*-
"""
Fri Jan 17 2020

@author: situa
Set player_names to be blank, Remove Annie from Game, 
Remove the other two from the game besides Annie
"""

import Dominion
import testUtility
import random
from collections import defaultdict

#Get player names
player_names = []

#number of curses and victory cards
if len(player_names)>2:
    numVictCards=12
else:
    numVictCards=8
numCurses = -10 + 10 * len(player_names)

#Define box, # Victory Cards is for Gardens
box = testUtility.GetBoxes(numVictCards)

supply_order = testUtility.MakeSupplyOrder()

supply = testUtility.MakeSupply(player_names, box, numCurses, numVictCards)

players = testUtility.CreatePlayers(player_names)

#Play the game
testUtility.PlayGame(players, supply, supply_order)

testUtility.WriteFinalMessage(players)
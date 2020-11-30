## Riddler Express
# First problem involves diagonal sidewalks instead of following streets
# 7x7 grid

import numpy as np
xmap = [[x for x in range(-3,4)] for y in range(-3,4)]
ymap = [[y for x in range(-3,4)] for y in range(-3,4)]

# print(xmap)
# print(ymap)

# Indices of initial x and y
xi = 3
yi = 3

oldisbetter = 0
newisbetter = 0
nodifferent = 0

for ii in range(len(xmap)):
   for jj in range(len(xmap[0])):
      xdist = abs(xmap[ii][jj] - xmap[xi][yi])
      ydist = abs(ymap[ii][jj] - ymap[xi][yi])

   # Old distance:
   # Travel is simply sum of x and y distance    
      dist_old = xdist + ydist

   # New distance:
   # Case 1: Route is purely diagonal, distance is hypotenuse of right triangle
   # Case 2: Travel diagonally until you run out of x or y distance, then distance
   #         is root 2 times the leftover distance
      dist_new = 2**.5 * min([xdist, ydist]) + 2**.5 * (abs(xdist - ydist))
   
      if (dist_old < dist_new):
         oldisbetter = oldisbetter + 1
      
      elif (dist_new < dist_old):
         newisbetter = newisbetter + 1
      
      else:
         nodifferent = nodifferent + 1

print(oldisbetter)
print(newisbetter)
print(nodifferent)

# Gave up on Classic because the problem is poorly defined. Is City Hall still located
# in the middle of the city? If so, it is at an intersection which doesn't have a clear
# starting point for walking. Homes no longer being located at intersection also makes
# check-casing more difficult. I don't want to resort to conjecture to solve the problem.

## Riddler Classic
# Second problem involves sidewalks that follow streets until intersections,
# at which they become diagonal. Ratio of diagonal intersections to a normal
# block is sqrt(2)/6 to 1

# Check-casing should be in 0.5 block increments for consistency
#     First x block: (0,-2.5),(0,-1.5),(0,-0.5),(0,0.5),(0,1.5),(0,2.5)
#     First y block: (-2.5,0),(-1.5,0),(-0.5,0),(0.5,0),(1.5,0),(2.5,0)
# Assume trip begins from same place (0,0) and first move is to closest corner

#for ii in range(len(xmap)):
#   for jj in range(len(xmap[0])):
#      first_move = 1/6 # first move is always from (0,0) to closest corner
#      startx = xmap[xi][yi]
#      starty = ymap[xi][yi]
#      
#      # N-S blocks
#      endnsx = xmap[ii][jj]
#      endnsy = ymap[ii][jj] + 0.5 # don't use last column in matrix
#      
#      if endnsy < 3:
#         xdist = abs(endnsx - startx)
#         ydist = abs(endnxy - starty)
#         
#         
#      
#      
#      # E-W blocks
#      endewx = ymap[ii][jj] + 0.5 # don't use last row in matrix
#      endewy = ymap[ii][jj]
#      
#      if endewx < 3:
#         
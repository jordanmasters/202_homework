def CellularAutomata():

   # set canvas width and height
   # move laptops can handle ~180 columns, but for the larger images
   # set width big (ex: 500) and 
   width = 500
   height = 500

   # 
   row = [0] * width   
   # set seed at center
   # seed_pos = width / 2
   seed_pos = width - 5
   row[seed_pos] = 1

   # Map the cell values to a symbol for printing
   img_map = {0:'*', 1:' '}

   # print first line with seed: effectively row_index 0 
   print  ''.join( [img_map[x] for x in row])

   # Generate cellular automata by applying simple 
   row_index = 1
   while(row_index < height):
      # new Cellular values
      next_row = []

      # next_row = []
      # loop through 0 to width size and store the current cell status in next_row list
      for i in range(0,width):

         # RULES - MAIN RULE
         # next_row = rule_0(row, next_row, width, col)

         # Main Condition
         if i > 0 and i < width-1:
            # rule1_status = rule1(row[i-1],row[i],row[i+1])
            # rule2_status = rule2(row[i-1],row[i],row[i+1])
            next_cell = ruleSetUniversal([row[i-1],row[i],row[i+1]])
            next_row.append(next_cell)


            # if (rule1_status == 1) or (rule2_status == 1):
            #    next_row.append(1)
            # else:
            #    next_row.append(0)
            
         # Left Boundary Condition
         elif(i == 0):
            if row[1] == 1:
               next_row.append(1)
            else:
               next_row.append(0)


         # Right Boundary Condition
         elif(i == width-1):
            if row[width-2] == 1:
               next_row.append(1)
            else:
               next_row.append(0)


      # draw current cell state
      print  ''.join( [img_map[e] for e in next_row])

      # update cell list
      row = next_row

      # row_index count
      row_index += 1


def ruleSet1():
   [
      [[1,0,0],1],
      [[0,0,1],1]
   ]
   pass 

def ruleSetUniversal(env):

   rules = [[[1,1,1],0],
            [[1,1,0],1],
            [[1,0,1],1],
            [[1,0,0],0],
            [[0,1,1],1],
            [[0,1,0],1],
            [[0,0,1],1],
            [[0,0,0],0]]
   for rule in rules:
      if env == rule[0]:
         return rule[1]










































def rule1(l, c, r):
   '''
   Does a calulation to check current cell/neightbors and output cell for X position 
   '''
   env = []
   env.extend([l,c,r])
   # print env, 'vs', [1,0,0] 
   if env == [1,0,0]:
      next_cell = 1
      # print 1
   else:
      next_cell = 0
      # print 0
   return next_cell
def rule2(l, c, r):
   '''
   Does a calulation to check current cell/neightbors and output cell for X position 
   '''
   env = []
   env.extend([l,c,r])
   # print env, 'vs', [0,0,1] 
   if env == [0,0,1]:
      next_cell = 1
      # print 1
   else:
      next_cell = 0
      # print 0

   return next_cell


def rule_0(row, next_row, width, i):
   '''
   This function says it has one rules, but it really has two
   rule one: neightbor to the lft 
   #  1
   #  local seed: 1
   #  left:       1
   #  right:      0
   #  
   #  result:     0

   #  2
   #  local seed: 1
   #  left:       1
   #  right:      0
   #  
   #  result:     0
   rule two:
   '''

   # inside cells - check the neighbor cell state
   if i > 0 and i < width-1:
      if row[i-1] == row[i+1]:
         next_row.append(0)
      else:
         next_row.append(1)


   # RULES - Boundary Cleanup

   # left-most cell : check the second cell
   elif(i == 0):
      if row[1] == 1:
         next_row.append(1)
      else:
         next_row.append(0)

   # right-most cell : check the second to the last cell
   elif(i == width-1):
      if row[width-2] == 1:
         next_row.append(1)
      else:
         next_row.append(0)
   return next_row


   [
      [[0,0,0],1],
      [[0,0,1],0],
      [[0,1,0],0],
      [[0,1,1],1],
      [[1,0,0],0],
      [[1,0,1],0],
      [[1,1,0],0],
      [[1,1,1],1]
   ]

#   
#   1 
#      local seed: 0
#      left:       0
#      right:      0
#   
#      result:     1
#   2
#      local seed: 0
#      left:    0
#      right:      1
#   
#      result:     0
#   3
#      local seed: 1
#      left:    0
#      right:      0
#   
#      result:     0
#   4
#      local seed: 1
#      left:    0
#      right:      1
#   
#      result:     1
#   5
#      local seed: 0
#      left:    1
#      right:      0
#   
#      result:     0
#   6
#      local seed: 0
#      left:    1
#      right:      1
#   
#      result:     0
#   7
#      local seed: 1
#      left:    1
#      right:      0
#   
#      result:     0
#   8
#      local seed: 1
#      left:    1
#      right:      1
#   
#      result:     1
#   












if __name__ == '__main__':
   CellularAutomata()

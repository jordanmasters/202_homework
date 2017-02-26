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

      # loop through 0 to width size and store the current cell status in next_row list
      for i in range(0,width):

         # Main Condition
         if i > 0 and i < width-1:

            next_cell = ruleSetUniversal([row[i-1],row[i],row[i+1]])
            next_row.append(next_cell)
            
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



if __name__ == '__main__':
   CellularAutomata()


def valid(coords, cols, rows):
  (r,c) = coords
  return (
    r >= 0 and 
    c >=0 and
    r < rows and
    c < cols
  )

def traverse(coords, matrix, cols, rows):
  
  if not valid(coords,cols,rows):
    return
  
  (row,col) = coords
  
  if not matrix[row][col]:
    return
  
  matrix[row][col] = 0
  
  children = [(row-1,col),(row+1,col),
             (row,col-1),(row,col+1)]
  
  for child in children:
    traverse(child, matrix, cols, rows)
  
def get_number_of_islands(binaryMatrix):
  # itterate through the matrix
  cols = len(binaryMatrix[0])
  rows = len(binaryMatrix)
  islands = 0
  
  for row in range(rows):
    for col in range(cols):
      coords = (row,col)
      value = binaryMatrix[row][col]
      
      if value:
        islands += 1
        traverse(coords, binaryMatrix, cols, rows)
        
  return islands

print(get_number_of_islands([[1,0,1,0]]))


# def get_number_of_islands(binaryMatrix):

#   visit_map_row = [False for element in binaryMatrix[0]]
#   visit_map = [visit_map_row for element in binaryMatrix]
  
#   island_count = 0
  
#   # create helper function for what happens when you visit a cell
#   def process_cell(coords):
#     (x, y) = coords
    
#     if visit_map[x][y]:
#       return 0
    
#     visit_map[x][y] = True
    
#     if not binaryMatrix[x][y]:
#       return 0
    
#     e = False
    
#     try: 
#       process_cell(x-1,y) # up
#     except Exception: 
#       e = True
#     try: 
#       process_cell(x+1,y) # down
#     except Exception: 
#       e = True
#     try: 
#       process_cell(x,y-1) # left
#     except Exception:
#         e = True
#     try: 
#       process_cell(x,y+1) # right
#     except Exception:
#       e = True
    
#     return 1
    
#     # loop through BM and process each cell adding the return value to counts
  
#   for x,row in enumerate(binaryMatrix):
#     for y,cell in enumerate(binaryMatrix[x]):
#       coords = (x,y)
#       island_count += process_cell(coords)
  
#   return island_count



# function getNumberOfIslands(binaryMatrix):
#     islands = 0
#     rows = binaryMatrix.length # number of rows
#     cols = binaryMatrix[0].length # number of columns

#     for i from 0 to rows-1:
#         for j from 0 to cols-1:
#             if (binaryMatrix[i][j] == 1):
#                 markIsland(binaryMatrix, rows, cols, i, j)
#                 islands++
                
#     return islands


# function markIsland(binaryMatrix, rows, cols, i, j):
#     q = new Queue()
#     q.push([i,j])
#     while (!q.isEmpty()):
#         item = q.pop()
#         x = item[0]
#         y = item[1]
#         if (binaryMatrix[x][y] == 1):
#             binaryMatrix[x][y] = -1
#             pushIfValid(q, rows, cols, x-1, y)
#             pushIfValid(q, rows, cols, x, y-1)
#             pushIfValid(q, rows, cols, x+1, y)
#             pushIfValid(q, rows, cols, x, y+1)


# function pushIfValid(q, rows, cols, x, y):
#     if (x >= 0 AND x < rows AND y >= 0 AND y < cols):
#         q.push([x,y])
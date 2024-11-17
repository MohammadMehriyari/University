# Missionaries and Cannibals problem
# With DFS and BFS algorithm

def move1M(state): # Move 1 missionarie
    if (state[0] >= 1 and state[2] == 1): 
        successor = (state[0]-1, state[1],0) 
        if ((successor[0]>0 and successor[0] < successor[1]) or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor

    elif (state[0] <= 2 and state[2] == 0): 
        successor = (state[0]+1, state[1],1) 
        if ((successor[0]>0 and successor[0] < successor[1]) or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            return successor
        return successor

def move2M(state): # Move 2 missionaries
    if (state[0] >= 2 and state[2] == 1): 
        successor = (state[0]-2, state[1],0) 
        if ((successor[0]>0 and successor[0] < successor[1])  or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor

    elif (state[0] <= 1 and state[2] == 0 ):  
        successor = (state[0]+2, state[1],1) 
        if ((successor[0]>0 and successor[0] < successor[1])  or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor

def move1C(state): # Move 1 cannibal
    if (state[1] >= 1 and state[2] == 1): 
        successor = (state[0], state[1]-1,0) 
        if ((successor[0]>0 and successor[0] < successor[1])  or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor

    elif (state[1] <= 2 and state[2] == 0): 
        successor = (state[0], state[1]+1,1) 
        if ((successor[0]>0 and successor[0] < successor[1])  or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor

def move2C(state): # Move 2 cannibals
    if (state[1] >= 2 and state[2] == 1): 
        successor = (state[0], state[1]-2,0) 
        if ((successor[0]>0 and successor[0] < successor[1])   or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor

    elif (state[1] <= 1 and state[2] == 0): 
        successor = (state[0], state[1]+2,1) 
        if ((successor[0]>0 and successor[0] < successor[1])  or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor


def move1M1C(state): # Move 1 missionarie and 1 cannibal
    if (state[0] >=1 and state[1] >=1 and state[2] == 1): 
        successor = (state[0]-1,state[1]-1,0) 
        if ((successor[0]>0 and successor[0] < successor[1])  or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor

    elif (state[0] <= 2 and state[1] <= 2 and state[2] == 0): 
        successor = (state[0]+1,state[1]+1,1) 
        if ((successor[0]>0 and successor[0] < successor[1])  or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor

def format(parent,explored,solution,move):
  if (parent!= None):
    for node in explored:
      if (node[0] == parent):
        if move==0:
          a="1M"
        if move==1:
          a="2M"
        if move==2:
          a="1C"
        if move==3:
          a="2C"
        if move==4:
          a="1M1C"
        return format(node[1],explored,str(parent)+"--->"+a+"--->"+str(solution),node[2])
  return solution


# # BFS

def addbfs(successor,frontier,explored):
  new=True
  for node in frontier:
    if node[0]==successor[0]:
      new=False
  if (new):
    for node in explored:
      if node[0]==successor[0]:
        new=False
  if (new):
    frontier.append(successor)
  return frontier


def bfs(frontier,explored,goal):
    while (frontier): 
        node = frontier.pop(0) 
        explored.append(node) 
        
        fun = [move1M(node[0]), move2M(node[0]), move1C(node[0]), move2C(node[0]), move1M1C(node[0])] 
        cost= [1,1,1,1,1]
        
        for f in range(len(fun)):
          if fun[f]!= None:
            successor = (fun[f],node[0],f,node[3]+cost[f]) 
            if (goal==fun[f]): 
              print("\nPath:",format(node[0],explored,successor[0],successor[2])) 
              print("\nTotal cost:",successor[3],"movements.")
              return True    
            frontier=addbfs(successor,frontier,explored)
    return False 


# # DFS

def adddfs(successor,frontier,explored):
  new=True
  for node in frontier:
    if node[0]==successor[0]:
      new=False
  if (new):
    for node in explored:
      if node[0]==successor[0]:
        new=False
  if (new):
    frontier.insert(0,successor) 
  return frontier

def dfs(frontier,explored,goal):
    while (frontier): #if frontier has at least one element
        node = frontier.pop(0) #extract first node from the frontier list
        explored.append(node) #add node to explored list
        fun = [move1M(node[0]), move2M(node[0]), move1C(node[0]), move2C(node[0]), move1M1C(node[0])] 
        cost=[1,1,1,1,1]
        for f in range(len(fun)):
          if fun[f]!= None:
            successor = (fun[f],node[0],f,node[3]+cost[f]) 
            if (goal==fun[f]): #If I reach the goal state, print solution and end program
              print("\nPath:",format(node[0],explored,successor[0],successor[2])) #Print path
              print("\nTotal cost:",successor[3],"movements.\n") #Print cost
              return True    
            frontier=adddfs(successor,frontier,explored)
    return False 

# ### BFS

state =(3,3,1) #initial state
goal=(0,0,0) #goal state

frontier=[(state,"None","None",0)] #State, parent, movement, cost
explored=[]

print("\nBFS result is: ")
bfs(frontier, explored,goal)


# ### DFS

state =(3,3,1) #initial state
goal=(0,0,0) #goal state

frontier=[(state,"None","None",0)] #State, parent, movement, cost
explored=[]

print("\nDFS result is: ")
dfs(frontier, explored,goal)
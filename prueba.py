from collections import deque #queues required for the resolution
#to define the function to solve the problem
def solvelabyrinth(labyrinth): 
    n = len(labyrinth)
    m = len(labyrinth[0])
    vertical = False #variable for the orientation
    start=(0,2) #start at x=2 since it is the head of the rod
    queue1=[]
    queue2=[] #queue to remove duplicate locations
    queue1.append((start[0],start[1],0,vertical)) #introduce the first coordinate to the queue
    queue2.append((start[0],start[1],vertical)) 
    directions=[[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,-1]] #the last two are the rotations

#Loop to search for the exit
    while len(queue1) !=0:
        coord=queue1.pop(0)
        #coordinates match the endpoint
        if coord[0]==n-1 and coord[1]==m-1:
            return coord[2] 
        #search for new coordinates
        for dir in directions:
            n1=coord[0]+dir[0]
            m1=coord[1]+dir[1]
            #no possible locations
            if(n1<0 or n1 >=n or m1<0 or m1>=m or labyrinth[n1][m1]=="#"):continue
            vertical = coord[3]
            if(dir==[1,-1] or dir==[1,-1]):
                vertical = not vertical
             #test that it can rotate in the 3x3 square
            if(dir==[-1,1]):
                if(labyrinth[n1 - 1][m1] == "#" or labyrinth[n1 + 1][m1] == "#" or labyrinth[n1 + 1][m1 - 2] == "#" or labyrinth[n1 - 1][m1 - 2] == "#"):continue
            if(dir==[1,-1]):
                if(labyrinth[n1][m1 - 1] == "#" or labyrinth[n1][m1 + 1] == "#" or labyrinth[n1 - 2][m1 + 1] == "#" or labyrinth[n1 - 2][m1 - 1] == "#"):continue
            #check if the queue meets the restrictions
            if(vertical == False):
                if(n1 <0 or n1 >=n or m1 - 1 <0 or m1 - 1 >=m or labyrinth[n1][m1 - 1] == "#"):continue
                if(n1 <0 or n1 >=n or m1 - 2 <0 or m1 - 2 >=m or labyrinth[n1][m1 - 2] == "#"):continue
            else:
                if(n1 - 1 <0 or n1 - 1 >=n or m1<0 or m1>=m or labyrinth[n1 - 1][m1]=="#"):continue
                if(n1 - 2 <0 or n1 - 2 >=n or m1<0 or m1>=m or labyrinth[n1 - 2][m1]=="#"):continue
            #new movement
            new_node = (n1,m1,coord[2]+1, vertical)
            #if the new movement is not recorded, it adds it
            if (not queue2.count((n1,m1,vertical))):
                queue1.append(new_node)
                queue2.append((n1,m1,vertical))    
            
    else:
        return -1
            


#Test 1
labyrinth = [
    [".",".",".",".",".",".",".",".","."],
    ["#",".",".",".","#",".",".",".","."],
    [".",".",".",".","#",".",".",".","."],
    [".","#",".",".",".",".",".","#","."],
    [".","#",".",".",".",".",".","#","."]
]

solve = solvelabyrinth(labyrinth)
print(solve)  

#Test 2
labyrinth = [
    [".",".",".",".",".",".",".",".","."], 
    ["#",".",".",".","#",".",".","#","."], 
    [".",".",".",".","#",".",".",".","."], 
    [".","#",".",".",".",".",".","#","."], 
    [".","#",".",".",".",".",".","#","."]
]
solve = solvelabyrinth(labyrinth)
print(solve)

#Test 3
labyrinth = [
    [".",".","."],
    [".",".","."],
    [".",".","."]
]
solve = solvelabyrinth(labyrinth)
print(solve)  

#Test 4
labyrinth = [
    [".",".",".",".",".",".",".",".",".","."],
    [".","#",".",".",".",".","#",".",".","."],
    [".","#",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".","#",".",".",".",".",".",".",".","."],
    [".","#",".",".",".","#",".",".",".","."],
    [".",".",".",".",".",".","#",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."]
]
solve = solvelabyrinth(labyrinth)
print(solve) 
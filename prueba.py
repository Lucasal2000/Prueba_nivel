from collections import deque
def solvelabyrinth(labyrinth):
    n = len(labyrinth)
    m = len(labyrinth[0])
    start=(0,0)
    queue=deque()
    queue.appendleft((start[0],start[1],0))
    directions=[[0,1],[0,-1],[1,0],[-1,0]]
    visited=[[False]*m for _ in range(n)] 

    while len(queue) !=0:
        coord=queue.pop()
        visited[coord[0]][coord[1]]=True

        if coord[0]==n-1 and coord[1]==m-1:
            return coord[2]+1
        for dir in directions:
            n1=coord[0]+dir[0]
            m1=coord[1]+dir[1]
            if(n1<0 or n1 >=n or m1<0 or m1>=m or labyrinth[n1][m1]=="#" or visited[n1][m1]):continue
            queue.appendleft((n1,m1,coord[2]+1))


labyrinth = [
    [".",".",".",".",".",".",".",".","."],
    ["#",".",".",".","#",".",".",".","."],
    [".",".",".",".","#",".",".",".","."],
    [".","#",".",".",".",".",".","#","."],
    [".","#",".",".",".",".",".","#","."]
]

solve = solvelabyrinth(labyrinth)
print(solve)  


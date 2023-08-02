from collections import deque #colas necesarias para la resolución
#definimos la función para resolver el problema
def solvelabyrinth(labyrinth): 
    n = len(labyrinth)
    m = len(labyrinth[0])
    vertical = False #variable vertical 
    start=(0,2) #empieza en x=2 ya que es la cabeza de la barra 
    queue1=[]
    queue2=[] #cola para eliminar ubicaciones duplicadas
    queue1.append((start[0],start[1],0,vertical)) #introducimos la primera coordenada a la cola
    queue2.append((start[0],start[1],vertical)) #introducimos la primera coordenada a la cola
    directions=[[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,-1]] #las dos últimas son las rotaciones

#Bucle para buscar la salida
    while len(queue1) !=0:
        coord=queue1.pop(0)
        #coordenadas coinciden con el final
        if coord[0]==n-1 and coord[1]==m-1:
            return coord[2] 
        #busqueda de nuevas coordenadas
        for dir in directions:
            n1=coord[0]+dir[0]
            m1=coord[1]+dir[1]
            #no posibles lugares
            if(n1<0 or n1 >=n or m1<0 or m1>=m or labyrinth[n1][m1]=="#"):continue
            vertical = coord[3]
            if(dir==[1,-1] or dir==[1,-1]):
                vertical = not vertical
             #probamos que puede rotar en el cuadrado 3x3
            if(dir==[-1,1]):
                if(labyrinth[n1 - 1][m1] == "#" or labyrinth[n1 + 1][m1] == "#" or labyrinth[n1 + 1][m1 - 2] == "#" or labyrinth[n1 - 1][m1 - 2] == "#"):continue
            if(dir==[1,-1]):
                if(labyrinth[n1][m1 - 1] == "#" or labyrinth[n1][m1 + 1] == "#" or labyrinth[n1 - 2][m1 + 1] == "#" or labyrinth[n1 - 2][m1 - 1] == "#"):continue
            #comprobar si la cola cumple ras restricciones
            if(vertical == False):
                if(n1 <0 or n1 >=n or m1 - 1 <0 or m1 - 1 >=m or labyrinth[n1][m1 - 1] == "#"):continue
                if(n1 <0 or n1 >=n or m1 - 2 <0 or m1 - 2 >=m or labyrinth[n1][m1 - 2] == "#"):continue
            else:
                if(n1 - 1 <0 or n1 - 1 >=n or m1<0 or m1>=m or labyrinth[n1 - 1][m1]=="#"):continue
                if(n1 - 2 <0 or n1 - 2 >=n or m1<0 or m1>=m or labyrinth[n1 - 2][m1]=="#"):continue
            #nuevo movimiento
            new_node = (n1,m1,coord[2]+1, vertical)
            #en caso de que el nievo movimiento no este registrado lo añade
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
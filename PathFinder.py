import sys
sys.setrecursionlimit(15000)
maze=[]
a = open(sys.argv[1],"r",encoding = "utf-8")
for mapp in a.readlines():
    mapp = mapp.rstrip("\n")
    maze.append([i for i in mapp])
    if "S" in mapp:
        x = len(maze) -1
        y = mapp.index("S")
satir = x
sutun = y
adımlist = []
i_copy = int()
j_copy = int()
def Motor(x,y,adımlist,i_copy,j_copy):
    global list
    global changepos
    possiblelist = []
    list = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
    for i, j in list:
        if (i >= 0 and i < len(maze)) and (j >= 0 and j < len(maze[0])):
            possiblelist.append([i, j])
    checklist = []
    for i,j in possiblelist:
        checklist.append(maze[i][j])
        if checklist.count("P") > 1:
            if maze[x][y] != "S":
                maze[x][y] = "K"
    if maze[x][y] == "K" :
        if not "P" in checklist :
            maze[x][y] = "W"
    for i, j in possiblelist:
        if maze[i][j] == "P":
            maze[i][j] = "1"
            adımlist.append([i,j])
            return Motor(i, j, adımlist, i_copy, j_copy)
        elif maze [i][j] == "F":
            return
    if not "P" in checklist and not "S" in checklist:
        for i in adımlist[-1::-1]:
            if maze[i[0]][i[1]] != "K":
                maze[i[0]][i[1]] = "W"
                adımlist.pop()
            elif maze[i[0]][i[1]] == "K":
                break
        return Motor(i[0], i[1], adımlist, i_copy, j_copy)
    elif "S" in checklist:
        for i, j in possiblelist:
            if maze[i][j] == "S" :
                adımlist.clear()
                return Motor(i, j, adımlist, i_copy, j_copy)
Motor(x,y,adımlist,i_copy,j_copy)
b = open(sys.argv[4], "w")
for i in maze:
    for k in range(len(maze[0])):
        if "W" in i:
            i[i.index("W")] = "0"
        if "K" in i:
            i[i.index("K")] = "1"
        if "P" in i:
            i[i.index("P")] = "0"
for i in maze:
    b.write("".join(i))
    b.write("\n")
maze = []
H = int(sys.argv[3])
Full = H
c = open(sys.argv[2],"r",encoding="utf-8")
for mapp in c.readlines():
    mapp = mapp.rstrip("\n")
    maze.append([i for i in mapp])
    if "S" in mapp:
        x = len(maze) -1
        y = mapp.index("S")
satir = x
sutun = y
adımlist = []
i_copy = int()
j_copy = int()
def Motor(x,y,adımlist,i_copy,j_copy):
    global list
    global H
    global Full
    possiblelist = []
    list = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
    for i, j in list:
        if (i >= 0 and i < len(maze)) and (j >= 0 and j < len(maze[0])):
            possiblelist.append([i, j])
    checklist = []
    for i,j in possiblelist:
        checklist.append(maze[i][j])
        if checklist.count("P") > 1:
            if maze[x][y]!= "S":
                maze[x][y] = "K"
    if maze[x][y] == "K" :
        if not "P" in checklist :
            if maze[i[0]][i[1]] !="S":
                maze[x][y] = "W"
    if H == 0 and maze [i][j] != "F" and maze[i][j] != "H":
        for i in adımlist[-1::-1]:
            if maze[i[0]][i[1]] != "K":
                if maze[i[0]][i[1]] !="S":
                    maze[i[0]][i[1]] = "W"
                    adımlist.pop()
                    H += 1
            elif maze[i[0]][i[1]] == "K":
                H += 1
                break
        return Motor(i[0], i[1], adımlist, i_copy, j_copy)
    for i, j in possiblelist:
        if maze[i][j] == "H":
            maze[i][j] = "1"
            adımlist.append([i, j])
            H = Full
            return Motor(i, j, adımlist, i_copy, j_copy)
        elif maze[i][j] == "P":
            maze[i][j] = "1"
            adımlist.append([i,j])
            H-=1
            return Motor(i, j, adımlist, i_copy, j_copy)
        elif maze [i][j] == "F":
            return
    changepos = []

    for i in adımlist[-1::-1]:
        possiblelist = []
        list = [[i[0] - 1, i[1]], [i[0] + 1, i[1]], [i[0], i[1] - 1], [i[0], i[1] + 1]]
        for k, j in list:
            if (k >= 0 and k < len(maze)) and (j >= 0 and j < len(maze[0])):
                possiblelist.append([k, j])
        checklist = []
        for k, j in possiblelist:
            checklist.append(maze[k][j])
        if not "P" in checklist and not "S" in checklist and not "H" in checklist:
            if maze[i[0]][i[1]] != "K":
                maze[i[0]][i[1]] = "W"
                H+=1
                adımlist.pop()
            elif maze[i[0]][i[1]] == "K":
                maze[i[0]][i[1]] = "0"
                adımlist.pop()
                H+=1
                break
        elif "P" in checklist or "H" in checklist:
            break
    for i in adımlist[-1::-1]:
        return Motor(i[0], i[1], adımlist, i_copy, j_copy)
    if "S" in checklist:
        for i, j in possiblelist:
            if maze[i][j] == "S":
                adımlist=[]
                H+=1
                changepos.append([i,j])
                return Motor(i, j, adımlist, i_copy, j_copy)
        return Motor(i[0],i[1],adımlist,i_copy,j_copy)
    for k, j in changepos:
        maze[k][j] = "S"
Motor(x,y,adımlist,i_copy,j_copy)
for i in maze:
    for k in range(len(maze[0])):
        if "W" in i:
            i[i.index("W")] = "0"
        if "K" in i:
            i[i.index("K")] = "1"
        if "P" in i:
            i[i.index("P")] = "0"
b.write("\n")
for i in maze:
    b.write("".join(i))
    b.write("\n")
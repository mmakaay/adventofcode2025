grid=[l[:-1]for l in open(0)]
w,h,D=len(grid[0]),len(grid),[(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
print(sum(grid[y][x]=="@"and sum(grid[y+j][x+i]=="@" for i,j in D if 0<=x+i<w and 0<=y+j<h)<4 for y in range(h) for x in range(w)))

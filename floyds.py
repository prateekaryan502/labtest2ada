d=[[0,2,float('inf'),1,8],
   [6,0,3,2,float('inf')],
   [float('inf'),float('inf'),0,4,float('inf')],
   [float('inf'),float('inf'),2,0,3],
   [3,float('inf'),float('inf'),float('inf'),0]
  ]

v=len(d)
for k in range(len(d)):
    for i in range(v):
        for j in range(v):
            d[i][j]=min([d[i][j],d[i][k]+d[k][j]])

print(d)
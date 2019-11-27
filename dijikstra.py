cost=[[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
d=[float('inf')]*len(cost)
visited=[False for i in range(len(cost)+1)]
source=0
d[source]=0
for _ in range(len(d)):
    source=d.index(min([d[i] for i in range(len(d)) if visited[i]==False]))
    visited[source]=True
    for i in range(len(d)):
        if visited[i]==False and cost[source][i]!=0 and d[i]>d[source]+cost[source][i]:
            d[i]=d[source]+cost[source][i]


print("Verex    Distance from the source")
for i in range(len(d)):
    print(i,"       ",d[i])

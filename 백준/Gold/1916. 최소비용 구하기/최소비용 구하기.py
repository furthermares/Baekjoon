import sys
def input(): return sys.stdin.readline().rstrip()

import heapq
INF = int(1e9)

V = int(input())
E = int(input())
graph = [[] for i in range(V+1)]
distance = [INF]*(V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(start):
    q=[]

    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

start, end = map(int,input().split())

dijkstra(start)

print(distance[end])
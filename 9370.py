'''
첫 번째 줄에는 테스트 케이스의 T(1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스마다

첫 번째 줄에 3개의 정수 n, m, t (2 ≤ n ≤ 2 000, 1 ≤ m ≤ 50 000 and 1 ≤ t ≤ 100)가 주어진다. 각각 교차로, 도로, 목적지 후보의 개수이다.
두 번째 줄에 3개의 정수 s, g, h (1 ≤ s, g, h ≤ n)가 주어진다. s는 예술가들의 출발지이고, g, h는 문제 설명에 나와 있다. (g ≠ h)
그 다음 m개의 각 줄마다 3개의 정수 a, b, d (1 ≤ a < b ≤ n and 1 ≤ d ≤ 1 000)가 주어진다. a와 b 사이에 길이 d의 양방향 도로가 있다는 뜻이다.
그 다음 t개의 각 줄마다 정수 x가 주어지는데, t개의 목적지 후보들을 의미한다. 이 t개의 지점들은 서로 다른 위치이며 모두 s와 같지 않다.
교차로 사이에는 도로가 많아봐야 1개이다. m개의 줄 중에서 g와 h 사이의 도로를 나타낸 것이 존재한다. 또한 이 도로는 목적지 후보들 중 적어도 1개로 향하는 최단 경로의 일부이다.

'''

'''
교차로 = 노드
도로 = 간선
a와 b 사이에 길이 d의 양방향 도로 => 무방향 그래프이고, d가 가중치 graph[a].append((b,d)), graph[b].append((a,d)) 
'''

import sys, heapq

input = sys.stdin.readline
INF = (1e9)

def dijkstra(start, end):
    heap_arr = []
    distance = [INF]*(n+1)
    heapq.heappush(heap_arr, (0, start))
    distance[start] = 0

    while heap_arr:
        dist, now = heapq.heappop(heap_arr)
        if distance[now] < dist: continue
        for nxt in graph[now]:
            cost = dist + nxt[1]
            if cost < distance[nxt[0]]:
                distance[nxt[0]] = cost
                heapq.heappush(heap_arr, (cost, nxt[0]))
    return distance

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, m, t = map(int,input().split()) # 교차로, 도로, 목적지 후보
        s, g, h = map(int, input().split()) # 출발지, g,h는 지나간곳. 추후 이것을 기반으로 다 출발지 계산하고 이를 바탕으로 path 계산해야할것.
        graph = [[] for _ in range(n+1)]
        for i in range(m):
            a, b, d = map(int, input().split()) # a, b에 d 양방향 도로
            graph[a].append((b,d))
            graph[b].append((a,d))
        
        end_list = []
        for i in range(t):
            x = int(input())
            end_list.append(x)
        
        result = []

        for end_point in end_list:
            origin = dijkstra(s,end_point)
            g_dist = dijkstra(g,end_point)
            h_dist = dijkstra(h,end_point)
            '''
            여기서 g,h 는 무조건 들러야하는곳이니까 가능한 path는
            s -> g -> h -> end
            s -> h -> g -> end 
            뿐임
            '''
            
            g_path = origin[g] + g_dist[h] + h_dist[end_point]
            h_path = origin[h] + h_dist[g] + g_dist[end_point]

            min_path = min(g_path,h_path)
            if origin[end_point] == min_path and min_path != INF:
                min_path_val = min_path
                result.append(end_point)
        result.sort()
        print(*result)

        

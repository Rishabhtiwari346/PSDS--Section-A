N, K = map(int, input().split())
arr = list(map(int, input().split()))

current_sum = sum(arr[:K])
max_sum = current_sum

for i in range(K, N):
    current_sum += arr[i] - arr[i - K]
    if current_sum > max_sum:
        max_sum = current_sum

print("maximum sum:", max_sum) 
#ques2
s = input()
seen = set()
left = 0
max_length = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    length = right - left + 1
    if length > max_length:
        max_length = length

print("length of longest substring :", max_length) 
#ques3
import heapq

N, M, K = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

pq = [(0, 1, 0)]  # (cost, node, edges)
dist = {}

while pq:
    cost, node, edges = heapq.heappop(pq)
    
    if node == N:
        print("minimum path weight:", cost)
        break
        
    if edges == K:
        continue
        
    if (node, edges) in dist and dist[(node, edges)] < cost:
        continue
        
    dist[(node, edges)] = cost
    
    for next_node, weight in graph[node]:
        new_cost = cost + weight
        new_edges = edges + 1
        next_state = (next_node, new_edges)
        
        if next_state not in dist or new_cost < dist[next_state]:
            dist[next_state] = new_cost
            heapq.heappush(pq, (new_cost, next_node, new_edges))
else:
    print("minimum path weight: -1")
from collections import defaultdict
friend = defaultdict(list)
n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

def dfs(x, new_x, i):
    global result
    if result[i][x] != -1:
        return
    result[i][new_x] = result[i][x] + 1
    for f in friend[x]:
        dfs(new_x, f, i)

result = [[-1] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    result[i][0], result[i][i] = 0, 0
    dfs(0, i, i)

min_val = (1e9, n)
for i in range(1, n+1):
    min_val = min(min_val, (sum(result[i]), i))

print(result)
print(min_val[1])
    


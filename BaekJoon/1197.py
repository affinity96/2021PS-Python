def getpar(arr, n):
    if arr[n] == n : return n
    else : return getpar(arr, arr[n])

def union(arr, n_1, n_2):
    a = getpar(arr, n_1)
    b = getpar(arr, n_2)
    if a<b : arr[b] = a
    else : arr[a] = b

def find(arr, n_1, n_2):
    a = getpar(arr, n_1)
    b = getpar(arr, n_2)
    if a==b : return 1
    else : return 0



v, e = map(int, input().split(' '))

edges = []
parent = [i for i in range(v+1)]

for _ in range(e):
    l = [*map(int, input().split(' '))]
    edges.append(l)


edges.sort(key = lambda val:val[2])

mst = []

for e in edges:
    v, u, w = e

    if find(parent, v, u) == 0 :
        union(parent, v, u)
        mst.append(e)

print(sum([w for v, u, w in mst]))
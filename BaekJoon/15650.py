N, M = map(int, input().split())
arr = [ 0 for _ in range(100)]
nums = [ 0 for _ in range(N) ]
visited = [ False for _ in range(N+1)]

def dfs(cnt, cur):
    if cnt == M :
        print(' '.join(map(str, arr[0:M])))
        return
    else : 
        for m in range(cur, N+1):
            if not visited[m]:
                visited[m] = True
                arr[cnt] = m
                dfs(cnt+1, m)
                visited[m] = False

def main():
    
    dfs(0, 1)

if __name__ == '__main__' : main()
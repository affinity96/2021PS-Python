N, M = map(int, input().split())
arr = [0 for _ in range(100)] 
visited = [False for _ in range(N+1)]

def dfs(cnt) :
    if cnt == M : 
        print(' '.join(map(str, arr[0:M])))
        return
    else : 
        for i in range(1, N+1) :
            if not visited[i] : 
                visited[i] = True
                arr[cnt] = i
                dfs(cnt+1)
                visited[i] = False

def main():
    
    dfs(0)

if __name__ == '__main__' : main()
N, M = map(int, input().split())
arr = [0 for _ in range(M)]
def dfs(cnt, cur):
    if cnt == M : print(' '.join(map(str, arr[0:M])))
    else:
        for i in range(cur, N+1):
            arr[cnt] = i
            dfs(cnt+1, i)
def main(): dfs(0,1)

if __name__ == '__main__' : main()

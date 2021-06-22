N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = [0 for _ in range(M)]
visited = [False for _ in range(10001)]
def dfs(cnt) :
    if cnt == M : 
        print(' '.join(map(str, arr[0:M])))
        return
    else:
        for num in nums : 
            if not visited[num] : 
                visited[num] = True
                arr[cnt] = num
                dfs(cnt+1)
                visited[num] = False
def main() : dfs(0)

if __name__ == '__main__' : main()

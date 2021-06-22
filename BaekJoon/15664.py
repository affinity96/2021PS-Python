N, M = map(int, input().split())
nums = list(map(int, input().split()))
arr = [0 for _ in range(M)]
visited = [False for _ in range(N)]
nums.sort()

def dfs(cnt, cur):
    if cnt == M : print(' '.join(map(str, arr[0:M])))
    else:
        before = -1
        for i in range(cur, N) :
            if nums[i] != before and not visited[i]:
                arr[cnt] = nums[i]
                before = nums[i]
                
                visited[i] = True
                dfs(cnt+1, i)
                visited[i] = False
def main() : dfs(0, 0)

if __name__ == '__main__' : main()
    
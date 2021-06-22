N, M = map(int, input().split())
nums = list(map(int, input().split()))
visited = [False for _ in range(10001)]
arr = [0 for _ in range(M)]
nums.sort()
def dfs(cnt, cur) :
    if cnt == M : 
        print(' '.join(map(str, arr[0:M])))
        return
    else :
        for i in range(cur, N):
            if not visited[nums[i]]:
                visited[nums[i]] = True
                arr[cnt] = nums[i]
                dfs(cnt+1, i)
                visited[nums[i]] = False

def main() : dfs(0, 0)

if __name__ == '__main__' : main()
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = [ 0 for _ in range(M)]
def dfs(cnt, cur):
    if cnt == M : print(' '.join(map(str, arr[0:M])))
    else:
        for i in range(cur, N):
            arr[cnt] = nums[i]
            dfs(cnt+1, i)
def main() : dfs(0, 0)
if __name__ == '__main__' : main()
N, M = map(int, input().split())
nums = list(map(int, input().split()))
arr = [0 for _ in range(M)]
nums.sort()
def dfs(cnt):
    if cnt == M : print(' '.join(map(str, arr[0:M])))
    else : 
        for num in nums :
            arr[cnt] = num
            dfs(cnt+1)
def main() : dfs(0)
if __name__ == '__main__' : main()
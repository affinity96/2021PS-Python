N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
totalarr = []
arr = [0 for _ in range(M)]
visited = [False for _ in range(9)]

def dfs(cnt, cur):
    if cnt == M : totalarr.append(arr[0:M])
    else:
        for i in range(N):
            if not visited[i] :
                visited[i] = True
                arr[cnt] = nums[i]
                dfs(cnt+1, i)
                visited[i] = False

def main():
    dfs(0,0)
    global totalarr
    # print(totalarr)
    totalarr = list(set([tuple(elem) for elem in totalarr]))
    totalarr.sort()
    for elem in totalarr:
        print(' '.join(map(str, list(elem))))
    
if __name__ == '__main__' : main()
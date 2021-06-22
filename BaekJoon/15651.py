N, M = map(int, input().split())
arr = [0 for _ in range(M)]
def dfs(cnt):
    if cnt == M :
        print(" ".join(map(str, arr[0:M])))
        return 
    else:
        for i in range(1, N+1):
            arr[cnt] = i
            dfs(cnt+1)

def main():
    dfs(0)

if __name__ == "__main__" : main()
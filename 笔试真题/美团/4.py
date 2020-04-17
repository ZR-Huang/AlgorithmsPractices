'''
定义一个长度为N的序列的中位数为 f((N+1)/2), f()表示向下取整。
最少需要填充多少个数字，才能使得K成为该序列的中位数。

Input:
4, 2 (N，K)
2, 3, 3, 3

Output:
2
Explaination: (1,1,2,3,3,3) 填充2个1
'''
def solve(arr, k, n): # Pass 18%
    arr = sorted(arr)
    # k_index = arr.index(k)
    l, r = 0, n-1
    k_index = None
    while l < r:
        mid = (l+r) // 2
        if arr[mid] < k:
            l = mid + 1
        elif arr[mid] > k:
            r = mid - 1
        else:
            k_index = mid
            break
    k_index = l
    return (n+1)//2-k_index

if __name__ == "__main__":
    s = input()
    n, k = s.strip().split(' ')
    n, k = int(n), int(k)
    s = input()
    arr = list(map(int, s.strip().split(' ')))
    res = solve(arr, k, n)
    print(res)
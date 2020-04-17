'''
给定n个数，（n个数中可以重复）。
这n个数两两组成一个数对，自己和自己也组成一个数对。
数对的大小比较规则：先比较第一个元素，如果第一个元素相同，再比较第二个元素
在n个数所组成的所有n^2个数对中，输出第k小的数对。

Input:
3 4 (n, k)
3 1 2 (n个数字)

Output:
(2,1)
'''
def solve(arr, k, n): # Pass 45%
    arr = sorted(arr)
    i = (k-1) // n
    j = (k-1) % n
    return "({},{})".format(arr[i], arr[j])



if __name__ == "__main__":
    s = input()
    n, k = s.strip().split(' ')
    n, k = int(n), int(k)
    s = input()
    arr = list(map(int, s.strip().split(' ')))
    res = solve(arr, k, n)
    print(res)
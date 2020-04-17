'''
有n个人和m科考试的成绩，给每科成绩最高的人发单科优秀奖。
则获奖的人数是多少？
所求的是人数，而不是人次，其中如果一个人有两科成绩均是最高，则人数依然为1.

输入：
4 5 (n, m)
12 40 50 70 90 (一个人的m科成绩)
60 20 40 60 87
45 78 92 83 10
38 47 92 45 76

Output:
4
'''
def solve(grades, n, m): # AC
    ans = []
    for j in range(m):
        max_ = 0
        for i in range(n):
            if grades[i][j] > max_:
                max_ = grades[i][j]
        max_people = []
        for i in range(n):
            if grades[i][j] == max_:
                max_people.append(i)
        ans += max_people
    return len(set(ans))

if __name__=="__main__":
    s = input()
    n, m = s.strip().split(" ")
    n, m = int(n), int(m)
    grades = []
    for _ in range(n):
        s = input()
        s = list(map(int, s.strip().split(" ")))
        grades.append(s)
    res = solve(grades, n, m)
    print(res)
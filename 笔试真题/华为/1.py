M, N = input().strip().split()
M = 10
N = 10
ans = []
if M<10 or N<10 or M>1000 or N>1000:
    print(ans)

top, bottom, left, right = 0, M-1, 0, N-1
count = 0
while True:
    i, j = top, left
    while left<=right and j<=right:
        count+=1
        if count%10 == 7 and ((count//10)%10) % 2==1:
            ans.append([i, j])
        j+=1
    top+=1
    i, j = top, right
    while top<=bottom and i<=bottom:
        count+=1
        if count%10 == 7 and ((count//10)%10) % 2==1:
            ans.append([i, j])
        i+=1
    right-=1
    i, j = bottom, right
    while left<=right and j>=left:
        count+=1
        if count%10 == 7 and ((count//10)%10) % 2==1:
            ans.append([i, j])
        j-=1
    bottom-=1
    i, j = bottom, left
    while top<=bottom and i>=top:
        count+=1
        if count%10 == 7 and ((count//10)%10) % 2==1:
            ans.append([i, j])
        i-=1
    left+=1
    if left > right or top > bottom: break;

output = ['[{},{}]'.format(pair[0], pair[1]) for pair in ans]
output = ','.join(output)
output = '[' + output + ']'
print(output)
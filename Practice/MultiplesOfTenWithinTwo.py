def near_ten(num):
    return (num+2) % 10 <= 4
numb = int(input())
ans = near_ten(numb)
print(ans)

f = open('input.txt')
s = f.read()
count_R = 0
count_L = 0
left = 0
right = 0
kmax = 0

while right < len(s):
    if count_R > 44 or count_L > 22:
        if s[left] == 'R':
            count_R -= 1
        if s[left] == 'L':
            count_L -= 1
        left += 1
    else:
        if s[right] == 'R':
            count_R += 1
        if s[right] == 'L':
            count_L += 1
        right += 1
        if count_R == 44 and count_L <= 26:
            kmax = max(kmax, right - left)

print(kmax)
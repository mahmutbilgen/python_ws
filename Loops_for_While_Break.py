'''
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)


output :
1
2
3
4
5
'''
'''
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

output:
1
2
Found!
'''
'''
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

output:
1
2
Found!
4
5
'''

'''
nums = [1, 2, 3, 4]

for num in nums:
    for letter in 'abc':
        print(num, letter)

output:
1 a
1 b
1 c
2 a
2 b
2 c
3 a
3 b
3 c
4 a
4 b
4 c
'''

'''
for i in range(1, 11):
    print(i)

Output:
1
2
3
4
5
6
7
8
9
10
'''
'''
x = 0

while x < 10:
    print(x)
    x += 1

output:
0
1
2
3
4
5
6
7
8
9

'''
'''
x = 0

while True:
    if x == 5:
        break
    print(x)
    x += 1

Output:
0
1
2
3
4
'''

#Keep It Sorted!
#You have given some numbers, your task is to insert them in such a way such that list is still in ascending order.
#Display all the integers by seperating them with space.

#Solution:

import bisect
l = []
for _ in range(int(input())):
  bisect.insort(l, int(input()))
print(*l)

#Strange Cutting
#You have been given a rod N meters long. First you will cut the rod by 1 metre, cut it again by 1 metre, then cut it by sum of previous two cut rods lengths until the sum of
#previous two cut rods length is more than the length of uncut rod part.
#Your task is to find the length of uncut rod part left with you.

#Solution:

N, a, b = int(input()), 1, 1
while b <= N:
  a, b = b, a+b
  N -= b
print(N)

#Sabse Zyada Aavriti!
#Rakshit has been given a list and asked for the most frequent item in the list and its frequency. Help Rakshit to find out.
#If all items are of equal frequency or the list is empty, print -1.

#Solution:

from collections import Counter
l = input().split()
if not l or len(l)==len(set(l)):
  print(-1)
else:
  print(*Counter(l).most_common(1)[0])

#Arrange the dice!
#You know that sum of two opposite sides of a dice is 7. You have given a dice with shuffled sides (sum of opposite sides is not 7). You can also interchange the number faces which
#are opposite of each other. The arrangment of faces are like this with indices:
#   0
# 1 2 3
#   4
#   5
#Your task is to find the minimum number of flips to arrange the dice into real dice.

#Solutions:

a, b, c = int(input()), int(input()), int(input())
d, e, f = int(input()), int(input()), int(input())


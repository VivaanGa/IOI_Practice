#Note: All the solutions are given in Python Language

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
#If all items are of equal frequency or the list is empty, print -1. (You will be given a list with item seperated by space)

#Solution:

from collections import Counter
l = input().split()
if not l or len(l)%len(set(l))==0:
  print(-1)
else:
  print(*Counter(l).most_common(1)[0])

#Pairings
#You will be given N lists with item seperated by space. Your task is to zip the lists and display zipped items by seperating them with space.

#Solution:

l = []
for _ in range(int(input())):
  l.append(input().split())
for z in zip(*l):
  print(*z)

#Secret Message: Part 1
#You will be given a list which contains integer each = i seperated by space such that 0 < i < 27 . Your task is to find the alphabet at position i in uppercase.

#Solution:

l = list(map(int, input().split()))
f = lambda t: chr(t+64)
print(*map(f, l))

#Secret Message: Part 2
#You will be given a list which contains integer each = i seperated by space such that 0 < i < 27 . Your task is to find the alphabet at position i in lowercase.

#Solution:

l = list(map(int, input().split()))
f = lambda t: chr(t+96)
print(*map(f, l))

#Secret Message: Part 3
#You will be given a list which contains integer each = i seperated by space such that 0 < i < 27 . If i is even print the letter in uppercase else in lowercase.

#Solution:

l = list(map(int, input().split()))
for i in range(len(l)):
  l[i] = chr(l[i]+64) if l[i]%2==0 else chr(l[i]+96)
print(*l)

#Secret Message: Part 4
#You will be given N messages which each contains integers. Convert them into lower alphabets and check if how many messages contains at least one palindrome such that its length > 1.
#A palindrome is a word that equal its reverse.

#Solution:

c, m = 0, []
for _ in range(int(input())):
  f = False
  m = list(map(int, input().split()))
  m = list(map(lambda t: chr(t+96), m))
  for i in range(len(m)):
    for j in range(i+1, len(m)+1):
      if m[i:j] == m[i:j][::-1] and len(m[i:j]) > 1:
        c, f = c+1, True
        break
    if f == True:
      break
print(c)

#Heapogiri: Part 1
#You are given a list of integers. Your task is to convert it into a min heap and print it.

#Solution:

import heapq
l = list(map(int, input().split()))
heapq.heapify(l)
print(*l)

#Heapogiri: Part 2
#You are given a list of integers. Your task is to convert it into a max heap and print it.

#Solution:

import heapq
f = lambda t: -int(t)
l = list(map(f, input().split()))
heapq.heapify(l)
print(*map(abs, l))

#LIS Length: Part 1
#You task is to find the length of the longest increasing subsequence in any integer list.

#Solution:

import bisect
l = list(map(int, input().split()))
s = []
for i in range(len(l)):
  if not s or s[-1] <= l[i]:
    s.append(l[i])
  else:
    s[bisect.bisect(s, l[i])] = l[i]
print(len(s))

#Longest Decreasing Subsequence (LIS Length: Part 2)
#You task is to find the length of the longest decreasing subsequence in any integer list.

#Solution:

import bisect
l = list(map(int, input().split()))
s = []
for i in range(len(l)):
  if not s or s[-1] >= l[i]:
    s.append(l[i])
  else:
    s[bisect.bisect_left(s, l[i])] = l[i]
print(len(s))

#Is it a min-heap or max-heap? (Heapogiri: Part 3)
#Your task is to find out if B is a min-heap or max-heap of A.

#Solution:

import heapq
f = lambda t: -int(t)
l = list(map(int, input().split()))
h = list(map(int, input().split()))
x = l
heapq.heapify(x)
y = list(map(f, l))
heapq.heapify(y)
y = list(map(f, y))
print(h in {x, y})

#Keep it a min-heap! (Heapogiri: Part 4)
#You have given some numbers, your task is to insert or pop  them in such a way such that list is still a min heap.
#Display all the integers by seperating them with space.
#Commands: 1 for popping, 2 for inserting.

#Solution:

import heapq
l = []
for _ in range(int(input())):
  c, n = map(int, input().split())
  if c == 2 and l:
    heapq.heappush(l, n)
  elif c == 1:
    heapq.heappop(l)
print(*l)

#Print the permutations
#You have given some digits. Find the permutations of them.

#Solution:

import itertools
l = list(map(int, input().split()))
p = itertools.permutations(l, len(l))
for a in p:
  print(*a)

#Integer Square Root: Part 1
#Your task is to find the integer square root of N any number.

#Solution:

import math
print(math.isqrt(int(input()))

#Integer Square Root: Part 2
#Your task is to find how many numbers are there in L such that the integer square root of the numbers are strictly greater than K.

#Solution:

import math
l = list(map(int, input().split()))
k = int(input())
z = list(filter(lambda t: math.isqrt(t) > k, l))
print(len(z))
      
#Integer Square Root: Part 3
#Your task is to find the maximum number are there in L such that the integer square root of the numbers are strictly greater than K.

#Solution:

import math
l = list(map(int, input().split()))
k = int(input())
z = list(filter(lambda t: math.isqrt(t) > k, l))
try:
  print(max(z))
except ValueError:
  print(0)

#What is x(n)?
#x(n) = x(n-1) * 2 and x(1) = 1. What is x(n)?

#Solution:

n = int(input())
dp = [0] * (n+1)
dp[0] = 1
for i in range(n-1):
  dp[i+1] = dp[i]*2
print(dp[n])

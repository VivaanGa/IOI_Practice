#Keep It Sorted!
#You have given some numbers, your task is to insert them in such a way such that list is still in ascending order
#But you cannot use: l.append(n); l.sort()
#Display all the integers by seperating them with space

#Solution

import bisect #import
l = [] #define
for _ in range(int(input())): #loop
  bisect.insort(l, int(input())) #insert
print(*l) #display


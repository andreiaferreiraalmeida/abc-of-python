
#information comments
# List[start:stop:step] (start = begin of the list, stop the end of the list, step nbr of "elements u will jump")

## exercises
##visualize Positive indexing 
#    0      1       2       3         4        5      6        7      8       9      10
l_ex1=[1,     2,       3,      4,        4,       5,     6,       7,     8,      9,     10]
#   -11    -10      -9      -8        -7      -6      -5      -4      -3      -2     -1
##visualize Negative indexing

##first do some random list samples
##before u print, comment above the print what do u expect to be printed. 
print('print 1, general slice')
print(l_ex1[2:3])
#3

print('print 2, general slice')
print(l_ex1[0:4])
#1,     2,       3,      4
#
print('print 3, general slice')
print(l_ex1[4:6])
#4,5

# Adding steps
#positive steps

#from left to right
print(l_ex1[0:8:3])
#1,4,6  

##negative steps
#from left to right
print(l_ex1[-1:-10:-5])
#10,5

#mixed indexing and steps
print(l_ex1[2:-2:2])
# 3,4,6,8

##start
print(l_ex1[2:])
#3,      4,        4,       5,     6,       7,     8,      9,     10


##stop
print(l_ex1[:4])
#1,     2,       3,      4

##reverse the list
print(l_ex1[::-1])

##delete entry
del(l_ex1[0:1])
print(l_ex1)
#

##copy entire list
L2 = l_ex1[:]
print(L2)
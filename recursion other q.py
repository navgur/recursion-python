# import sys
# print(sys.setrecursionlimit(4000))
# print(sys.getrecursionlimit())
# # i=0
# # def myfun():
# #     global i
# #     i=i+1
# #     print("rani",i)
# #     myfun()
# # myfun()
list=[1,2,-3,4,5,-10]
i=0
while i<len(list):
    if list[i]<0:
        list[i]=0
    i=i+1
print(list)
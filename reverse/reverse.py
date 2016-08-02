# Reverse a list

def reverse(alist):
    begin = 0
    end = len(alist) - 1
    tmp = False
    while begin < end:
        tmp = alist[begin]
        alist[begin] = alist[end]
        alist[end] = tmp
        begin += 1
        end -= 1
    return alist

list0 = [i for i in range(50)]
print(reverse(list0))
print(reverse(list0))

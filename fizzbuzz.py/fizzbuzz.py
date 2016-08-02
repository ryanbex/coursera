
def fizzbuzz(i):
    astring = ''
    if i%3 == 0:
        astring += 'Fizz'
    if i%5 == 0:
        astring += 'Buzz'
    if astring:
        return astring
    return i

def client(alist=[]):
    return [fizzbuzz(i) for i in alist]

list0 = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,15,16,11,17,43,324,255,513253,4,51325,34234,32344,123,7,675,7,9,6797,5675,54,7,76,86]
list1 = [i for i in range(16)]
print(client(list0))
print(client(list1))



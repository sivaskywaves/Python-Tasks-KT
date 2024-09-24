#Problem 1
lst=["1","4","3","7","5","2","9","8"]
list1=[int(i) for i in lst] # for converting string data into integers
print(list1)
def sqr(x):
    return x*x
list2=map(sqr,list1)
print(list(list2))



#Problem 2
s="python learning is very easy"
#case 1:
def reverse (x):
    print (x[::-1])
print(reverse(s))

#case 2:
words=s.split(" ")
words=words[-1::-1]
print(words)

#
# def add(*args):
#     return sum(args)
#
# a=[1,2,3]
# b=[1,2,3]
#
#
# # print(add(1,2,4))
# # print(a is b)
#
# def mul(*args):
#     print(args)
#     sum=1
#     for n in args:
#         sum=sum*n
#     return  sum
#
#
# a=mul(1,2,3)
# print(a)

# obj={
#     "name":"shashi",
#     "age":20,
#     "address":"Haraiya"
# }
#
# # i=0;
# a=obj.values()
# # print(a)
# # for key, value in obj.items():
# #     print(obj.get(key))
#
# list=[1,2,3, 4,5]
#
# for i in list:
#     print(i)
#
#
# print(list[2::-1])


from collections import Counter

items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = Counter(items)

print(frequency)
# Output: {'apple': 3, 'banana': 2, 'orange': 1}

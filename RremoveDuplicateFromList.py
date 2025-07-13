def removeDuplicate(my_list):
   a= set(my_list)

   print(list(a))
   return  list(a)


ans=  removeDuplicate([1,2,2,3,3,4,5,6])
print(ans)


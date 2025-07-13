def reverseTheWordOfString(sentence):
    arr=sentence.split(" ")
    print(arr)
    data=[]
    for item  in arr:
        revWord=item[::-1]
        data.append(revWord+" ")

    s=''

    for item in data:
        s=s+item

    return  s

def reverseTheString(sentence):
    a=sentence.split(" ")
    arr=(a[::-1])
    s=""
    for i in arr:
        s=s+i+" "
    return  s


# a=reverseTheWordOfString("Shashi is a Goodman")
# print(a)

a=reverseTheString("shashi is pm of india")
print(a)
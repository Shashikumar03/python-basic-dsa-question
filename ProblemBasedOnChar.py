
def count_vowel():
    s='shashi'
    vowel=['a','e','i', 'o','u']
    count =0
    for c in s:
        # print(c)
        if c in vowel:
            count= count+1

    print(count)

def remove_duplicate_from_string(string ):
    result1= ''
    for c in string:
        if c.lower() not in result1.lower():
            result1=result1+c

    print(result1)




# count_vowel()

remove_duplicate_from_string("Shashi")
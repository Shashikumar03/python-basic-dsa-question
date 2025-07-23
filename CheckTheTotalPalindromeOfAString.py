from selenium.webdriver.common.devtools.v136.debugger import step_out


def check_palindrome2(s):
    a=s.replace('.', '')

    a=a.split(" ")
    print(a)
    list=[]
    for i in a:
       print(i)
       if i==i[::-1]:
           list.append(i)

    return list



a=check_palindrome2("Shashi is a good man. i know malayalam.")
print(a)

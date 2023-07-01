''' This is the simple program for checking the palindrom number '''

home='Palindrome Number'
print(home.center(50))
# # palindrome number example - 4334, 5665, 232
#defining func for checking if palindrome
def palindrom_check(chk_num,num):
  
  if chk_num==chk_num[::-1]:
    print('YES',num,'is palindrome')
  else:
    print('NO',num,'is not palindrome')

#__main__
num=input('Enter your number:')
chk_num=list(num)
palindrom_check(chk_num,num)

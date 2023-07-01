''' This is the simple program for calculating the largest number in the list '''

home='Largest Number in the list'
print(home.center(50))

#defining func for making the list
def mk_list(ls):
  len_list=int(input('Enter how many numbers you want to add in list:'))
  for i in range(len_list):
    num=int(input(f'Enter the number {i+1}:'))
    ls.append(num)
  return ls

#defining func for getting largest number from list
def largest_num(list):
  sorted_list=sorted(list,reverse=True)
  n=eval(input('Enter your preferred :'))

  if n==1:
    print(f'The {n}st largest number in the {list} is',sorted_list[n-1])
  if n==2:
    print(f'The {n}nd largest number in the {list} is',sorted_list[n-1])
  if n==3:
    print(f'The {n}rd largest number in the {list} is',sorted_list[n-1])
  else:
    print(f'The {n}th largest number in the {list} is',sorted_list[n-1])
  

#__main__
ls=[]
list=mk_list(ls)
largest_num(list)

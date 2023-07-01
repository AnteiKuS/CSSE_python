''' Simple program for getting prime numbers between 0 to 999 '''

home='Prime Numbers between 0 to 999'
print(home.center(50))

#function for prime numbers
def primetill999():
  for num in range(0,1000):
    condition=True
    if num == 0 or num==1 :
      condition=False
    else:
      for i in range(2,num):
        if num%i==0:
          condition=False
    if condition:
      print(num)

#__main__
primetill999()

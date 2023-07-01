''' This is the simple program for calculating the Body Mass Index(BMI) of a person '''

home='BMI calculator'
print(home.center(50))

#defining function for calculating bmi
def bmi_calc(h,w):
  bmi= weight/ height**2
  return bmi

#__main__
height= float(input('Enter your height in meters(m):'))
weight= float(input('Enter your weight in kilograms(kg):'))
ans=bmi_calc(height,weight)
print("Your BMI:\t",ans)

#checking health
if ans<18.5:
  print('Considered Underweight')
elif 18.5<ans<24.9:
  print("Considered Healthy weight")
elif 25<ans<29.9:
  print('Considered Overweight')
elif ans>30:
  print("Considered Obese")
   


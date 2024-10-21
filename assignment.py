import math
diameter = float(input("Enter the diameter of the circle: "))
if diameter <= 0:
  print("Reenter diameter, number must be grater than 0")
else:
  def calc(d):
      r = d / 2 
      area = math.pi * r ** 2
      cirumference = 2 * math.pi * r  
      print (area) 
      print (cirumference)
calc (diameter)

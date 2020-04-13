yes = 1
no = 0

def initialize():
  return 1

def isHome():
  g = input("Is the fin in home position?: ")
  print(g)
  if(g == 'yes'):
    isHome = yes
  elif(g == 'no'):
    isHome = no
  return isHome

import timer

timeToStartPosition = 2000  #in Msec

def initialize():
  return 1

def turnCCW():
  #output PWM
  print('turning motor counter clockwise.')
  timer.delay(50)
  return 1

def turnCW():
  #output PWM
  print('turn motor clockwise.')
  timer.delay(50)
  return 1

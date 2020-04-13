import stabilizeSwitch
import gyroSensor
import homePositionSwitch
import motor
import timer
import controller

def goHome():
  while not((homePositionSwitch.isHome())):
    motor.turnCCW()
  
def goToStartStabilizePosition():
  print('go to stabilize position.')
  motor.turnCW()
  timer.delay(motor.timeToStartPosition)

def stabilize():
  controller.Control(gyroSensor.rotation())

def main():
  stabilizeSwitch.initialize()
  gyroSensor.initialize()
  homePositionSwitch.initialize()
  motor.initialize()

  timer.delay(500);

  stabilizeState = stabilizeSwitch.position()
  
  while 1:
    while stabilizeSwitch.position() == stabilizeState:
      pass
    
    stabilizeState = stabilizeSwitch.position()
    goHome()

    if stabilizeState == stabilizeSwitch.on:
      goToStartStabilizePosition()
      stabilize()

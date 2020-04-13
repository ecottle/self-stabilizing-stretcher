import gyroSensor

def Control(rotation):
  if(not(rotation == 0)):
    print('System unstable, controlling.')
    rotation = gyroSensor.rotation()
  else:
    return 1

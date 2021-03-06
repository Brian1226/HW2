import time

def calculate_time(func):
  def wrapper():
    func()
  return wrapper

@calculate_time
def time_sleep():
  time.sleep()



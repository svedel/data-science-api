import time

def create_task(task_type):
  """Simple mock task creation function, mimicking a long-running server-side process."""
  time.sleep(int(task_type) * 10)
  return True

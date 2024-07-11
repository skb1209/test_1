import sys

def test():
  print("hello")
  test()

cnt = 0
while True:
  test()
  cnt += 1
  if cnt == 4:
    break

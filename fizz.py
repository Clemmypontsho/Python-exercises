def fizz_buzz(max):
  nums = []

  i = 0
  while (i < max):
    if (i % 4 == 0 or i % 6 == 0) and not(i % 4 == 0 and i % 6 == 0):
      nums << i
      i += 1
  

  return nums


print (fizz_buzz(20)) 


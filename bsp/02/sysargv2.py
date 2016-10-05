import sys
sum = 0
for element in sys.argv[1:]:
  sum += int(element)
print(sum)

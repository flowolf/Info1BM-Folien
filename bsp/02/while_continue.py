a = 1
while a < 10:
  a += 1
  if not a % 2:
    print(a)
    continue
  a += 2
print(a)

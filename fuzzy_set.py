# Fuzzy set operations


#define fuzzy set close to 10

f = {5:0.0,
     6:0.2,
     7:0.4,
     8:0.6,
     9:0.8,
     10:1.0,
     11:0.8,
     12:0.6,
     13:0.4,
     14:0.2,
     15:0.0}
print(f)

#define 3 fuzzy sets
f3 = dict()
f1 = {1.0:1.0, 1.5: 0.75, 2.0: 0.3, 2.5: 0.15, 3.0:0.0}
f2 = {1.0: 1.0, 1.5: 0.6, 2.0:0.2, 2.5:0.1, 3.0: 0.0}

print(f"Fuzzy set F1: {f1}")
print(f"Fuzzy set f2: {f2}")

#equality
for k1, k2 in zip(f1, f2):
  if f1[k1] != f2[k2]:
    print("Not equal")
    break
else:
  print("equal")


#union

f3 = dict()
for key1, key2 in zip(f1, f2):
    f3[key1] = max(f1[key1], f2[key2])
print(f3)

#intersection
f3 = dict()
for key1, key2 in zip(f1, f2):
    f3[key1] = min(f1[key1], f2[key2])
print(f3)


#Complement  fuzzy set
fz = {1.0: 1.0, 1.5: 0.6, 2.0:0.2, 2.5:0.1, 3.0: 0.0}

f3 = dict()
for k, v in fz.items():
    f3[k] = 1 - v
print(f3)


#Difference fuzzy set
f3 = dict()
for k1, k2 in zip(f1,f2):
  f3[k1] = min(f1[k1], 1-f2[k2])
print(f3)

#algebraic Multiplication
f3 = dict()
for k1, k2 in zip(f1,f2):
  f3[k1] = f1[k1] * f2[k2]

#multiplication fuzzy with crisp num
f3 = dict()
crisp_num = 0.6
for k1 in f2.keys():
  f3[k1] = f2[k1] * crisp_num

print(f2)
print(f3)

#power of fuzzy set
f3 = dict()
pow = 2
for k, v in f2.items():
  f3[k] = round(v ** pow, 2)
print(f3)

#Algebraic sum fuzzy set
f3 = dict()
for key1, key2 in zip(f1, f2):
  f3[key1] = (f1[key1] + f2[key2]) - (f1[key1] * f2[key2])
  f3[key1] = round(f3[key1], 2)
print(f3)


f3 = dict()
#shorter if keys are the same
for key in f1:
  f3[key] = (f1[key] + f2[key]) - (f1[key] * f2[key])
print(f3)

#bounded sum
f3 = dict()
for key1, key2 in zip(f1, f2):
  f3[key1] = min(1, (f1[key1] + f2[key2]))
print(f3)


#bounded product
f3 = dict()
for key1, key2 in zip(f1, f2):
  f3[key1] = min(1, (f1[key1] * f2[key2]))
print(f3)

#Cartesian Product
f3 = dict()
f1 = {1.0:1.0, 1.5: 0.75, 2.0: 0.3, 2.5: 0.15}
f2 = {1.0: 1.0, 1.5: 0.6, 2.0:0.19, 2.5:0.8}

for key_A in f1:
  f3[key_A] = f1[key_A]
  for val in f2.values():
    f3[key_A] = min(f3[key_A], val)
print(f1)
print(f2)
print(f3)

#end of assignment
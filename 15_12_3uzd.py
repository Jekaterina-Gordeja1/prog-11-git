print('Ievadi skaitli tikai no 1 līdz 10 !')
a = int(input('Ievadi pirmo skaitli!'))
b = int(input('Ievadi otro skaitli!'))
c = int(input('Ievadi trešo skaitli!'))

smallest = 0

if a < b and a < c :
  smallest = a 
if b < a and b < c :
  smallest = b
if c < a and c < b :
  smallest = c

  print(smallest, " Tas is mazakais sdkaitlis!")

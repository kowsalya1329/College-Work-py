import random
listing = []
for i in range(0,234):
  a = random.randint(0,1)
  if a == 0:
    listing.append("a")
  b = random.randint(1,2)
  if b == 1:
    listing.append("b")
  c = random.randint(2,3)
  if c == 2:
    listing.append("c")
  d = random.randint(0,3)
  if d == 3:
    listing.append("d") 
  else:
    print("Constitution election no one")
print("Constituion election:", listing)
count = 0
a_count = 0
b_count = 0
c_count = 0
d_count = 0
for i in listing:
  count+= 1
  if i=="a":
    a_count+=1
  if i=="b":
    b_count+=1
  if i=="c":
    c_count+=1
  if i=="d":
    d_count+=1
  else:
    print("Election results total count:", count)
print("a count is", a_count, "b count is", b_count, "c count is", c_count, "d count is", d_count)

winner = 0
a_winner=0
b_winner=0
c_winner=0
d_winner=0
for i in count:
  winner <=1
  if a_count > b_count:
    print("a is winner")
  else:
    print("b is winner") 
  if a_count > c_count:
    print("a is winner")
  else:
    print("c is winner") 
  if a_count > d_count:
    print("a is winner")
  else:
    print("d is winner") 
  if b_count > c_count:
    print("b is winner")
  else:
    print("c is winner")
  if b_count > d_count:
    print("b is winner")
  else:
    print("d is winner")
  if c_count > d_count:
    print("c is winner")
  else:
    print("d is winner")
print("The winner of this election is:", winner)
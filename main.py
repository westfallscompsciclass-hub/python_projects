character = input("What is your characters name?")
print "Our journey begins with " + character

print character + " walks through the dark woods. They see two paths. Which path will they take?"
path = input("Type 'left' or 'right'")

if path == "left":
  print character + " takes the left path"
  print character + " sees a serpant. Do they fight it?"

  fight = input("Type 'yes' or 'no'")
  
  if fight == "yes":
    print character + " chose to fight the serpant"
    
    weapon = input("Do you use the 'sword' or 'mace'")
    if weapon == "sword":
      print "You hack at the serpant with a sword"
    elif weapon == "mace":
      print "the mace breaks and the serpant eats you"
  
  elif fight == "no":
    print character + " chose not to fight the serpant"

elif path == "right":
  print character + " takes the right path"
  
  print character + " finds themselves at the door of a hobbit hut"
  enter = input("Do they enter type 'yes' or 'no")
  if enter == "yes":
    print "Bilbo bagins eats you"
  elif enter == "no":
    print "Our journey continues"
      

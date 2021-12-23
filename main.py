
# Name : Shubham Gorakh Kashmire
# Course: Software Engineering - Semester 1
# Project: Advance Programming - Text Adventure Gamer.
# Date: 18.12.2021
# Theme: Horror

import room
import item
import character

print ("""\nYou are trapped in a haunted villa, your current location is Kitchen. \nNavigate yourself and kill all demons so that you can live in the villa.
\n••••KEYWORDS••••
Navigation --> north, south, west and east
Pick up object and put inside bagpack --> take
Hug enemy/friend --> hug
Talk with enemy/friend --> talk
Fight with enemy/friend --> fight
Steal objects --> steal
••••••••••••••••
Text based navigation map 

               +-----------+
               | Kitchen   |
               |(u r here) |
               +-----------+
+-----------+  +-----------+   
| Living rm |  | Bedroom   |
|           |  |           |
+-----------+  +-----------+
••••••••••••••••
""")
kitchen = room.Room("Kitchen")
kitchen.set_description("Dark, dirty room with spider web all over and flies.")

living_room = room.Room("Living Room")
living_room.set_description("Creepy room with dust, broken paintings and torn curtains.")

bedroom = room.Room("Bedroom")
bedroom.set_description("Bedroom with broken bed and blood on the floor.")

kitchen.link_room(living_room, "south")
living_room.link_room(kitchen, "north")
living_room.link_room(bedroom, "west")
bedroom.link_room(living_room, "east")

donna = character.Enemy("Donna", "A smelly zombie with broken hands and scary head")
donna.set_conversation("What's up world!! How is it going?? I am hear to eat your brain")
donna.set_weakness("cheese")

angle = character.Friend("Angle", "Angle with white wings")
angle.set_conversation("Hello!!! I am your new friend, here to help")
angle.set_weakness("sword")

mosquitoe = character.Enemy("Big Mosquitoe", "A mosquitoe with big sting")
mosquitoe.set_conversation("I am here to eat all your blood.")
mosquitoe.set_weakness("book")
bedroom.set_character(mosquitoe)

book = item.Item("book")
book.set_description("Book with title 'Nineteen Eighty Hour'")
living_room.set_item(book)

cheese = item.Item("cheese")
cheese.set_description("Stinky chesse with fungus")
bedroom.set_item(cheese)

bedroom.set_character(angle)

living_room.set_character(donna)

current_room = kitchen

backpack = []

dead = False

while dead == False:
  print("\n")         
  current_room.get_details()

  inhabitant = current_room.get_character()
  if inhabitant is not None:
    inhabitant.describe()
  
  item = current_room.get_item()
  if item is not None:
    item.describe()
      
  command = input("Choose your action? ")    
  if command in ["north", "south", "east", "west"]:
    current_room = current_room.move(command)
    
  elif command == "talk":
    if inhabitant is not None:
      inhabitant.talk()
      
  elif command == "fight":
    if inhabitant is not None:

      print("Choose object to fight with?")
      # choose what you want to fight with
      fight_with = input()
      item_found = False
      for i in backpack:
        if(i.name == fight_with) :
          item_found = True
      
      if (item_found == True):
        if inhabitant.fight(fight_with) == True:
          print("Congrats! You won fight")
          current_room.character = None
          if inhabitant.get_defeated() == 2:
            print("Hurrah, you have killed enemy")
            dead = True
          else:
            print("Oops! Enemy killed you")
            print("GAME OVER")
            dead = True
      else:
        print("You dont have a " + fight_with)
    else:
      print("There's no one here to fight with")
        
  elif command == "hug":
    if inhabitant == None:
      print("There is no one to give a hug")
    else:
      if isinstance(inhabitant,character.Enemy):
        print("I would never hug an enemy")
      else:
        inhabitant.hug()
        
  elif command == "steal":
    if inhabitant == None:
      print("There's no one you can steal from")
    elif isinstance(inhabitant,character.Friend):
      print("Do you really want to steal from your friend?")
    else:
      print("You need to fight to steal object. Choose an object to fight with:")
      fight_with = input()
      if inhabitant.fight(fight_with) == True:
        print("You stole an item")
      else:
        print("Oops! You lost the fight")
        print("GAME OVER")
        dead = True
        
  elif command == "take":
    if current_room.get_item() != None:
      print("You have successfully put the " + item.get_name() + " in your backpack")
      backpack.append(current_room.get_item())
      current_room.set_item(None)
    else:
      print("There's nothing here to take")
      
  else:
    print("I don't know how to " + command)
   
#End of file
  
  
      
      
        
  
  
        




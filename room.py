# Class Room
class Room:
  def __init__(self, room_name):
    self.name = room_name
    self.description = None 
    self.linked_rooms = {}
    self.character = None
    self.item =  None
    
  # Getters and setters for characters - enemy, friend, etc.
  def set_character(self,character):
    self.character = character
    
  def get_character(self):
    return self.character

  # Getters and setters for item
  def set_item(self,item_name):
    self.item = item_name

  def get_item(self):
    return self.item

  # Getters and setters for item description 
  def set_description(self, room_description):
    self.description = room_description
  
  def get_description(self):
    return self.description
  
  # Getters and setters for room
  def set_name(self, room_name):
    self.name = room_name
  
  def get_name(self):
    return self.name
  
  def describe(self):
    print( self.description )
  
  # Linking room to directions
  def link_room(self, room_to_link, direction):
    self.linked_rooms[direction] = room_to_link
  
  # Game start details
  def get_details(self):
    print(self.name)
    print("•••••••••••••••")
    print(self.description)
    for direction in self.linked_rooms:
        room = self.linked_rooms[direction]
        print( "The " + room.get_name() + " is " + direction)
  
  #Navigate
  def move(self, direction):
    if direction in self.linked_rooms:
        return self.linked_rooms[direction]
    else:
        print("Opps! You smashed your head against wall, direction you choose is invalid")
        return self
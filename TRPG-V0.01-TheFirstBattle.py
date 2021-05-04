#This Software is a Text Based RPG called TRPG.
# This game will simulate an rpg game in a text variation
# This has been an ARCSec Software deveopled by Cesar Julian Quezada on April 23 2021 on Version 0.01
import random
print ("Welcome to TRPG\n Where text fanatasies come to like")
s = input("Type start to begin your adventure ")
#Defines the Charaters charateristics
class Protagonist:
    def __init__(self, name, HP, mana):
      self.name = name
      self.HP = HP
      self.mana = mana

class Monster:
    def __init__(self, name, HP):
     self.name = name
     self.HP = HP
#Defines the Protagonist base skill level and ask who is the progatonist
Protagonist.HP = 20
Protagonist.mana = 10
Protagonist.name = input("Who are you? ")
print("Welcome " + Protagonist.name)
print(Protagonist.name + " you must save the world")
#Defines the Monster class and base skill level
Monster.name = "Goblin"
Monster.HP = 20
r = random.randint(1, 6)
print("A " + Monster.name + " has appeared")
#initiates the battle sequence
while Monster.HP != 0 or Protagonist.HP != 0:
  #Protagonist must choose whether to fight, use magic, or escape the battle
  a =input("What will you do Fight, Magic, Run ")
  #If fight is choosed then the protagoonist and the monster will battle via random number between 1 to 6 for damage
  if a == "Fight":
      r = random.randint(1, 6)
      Monster.HP = Monster.HP - r
      print(Monster.name + " has taken damage " + str(Monster.HP) + " HP is remaining ")
      r = random.randint(1, 6)
      print(Monster.name + " is attacking")
      Protagonist.HP = Protagonist.HP - r
      print("You have taken damage " + str(Protagonist.HP) + "HP is remaining")
  #If magic is choosen then the protagonist gets to deal double damage at the cost of their mana. In which it depletes by 2
  elif a == "Magic":
      r = random.randint(0, 6) * 2
      print(str(r))
      Protagonist.mana = Protagonist.mana - 2
      if r == 4 or r == 8 or r == 0:
          print(Monster.name + " has taken no damage " + str(Monster.HP) + " HP Remaining")
          print(Monster.name + " is attacking")
          Protagonist.HP = Protagonist.HP - r
          print("You have taken damage " + str(Protagonist.HP) + "HP is remaining")
      Monster.HP = Monster.HP - r
      print(Monster.name + " has taken damage " + str(Monster.HP) + " HP is remaining ")
      r = random.randint(1, 6) 
      print(Monster.name + " is attacking")
      Protagonist.HP = Protagonist.HP - r
      print("You have taken damage " + str(Protagonist.HP) + "HP is remaining")
      if Protagonist.mana == 0:
          print("You are out of Mana")
  #if run is choosen then there is a 50% chance of escaping if unable to escape then the monster deals damage.
  elif a == "Run":
      r = random.randint(1, 4)
      if r == 2 or r == 4:
          print("You have escaped")
          break
      else:
          print(Monster.name + " has bloked your escape ")
          r = random.randint(1, 6)
          print(Monster.name + " is attacking")
          Protagonist.HP = Protagonist.HP - r
          print("You have taken damage " + str(Protagonist.HP) + "HP is remaining")
  #If the protagonist or the monster is at 0 HP then the battle ends
  if Protagonist.HP == 0 or Protagonist.HP < 0:
      print("You have no HP left\n" + "You don't have the strength to stand\n" + "GAME OVER!")
      break
  if Monster.HP < 0 or Monster.HP == 0:
      print(Monster.name + " has been defeated")
      break

      


    
        
      
    


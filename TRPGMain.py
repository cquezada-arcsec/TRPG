#This Software is a Text Based RPG called TRPG.
# This game will simulate an rpg game in a text variation
# This has been an ARCSec Software deveopled by Cesar Julian Quezada on June 22 2021 on Version 0.03
import random
import time 
from items import Items
import Towns 
print("""    _  _  _                        
               | |                         
               | |                         
               | |                         
               | |                         
            __ | | __                      
            \ \| |/ /                      
             \ \_/ /                       
              \   /                        
  _______ _____| | _____   _____           
 |__   __|  __ \_||  __ \ / ____|          
    | |  | |__) | | |__) | |  __           
    | |  |  _  /  |  ___/| | |_ |          
    | |_ | | \ \ _| |_   | |__| |_         
    |_(_)|_|  \_(_)_(_)   \_____(_)        
               | |                         
               | |                         
               | |                         
               | |                         
               | |                         
             __| |__                       
             \ \_/ /                       
              \ V /                        
               \_/ """)



print ("       Welcome to TRPG\n Where text fanatasies come to like")
s = input("Type start to begin your adventure\n " + ">> ")
#Defines the Charaters charateristics
class Protagonist:
    def __init__(self, name, HP, mana, level, xp, xpCap, itemStore):
      self.name = name
      self.HP = HP
      self.mana = mana
      self.level = level
      self.xp = xp
      self.xpCap = xpCap
      self.itemStore = itemStore

class Monster:
    def __init__(self, name, HP):
     self.name = name
     self.HP = HP
#Defines the Protagonist base skill level 
Protagonist.HP = 20
Protagonist.mana = 10
Protagonist.level = 1
Protagonist.xp = 0 
Protagonist.xpCap = 15
Protagonist.itemStore = []
Protagonist.name = input("Who are you?\n >> ") #Asks for the Protagonist name
print("Welcome\n " + Protagonist.name)
print(Protagonist.name + " you must save the world")
#Defines the Monster class and base skill level
Monster.name = "Goblin"
Monster.HP = 20
r = random.randint(1, 6)
print("A " + Monster.name + " has appeared")
#initiates the battle sequence
#Uses a loop while Protagonist and Monster HP are above 0
while Monster.HP != 0 or Protagonist.HP != 0:
  #Protagonist must choose whether to fight, use magic, or escape the battle
  a =input("What will you do\n Fight | Magic | Stats | Help | Run |\n >>  ")
  #If fight is choosed then the protagoonist and the monster will battle via random number between 1 to 6 for damage
  #Dmamage is declared by selecting a random number between 1 to 6
  if a == "Fight":
      r = random.randint(1, 6)
      Monster.HP = Monster.HP - r
      if Monster.HP < 0:
          Monster.HP == 0
      print(Monster.name + " has taken damage " + str(Monster.HP) + " HP is remaining ")
      r = random.randint(1, 6)
      print(Monster.name + " is attacking")
      Protagonist.HP = Protagonist.HP - r
      if Protagonist.HP < 0:
       Protagonist.HP == 0
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
     #Here is where the monster blocks your escape and deals damange
      else:
          print(Monster.name + " has bloked your escape ")
          r = random.randint(1, 6)
          print(Monster.name + " is attacking")
          Protagonist.HP = Protagonist.HP - r
          print("You have taken damage " + str(Protagonist.HP) + "HP is remaining")
  elif a == "Stats":
      print("Your Stats are: " ,Protagonist.HP ,"HP | " , Protagonist.mana,"Mana | ")
  elif a == "Help":
      h = input("What do you need help with:\n Fighting | \n, Magic | \n, Stats | \n >>")
      if h == "Fighting":
          print("Selecting this during battle will enage between you and your opponent\n Damage is taken by a randomly genrerated number between 1 to 6 and this applys to both you and your opponent")
      elif h == "Magic":
          print("Magic batlle is taken by generating a random number between 0 to 6 times 2: however,\n You use up mana by 2 each time you slect magic\n There is a 50 percent chance of missing and your oppnent will get to attack twice")
  #If the protagonist or the monster is at 0 HP then the battle ends
  if Protagonist.HP == 0 or Protagonist.HP < 0:
      print("You have no HP left\n"  +  "You don't have the strength to stand\n" + "GAME OVER!")
      input("Press Enter to Continue")
      quit()
  if Monster.HP < 0 or Monster.HP == 0:
      print(Monster.name + " has been defeated")
      r = random.randint(1,5)
      print("You gained " + str(r)+ "XP")
      Protagonist.xp = Protagonist.xp + r
      if Protagonist.xp == Protagonist.xpCap:
          Protagonist.level = Protagonist.level + 1
          Protagonist.xpCap +=1
          Protagonist.mana+=2
          Protagonist.HP+=2 
          print("You Leveled up:\n " + "You are at level: " +str(Protagonist.level))
      #This ends the battle loop    
      break

#Player dialouge between the player and an NPC called NPC
print("Stranger:\n You survived, you saved me")
#These are empty input statements to allow the player to press enter between the dialouge between the player and the NPC
input()
print(Protagonist.name + ":\n You're Welcome. Who are you?")
input()
print("Stranger: me? my name")
input()
print(Protagonist.name + ":\n Nah that dead goblin I slayed, OF COURSE YOUR NAME!")
input()
print("Stranger: \nSorry for my stupidity. My name is NormanPaul Caust but most folks call me NPC. May I ask the name of the hero who saved me")
input()
print(Protagonist.name + ":\n You can call me " + Protagonist.name)
input()
print("NPC:\n What were you doing in the forest. You know the forest is full of monsters.")
input()
print(Protagonist.name + ":\n The forest is dangerous? Huh! The monsters must love you for keeping them company.")
input()
print("NPC:(Angrily)\n You're avoiding the question.")
input()
print(Protagonist.name + ":\n Sorry I couldn't help it. (Pause")
time.sleep(3) #These are timed 3 seconds between print statements
print(Protagonist.name + ":\n Honestly, I don't remember why I was there. All I do know is that I woke up and a voice told me to save the world.")
input()
print("NPC:\n (Internal Thoughts) This guy is wacked up on some drugs but he did save me")
time.sleep(3)
print("NPC:\n You must be some big shot hero to save this world. You did save me so please take this potion to heal your self.")
Protagonist.itemStore = Items.Hpotion + 1
print("You recieved one Hpotion. This allows you to heal your HP by 3 HP")
input()
print(Protagonist.name + ":\n Thank you, May I ask what were you doing in the forest?")
input()
print("NPC:\n Well I am a traveling merchant. I was acually traveling back to A Town and that when I got attacked.")
input()
print(Protagonist.name + ":\n I see you can handle yourself in this forest full of monsters")
input()
print("NPC:\n Well usually I have an adventurer as a bodyguard but my buddy got pulled in an emergency quest. So I had to go alone this time. Usually this time of the year monsters are not as active as in the Summer.")
input()
print(Protagonist.name + ":\n You couldn't hire another adventurer?")
input()
print("NPC:\n The Adventurers Guild had none available due to an S class emergency")
input()
print(Protagonist.name +":\n What about your wonderful knights?")
input()
print("NPC:\n The knights are all out in helping the war effort.")
input()
print(Protagonist.name + ":\n So, you're telling me that your so, called kingdom can't defend a single town. Ah, the epitome of ineptitude! Your kingdom's defense strategy is like watching a comedy show where the punchline is how easily you surrender.")
input()
print("NPC:\n The Kingdom of Terrakaan has suffered from the wars from the Roku Dynansty, and Godrin Empire. We also have rebellion factions that threaten the kingdom once every couple of years. There is also the imminent threat of the Devil Lord.(pause)")
time.sleep(3)
print("NPC:\n With the weakend kingdom defenses, we could use someone with your skill.")
input()
print(Protagonist.name + "\n My skill huh? You know you just met me. Impressive deduction skills you have there! In the span of a single meeting, you've concluded that I possess the exact skill your weakened defenses need. Truly, you should be a royal clairvoyant!")
input()
print("NPC:\n I understand the risk of asking a stranger especially with the state of the Kingdom of Terrakaan but please help us.")
aDecide = input("Will you help NPC?\n Yes | No \n ")
if aDecide == "Yes":
    print(Protagonist.name + "\n Alright fine, I'll help you")
    print("NPC: \n Thank you kind sir. ")
    Towns()
else:
    input("Well looks whose a quiiter")
    quit()
        
      
    


#
#
#
import time



class ATown:
    def _init_(self,Inn, Trader, QuestBoard, Teller):
        self.Inn = Inn
        self.Trader = Trader
        self.Teller = Teller
        self.QuestBoard = QuestBoard
        
ATown.Inn = []
ATown.Trader = []
ATown.Teller = []
ATown.QuestBoard = []

def QuestBoard(QuestBoard):
    print("Welcome to the Quest Board.\n Here citizens of A Town post quests for you complete\n There are 4 types of quests you will see on the Quest Board; Main Quest, Dungeon, Mini Boss, Bounty")
    time.sleep(3)
    print("Main Quest will continue the Story")
    time.sleep(3)
    print("Dungeon quests allow you to explore dungeons, fight monstsers, collect loot\n Dungeon quests are limited to per town questboard")
    time.sleep(3)
    print("Mini Boss quest allow you to take on a harder enemy. These quests are limited to only one per towm visit")
    time.sleep(3)
    print("Monster quests are a ramdom monster quest. Here is where you can grind for XP as you can take on as many quests as you can")
    time.sleep(3)
    print("Here is the questboard:")
    input("Main Quest | Dungeon | Mini Boss | Bounty\n ")

def Inn(Inn):
    print("The Inn allows you to recover your HP and MP as well as to save your progress")



        


    

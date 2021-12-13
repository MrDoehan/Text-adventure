
failure = "you lost"
exhaustion = "Your exhaustion from a lack of a healthy meal results in your movement becoming slower and you are quickly defeaten by the orcs."
resting = "After a short rest and a nearby damp log, you get back up on your feet and once again, travel into the great unknown."
def fight():
  
  print("You travel for 10 more minutes until the peace and quiet that filled the atmosphere is suddenly disrupted by 2 orcs that ambush you ")
  attack1 = input("How do you attack? bow/ sword/ spell: ")
  if attack1 == "spell":
    if restored == False:
      print(exhaustion)
    else:  
      print("You begin to perform a spell to create a fireball only to realise you aren't a wizard and are immediately slayed by the orcs.")
      print("You lost.")
    
  if attack1 == "sword":
    
    if restored == False:
        print(exhaustion)
    
    else:  
      print("You charge forward to meet them. You successfully strike one of the orcs with two quick successive strokes, the remaining orc leaps forward but you instinctively react and counter the orc, knocking it unconscious.")
      print(resting)
    
  if attack1 == "bow":
    
    if restored == False:
        print(exhaustion)

    else:  
      print("You keep your distance and shoot once of the orcs which causes it to fall over in agony. During this, an orc leaps onto you with tremendous strength, fortunately, you are prepared and whip out your sword and impale the orc.")
      print(resting)
  elif attack1 == "":
    print("Your lack of decision making results in the orcs taking advantage of your immobility.")
    print(failure)  
  
  



failure = "you lost"
gold = 100
print("After a long and tiresome jounrey, you find youself at a fork in the road with your only two options being to turn left or right.")
query = input("What do you do? right/ left: ")
if query == "left":
  print("You died from a random twig in your way (yes this was intentionally made to be annoying :p)")
  choice = False
if query == "right":
  print("After 10 more minutes or travel, you are guided along a path of torches that lead you to the unrecognisable figures of houses. Finally, you are met by a looming gate. Your peace is broken by discordant screaming that follows a single person running away who is screaming for help.")
  choice = input("How do you react? block the chasers/ grab the person: ")
if choice == "grab the person":
  print("You decide to help the villages by grabbing the individual.")
  print("The village expresses their grattitude and lets you stay around for a certain amount of time. They explain to you the chaser was a spy from a nearby orc camp.")
  exp = 20
  attack1 = False   
 
  print("As you enter the door, you are met by soothing chimes and a bedraggled shopkeeper. The shopkeeper looks at you with interest.")
  print("the shopkeeper inquires,'What would you like to buy? Your sword looks rather blunt, and your quiver is clearly empty.'")
  print("Each item is 33 gold pieces and you have 100.")
  items = input("What would you like to buy? spellbook/sword/arrows: ")
  test = items.split()
  num = len(test)
  wow = num * 33
  if "spellbook" in items:
    rope = 0

  elif "sword" in items:
    global sword
    sword = 0
    if "sword" not in items:
      sword = False
    
  elif "arrows" in items:
    global arrows
    arrows = 0
    if "arrows" not in items:
      arrows = False
  current = gold - wow
  print(f"You have {current} gold piece/s left.")

  placesnd = input("Do you want to go to the tavern or are you finished? tavern/finished:  ")
  if "finished" in placesnd:
    restored = False
    fight()
  elif "tavern" in placesnd:
    if current < 30:
      print("You do not have enough money to afford anything from the tavern. This causes the bartender to be angered and in his drunk state, gets the whole bar to attack you.")
      print("You died")
      restored = False
      
    else:
      print("You feel completely restored and are prepared for anything that happens. You decide the money was well-spent.")
      restored = True
      setout = input("Are you ready to leave? y/n: ")
      if setout == "y":
        fight()
      else:
        print("Your decision __to stay in the village is met with joy as its clear you have happily affected many citizens. You put your life of adventuring behind you and live to a ripe age.")  
   
    

    
 
if choice == "block the chasers":
  print("You are no match for the oncoming stampede and are knocked unconscious.")
  print(failure)
  attack1 = False

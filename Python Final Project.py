#Jackson Schlosser
#Intro to Programming 120L
#Python Final Project.py
#03/30/2022
import time
health = 5
def main():
    #main function calls all levels in order and prompts user to play again
    global health
    while True:
        health = 5
        not_again = 0
        intro()
        creature_lvl()
        skele_lvl()
        dragon_lvl()
        pagain = input("Do you want to play again?(yes/no) ").lower()
        if pagain == "no":
            print("Good Bye")
            print()
            print("Copyright: Jackson Schlosser|jackson.schlosser1@marist.edu")
            break
    
def intro():
    #intro function gives introduction, explaining the rules and saves name
    print("Welcome to Cave Quest! This is a text-based adventure game in which only the most talented people can survive and claim the loot.")
    print()
    name = input("What is your name traveler? ")
    print()
    print(name + ", " + "you start with only 5 health, and your goal is to complete the game while losing the least amount of  health!")
    input("If you wish to start your quest into the cave, press <Enter> to start!")
    print()
    return name
    
def left_path():
    #This function is called if the user chooses the left path at the fork
    #It's main purpose is to lead the user towards the token of health 
    global health
    global not_again
    #This varible makes it so you can only use the left path once
    not_again += 1
    print("You continue to the left, towards the dim light.")
    input()
    print("The light seems to get brighter as you approach...")
    print("When you reach the light, you find a shining trophy sitting on a pedestal.")
    input()
    print("You inspect the trophy, and it reads: Instant Token of Health.")
    input()
    print("When you take the token the walls around you start to shake and a huge boulder begins to roll quickly towards you!")
    input()
    print("You sprint as fast as you can all the way back to the fork in the tunnel, and the boulder safely rolls right past you.")
    print()
    while True:
        IToH = input("Would you like to use the Instant Token of Health? (Yes/No) ").lower()
        if IToH == "yes":
            print("MMMmmMM that's some good health.")
            print()
            health += 1
            print(f"You now have {health} health.")
            input()
            break
        elif IToH == "y":
            print("MMMMmmMM that's some good health.")
            print()
            health += 1
            print(f"You now have {health} health.")
            input()
            break
        elif IToH == "no":
            print("No health for you!")
            print()
            print(f"You still have {health} health.")
            input()
            break
        elif IToH == "n":
            print("No health for you!")
            print()
            print(f"You still have {health} health.")
            input()
            break
        else:
            print("That's not right. Try again.")
        
def creature_lvl():
    #This function includes the first boss fight where the user has many choices to choose their fate, and location is set to 1
    global health
    global name
    global not_again
    location = 1
    print("As you slowly spelunk into the moist cave, you start to smell something rotten...")
    print()
    #User can light torch
    while True:
        light = input("It's too dark in this cave! Type <L> to light your torch!").lower()
        print()
        if light == "l":
            print("That's better!")
            input()
            break
        else:
            print("That is not your torch. Try again.")
    print("As the torch illuminates the cave, you notice large scratches on the wall.")
    print("You follow the scratches on the wall until you notice a creature in the corner of the cave.")
    input()
    print("Creature: Hello young one, I've heard a lot about you. Too bad I'm gonna eat you. MWAHAHWMA!")
    print()
    #User is prompted to attack the creature by typing S or P
    while True:
        attack_1 = input("To attack the creature, type <S> to use sharp spear, or <P> to throw a pebble.").lower()
        print()
        if attack_1 == "s":
            print("The creature snaps your spear and rips your arms out from their sockets.")
            health -= 1
            print()
            print("You managed to escape, but you sacrificed a life in the process.")
            input()
            print(f"You now have {health} health.")
            input()
            break
        elif attack_1 == "p":
            print("You hit the sweet spot and the creature falls on his face. You walk right over him.")
            print()
            break
        else:
            print("You can't do that. Try again.")
    print("You continue to walk through the damp cave when you stumble upon a hidden mineshaft.")
    input()
    #The user can choose whether or not to read the sign
    while True:
        read_sign = input("There is a sign on the entrance to the mineshaft. Would you like to read it? (Yes/No) ").lower()
        print()
        if read_sign == "yes":
            print("The sign says: My bones thrive in darkness.")
            input()
            break
        elif read_sign == "y":
            print("The sign says: My bones thrive in darkness.")
            input()
            break    
        elif read_sign == "no":
            print("Alright. Suit yourself!")
            input()
            break
        elif read_sign == "n":
            print("Alright. Suit yourself!")
            input()
            break
        else:
            print("What? Try that again.")
    print("You slowly creep through the mineshaft, using your torch to shed light on the dark passage.")
    input()
    print("On your journey, you encounter a fork in the road:")
    print("To the left, you see a dim light at the end of the tunnel and to the right, there is complete darkness.")
    input()
    not_again = 0
    #The variable not_again is tested to prevent user from using the left path twice
    while True:
        if not_again == 1:
            break
        fork = input("Which path do you choose? Left or Right? ").lower()
        print()
        if fork == "left":
            left_path()
        elif fork == "l":
            left_path()
        elif fork == "right":
            break
        elif fork == "r":
            break
        else:
            print("You can't go there. Try again.")
    #regardless of of they chose left or right, they will eventually be sent on the right path
    print("You continue to the right, with the darkness sending a shiver down your spine.")
    input()            
    print("This path is covered with sand and sharp rocks.")
    print()
    #User is prompted to pick up bottle by typing E
    while True:
        bottle = input("You find a broken bottle on the ground. Press <E> to pick it up. ").lower()
        print()
        if bottle == "e":
            print("That might come in handy.")
            input()
            break
        else:
            print("You can't do that to the bottle. Try again.")
            
def skele_lvl():
    #This function includes the second boss fight where the user has many choices in fighting a skeleton. Location is set to 2
    global health
    global name
    location = 2
    print("As you walk on the sandy path, you see a pile of bones in the distance.")
    input()
    print("You move closer to get a better look. Right before you reach down to pick up one of the bones, they start to levitate, forming a human skeleton.")
    input()
    print("Sir Skeleton: How dare you try and touch my bones! Now you must pay the consequences.")
    input()
    print("The skeleton throws his arm at you like a boomerang!")
    input()
    print("This costs you 1 health.")
    input()
    health -= 1
    print(f"You now have {health} health.")
    input()
    #The user chooses to attack the skeleton by typing S or B
    while True:
        attack2 = input("To attack the skeleton, type <S> to use your sword, or <B> to throw the broken bottle.").lower()
        print()
        if attack2 == "b":
            print("You throw the bottle at the skeleton and it shatters his skull.")
            print()
            print("The skeleton crumbles into a pile of dust, leaving an enchanted bow with 3 arrows behind.")
            input()
            break
        elif attack2 == "s":
            print("The skeleton takes your sword and starts to swing at you.")
            input()
            #dodge and bottle_attack are two parts of the boss fight that are called in order
            dodge()
            bottle_attack()
            break
        else:
            print("What? Try that again.")
    #User collects bow and arrows after fighting skeleton by typing E
    while True:
        bow1 = input("Type <E> to pick up the bow and arrows. ").lower()
        print()
        if bow1 == "e":
            print("This weapon is great for long distances!")
            input()
            break
        else:
            print("Try that again.")
    print("You move along with your bow in hand, knocked with an arrow.")
    input()
    #User chooses an amount of time to sit at the campfire to heal, then fire_timer function is called
    while True:
        fire_light = input("You come across an old campfire. Type <L> to light it with your torch.").lower()
        print()
        if fire_light == "l":
            print("The fire is nice and warm. You feel the heat healing your wounds.")
            input()
            fire_timer()
            break
        else:
            print("You can't do that. Try lighting the fire.")
                
def dodge():
    #This function is a part of the skeleton boss fight where the user can choose to press D to dodge or not
    global health
    while True:
        dodge1 = input("Type <D> to dodge the attack. ").lower()
        print()
        if dodge1 == "d":
            print("You successfully dodged the attack.")
            input()
            break
        else:
            print("You fail to dodge the attack and the skeleton hurls the sword into your side, costing you 1 health.")
            print()
            health -= 1
            print(f"You now have {health} health.")
            input()
            break
        
def bottle_attack():
    #In this fuction, the user is prompted to throw a bottle at the skeleton by typing B
    global health
    while True:
        attack3 = input("Type <B> to throw the broken bottle. ").lower()
        print()
        if attack3 == "b":
            print("You throw the bottle at the skeleton and it shatters his skull.")
            print()
            print("The skeleton crumbles into a pile of dust, leaving an enchanted bow with 3 arrows behind.")
            input()
            break
        else:
            print("What? Try that again.")
                   
def fire_timer():
    #The fire timer is used to output how ever many seconds the user wants to wait at the fire.
    global health
    global seconds
    errorCheck()
    print()
    for i in range(seconds):
        print(seconds - i)
        time.sleep(1)
    while True:
        print()
        #User will gain 3 health if they waited longer than 29 seconds
        if seconds > 29:
            health += 3
            print(f"You stayed at the campfire for {seconds} minutes. The campfire healed you greatly!")
            print()
            print(f"You now have {health} health.")
            input()
            break
        #User will gain 2 health if they waited longer than 19 seconds
        elif seconds > 19:
            health += 2
            print(f"You stayed at the campfire for {seconds} minutes. The campfire healed you a good amount!")
            print()
            print(f"You now have {health} health.")
            input()
            break
        #User will gain 1 health if they waited longer than 9 seconds
        elif seconds > 9:
            health += 1
            print(f"You stayed at the campfire for {seconds} minutes. The campfire healed you a little.")
            print()
            print(f"You now have {health} health.")
            input()
            break
        #User will gain 0 health becuase they didnt wait at the fire long enough to heal
        else:
            print(f"You stayed at the campfire for {seconds} minutes. The fire gave you a tingly feeling but gave you no health.")
            print("Next time try staying at the campfire a little longer.")
            input()
            break
        
def errorCheck():
    global seconds
    while True:
        try:
            seconds = int(input("How long would you like to stay at the campfire? Enter a number 1-30 "))
            break
        except ValueError:
            print("Please enter a valid number!")
            print()
        
def dragon_lvl():
    #This function includes the dragon boss fight allowing the user to have many choices for their fate, and location is set to 3
    global health
    global name
    global not_again
    location = 3
    print("After a nice rest, you leave camp to explore the deepest parts of the cave.")
    input()
    print("This part of the cave is burnt to a crisp as if a wildfire has blown through it.")
    input()
    print("All the wood holding up the cave has been turned into charcoal.")
    #User is prompted to collect charcoal by typing E
    while True:
        print()
        grab_coal = input("Type <E> to collect a piece of charcoal.").lower()
        print()
        if grab_coal == "e":
            print("Charcoal can be used as a weapon or as a fire starter.")
            break
        else:
            print("You can't do that to the charcoal. Try again.")
    input()
    print("You continue walking when the cave begins to shake.")
    input()
    while True:
        #User is prompted to move left or right by typind L or R
        left_right = input("A rock falls from the ceiling, type <L> to dodge to the left and <R> to dodge to the right.").lower()
        print()
        if left_right == "left":
            print("You throw yourself to the left, and the rock hits you directly on the head.")
            input()
            print("This costs you 1 health.")
            print()
            health -= 1
            print(f"You now have {health} health.")
            input()
            break
        elif left_right == "l":
            print("You throw yourself to the left, and the rock hits you directly on the head.")
            input()
            print("This costs you 1 health.")
            print()
            health -= 1
            print(f"You now have {health} health.")
            input()
            break
        elif left_right == "right":
            print("You throw yourself to the right, and you hit your head on the wall.")
            input()
            break
        elif left_right == "r":
            print("You throw yourself to the right, and you hit your head on the wall.")
            input()
            break
        else:
            print("WHERE do you wanna go?? Try again.")
    #user is prompted to type W to drink water
    print("You continue on your journey, with a great headache.")
    while True:
        print()
        water = input("Type <W> to drink the water in your backpack.").lower()
        print()
        if water == "w":
            print("Ahhh that's refreshing!!")
            input()
            break
        else:
            print("You need to drink water.")
    print("You walk for a while until your feet are completely black from all the ash and dirt.")
    print()
    print("In the distance, there is a bright opening in the path.")
    input()
    print("When you walk closer, you realize you aren't in a normal cave system...")
    input()
    print("You are inside a volcano.")
    input()
    print("The path comes to an end and there is a gigantic pool of lava beneath you.")
    input()
    print("All of a sudden, a raging dragon flies in through the top of the volcano and sits on a rock in the middle of the lava pit.")
    input()
    print("Dragon: HHHRRREEEEEE! What are you doing in my volcano?! You'll make the perfect snack!!")
    input()
    #User is propted to type D to dodge the blast, they will take damage regardless
    fireball = input("The dragon shoots his dragon breath at you! Type <D> to dodge the blast.")
    print()
    print("You try to dodge the blast, but you didn't have enough time to react.")
    input()
    print("This costs you 1 health.")
    health -= 1
    print()
    print(f"You now have {health} health.")
    #User is prompted to throw coal or use bow against dragon by typing C or B
    while True:
        input()
        finish_move = input("Type <C> to throw coal, or <B> to shoot an arrow at the dragon.").lower()
        print()
        if finish_move == "c":
            print("You try to throw the piece of coal at the dragon, but it does nothing.")
            input()
            print("You then use your bow to shoot 3 arrows at the dragon.")
            input()
            print("This first one hits his left wing causing no permanent damage.")
            input()
            print("The second misses completely.")
            input()
            print("The third one hits the dragon directly in the eye.")
            input()
            print("The dragon cries HHHREEEEEEEE, and lays to rest in the pool of lava.")
            input()
            endgame()
            break
        elif finish_move == "b":
            print("You use your bow to shoot 3 arrows at the dragon.")
            input()
            print("This first on hits his left wing.")
            input()
            print("The second misses completely.")
            input()
            print("The third one hits the dragon directly in the eye.")
            input()
            print("The dragon cries HHHREEEEEEEE, and lays to rest in the pool of lava.")
            input()
            endgame()
            break
        else:
            print("You can't do that to the dragon.")
            
def endgame():
    #This function explains the end of the game and whether or not they won
    #User is then prompted to play again from main function
    while True:
        if health > 0:
            print("You did it! You defeated the dragon and completed Cave Quest!")
            input()
            print(f"You finished with {health} health left! Replay the game to try and beat your score!")
            print()
            break
        else:
            print("You failed the game! Better luck next time.")
            print()
            break
main()



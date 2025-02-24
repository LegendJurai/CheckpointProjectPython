# Pokémon Game starts:
import random

player = input("Prof. Oak: Hello! So, I heard you want to start your pokémon adventure to become the best pokémon trainer in the whole world? That's awesome! Can you tell me your name?")
print("================================================================================================================================================================================================")
print("Prof. Oak: Well, nice to meet you " + str(player) + "! To start your adventure, you have to get a pokémon first!")
print("Here I have three pokémons who would love to start an adventure with you!")
print("There is Bulbasaur from the grass- and poison-type...(1)")
print("There is Charmander from the fire-type...(2)")
print("And there is Squirtle from the water-type...(3)")
print("Which one do you choose?")
print("================================================================================================================================================================================================")

# Choosing starter pokémon 
choice = 0
while choice != 1 and choice != 2 and choice != 3:
  choice = int(input("Your choice (enter '1', '2' or '3'):"))

print("================================================================================================================================================================================================")

if choice == 1:
  starter_pokemon = "Bulbasaur"
  cody_starter_pokemon = random.randint(1, 2)
  if cody_starter_pokemon == 1:
    cody_starter_pokemon = "Squirtle"
  else:
    cody_starter_pokemon = "Charmander"

if choice == 2:
  starter_pokemon = "Charmander"
  cody_starter_pokemon = random.randint(1, 2)
  if cody_starter_pokemon == 1:
    cody_starter_pokemon = "Bulbasaur"
  else:
    cody_starter_pokemon = "Squirtle"

if choice == 3:
  starter_pokemon = "Squirtle"
  cody_starter_pokemon = random.randint(1, 2)
  if cody_starter_pokemon == 1:
    cody_starter_pokemon = "Charmander"
  else:
    cody_starter_pokemon = "Bulbasaur"

print("Prof. Oak: Great! You've picked " + str(starter_pokemon) + "! I'm sure that you will become best friends!")
print("================================================================================================================================================================================================")

# Meet Rival friend Cody
print("*Your friend Cody, who you've known since you were children, enters Prof. Oak's house*")
print("================================================================================================================================================================================================")
print("Cody: Hey " + str(player) + "! Did you already choose your pokémon? Oh, so you picked " + str(starter_pokemon) + "?")
print("Great! Well, I've picked " + str(cody_starter_pokemon) + "!")
print("I want to become the best pokémon trainer in the whole world! And since I know, it has been your childhood dream too, let's have our first pokémon fight together!")
print("================================================================================================================================================================================================")

okay = 0
while okay != "Okay" and okay != "okay":
  okay = input("*Enter 'Okay' to start your first pokémon fight* ")

print("================================================================================================================================================================================================")

# Starter Pokédex
if starter_pokemon == "Bulbasaur":
  hp_max = 100
  type_1 = "Grass"
  att_1_name_1 = "Tackle"
  att_1_name_2 = "Tackle -> Damage: "
  att_1_dmg = 20
  att_1_type = " -> Type: Normal"
  att_2_name_1 = "Razor Leaf"
  att_2_name_2 = "Razor Leaf -> Damage: "
  att_2_dmg = 20
  att_2_type = " -> Type: Grass"
  spec_att_1_eff = 20
  spec_att_1_name_1 = "Leech Seed"
  spec_att_1_name_2 = "Leech Seed -> Heals itself by " + str(spec_att_1_eff) + "hp."
  spec_att_1_type = " -> Type: Grass"
  spec_att_2_eff = 10 
  spec_att_2_name_1 = "Sludge Bomb"
  spec_att_2_name_2 = "Sludge Bomb -> Poisons the enemy for a random amount of rounds, each by " + str(spec_att_2_eff) + "hp."
  spec_att_2_type = " -> Type: Poison"

if starter_pokemon == "Charmander":
  hp_max = 100
  type_1 = "Fire"
  att_1_name_1 = "Tackle"
  att_1_name_2 = "Tackle -> Damage: "
  att_1_dmg = 20
  att_1_type = " -> Type: Normal"
  att_2_name_1 = "Fire Fang"
  att_2_name_2 = "Fire Fang -> Damage: "
  att_2_dmg = 20
  att_2_type = " -> Type: Fire"
  spec_att_1_eff = 25
  spec_att_1_name_1 = "Blazing Destruction"
  spec_att_1_name_2 = "Blazing Destruction -> Damage: " + str(spec_att_1_eff)
  spec_att_1_type = " -> Type: Fire"
  spec_att_2_eff = 10 
  spec_att_2_name_1 = "Steady Firebreathing"
  spec_att_2_name_2 = "Steady Firebreathing -> Burns the enemy for a random amount of rounds, each by " + str(spec_att_2_eff) + "hp."
  spec_att_2_type = " -> Type: Fire"

if starter_pokemon == "Squirtle":
  hp_max = 100
  type_1 = "Water"
  att_1_name_1 = "Tackle"
  att_1_name_2 = "Tackle -> Damage: "
  att_1_dmg = 20
  att_1_type = " -> Type: Normal"
  att_2_name_1 = "Water Gun"
  att_2_name_2 = "Water Gun -> Damage: "
  att_2_dmg = 20
  att_2_type = " -> Type: Water"
  spec_att_1_eff = 10
  spec_att_1_name_1 = "Shell Retreat"
  spec_att_1_name_2 = "Shell Retreat -> Attacks the enemy by " + str(spec_att_1_eff) + "hp and increases his defense for the next enemy attack."
  spec_att_1_type = " -> Type: Water"
  spec_att_2_eff = 10 
  spec_att_2_name_1 = "Bubble"
  spec_att_2_name_2 = "Bubble -> Attacks the enemy by " + str(spec_att_2_eff) + "hp and paralyzes the enemy for one round." 
  spec_att_2_type = " -> Type: Water"

# Cody Starter Pokédex
if cody_starter_pokemon == "Bulbasaur":
  cody_hp_max = 100
  cody_type_1 = "Grass"
  cody_att_1_name = "Tackle"
  cody_att_1_dmg = 20
  cody_att_1_type = "Normal"
  cody_att_2_name = "Razor Leaf"
  cody_att_2_dmg = 20
  cody_att_2_type = "Grass"
  cody_spec_att_1_eff = 20
  cody_spec_att_1_name = "Leech Seed"
  cody_spec_att_1_type = "Grass"
  cody_spec_att_2_eff = 10 
  cody_spec_att_2_name = "Sludge Bomb"
  cody_spec_att_2_type = "Poison"

if cody_starter_pokemon == "Charmander":
  cody_hp_max = 100
  cody_type_1 = "Fire"
  cody_att_1_name = "Tackle"
  cody_att_1_dmg = 20
  cody_att_1_type = "Normal"
  cody_att_2_name = "Fire Fang"
  cody_att_2_dmg = 20
  cody_att_2_type = "Fire"
  cody_spec_att_1_eff = 25
  cody_spec_att_1_name = "Blazing Destruction"
  cody_spec_att_1_type = "Fire"
  cody_spec_att_2_eff = 10 
  cody_spec_att_2_name = "Steady Firebreathing"
  cody_spec_att_2_type = "Fire"

if cody_starter_pokemon == "Squirtle":
  cody_hp_max = 100
  cody_type_1 = "Water"
  cody_att_1_name = "Tackle"
  cody_att_1_dmg = 20
  cody_att_1_type = "Normal"
  cody_att_2_name = "Water Gun"
  cody_att_2_dmg = 20
  cody_att_2_type = "Water"
  cody_spec_att_1_eff = 10
  cody_spec_att_1_name = "Shell Retreat"
  cody_spec_att_1_type = "Water"
  cody_spec_att_2_eff = 10 
  cody_spec_att_2_name = "Bubble" 
  cody_spec_att_2_type = "Water"


# Cody First Pokémon Fight
hp = hp_max
cody_hp = cody_hp_max

print("Cody: I choose you, " + str(cody_starter_pokemon) + "!")
print("You: Go, " + str(starter_pokemon) + "!")

status = "Normal"
cody_status = "Normal"
benefit = 0
cody_benefit = 0

while hp > 0 or cody_hp > 0:
  if hp > 0 and cody_hp > 0:

  
    factor = 1
    attack = 0

    if status == "Paralyzed":
      print("================================================================================================================================================================================================")
      print(str(starter_pokemon) + " is paralyzed. He can attack next round.")
      status = "Normal"

    else:
     print("================================================================================================================================================================================================")
     print("Attack:")
     print("1) " + str(att_1_name_2) + str(att_1_dmg) + str(att_1_type))
     print("2) " + str(att_2_name_2) + str(att_2_dmg) + str(att_2_type))
     print("3) " + str(spec_att_1_name_2) + str(spec_att_1_type))
     print("4) " + str(spec_att_2_name_2) + str(spec_att_2_type))

     attack = 0
     while attack != 1 and attack != 2 and attack != 3 and attack != 4:
       attack = int(input("Your turn (enter '1', '2', '3' or '4'): "))
     print("================================================================================================================================================================================================")

     if attack == 1:
       print("You: " + str(starter_pokemon) + ", use " + str(att_1_name_1) + "!" )
       cody_hp = cody_hp - att_1_dmg
       print(str(starter_pokemon) + " uses " + str(att_1_name_1) + ".")
       if cody_benefit == 1:
         cody_hp = cody_hp + cody_spec_att_1_eff
         print("Squirtle used Shell Retreat before. That covers 10points of damage.")
         cody_benefit = 0

     if attack == 2:
       print("You: " + str(starter_pokemon) + ", use " + str(att_2_name_1) + "!" )
       if att_2_type == " -> Type: Grass":
         if cody_type_1 == "Water":
           factor = 1.25
         if cody_type_1 == "Fire":
           factor = 0.75
       if att_2_type == " -> Type: Fire":
         if cody_type_1 == "Grass":
           factor = 1.25
         if cody_type_1 == "Water":
           factor = 0.75
       if att_2_type == " -> Type: Water":
         if cody_type_1 == "Fire":
            factor = 1.25
         if cody_type_1 == "Grass":
            factor = 0.75
       cody_hp = cody_hp - (att_2_dmg * factor)
       print(str(starter_pokemon) + " uses " + str(att_2_name_1) + ".")
       if factor == 1.25:
         print("Critical hit!")
       if factor == 0.75:
         print("This is not very effective.")
       if cody_benefit == 1:
         cody_hp = cody_hp + cody_spec_att_1_eff
         print("Squirtle used Shell Retreat before. That covers 10points of damage.")
         cody_benefit = 0
   
     if attack == 3:
       print("You: " + str(starter_pokemon) + ", use " + str(spec_att_1_name_1) + "!" )
       if starter_pokemon == "Bulbasaur":
         factor = 0
         if hp >= hp_max - spec_att_1_eff:
           hp = hp_max
         else:
           hp = hp + spec_att_1_eff
       if starter_pokemon == "Charmander":
         if spec_att_1_type == " -> Type: Fire":
           if cody_type_1 == "Grass":
             factor = 1.25
           if cody_type_1 == "Water":
             factor = 0.75
       if starter_pokemon == "Squirtle":
         benefit = 1
         if spec_att_1_type == " -> Type: Water":
           if cody_type_1 =="Fire":
             factor = 1.25
           if cody_type_1 == "Grass":
             factor = 0.75
       cody_hp = cody_hp - (spec_att_1_eff * factor)
       print(str(starter_pokemon) + " uses " + str(spec_att_1_name_1) + ".")
       if factor == 1.25:
         print("Critical hit!")
         if cody_benefit == 1:
           cody_hp = cody_hp + cody_spec_att_1_eff
           print("Squirtle used Shell Retreat before. That covers 10points of damage.")
           cody_benefit = 0
       if factor == 0.75:
         print("This is not very effective.")
         if cody_benefit == 1:
           cody_hp = cody_hp + cody_spec_att_1_eff
           print("Squirtle used Shell Retreat before. That covers 10points of damage.")
           cody_benefit = 0
       if factor == 0:
         print("Bulbasaur has healed himself.")

     if attack == 4: 
        print("You: " + str(starter_pokemon) + ", use " + str(spec_att_2_name_1) + "!" )
        print(str(starter_pokemon) + " uses " + str(spec_att_2_name_1) + ".")
        if starter_pokemon == "Bulbasaur":
          cody_status = "Poisoned"
          print(str(starter_pokemon) + " has poisoned " + str(cody_starter_pokemon) + "!")
        if starter_pokemon == "Charmander":
          cody_status = "Burned"
          print(str(cody_starter_pokemon) + " is burning!")
        if starter_pokemon == "Squirtle":
          cody_hp = cody_hp - spec_att_2_eff
          paralyze = random.randint(1,2)
          if paralyze == 1:
            cody_status = "Paralyzed"
            print(str(cody_starter_pokemon) + " is paralyzed!")
          else:
            print("Paralyzing-effect failed.")


    if cody_hp > 0:
     if cody_status == "Poisoned" or cody_status == "Burned":
         cody_hp = cody_hp - spec_att_2_eff
         if cody_status == "Poisoned":
           print(str(cody_starter_pokemon) + " got " + str(spec_att_2_eff) + "points damage from the poisoning.")
         elif cody_status == "Burned":
           print(str(cody_starter_pokemon) + " got " + str(spec_att_2_eff) + "points damage from the burning.")
         cody_poisburn_heal = random.randint(1,3)
         if cody_poisburn_heal == 3:
           if cody_status == "Poisoned":
             print(str(cody_starter_pokemon) + " has healed from the poisoning.")
           elif cody_status == "Burned":
             print(str(cody_starter_pokemon) + " has healed from the burning.")
           cody_status = "Normal"

    print("================================================================================================================================================================================================")
    print("Your " + str(starter_pokemon) + ": " + str(hp) + " / " + str(hp_max) + " hp.")
    print("Cody's " + str(cody_starter_pokemon) + ": " + str(cody_hp) + " / " + str(cody_hp_max) + " hp.")
    print("================================================================================================================================================================================================")

  elif hp <= 0 and cody_hp > 0:
    print(str(starter_pokemon) + " is defeated! Cody and " + str(cody_starter_pokemon) + " have won!")
    victory = "Cody"
    cody_hp = 0 
     

  if cody_hp > 0 and hp > 0:
    factor = 1

    if cody_status == "Paralyzed":
      print("================================================================================================================================================================================================")
      print(str(cody_starter_pokemon) + " is paralyzed. He can attack again next round.")
      cody_status = "Normal"

    else:
      cody_attack = random.randint(1,4)

      print("================================================================================================================================================================================================")

      if cody_attack == 1:
        print("Cody: " + str(cody_starter_pokemon) + ", use " + str(cody_att_1_name) + "!" )
        hp = hp - cody_att_1_dmg
        print(str(cody_starter_pokemon) + " uses " + str(cody_att_1_name) + ".")
        if benefit == 1:
          hp = hp + spec_att_1_eff
          print("Squirtle used Shell Retreat before. That covers 10points of damage.")
          benefit = 0

      if cody_attack == 2:
        print("Cody: " + str(cody_starter_pokemon) + ", use " + str(cody_att_2_name) + "!" )
        if cody_att_2_type == "Grass":
          if type_1 == "Water":
            factor = 1.25
          if type_1 == "Fire":
            factor = 0.75
        if cody_att_2_type == "Fire":
          if type_1 == "Grass":
            factor = 1.25
          if type_1 == "Water":
            factor = 0.75
        if cody_att_2_type == "Water":
          if type_1 == "Fire":
            factor = 1.25
          if type_1 == "Grass":
            factor = 0.75
        hp = hp - (cody_att_2_dmg * factor)
        print(str(cody_starter_pokemon) + " uses " + str(cody_att_2_name) + ".")
        if factor == 1.25:
          print("Critical hit!")
        if factor == 0.75:
          print("This is not very effective.")
        if benefit == 1:
          hp = hp + spec_att_1_eff
          print("Squirtle used Shell Retreat before. That covers 10points of damage.")
          benefit = 0
   
      if cody_attack == 3:
        print("Cody: " + str(cody_starter_pokemon) + ", use " + str(cody_spec_att_1_name) + "!" )
        if cody_starter_pokemon == "Bulbasaur":
          factor = 0
          if cody_hp >= cody_hp_max - cody_spec_att_1_eff:
            cody_hp = cody_hp_max
          else:
            cody_hp = cody_hp + cody_spec_att_1_eff
        if cody_starter_pokemon == "Charmander":
          if cody_spec_att_1_type == "Fire":
            if type_1 == "Grass":
              factor = 1.25
            if type_1 == "Water":
              factor = 0.75
        if cody_starter_pokemon == "Squirtle":
          cody_benefit = 1
          if cody_spec_att_1_type == "Water":
            if type_1 == "Fire":
              factor = 1.25
            if type_1 == "Grass":
              factor = 0.75
        hp = hp - (cody_spec_att_1_eff * factor)
        print(str(cody_starter_pokemon) + " uses " + str(cody_spec_att_1_name) + ".")
        if factor == 1.25:
          print("Critical hit!")
          if benefit == 1:
            hp = hp + spec_att_1_eff
            print("Squirtle used Shell Retreat before. That covers 10points of damage.")
            benefit = 0
        if factor == 0.75:
          print("This was not very effective!")
          if benefit == 1:
            hp = hp + spec_att_1_eff
            print("Squirtle used Shell Retreat before. That covers 10points of damage.")
            benefit = 0
        if factor == 0:
          print("Bulbasaur has healed himself.")

      if cody_attack == 4: 
        print("Cody: " + str(cody_starter_pokemon) + ", use " + str(cody_spec_att_2_name) + "!" )
        print(str(cody_starter_pokemon) + " uses " + str(cody_spec_att_2_name) + ".")
        if cody_starter_pokemon == "Bulbasaur":
          status = "Poisoned"
          print(str(cody_starter_pokemon) + " has poisoned " + str(starter_pokemon) + "!")
        if cody_starter_pokemon == "Charmander":
          status = "Burned"
          print(str(starter_pokemon) + " is burning!")
        if cody_starter_pokemon == "Squirtle":
          hp = hp - cody_spec_att_2_eff
          cody_paralyze = random.randint(1,2)
          if cody_paralyze == 1:
            status = "Paralyzed"
            print(str(starter_pokemon) + " is paralyzed!")
          else:
            print("Paralyzing-effect failed.")

    if hp > 0:
      if status == "Poisoned" or status == "Burned":
        hp = hp - cody_spec_att_2_eff
        if status == "Poisoned":
          print(str(starter_pokemon) + " got " + str(cody_spec_att_2_eff) + "points damage from the poison.")
        elif status == "Burned":
          print(str(starter_pokemon) + " got " + str(cody_spec_att_2_eff) + "points damage from the burning")
        poisburn_heal = random.randint(1,3)
        if poisburn_heal == 3:
          if status == "Poisoned":
            print(str(starter_pokemon) + " has healed from the poisoning!")
          elif status == "Burned":
            print(str(starter_pokemon) + " has healed from the burning!")
          status = "Normal"

    print("================================================================================================================================================================================================")
    print("Your " + str(starter_pokemon) + ": " + str(hp) + " / " + str(hp_max) + " hp.")
    print("Cody's " + str(cody_starter_pokemon) + ": " + str(cody_hp) + " / " + str(cody_hp_max) + " hp.")
    print("================================================================================================================================================================================================")

  elif cody_hp <= 0 and hp > 0:
    print(str(cody_starter_pokemon) + " is defeated! " + str(player) + " and " + str(starter_pokemon) + " have won!")
    victory = "You"
    hp = 0     


# End of Fight -> Resolution
print("================================================================================================================================================================================================")
if victory == "You":
  print("Cody: Wow, I'm really impressed " + str(player) + "! You and " + str(starter_pokemon) + " fought great together! I'm sure that you and him are gonna be an amazing team together! I can't wait 'til next time we'll meet, because then, me and " + str(cody_starter_pokemon) + " are gonna defeat you!") 

elif victory == "Cody":
  print("Cody: Ha! I said to you that you have no chance to win against me and " + str(cody_starter_pokemon) + "! Though, you and " + str(starter_pokemon) + " were a great team together! I can't wait 'til next time we'll meet! Maybe then, you have a chance to win? We'll see, but don't get your hopes up!")

print("================================================================================================================================================================================================")
print("Prof. Oak: Well, that was a great fight! I'm sure that you and " + str(starter_pokemon) + " are gonna be an amazing team together! I can't wait to see you both grow stronger and stronger! Good luck on your journey to become the best pokémon trainer in the whole world!")

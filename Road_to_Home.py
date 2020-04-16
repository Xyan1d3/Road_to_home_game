import random
import sys
import time


def generate_virus(val):
    varr = []
    while len(varr) != val:
        r = random.randint(1, 149)
        if r not in varr:
            varr.append(r)
    return varr


def generate_bacteria(val, virus_arr):
    barr = []
    while len(barr) != val:
        r = random.randint(1, 149)
        if r not in barr and r not in virus_arr:
            barr.append(r)
    return barr


def generate_bandage(val, virus_arr, bacteria_arr):
    bandarr = []
    while len(bandarr) != val:
        r = random.randint(1, 149)
        if r not in bandarr and r not in virus_arr and r not in bacteria_arr:
            bandarr.append(r)
    return bandarr


def generate_painkiller(val, virus_arr, bacteria_arr, bandage_arr):
    parr = []
    while len(parr) != val:
        r = random.randint(1, 149)
        if r not in parr and r not in virus_arr and r not in bacteria_arr and r not in bandage_arr:
            parr.append(r)
    return parr


def generate_medkit(val, virus_arr, bacteria_arr, bandage_arr, painkiller_arr):
    mkarr = []
    while len(mkarr) != val:
        r = random.randint(1, 149)
        if r not in mkarr and r not in virus_arr and r not in bacteria_arr and r not in bandage_arr and \
                r not in painkiller_arr:
            mkarr.append(r)
    return mkarr


def generate_taxi_service(val, virus_arr, bacteria_arr, bandage_arr, painkiller_arr, medkit_arr):
    tsarr = []
    while len(tsarr) != val:
        r = random.randint(1, 149)
        if r not in tsarr and r not in virus_arr and r not in bacteria_arr and r not in bandage_arr and \
                r not in painkiller_arr and r not in medkit_arr:
            tsarr.append(r)
    return tsarr


def rules():
    print("===========Welcome to Road to Home")
    print("-----------This game is written by c0ld_z3r0")
    print()
    print("========================================================================")
    print("Rules :")
    time.sleep(1)
    print("[*] You have to reach your home which is position 150")
    print("[*] The Road to your home is very difficult")
    print("[*] There are many elements in this board")
    print("[*] Your Health is Full wich is 30")
    print("[*] Your Buffs(Damage over time) is 0")
    print("[*] If virus infects you your HP is reduced by 2 and Buff is -2")
    print("[*] If virus infects you your HP is reduced by 1 and Buff is -1")
    print("[*] Means Everytime you roll your dice your buff will reduce your HP")
    print("[*] You buffs can stack up but maximum buff damage is -5")
    time.sleep(5)
    print("[*] Wait! There are healing elements also in this game")
    print("[*] The Medkit which will remove all buffs and fill you HP to full")
    print("[*] The Painkiller which will remove your buffs but doesn't affect your HP")
    print("[*] The Bandage which will increase your HP by 5 doesn't affect your Buffs")
    print("[*] If you want to play with a bot enter a player name bot")
    print()
    print()
    input("Press Enter when you are ready")


if __name__ == '__main__':
    rules()
    max_health = 30
    Health = []
    Buffs = []
    Position = []
    pnames = []
    pno = int(input("Enter Number of player's : "))

    for useless in range(pno):
        pnames.append(input("Enter player " + str(useless) + " name : "))
        Health.append(max_health)
        Buffs.append(0)
        Position.append(0)

    virus = generate_virus(15)
    bacteria = generate_bacteria(15, virus)
    bandage = generate_bandage(20, virus, bacteria)
    painkiller = generate_painkiller(10, virus, bacteria, bandage)
    medkit = generate_medkit(10, virus, bacteria, bandage, painkiller)
    taxi = generate_taxi_service(25, virus, bacteria, bandage, painkiller, medkit)

    while True:
        for turn in range(pno):
            print("----------------------------------------------------------------")
            if "bot " not in pnames[turn].lower():
                input(pnames[turn] + "'s turn press Enter to roll the dice")
            Health[turn] = Health[turn] + Buffs[turn]
            dice = random.randint(1, 6)

            if Position[turn] + dice > 150:
                pass
            if Position[turn] + dice == 150 or Position[turn] == 150:
                print(pnames[turn] + " won the match")
                sys.exit()

            print(pnames[turn] + " got : " + str(dice))
            print("Your Position was : ", str(Position[turn]))
            Position[turn] = Position[turn] + dice

            if (Position[turn]) in taxi:
                print("You landed on free Taxi Service")
                newpos = random.randint(-20, 45)
                Position[turn] = Position[turn] + newpos
                if Position[turn] < 0:
                    Position[turn] = 0
                if Position[turn] > 150:
                    Position[turn] = 150
                if newpos < 0:
                    print("The Taxi driver was drunk and took you back " + str(abs(newpos)) + " blocks")
                else:
                    print("You have advanced " + str(newpos) + " blocks")

            if (Position[turn]) in virus:
                Health[turn] += -2
                Buffs[turn] += -2
                if Buffs[turn] < -5:
                    Buffs[turn] = -5
                print("Oh! No you are infected by virus you are losing HP by 2")

            if (Position[turn]) in bacteria:
                Health[turn] += -1
                Buffs[turn] += -1
                if Buffs[turn] < -5:
                    Buffs[turn] = -5
                print("Oh! No you are infected by bacteria you are losing HP by 1")

            if (Position[turn]) in bandage:
                Health[turn] += 5
                print("You used a bandage and your HP is increased by 5")
                if Health[turn] > 30:
                    Health[turn] = 30
            if (Position[turn]) in medkit:
                Health[turn] = max_health
                Buffs[turn] = 0
                print("You used a MedKit your HP is full and buffs are gone")

            if (Position[turn]) in painkiller:
                Buffs[turn] = 0
                print("You used some painkillers your all buffs are gone")
                print("Your position is :" + str(Position[turn]) + " blocks")

            print(pnames[turn] + "'s " + "HP is :" + str(Health[turn]))
            print(pnames[turn] + "'s " + "buffs are :" + str(Buffs[turn]))
            print("Your position is :" + str(Position[turn]) + " blocks")

            if Position[turn] == 150:
                print("----------------------------!!!!--------------------------------")
                print(pnames[turn] + " won the match")
                sys.exit()
            if Health[turn] <= 0:
                print("----------------------------!!!!--------------------------------")
                print(pnames[turn] + " has lost the game and is kicked out :(")
                if pno <= 2:
                    pnames.pop(turn)
                    print(pnames[0] + " won the match !!!!")
                    sys.exit()
                else:
                    pno = pno - 1
                pnames.pop(turn)
                Health.pop(turn)
                Buffs.pop(turn)
                Position.pop(turn)

                pass

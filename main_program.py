import classstat as sample_stat
import classev as sample_ev

def option_menu():
    sample1 = int(input("1 Compute Again or 2 Exit: "))
    if sample1 == 1:
        main()
    elif sample1 == 2:
        exit()
    else:
        print("Wrong Input")

def main():   
    base1 = int(input("Base: ")) 
    trap1 = 1
    while trap1 == 1:
        iv = int(input("Individual Value: "))
        if iv >= 0 and iv <=31:
            trap1=0
        else:
            print("Error Input")
        
    trap1 = 1
        
    while trap1 == 1:
        ev = int(input("Effort Values: "))
        if ev >= 0 and ev <=255:
            trap1=0
        else:
            print("Error Input")
            
    lvl = int(input("Level: "))
            
    trap1 = 1
    nature_input = int(input("(1)Benificial or (2)Hindering: "))
    if nature_input == 1:
        nature = 1.1
    else:
        nature = 0.9

    print('\n')
    a = int(input("1 = Stat or 2 = EV Input: "))

    if a==1:
        
        hp= sample_stat.Classstat.statReturnHP(base1,iv,ev,lvl)
        ostat = sample_stat.Classstat.statReturnOtherStat(base1,iv,ev,lvl,nature)
        print("HP is ", hp)
        print("Other Stats is", ostat, '\n')

        option_menu()

    elif a==2:
        stats = int(input("Stats: "))
        d = sample_ev.Classev.statReturnD(base1,iv,ev,lvl)
        evs = sample_ev.Classev.statReturnEvs(stats,nature,d,lvl)    
        print("Desired Stat Increase: ", d)
        print("Effort Value Stats: ", evs, '\n')

        option_menu()
        
    else:
        print("Wrong input")

main()
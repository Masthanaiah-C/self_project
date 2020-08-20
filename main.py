import rand
#per each game code reaches here and return to main file after completing the game with results 
def start(target_score,terms,name):
    j=rand.comp()
    cm=rand.gen()
    score_me=0
    score_com=0
    count=0
    f=True
    while (score_me<target_score and score_com<target_score):
        if count==0 and f:
            print("----GAME STARTS-----::Target=",target_score)
        
        print("\"1\" for \"rock\"\n\"2\" for \"paper\"\n\"3\" for \"scissors\"")
        try:
            me=int(input("ENTER UR OPTION (round "+str(count+1)+"):\n"))
        except ValueError:
            print("wrong value:(")
            f=False
            continue
        if me not in [1,2,3] :
            print("choose out of bound.....try again!\n")
            continue
        
            
        comp_choice=cm.com_choice() #takes to other file rand to get computer choice 
        
        x,y=(j.result(terms[me],terms[comp_choice]))
        score_me+=x # adding score of each turn
        score_com+=y
        won=x-y #to determine winner of each term 
        print( "you choose '"+ terms[me].upper()+"'    computer choose   '"+terms[comp_choice].upper() +"'")
        if won==0:
            print("clash : no point each\n")
        elif won>0:
            print("wow!,you scored 1 points\n")
        else:
            print("oops!,computer scored 1 points\n")

        print("                                                      SCORES :-  "+name+"   "+str(score_me)+"  :: computer   "+str(score_com))
        lead=score_me-score_com #to determine the winner of the game
        if lead>0:
            print("you are in lead with :"+str(lead))
        elif lead<0:
            print("computer is in lead with :"+str(abs(lead)))
        else:
            print("scores are tie! with '"+ str(score_com) + "' each")
        
        #below one is crucial as: one cant win with luck in the border and to maintain atleast diff of 2 in the end of game
        
        if score_com==target_score-1 and score_me==target_score-1:
            target_score+=1
            print("target extended to "+str(target_score))
        count+=1
    
    if score_com<score_me:
        print("YOU WON  "+name.capitalize())
    else:
        print("YOU LOSE  "+name.capitalize())
terms=dict()
terms[1]="rock"
terms[2]="paper"
terms[3]="scissors"
name=input("Enter your Name:")
target_score=int(input("set the game score:(>1)"))
start(target_score,terms,name)
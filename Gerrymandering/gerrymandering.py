#Xavier Caracter, CSc 110
#Section H, Jessie B.
#3/18/18
#This program will how the results of gerrymandering voter results from a specific state
from DrawingPanel import * #so I can use graphics
#Sets the constant for the panel's Length and Width
MAXPANELX = 500
MAXPANELY = 500
#main function that contains all running functions
def main():
    introPhrase()
    sortRead()
#Displays the actions of the program to the user
def introPhrase():
    print("This program allows you to search through")
    print("data about congressional votiong districts")
    print("and determine whether a particular state is")
    print("gerrymandered.")
#Reads and sorts the data from the files
def sortRead():
    findState = False
    democratSum = 0
    republicanSum = 0
    dist = open("districts.txt")
    vote = open("eligible_voters.txt")
    districts = dist.readlines()
    voters = vote.readlines()
    userSelection = input("\nWhich state do you want to look up? ")
    demList = []
    gopList = []
    for line in districts:
        #print(userSelection.lower() in line.lower())
        if userSelection.lower() in line.lower():
            findState = True
            dist = line.split(",")
            #Loops through the selected line and adds together democrat and GOP votes
            for i in range(2,len(dist),3):
                demList.append(dist[i])
                gopList.append(dist[i+1])
                democratSum += int(dist[i])
                republicanSum += int(dist[i+1])
                winningAmount = (democratSum + republicanSum)//2
                if winningAmount % 2 == 0:
                    winningAmount += 1
                else:
                    round(winningAmount)
                    if democratSum > winningAmount:
                        wastedGOP = republicanSum
                        wastedDemocrat = democratSum - winningAmount
                    else:
                        wastedDemocrat = democratSum
                        wastedGOP = republicanSum - winningAmount
            print("Total wasted Democratic votes: ", wastedDemocrat)
            print("Total wasted Republican votes: ", wastedGOP)
            #Prints the the number of total voters for user
            for section in voters:
                if userSelection.lower() in section.lower():
                    eligible = section.split(",")
                    print(eligible[1].strip(),"eligible voters")
    if findState == False:
        print('"',userSelection,'"', 'not found')
        return
    graphic(dist,eligible,demList,gopList)
#Shows graphical representation of the data
def graphic(dist,eligible,demList,gopList):
    panel= DrawingPanel(MAXPANELX,MAXPANELY,background="white")
    panel.draw_line(MAXPANELX/2,0,MAXPANELX/2,MAXPANELY)
    panel.draw_line(0,20,MAXPANELX,20)
    panel.draw_string(dist[0],0,0)
    panel.draw_string(eligible[1].strip("\n")+" eligible voters",MAXPANELX-120,0)
    shiftList = demList.insert(0,"0")
    shiftedList = gopList.insert(0,"0")
    for i in range(1,len(demList)):
            demVote = (int(demList[i]))
            repubVote = (int(gopList[i]))
            barLength = ((demVote/(demVote+repubVote))*MAXPANELX)
            panel.fill_rect(0,(i*25)+5,barLength,20,"blue")
            panel.fill_rect(barLength,(i*25)+5,MAXPANELX - barLength,20,"red")
main()    

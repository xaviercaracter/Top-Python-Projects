#Xavier Carcater, CSC 110
#Sectoin H, Jessie B.
#4/27/18
#This program will demonstrate my knowledge of data structures and will give people recommendations based off of people's (users) ratings

def main():
    ratingdict,booklist,namelist,totallist = process()
    ratingdict  = combine(totallist,booklist,ratingdict)
    ratings = calculate(booklist,ratingdict)
    intro()
    userIn = input("next task? ")
    while userIn == "recommend" or "average": 
        if userIn == "recommend":
            recomend(ratingdict,ratings)
            userIn = input("next task? ")
        elif userIn == "averages":
            averages(ratings)
            userIn =input("next task? ")
        elif userIn == "quit":
            exit()

#processes informaiton given and creates the booklist, names list, and processes the input fil
def process():
    ratingdict = {}
    bookset = set()
    nameset = set()
    totallist = []
    ratings = []
    file = open("ratings.txt").read().splitlines()
    for line in file:
        line = line.strip()
        totallist.append(line)
        for i in range(1,len(totallist),3):
            bookset.add(totallist[i])
        for j in range(0,len(totallist),3):
            nameset.add(totallist[j])
            
    namelist = list(nameset)
    booklist = list(bookset)
    
    return ratingdict,booklist,namelist,totallist
#coombines data and f=creates full data dictioonary of names and ratings
def combine(totallist,booklist,ratingdict):
    for i in range(0,len(totallist),3):
        if totallist[i] not in ratingdict.keys():
            ratingdict[totallist[i]] = list((0,)*len(booklist))
        ratingdict [totallist[i]][booklist.index(totallist[i+1])] = totallist[i+2]
    return ratingdict
#Prints intro
def intro():
    print("Welcome to the CSC110 Book Recommender. Type the word in the\nleft column to do the action on the right.\nrecommend : recommend books for a particular user\naverages  : output the average ratings of all books in the system\nquit      : exit the program")

def recomend(ratingdict,ratings):
    askOne = input("user? ")
    if askOne not in ratingdict.keys():
        averages(ratings)
    print("Books\n")
    return askOne
#Calculates the averages and retrns data to main
def calculate(booklist,ratingdict):
    ratings = []
    for i in range(len(booklist)):
        summ = 0
        num = 0
        for j in ratingdict:
            summ += int(ratingdict[j][i])
            if ratingdict[j][i] != 0:
                num += 1
        average = summ/num
        title = booklist[i]
        tup = (average,title)
        
        ratings.append(tup)
        ratings.sort()
        ratings.reverse()
    return ratings
#Takes the list of tuples in rating and prints them to the console
def averages(ratings):
    for tup in ratings:
        for items in reversed(tup):
            print(items)
    print("")




            
main()

'''
Author: Xavier Caracter
Description: This program will take the information given from
two input files and produce a chord progression and small solo piece
'''

#Importing Random module
import random

def main():
    keys, cusChord, soloNotes = intro()
    chordsdict = chordsprocess()
    notesdict = notesprocess()
    prog = progression(chordsdict,notesdict,keys,cusChord)
    chosenNotes = choosenotes(prog,notesdict,keys, soloNotes)
    print("\n")
    print(chosenNotes)
    

#Getting uer input for what key we are in and how many unique chords we can play
def intro():
    keys = input("What key would you like to play in? ")
    cusChord = int(input("How many unique chords? (up to 6) "))
    soloNotes = int(input("How long would your like you solo to be? "))
    return keys,cusChord,soloNotes

#Processes chords.txt file and returns a dictionary of chords
def chordsprocess():
    chords = open("chords.txt").readlines()
    chordsdict = {}
    chordslist = []
    for i in range(len(chords)):
        chords[i] = chords[i].split()
        chordsdict[chords[i][0]]= chords[i][1:]
    return chordsdict

#Processes the notes.txt file and returns a dictionary of notes
def notesprocess():
    notes = open("notes.txt").readlines()
    notesdict = {}
    for j in range (len(notes)):
        notes[j] = notes[j].split()
        notesdict[notes[j][0]]= notes[j][1:]
    return notesdict

#Selects a chord progression from the key given by user out of the chords dictionary
def progression(chordsdict,notesdict,keys,cusChord):
    prog = chordsdict[keys]
    print("Chord Progression: ", end='')
    while len(prog) > cusChord:
        prog.pop()
    for i in range(len(prog)):
        print(prog[i],"",end ='')
    return prog

#Chooses random notes from the chords dicitonary
def choosenotes(prog, notesdict, keys, soloNotes):
    notes = notesdict[keys]
    chosennotes = []
    for i in range(soloNotes):
        x = random.randint(0,len(notes)-1)
        chosennotes.append(notes[x])
    return chosennotes





    
main()

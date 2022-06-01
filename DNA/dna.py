#This program will process the data from a given genome file
MINCOD = 5
MASSPER = 30
UNINUC = 4
NUCCOD = 3
def main():
    introPhrase()
    userInput()
#Writes the intro string before the inputs
def introPhrase():
    print("This program reports information about DNA\nnucleotide sequences that may encode proteins.")
def userInput():
    response = input("Input file name? ")
    outResponse = input("Output file name? ")
    file = open(response).readlines()
    outFile = open(outResponse, "w")
    regionList = []
    nucleotides = []
    #loop that goes through and appends the names and nucleotides
    for i in range(0,len(file),2):
        regionList = file[i].strip()
        nucleotides = file[i+1].strip()
        outFile.write("Region Name: "+regionList+"\n")
        outFile.write("Nucleotides: "+nucleotides.upper()+"\n")
        process(nucleotides,outFile)
        codonList(nucleotides,outFile)
        outFile.write('')
#processes the math involved with the nucleotides and masses
def process(nucleotides,outFile):
    dashCount = 0
    nucleotide_count = [0,0,0,0]
    mass_percentages = [0,0,0,0]
    #Sorts through the lettes in the nucleotide strings and calculates based on number of appearence
    for letter in nucleotides:
        if letter.upper() == "A":
            nucleotide_count[0]+=1
        elif letter.upper() == "C":
            nucleotide_count[1]+=1
        elif letter.upper() == "G":
            nucleotide_count[2]+=1
        elif letter.upper() == "T":
            nucleotide_count[3]+=1
        else:
            dashCount += 1
    #Calculated totals of A,C,G,T
    totalA = (nucleotide_count[0]*135.128)
    totalC = (nucleotide_count[1]*111.103)
    totalG = (nucleotide_count[2]*151.128)
    totalT = (nucleotide_count[3]*125.107)
    totalDash = (dashCount*100.000)
    grandTotal = (totalA+totalC+totalG+totalT+totalDash)
    #Percentage of A,C,G,T
    mass_percentages[0] = round((totalA/grandTotal)*100,1)
    mass_percentages[1] = round((totalC/grandTotal)*100,1)
    mass_percentages[2] = round((totalG/grandTotal)*100,1)
    mass_percentages[3] = round((totalT/grandTotal)*100,1)
    printTotal=round(totalA+totalC+totalG+totalT,1)
    outFile.write("Nuc. Counts: "+ str(nucleotide_count)+"\n")
    outFile.write("Total Mass%: "+ str(mass_percentages)+"of "+ str(printTotal)+"\n")
    return(totalC, totalG)
#Gives the separated codon list 
def codonList(nucleotides,outFile):
    isProtein = False
    codList = []
    codonString =(nucleotides.upper().replace("-",""))
    for i in range(0,len(codonString),3):
        codon = codonString[i:i+3]
        codList.append(codon)
    if codList[0] == "ATG" and codList[-1] == "TAA" or codList[-1] == "TAG" or codList[-1] == "TGA" and int(len(codList)) >= MINCOD:
        isProtein = True
        x = "YES"
    else:
        isProtein = False
        x = "NO"
    outFile.write("Codons List: "+str(codList)+"\n")
    outFile.write("Is Protein?: "+x+"\n"+"\n")
main()

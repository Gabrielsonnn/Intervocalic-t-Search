#Gabe Johnson
#Solution to finding intervoclaic /t/ within a txt file and printing it to a csv file

#TODO:
#be able to deal with [] and {}
##remove extra characters from words
#find /t/ in words
#print a csv

print("Welcome the intervocalic /t/ search.")
print("")

cont = False
while cont is False: #while loop used to get a file from the user that successfully opens
    
    t_file_name = input("Please enter the name of the file you would like to search: ") #asks user to input file name

    t_open = None

    try:
        t_open = open(t_file_name, "r") #try to open file
    except IOError:
        print("Could not open file. Please check file path, or use an absolute path.") #if it fails it outputs error
        print("")
    else:
        cont = True #if it doesn't fail it breaks out of while loop

    #this is purely here for visual studios so it looks nicer, don't ask. You can delete this if you want
    cont = cont 

t_word = [] #declare an empty list to hold t word
t_speaker = [] #to hold speaker of t word
t_time = [] #to hold time spoken of t word

temp = None #temp value
t_exist = False #value to test if there is a t or not in a word
current_speaker = None #value to hold current speaker
l_pos = 0 #value to hold current list posistion, starts at zero
l_count = 0 #counts how many positions were skipped, so it can add in the time

step_flag = 1 #flag to know what line in each entry is

t_lines = t_open.readlines()

for t_line in t_lines:
    if step_flag == 1: #first line of entry
        line_words = list(t_line.split()) #splits line into seperate words

        current_speaker = line_words[0] #gets current speaker from file

        for word in line_words[1:]: #skips first entry in list, iterates through words
            t_exist = False

            for ch in word: #iterates through each char in word
                if ch == 't' or ch == 'T': #checks if char is 't', if it is sets t_exist to true
                    t_exist = True

            if t_exist == True: #if its true puts t word in list
                t_word.append(word) #sets t_word to current word
                t_speaker.append(current_speaker) #sets t_speaker to current speaker
                l_pos += 1 #increments pos
                l_count += 1 #increments count

        step_flag = 2 #sets flag to next stage

    elif step_flag == 2: #second line of entry
        line_words = list(t_line.split()) #splits line into seperate words

        for i in range(0,l_count): #sets t_time to the start time of the entry, does that for however many t words were added
            t_time.append(line_words[0])

        l_count = 0 #sets count back to zero
        step_flag = 3 #sets flag to next stage

    elif step_flag == 3: #third line of entry
        #do nothing
        step_flag = 1 #sets flag to first stage

step_flag = step_flag #used to make for loop look nice

for t in range(0, len(t_word)):
    print("%10s %10s %10s" % (t_word[t], t_speaker[t], t_time[t]))
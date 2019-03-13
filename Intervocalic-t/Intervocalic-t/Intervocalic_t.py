#Gabe Johnson
#Solution to finding intervoclaic /t/ within a txt file and printing it to a csv file
import re #used for regex

#FUCNTION DEFINITIONS
def fileNameCheck():
    cont = False
    while cont is False: #while loop used to get a file from the user that successfully opens
    
        file_name = input("Please enter the name of the file you would like to search: ") #asks user to input file name

        file_open = None

        try:
            file_open = open(file_name, "r") #try to open file
        except IOError:
            print("Could not open file. Please check file path, or use an absolute path.") #if it fails it outputs error
            print("")
        else:
            cont = True #if it doesn't fail it breaks out of while loop
            file_open.close()

    #this is purely here for visual studios so it looks nicer, don't ask. You can delete this if you want
    return file_name

print("Welcome the intervocalic /t/ search.")
print("")

t_file_name = fileNameCheck() #gets file input name

t_open = open(t_file_name, "r") #open input file

t_outfile_name = input("Please enter the name of the file you would to output to: ") #input

t_out_open = open(t_outfile_name, "w+") #open output file

t_word = [] #declare an empty list to hold t word
t_speaker = [] #to hold speaker of t word
t_time = [] #to hold time spoken of t word
t_word_final = [] #declare an empty list to hold final t words
t_speaker_final = [] #to hold final speakers of t word
t_time_final = [] #to hold final times spoken of t word

temp = None #temp value
t_exist = False #value to test if there is a t or not in a word
is_skip_par = False #to see if we skip rest of par
current_speaker = None #value to hold current speaker
l_pos = 0 #value to hold current list posistion, starts at zero
l_count = 0 #counts how many positions were skipped, so it can add in the time

step_flag = 1 #flag to know what line in each entry is

t_lines = t_open.readlines()

for t_line in t_lines:
	if step_flag == 1:
		line_words = list(t_line.split()) #splits line into seperate words

		current_speaker = line_words[0] #gets current speaker from file
		
		if current_speaker == 'F001' or current_speaker == 'D001' or current_speaker == 'Notes' or  current_speaker == 'notes': #checks for father ID or notes
			step_flag = 2 #sets flag to next step
			continue #continues to next line

		is_skip_par = False #sets is_skip_par to false at the start of every new line

		for word in line_words[1:]: #skips first entry in list, iterates through words
			if is_skip_par == True: #if it it a starting par loop through words until end par is found
				for ch in word:
					if ch == '}' or ch == ']': #if finds end par sets skip par to false and breaks out of for loop
						is_skip_par = False
						break	

			else:
				t_exist = False

				for ch in word: #iterates through each char in word
					if ch == 't' or ch == 'T': #checks if char is 't', if it is sets t_exist to true
						t_exist = True
					elif ch == '{' or ch == '[':
						is_skip_par = True
					elif ch == '}' or ch == ']':
						t_exist = False
						is_skip_par = False

				if t_exist == True and is_skip_par == False: #if its true puts t word in list
					t_word.append(word) #sets t_word to current word
					t_speaker.append(current_speaker) #sets t_speaker to current speaker
					l_pos += 1 #increments pos
					l_count += 1 #increments count

		step_flag = 2 #sets flag to next step

	elif step_flag == 2:
		line_words = list(t_line.split()) #splits line into seperate words

		for i in range(0,l_count): #sets t_time to the start time of the entry, does that for however many t words were added
			t_time.append(line_words[0])

		l_count = 0 #sets count back to zero

		step_flag = 3 #sets flag to next step

	elif step_flag == 3:
		step_flag = 1 #sets flag to next step

for i in range(0,len(t_word)):
    t_word[i] = re.sub('[/,.!?;:()<>]+', '', t_word[i]) #uses regex to clean words
    

for i in range(0,len(t_word)):
    is_intervocalic = False #bool to tell if word is intervocalic

    t_test = re.sub('[aeiouy]+', 'V', t_word[i])

    if 'VtV' in t_test: #Test for VtV
        is_intervocalic = True

    if 'VttV' in t_test: #Test for VttV
        is_intervocalic = True

    if 'VtlV' in t_test or 'VttlV' in t_test: #Test for Vtle & Vttle
        is_intervocalic = True

    if 'VghtV' in t_test: #Test for ightV
        is_intervocalic = True

    if 'Vt\'' in t_test: #Test for Vt'
        is_intervocalic = True

    if 'ight\'' in t_test: #Test for ight'
        is_intervocalic = True
    
    if is_intervocalic == True:
        t_word_final.append(t_word[i])
        t_speaker_final.append(t_speaker[i])
        t_time_final.append(t_time[i])

for t in range(0, len(t_word_final)): #outputs file to file
    print("%s, %s, %s\n" % (t_word_final[t], t_speaker_final[t], t_time_final[t]))

for t in range(0, len(t_word_final)): #outputs file to file
    t_out_open.write("%s, %s, %s\n" % (t_word_final[t], t_speaker_final[t], t_time_final[t]))

t_open.close() #closes input file
t_out_open.close() #closes output file

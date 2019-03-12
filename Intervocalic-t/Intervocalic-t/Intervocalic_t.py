#Gabe Johnson
print("Welcome the intervocalic /t/ search.")
print("")

cont = False
while cont is False: #while loop used to get a file from the user that successfully opens

    t_file_name = input("Please enter the name of the file you would like to search: ")
    
    t_open = None

    try:
        t_open = open(t_file_name, "r")
    except IOError:
        print("Could not open file. Please check file path, or use an absolute path.")
    else:
        cont = True

    cont = cont #this is purely here for visual studios so it looks nicer, don't ask. You can delete this if you want

t_lines = t_open.readlines()
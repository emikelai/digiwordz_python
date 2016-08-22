dictionary_list = open(r"C:\Users\mlai.000\Desktop\python_learning\digiwordz\words_filtered.txt", mode="r")
# phone_numbers7 = open(r"phone_numbers2.txt", mode="r")
phone_numbers7 = open(r"3digit_list.txt", mode="r")

# print(dictionary_list.read()) #will print whole file

# key to map letters to each number in the phone number
# 1
# 2 abc
# 3 def
# 4 ghi
# 5 jkl
# 6 mno
# 7 pqrs
# 8 tuv
# 9 wxyz
# 0

def mapping_function(str):
    print(str)
    return
def create_num2letterlist(num2convert):
    num2letterlist = []
    if num2convert == '1':
        num2letterlist = []
    elif num2convert == '2':
        num2letterlist = ["a", "b", "c"]
    elif num2convert == '3':
        num2letterlist = ["d", "e", "f"]
    elif num2convert == '4':
        num2letterlist = ["g", "h", "i"]
    elif num2convert == '5':
        num2letterlist = ["j", "k", "l"]
    elif num2convert == '6':
        num2letterlist = ["m", "n", "o"]
    elif num2convert == '7':
        num2letterlist = ["p", "q", "r", "s"]
    elif num2convert == '8':
        num2letterlist = ["t", "u", "v"]
    elif num2convert == '9':
        num2letterlist = ["w", "x", "y", "z"]
    elif num2convert == '0':
        num2letterlist = []
    else:
        print("Invalid value in phone number!")
    # print("****************************************num2letterlist: ")
    # print_list(num2letterlist)
    return num2letterlist
def print_phone_number(phone_number_list):
    for i in range(len(phone_number_list)):
        print(phone_number_list[i])
def print_list(list):
    for i in range(len(list)):
        print(list[i], end='')
def print_list_nonewline(list):
    for i in range(len(list)):
        print(list[i])

for number in phone_numbers7:
    #chop(number) #remove new line at end of number to get length correct
    print("Finding words for %s " %(number))
    phone_number_list = list(number)  # split each number into an array

    i = 0  # initialize counter that keeps track of number of matches
    match_list = []  # initialize list of mab tches to phone number length
    match_list2 = []  # initialize list of matches that contains final list of matches

    for line in dictionary_list:
        # print(line, end='')
        # print(len(line)-1)  #need to subtract 1 because of newline
        # line_list = list(line)  #turn word into list


        # create single list to keep paring down matches
        # 1. Create list that matches length
        # 2. take result of #1, then match first letter
        # 3. take result of #2, then match second letter
        # 4. etc.
        # 5. return final list of matches to user

        # 1. Create list that matches length
        if len(phone_number_list) == len(line) - 1:  # check if phone number length matches word length
            i = i + 1  # increment counter to keep track of number of matches
            # for i in range(len(line_list)):
            #    print(line_list[i])
            match_list.append(line)
    print("There are %d words in the dictionary list for a phone number with a length of %d." % (i, len(phone_number_list)))

    # print_list(match_list)

    match_list2 = match_list.copy()  # copy list so I can safely remove elements over a list I'm not iterating over
    letter = 0
    i = 0
    j = 0
    # 2. take result of #1, then match first letter, second letter, etc.
    # If first letter matches the first letter in match_list, then do nothing (keep in the list) and try to match
    # second letter, and then third letter, etc.
    # If it doesn't match, remove it from the list.  Continue matching letters for remaining entries in match_list
    for letter in range(len(phone_number_list)):  # only execute the contents of for loop X times where X is the length of the phone number
        # map number to letters
        num2letterlist = create_num2letterlist(phone_number_list[letter])
        # print_list(num2letterlist)
        for line in match_list:
            # print ("Evaluating in match_list: ",line)
            # print("Comparing this phone number digit: ", phone_number_list[letter])
            # print("to this match_list letter", line[letter])
            # if phone_number_list[letter] == line[letter]:   #if digit of phone number matches corresponding position of word in dictionary
            if line[
                letter] in num2letterlist:  # if digit of phone number matches corresponding position of word in dictionary
                # print ("word: ", line, end='')#pass #do nothing, there is a match to the digit in the corresponding position
                i = i + 1
            else:
                # print("Removing this from match_list2: ", line)
                match_list2.remove(line)  # no match so remove from list; need to remove from a copy
                j = j + 1
        match_list = match_list2.copy()  # copy back modified list of deleted items to be iterated for subsequent letters



#print("Number of matching entries: %d." % (i))
#print("Number of deleted entries: %d." % (j))

#print_list(match_list2)
print_list(match_list)

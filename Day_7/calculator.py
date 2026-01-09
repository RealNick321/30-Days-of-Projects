# takes user input 
    # only numbers and certain symbols (^, !, ., /, *, +, -)
    # all else returns input help error message
# main calls operations functions (+, -, etc.)
# proper error handling 
# program cannot end after returning first value, user might want to operate further. Require end command, only allow this string. 

class AlphabeticalInput(Exception):
    """Raised when the user input is alphabetical, but not end"""

def main():
    user_input_cleaning()
    # writing out my problems
        #I want to scan user input to make sure only numbers and certain symbols are entered, and one word (end), if not, retry with error message. 
            #how can I scan this?
                #char by char, if int, no issue, if allowed characters no issue, and if letters only error after a an or of a few conditions
                    #1 1 letter then space
                    #2 2 letters then space
                    #3 3 letters then space that is not "end"
                    #4 letter then number 
                    #5 letter then symbol, even allowed symbol

def user_input_cleaning():
    user_input_clean = False
    end_array = {'e': False, 'n': False, 'd': False}

    while user_input_clean == False:
        try:
            initial = input("Welcome to The Calculator! Available operations include +, -, *, /, ^, and !. Decimals up to 9 places are calculated. You can operate on returned values. Type end to end program. Please enter your desired calculation\n").lower()
            for char in initial:
                char = ord(char)
                if 122 >= char >= 97:
                    if char != 101 and end_array["e"] == False:
                        raise AlphabeticalInput
                    elif char == 101:
                        end_array["e"] = True
                        continue
                    elif char != 110 and end_array["n"] == False:
                        raise AlphabeticalInput
                    elif char == 110:
                        end_array["n"] = True 
                        continue
                    #LEFT OFF HERE
        except AlphabeticalInput:
            print("You have entered letter(s) that is not the end command. Please enter only numbers, allowed symbols, or end.")
            continue
        

def user_input():
    input_string = input("Available operations include +, -, *, /, ^, and !. Decimals up to 9 places are calculated. Please enter your desired calculation\n").lower()
    return input_string



if __name__ == "__main__":
    main()
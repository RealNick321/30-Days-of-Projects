import sys 
# takes user input 
    # only numbers and certain symbols (^, !, ., /, *, +, -)
    # all else returns input help error message
# main calls operations functions (+, -, etc.)
# proper error handling 
# program cannot end after returning first value, user might want to operate further. Require end command, only allow this string. 

class AlphabeticalInput(Exception):
    """Raised when the user input is alphabetical, but not end"""
class NumbandSpaceError(Exception):
    """Raised when user inputs a number, then a space, then a number"""

def main():
    first_input = user_input_cleaning()
    print(first_input)

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
    first_input = []
    space_detected = False
    second_term_flag = False
    second_number = []
    operator = 0 


    while user_input_clean == False:
        try:
            initial = input("Welcome to The Calculator! Available operations include +, -, *, /, ^, and !. Decimals up to 9 places are calculated. You can operate on returned values. Type end to end program. Please enter your desired calculation\n").lower()
            for i, char in enumerate(initial):
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
                    elif char != 100 and end_array["d"] == False:
                        raise AlphabeticalInput
                    elif char == 100:
                        end_array["d"] == True
                        sys.exit()
                if 57 >= char >= 48 and second_term_flag == False:
                    if ord(initial[i - 1]) == 32 and 57 >= initial[i - 2] >= 48:
                        raise NumbandSpaceError
                    first_input.append(chr(char))
                    continue
                if char == 32:
                    if 57 >= ord(initial[i - 1]) >= 48:
                        if second_term_flag == True:
                            print("Max of 2 terms to operate on for now")
                            break
                        space_detected = True
                        continue
                    if space_detected == True and second_term_flag == False:
                        user_input_clean = True
                        print("Two spaced detected after numeric entry. Numeric entry saved. Type operation to perform on such number. If user was in-process of typing out full operation using double space format, type end and conform to single space moving forward.")
                        return first_input
                if ord(initial[i - 1]) == 32 and char == 43 or char == 47 or char == 42 or char == 45:
                    second_term_flag = True
                    operator = char
                    continue
                if ord(initial[i - 1]) == 32 and second_term_flag == True and 57 >= char >= 48:
                    second_number.append(chr(char))
                    continue
                if 57 >= char >= 48:
                    second_number.append(chr(char))
                    continue
            user_input_clean = True
        except AlphabeticalInput:
            print("You have entered letter(s) that is not the end command. Please enter only numbers, allowed symbols, or end.")
            continue
        except NumbandSpaceError:
            print("You have entered a number, then a space, then a number without an operating symbol (+, -, /, *) between them. Please try again")
            continue
    first_int = int("".join(map(str, first_input)))
    second_int = int("".join(map(str, second_number)))
    if operator == 43:
        answer = first_int + second_int
    return answer

        

def user_input():
    input_string = input("Available operations include +, -, *, /, ^, and !. Decimals up to 9 places are calculated. Please enter your desired calculation\n").lower()
    return input_string



if __name__ == "__main__":
    main()
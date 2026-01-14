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
class SymbolError(Exception):
    """Raised when user inputs improper symbols"""
    

def main():
    answer = user_input_cleaning()
    print(answer)


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
                    elif char == 101 and end_array["e"] == True:
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
                    if ord(initial[i - 1]) == 32 and 57 >= ord(initial[i - 2]) >= 48:
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
                if 47 >= char >= 33 or 96 >= char >= 91 and i == 0:
                    raise SymbolError
            if len(initial) == 1 and 122 >= ord(initial) >= 97:
                raise AlphabeticalInput
            user_input_clean = True
        except AlphabeticalInput:
            print("You have entered letter(s) that is not the end command. Please enter only numbers, allowed symbols, or end.")
            continue
        except NumbandSpaceError:
            print("You have entered a number, then a space, then a number without an operating symbol (+, -, /, *) between them. Please try again")
            continue
        except SymbolError:
            print("You have entered improper symbols. Please try again.")
            continue
    return first_input, second_number

        

def user_input():
    input_string = input("Available operations include +, -, *, /, ^, and !. Decimals up to 9 places are calculated. Please enter your desired calculation\n").lower()
    return input_string



if __name__ == "__main__":
    main()




#list of bugs:
    """type e alone or in multiple successive inputs then type end and it will infi loop alphabeticalinput error
    type en will go through entire program and print of empty supposed to be number list will occur
    typing a number then space then an allowed operator sign
    Prompts to enter values after the first prompt still contains Welcome to The Calculator!
      """
#things that are handled properly:
    """typing random letters will return helpful instructions. Typing end after such error exits successfully. 
    typing end will exit program
    if a user types a two numbers seperated by 2 spaces without an operator sign, a specific error is returned
    typing numbers then a space then letters still returns alphabetical error
    If user enters symbols in beginning of prompt, symbol error is returned
    """
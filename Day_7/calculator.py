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
    """Raised when user inputs symbols at beginning of prompt"""

Global_Vars = {
    "first_input_recieved_flag": False,
    "user_input_clean": False,
    "end_array": {'e': False, 'n': False, 'd': False},
    "first_term": [],
    "space_detected": False,
    "second_term_flag": False,
    "second_term": [],
    "operator": 0,
    "letter": True,
    "number": False,
}
    

def main():
    first, second = user_input_cleaning()
    first, second = list_to_string(first, second)


def user_input_cleaning():
    while Global_Vars["user_input_clean"] == False:
        try:
            user_string = user_input_message()
            for i, char in enumerate(user_string):
                char = ord(char)
                letter_detector(char)
                number_detector(char)
                if Global_Vars["letter"] == True:
                    letter_handling(char)
                NumberandSpaceError(i, char, user_string)
                FirstTermBuilding(char)
                if Space_Detected(char):
                    if Max2Terms(i, char, user_string):
                        break
                    if LastCharNumber(i, user_string):
                        if space_detected_flag():
                            continue
                    TwoSpacesHandling()
                if ord(user_string[i - 1]) == 32 and char == 43 or char == 47 or char == 42 or char == 45:
                    Global_Vars["second_term_flag"]= True
                    operator = char
                    continue
                if ord(user_string[i - 1]) == 32 and Global_Vars["second_term_flag"] == True and number_detector:
                    Global_Vars["second_term"].append(chr(char))
                    continue
                if 57 >= char >= 48:
                    Global_Vars["second_term"].append(chr(char))
                    continue
                if 47 >= char >= 33 or 96 >= char >= 91 and i == 0:
                    raise SymbolError
            if len(user_string) == 1 and 122 >= ord(user_string) >= 97:
                raise AlphabeticalInput
            Global_Vars["user_input_clean"] = True
        except AlphabeticalInput:
            print("You have entered letter(s) that is not the end command. Please enter only numbers, allowed symbols, or end.")
            continue
        except NumbandSpaceError:
            print("You have entered a number, then a space, then a number without an operating symbol (+, -, /, *) between them. Please try again")
            continue
        except SymbolError:
            print("You have entered symbols at the beginning of your prompt. Please try again.")
            continue
    return Global_Vars["first_term"], Global_Vars["second_term"]

        

def user_input_message():
    if Global_Vars["first_input_recieved_flag"] == False:
        input_string = input("Welcome to The Calculator! Available operations include +, -, *, /, ^, and !. Decimals up to 9 places are calculated. You can operate on returned values. Type end to end program. Please enter your desired calculation\n").lower()
        return input_string
    else:
        post_first_string = input("Available operations include +, -, *, /, ^, and !. Decimals up to 9 places are calculated. Please enter your desired calculation\n").lower()
        return post_first_string

def list_to_string(first, second):
    first = int("".join(map(str, first)))
    print(first)
    return first, second 

def letter_detector(char):
    if 122 >= char >= 97:
        Global_Vars["letter"] = True
        return 

def number_detector(char):
    if 57 >= char >= 48:
        Global_Vars["number"] = True
        Global_Vars["letter"] = False
        return 

def letter_handling(char):
    if char != 101 and Global_Vars["end_array"]["e"] == False:
        raise AlphabeticalInput
    elif char == 101 and Global_Vars["end_array"]["e"] == True:
        raise AlphabeticalInput
    elif char == 101:
        Global_Vars["end_array"]["e"]  = True
        return
    elif char != 110 and Global_Vars["end_array"]["n"]  == False:
        raise AlphabeticalInput
    elif char == 110:
        Global_Vars["end_array"]["n"]  = True 
        return
    elif char != 100 and Global_Vars["end_array"]["d"]  == False:
        raise AlphabeticalInput
    elif char == 100:
        Global_Vars["end_array"]["d"] == True
        sys.exit()
    
def NumberandSpaceError(i, char, user_string):
    if 57 >= char >= 48 and Global_Vars["second_term_flag"] == False:
        if ord(user_string[i - 1]) == 32 and 57 >= ord(user_string[i - 2]) >= 48:
            raise NumbandSpaceError

def FirstTermBuilding(char):
    if 57 >= char >= 48 and Global_Vars["second_term_flag"] == False:
        Global_Vars["first_term"].append(chr(char))

def Max2Terms(i, char, user_string):
    if LastCharNumber(i, user_string):
        if Global_Vars["second_term_flag"] == True:
            print("Max of 2 terms to operate on for now")
            return True

def Space_Detected(char):
    if char == 32:
        return True

def LastCharNumber(i, user_string):
    if 57 >= ord(user_string[i - 1]) >= 48:
        return True
    else:
        return False 

def space_detected_flag():
    if Global_Vars["second_term_flag"] == False:
        Global_Vars["space_detected"] = True
        return True

def TwoSpacesHandling():
    if Global_Vars["space_detected"] == True and Global_Vars["second_term_flag"] == False:
        Global_Vars["user_input_clean"]= True
        print("Two spaces detected after one numeric entry. Numeric entry saved. Type operation to perform on such number. If user was in-process of typing out full operation using double space format, type end and conform to single space moving forward.")
        return Global_Vars["first_term"] 


if __name__ == "__main__":
    main()




#list of bugs:
    """type e alone or in multiple successive inputs then type end and it will infi loop alphabeticalinput error
    type en will go through entire program and print of empty supposed to be number list will occur
    typing a number then space then an allowed operator sign
    Prompts to enter values after the first prompt still contains Welcome to The Calculator!
    typing a number then space then operator sign then space then a number yields two spaces error.
      """
#things that are handled properly:
    """typing random letters will return helpful instructions. Typing end after such error exits successfully. 
    typing end will exit program
    if a user types a two numbers seperated by 2 spaces without an operator sign, a specific error is returned
    typing numbers then a space then letters still returns alphabetical error
    If user enters symbols in beginning of prompt, symbol error is returned
    """
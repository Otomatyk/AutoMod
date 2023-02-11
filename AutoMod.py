from re import search, sub, match

def Clean(message):
    message = sub("[\&\\#\(\[\-\|\_\\\\^\@\)\]\=\}\/\*\-\+\.\!\:\;\,\?\.\§\%]+", "", message)
    message = message.lower()
    
    return message

#Repeated characters
def Repeated_characters_in(message):
    if search(LIMITE_REPEATED_CHARACTERS, message):
        return True
    else:
        return False

def Set_max_repeated_characters(max_):
    if type(max_) != int:
        print("Max_ must be an int")
    else:
        LIMITE_REPEATED_CHARACTERS = ".{0,"+str(max_)+"}"

#Ban words
def Ban_words_in(message):
    message = message.lower()
    message = message.split()
    
    for mot in message:
        for i,mot_banni in enumerate(BANED_WORDS):
            if len(mot) >= len(CLEAN_BAN_WORDS[i])//2 and match(mot_banni, mot) and mot not in AUTORHISED_WORDS:
                return True
    
    return False

def Get_ban_words():
    return CLEAN_BAN_WORDS
    
def Add_ban_word(word, max_noise=4):  
    if type(word) != str:
        print("The word must be a string")
        
    elif type(max_noise ) != int:
        print("Max_noise must be an int")

    else:
        word = word.lower()
        not_ = "[^"+word+"]"
        new_word = ""
        for i,char in enumerate(word):
            if i == 0 or i == len(new_word)-1:
                new_word += char+"{1,10}"+not_+"{0,"+str(max_noise)+"}"
            else:
                if char in "aeyuio":
                    char = "[a-y]"
                new_word += "([^a-zA-Z]|"+char+"){1,10}"+not_+"{0,"+str(max_noise)+"}"

        new_word = new_word[:-12]
        
        BANED_WORDS.append(new_word)
        CLEAN_BAN_WORDS.append(word)
    
def Del_ban_word(word):
    if word not in CLEAN_BAN_WORDS:
        print("The word must be in the list")
        
    elif type(word) != str:
        print("The word must be a string")

    else:
        index = CLEAN_BAN_WORDS.index(word)
        del CLEAN_BAN_WORDS[index]
        del BANED_WORDS[index]

#Autorhised words
def Get_autorhised_words():
    return AUTORHISED_WORDS

def Add_autorhised_word(word):
    if type(word) != str:
        print("The word must be a string")
    else:
        AUTORHISED_WORDS.append(word)
def Del_ban_word(word):
    if word not in CLEAN_BAN_WORDS:
        print("The word must be in the list")

    elif type(word) != str:
        print("The word must be a string")
        
    else:
        AUTORHISED_WORDS.remove(word)

LIMITE_REPEATED_CHARACTERS = ""

BANED_WORDS = []
AUTORHISED_WORDS = []

CLEAN_BAN_WORDS = []

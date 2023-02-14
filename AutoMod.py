from re import search, sub, compile

def Clean_message(message) -> str:
    message = sub("[^a-zA-Z0-9\s]", "", message)#sub("[\&\\#\(\[\-\|\_\\\\^\@\)\]\=\}\/\*\-\+\.\!\:\;\,\?\.\§\%]+", "", message)
    message = message.lower()
    
    return message

#Repeated characters
def Repeated_characters_in(message) -> bool:
    if search(LIMITE_REPEATED_CHARACTERS, message):
        return True
    else:
        return False

def Set_max_repeated_characters(max_) -> None:
    if type(max_) != int:
        print("Max_ must be an int")
    else:
        LIMITE_REPEATED_CHARACTERS = ".{0,"+str(max_)+"}"

#Ban words

def Banned_words_in(message) -> (int, list):
    "Return the count of banned words and the words found in"
    message = sub("\s", "", message)
    message = message.lower()
    
    count = 0
    words = []
    
    for mot_banni in BANNED_WORDS:
        trouve = search(mot_banni, message)
        if trouve != None:
            
            trouve = message[trouve.start():trouve.end()]
            claire = CLEAN_BANNED_WORDS[BANNED_WORDS.index(mot_banni)]
            
            if trouve not in AUTORHISED_WORDS and len(trouve) >= len(claire)//2:
            
                count += 1
                words.append((claire, trouve))

    return (count, words)

def Blur_banned_words_in(message) -> str:
    "Return the message but with the blured banned words "
    nouveau_message = message
    
    message = sub("\s", "", message)
    message = message.lower()
    
    for mot_banni in BANNED_WORDS:
        trouve = search(mot_banni, message)
        if trouve != None:
            
            debut,fin = trouve.start(),trouve.end()
            trouve = message[debut:fin]
            claire = CLEAN_BANNED_WORDS[BANNED_WORDS.index(mot_banni)]
            
            if trouve not in AUTORHISED_WORDS and len(trouve) >= len(claire)//2:
                nouveau_message = nouveau_message[:debut]+(HIDE_CHARACTER*(fin-debut))+nouveau_message[fin:]
        
    return nouveau_message
    
def Get_banned_words() -> list:
    return CLEAN_BANNED_WORDS

def Set_hide_character(char) -> None:
    HIDE_CHARACTER = char

def Add_banned_word(word, max_noise=6) -> None:  
    if type(word) != str:
        print("The word must be a string")
        
    elif type(max_noise ) != int:
        print("Max_noise must be an int")

    else:
        max_noise = str(max_noise)
        word = word.lower()
        not_ = "[^"+word+"]"
        new_word = ""
        
        for i,char in enumerate(word):
            if i == 0 or i == len(word)-1:
                new_word += "(\*|"+char+"){1,}"+not_+"{0,"+max_noise+"}"
            else:
                new_word += char+"{0,}"+not_+"{0,"+max_noise+"}"
                
        new_word = new_word[:-12]
        
        BANNED_WORDS.append(compile(new_word))
        CLEAN_BANNED_WORDS.append(word)
    
def Del_banned_word(word) -> None:
    if word not in CLEAN_BANNED_WORDS:
        print("The word must be in the list")
        
    elif type(word) != str:
        print("The word must be a string")

    else:
        index = CLEAN_BANNED_WORDS.index(word)
        del CLEAN_BANNED_WORDS[index]
        del BANNED_WORDS[index]

#Autorhised words
def Get_autorhised_words() -> list:
    return AUTORHISED_WORDS

def Add_autorhised_word(word) -> None:
    if type(word) != str:
        print("The word must be a string")
    else:
        AUTORHISED_WORDS.append(word)
        
def Del_autorhised_word(word) -> None:
    if word not in CLEAN_BANNED_WORDS:
        print("The word must be in the list")

    elif type(word) != str:
        print("The word must be a string")
        
    else:
        AUTORHISED_WORDS.remove(word)

LIMITE_REPEATED_CHARACTERS = ""

HIDE_CHARACTER = "*"

BANNED_WORDS = []
AUTORHISED_WORDS = []

CLEAN_BANNED_WORDS = []

Add_banned_word("fuck")

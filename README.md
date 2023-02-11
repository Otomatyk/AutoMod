# AutoMod
The AutoMod Python library, for filtering messages with strong words

-------------

Documentation :

  Clean(message) -> str:
  
  It deletes non-letter character like @^$*%/*-+ .
  Used for more faster reading when moderating messages
  
  Repeated characters :
  
    Repeated_characters_in(message) -> bool:
  
    Returns if the message contains reapeated characters, like : heeeeeelllloooo
  
  
    Set_max_repeated_characters(max_) -> None:
  
    Set the limit for Repeated_characters_in()
  
  Ban words :
  
    Ban_words_in(message) -> bool:
      Returns if a baned word is in the message
      
    Get_ban_words() -> list of str:
      
      Returns the human-readeable list of ban words
    
    
    Add_ban_word(word, max_noise) -> none:
      
      Create a regular expression and appends it to the list
      max_noise is the maximum number of undesirable characters can put between two characters of the ban word, example :
        With Add_ban_word("fuck", 1), "f_u_c_k" is detected but not with "f12u86c=_k" 

    Del_ban_word(word) -> None:
      Deletes a ban word of the list
  
  Autorhised words :
    
    If you want to some words won't be detected you can use those functions :
      Get_autorhised_words() -> list of string
      Add_autorhised_word(word) -> None
      Del_ban_word(word) -> None

You could give a star if you like/use it !

If you have a suggestion or a question you can contact me on gmail@otomatyk.com

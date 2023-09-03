import random

def get_responses(message: str) -> str:
    p_message = message.lower()#processed

    if p_message == "hello":
        return "Wag2. "

    if p_message == "roll":
        return str(random.randint(1,6))
    
    if p_message == "!help":
        return "`Idk how to help. charge it.`"
    
    return 'I didn\'t understand what you wrote. Try typing "!help".'

def daddy_responses(messaage: str) -> str:
    #dw bout it
    pass
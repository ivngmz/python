def sentence_marker(phrase):
    question_words=("how","what","why")
    if phrase.startswith(question_words) or phrase.endswith("?"):
        print("Yes, it seems to be a question")
        capitalized = phrase.capitalize()
        if capitalized.endswith("?"):
            return "This is the question: {}".format(capitalized)
        else:
            return "This is the question: {}?".format(capitalized)
    else:
        print("No, I'm sure you are not making correctly the question try again")
        while not (phrase.startswith(question_words) or phrase.endswith("?")):
            phrase=input("Write below again, please, I will say yo if it is a question\n")
            sentence_marker(phrase)
        capitalized = phrase.capitalize()
        if capitalized.endswith("?"):
            return "This was the question, i was hard to you to resolve the puzzle...: {}".format(capitalized)
        else:
            return "This was the question, i was hard to you to resolve the puzzle...: {}?".format(capitalized)
        
            
        
print("Hi, another program, Could you please make me a question??")
print(sentence_marker(input("Write below, please, I will say yo if it is a question\n")))
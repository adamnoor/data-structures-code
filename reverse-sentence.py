def reverse_sentence(sentence):
    all_words = []
    count = 0
    word = ""
    while count < len(sentence):
        
        if(sentence[count] == " "):
            all_words.append(word)
            word = ""
                
        else:
            word = word + sentence[count]
            if(count == len(sentence)- 1):
                all_words.append(word)
            
        count += 1

    for i in range(0, len(all_words)//2):
        temp = all_words[i]
        all_words[i] = all_words[~i]
        all_words[~i] = temp

    print(all_words)

reverse_sentence("Bob Likes Mary")

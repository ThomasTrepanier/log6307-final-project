def sms_encoding(data):

    vowels = set("aeiouAEIOU")
    
    words = data.split()
    
    encoded_words = []
    
    for i in range(0,len(words)):
        vow_count = 0
        cons_word = []
        for x in words[i]:
            if x in vowels:
                vow_count =vow_count+1
            elif x not in vowels:
                cons_word.append(x)
        if vow_count == len(words[i]):
            encoded_words.append(words[i])
        elif vow_count != len(words[i]):
            encoded_words.append("".join(cons_word))

 
    encoded_msg = " ".join(encoded_words)
    
    return encoded_msg

data=input("Kindly enter your message for sms encoding : ")

print(sms_encoding(data))

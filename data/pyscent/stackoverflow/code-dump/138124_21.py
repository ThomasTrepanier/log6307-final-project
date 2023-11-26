def sms_encoding(new_s):
    encrypt_string = []
    consonant_list = []
    vowel_set = set("aeiouAEIOU")

    for word in range(0, len(new_s)):
        v_letter = new_s[word]
        if  v_letter in vowel_set:
            encrypt_string.append(v_letter)

        for letter in v_letter:
            if letter not in vowel_set:
                consonant = " ".join(letter)
                encrypt_string.append(consonant)
        encrypt_string.append(" ")     
       
    encrypt_string = "".join(encrypt_string)
    print(encrypt_string)

s = input("Enter a string ")
new_s = s.split()           
sms_encoding(new_s)

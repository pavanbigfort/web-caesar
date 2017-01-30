import string
def alphabet_position(letter) :

        if letter in string.ascii_lowercase :
                x=(ord(letter)%97)
        if letter in string.ascii_uppercase :
                x=(ord(letter)%65)
        return(x)



def rotate_character(char, rot) :
    if char in string.ascii_lowercase or char in string.ascii_uppercase :
        y= (alphabet_position(char)+int(rot))%26
    if char in string.ascii_lowercase :
         return(chr(y+97))
    elif char in string.ascii_uppercase :
            return(chr(y+65))
    return(char)

def encrypt(text, rot) :
    i=0
    rot_str=''
    while i<len(text) :
        rot_str=rot_str+rotate_character(text[i],rot)
        i+=1
    return (rot_str)

def anagrams(str1, str2):
    #Removes spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    #check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False
    
    #sort the characters of both strings and compare them
    return sorted(str1) == sorted(str2)

# Example
string1 = "listen"
string2 = "silent"

print(anagrams(string1, string2))
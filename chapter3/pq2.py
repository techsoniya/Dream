# Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> '''


# name=input("Enter your name: ")
# date=input("Enter the date : ")
# print(f"Dear {name},\nYou are selected!\n{date}")


name=input("Enter your name: ")
date=input("Enter the date : ")
letter = '''Dear <|Name|>, 
            You are selected! 
<|Date|> '''

# print(letter.replace("<|Name|>","Soniya").replace("<|Date|>","05 May 2003"))
print(letter.replace("<|Name|>",name).replace("<|Date|>",date))

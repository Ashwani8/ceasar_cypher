alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(p_text, p_shift):
    encrypted_message =""
    for letter in p_text:
      if letter == " ":
        encrypted_message += " "
      # find index conrresponding to letter in the provided text
      else:
        position = alphabet.index(letter)
        # change the index location in alphabet list by the provided shift amount
        new_position = position + p_shift
        # since we have alphabet index upto 25, so we need to start over for letters having index more than 25
        if new_position >25:
          new_position -=25
        new_letter = alphabet[new_position]
        encrypted_message = encrypted_message + new_letter
    print(f" The encrypted message is : \n {encrypted_message}")
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
def decrypt(p_text, p_shift):
    encrypted_message =""
    for letter in p_text:
      if letter == " ":
        encrypted_message += " "
      # find index conrresponding to letter in the provided text
      else:
        position = alphabet.index(letter)
        # change the index location in alphabet list by the provided shift amount
        new_position = abs(position - p_shift)
        # since we have alphabet index upto 25, so we need to start over for letters having index more than 25
        new_letter = alphabet[new_position]
        encrypted_message = encrypted_message + new_letter
    print(f" The decrypted message is : \n {encrypted_message}")
if direction == "encode":
  encrypt(p_text=text, p_shift= shift)
elif direction == "decode":
  decrypt(p_text=text, p_shift= shift)
##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def EncDec(Direction,Test,Shift):
    while Direction != 'decode' and Direction !='encode':
      Direction =input("Type 'encode' or 'decode' please\n")
    new_test =""
    Shiftint =int(Shift)
      
    if Direction == 'decode':
      Shiftint *=-1

    for character in Test:
      if character in alphabet:
        position =alphabet.index(character)
        new_position =position + Shiftint
        
        while new_position>25:
          new_position =new_position-25
        while new_position<0:
          new_position =new_position+25
      
        new_character =alphabet[new_position]
        new_test +=new_character
      else:
        new_test +=character
    print(new_test)
    

answer =True
response ='idk'
while answer:
  direction =input("Type 'encode' to encrypt, or 'decode' to decrypt:\n")
  test =input("Type your message:\n")
  shift =input("Type the shift number:\n")
  EncDec(direction,test,shift)

  response =input("Do you want to Encode/Decode again? Answer Yes or No\n")
  response =response.lower()

  
  if response =='no':
    answer =False
  elif response =='yes':
    answer =True
  else:
    while response !='yes' and response !='no':
      response =input("Do you want to Encode/Decode again? Answer Yes or No\n")
      response =response.lower()
      
      if response =='no':
        answer =False
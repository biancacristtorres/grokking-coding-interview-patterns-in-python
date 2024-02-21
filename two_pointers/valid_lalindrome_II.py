def is_palindrome(sentence):
  left = 0
  right = len(sentence)-1
  skip=0

  while left != right:
    if sentence[left] == sentence[right]:
        left+=1
        right-=1
    if sentence[left] != sentence[right]:     
       right-=1
       skip

    if skip > 1:
       return False

    left+=1
    right-=1   
      

  return True


print(is_palindrome("madame"))
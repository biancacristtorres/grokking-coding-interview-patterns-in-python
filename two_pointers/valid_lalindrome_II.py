def is_palindrome(sentence):
  left = 0
  right = len(sentence)-1
  skip=0

  while left < right:
    if sentence[left] == sentence[right]:
        left+=1
        right-=1
        l = sentence[left]
        r = sentence[right]
    else:
       if sentence[left] != sentence[right] and skip < 1:     
            left+=1
            last_left=left
            if sentence[left] != sentence[right]:
                left-=1
                right-=1
                skip+=1
                l = sentence[left]
                r = sentence[right]
       else:
         return False        
    
  return True


print(is_palindrome("abcdedadedecba"))
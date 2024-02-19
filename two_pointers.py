def is_palindrome(array):
  left = len(array)
  right = -1
  for letter in (array):
    if left - right !=0:
      if letter == array[right]:
        left+=1
        right-=1
      else:
        return False  
  return True

result = is_palindrome("ABCDABCD")
print(result)

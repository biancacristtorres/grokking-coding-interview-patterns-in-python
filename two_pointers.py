def is_palindrome(array):
  left = 0
  right = len(array) - 1

  while left <= right:
    if array[left] != array[right]:
      return False

    left+=1
    right-=1 
  return True

result = is_palindrome("kayak")
print(result)

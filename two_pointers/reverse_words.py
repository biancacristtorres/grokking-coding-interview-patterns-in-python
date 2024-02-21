def reverse_words(sentence):

   sentence = list(sentence)

   sentence.reverse()
   print(sentence)
   start = 0
   end = 0

   while end < len(sentence):
        if sentence[end] == ' ':
            while sentence[end+1] == ' ':
                sentence.pop(end)
            count = end -1
            while count >= start:
                sentence[start], sentence[count] = sentence[count], sentence[start]
                start+=1
                count-=1
            start = end +1
        end+=1

        if end == len(sentence) -1:
            count = end
            while count >= start:
                sentence[start], sentence[count] = sentence[count], sentence[start]
                start+=1
                count-=1

   return ''.join(sentence)


text = "  To be or not  to be  "
print(text)
print("Resultado: " + reverse_words(text.strip()))


text2 = '      Bianca    Torres   '

print(text2.strip())






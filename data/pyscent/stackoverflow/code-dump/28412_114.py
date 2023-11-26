def getn(w):
   ans = []
   section = ''

   if w[0].isdigit():
       last = 'digit'
   else:
       last = 'letter'

   for char in w:
       if char.isdigit():
           if last == 'letter':
               ans.append(section)
               section = ''
               last = 'digit'
           section += char
       else:
           if last == 'digit':
               ans.append(section)
               section = ''
               last = 'letter'
           section += char
   ans.append(section)

   for index, section in enumerate(ans):
       if section.isdigit():
           ans[index] = section[::-1]
   return ''.join(ans)

string = 'abc123abc456abc7891'
print(getn(string))

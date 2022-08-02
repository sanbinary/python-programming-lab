import os
import platform
# class for using this function
class LOP():
    def __init__(self,number):
        self.number = number

    def lop(self):
        return """
1. Write a Python program to count the number of even/odd numbers in a given list.

2. Write a Python program to calculate the number of digits and letters in a given text. 

3. Write a Python program to check the validity of a password validation:

    a. At least 1 letter between [a-z] and 1 letter between [A-Z].

    b. At least 1 number between [0-9].

    c. At least 1 character from [$#@].

    d. Minimum length 6 characters.

    e. Maximum length 16 characters. 

4. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish. 

5. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 

6. Write a Python program to calculate the Fibonacci series using while loop.

7. Write a python program to find the factorial of a given number using recursion function.

8. Write a python program to implement the binary search algorithm. 

9. Write a python program to find the most frequent words in a text read from a file.

10. Write a python program to perform the matrix addition, subtraction and multiplication."""

class Aim(LOP):
    def aim(self):
        match self.number:
            case 1: return """  Write a Python program to count the number of even/odd numbers in a given list."""
            case 2: return """  Write a Python program to calculate the number of digits and letters in a given text."""
            case 3: return """  Write a Python program to check the validity of a password validation:

    a. At least 1 letter between [a-z] and 1 letter between [A-Z].

    b. At least 1 number between [0-9].

    c. At least 1 character from [$#@].

    d. Minimum length 6 characters.

    e. Maximum length 16 characters."""
            case 4: return """  Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish."""
            case 5: return """  Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters."""
            case 6: return """  Write a Python program to calculate the Fibonacci series using while loop."""
            case 7: return """  Write a python program to find the factorial of a given number using recursion function."""
            case 8: return """  Write a python program to implement the binary search algorithm."""
            case 9: return """  Write a python program to find the most frequent words in a text read from a file."""
            case 10: return """  Write a python program to perform the matrix addition, subtraction and multiplication."""
class Algorithm(Aim):
    def algorithm(self):
        match self.number:
            case 1: return '  coming soon'
            case 2: return '  coming soon'
            case 3: return '  coming soon'
            case 4: return '  coming soon'
            case 5: return '  coming soon'
            case 6: return '  coming soon'
            case 7: return '  coming soon'
            case 8: return '  coming soon'
            case 9: return '  coming soon'
            case 10: return '  coming soon'
class Program(Algorithm):
    def one(self, l):
        odd, even = 0, 0
        for i in l:
            if i%2==0: even+=1
            else: odd+=1
        return odd, even
    def two(self, s):
        digits, letters = 0, 0
        for i in s:
            if i.isdigit(): digits+=1
            elif i.isalpha(): letters+=1
            else: pass
        return digits, letters
    def three(self, s):
        b = True
        option = None
        l = []
        while True:
            if not any(s.islower() for s in s): b = False; option = 'a'; break
            elif not any(s.isupper() for s in s): b = False; option = 'b'; break
            elif not any(s.isdigit() for s in s): b = False; option = 'c'; break
            elif not any(s in ['$','#','@'] for s in s): b = False; option = 'd'; break
            elif len(s) < 6: b = False; option = 'e'; break
            elif len(s) > 16: b = False; option = 'f'; break
            else: break
        if b: return "Valid Password", option
        else: return "Invalid Password", option
    def four(self, i):
        count, sum = 0, 0
        if i != 0: 
            sum+=i
            count+=1
        while i !=0:
            while True:
                try:
                    i = int(input('  Enter the number (0 to finish): ')); break
                except: print('\n  Invalid Input (e.g. 1 or 2 or 3 etc.)\n')
            sum = sum+i
            count+=1
        if count == 0:
            return 0, 0
        else: return sum, sum/(count-1)
    def five(self, s):
        upper, lower = 0, 0
        for i in s:
            if i.isupper(): upper+=1
            elif i.islower: lower+=1
            else: pass
        return upper, lower
    def six(self, i):
        x, y, l = 0, 1, []
        while y <= i:
            l.append(y)
            x, y = y, x+y
        return str(l)[1:-1]
    def seven(self, i):
        if i == 1: return 1
        else: return i * (self.seven(i-1))
        
    def eight(self, l, i):
        low, high = 0, len(l)-1
        b = False
        while(low <= high and not b):
            mid = (low + high)//2
            if l[mid] == i:
                b = True
            else:
                if i < l[mid]:
                    high = mid - 1
                else: 
                    low = mid + 1
        return b, mid, low, high


    def nine(self, s):
        file = open("text.txt", 'w')
        file.write(s)
        file = open("text.txt", 'r')
        word = " "
        freq = 0
        words = []
        for line in file:
            splitted_words = line.replace(',',' ').replace('.',' ').split(" ")
            for w in splitted_words:
                words.append(w)
        for i in range(0, len(words)):
            count = 1
            for j in range(i+1, len(words)):
                if words[i] == words[j]:
                    count+=1
            if(count>freq):
                freq = count
                word = words[i]
        file.close()
        os.remove('text.txt')
        return word, freq
        
    def ten(self, r, c):
        mat, rix = [], []
        rows, columns = r, c
        print()
        while rows > 0:
            rows-=1
            while True:
                try:
                    l =  list(map(int,input('  Enter the row for the first matrix (separated by spaces): ').split(" ")))
                    if len(l) != r: raise ValueError(); break
                    else: mat.append(l); break
                except: print('\n  Invalid Input (e.g. 1 2 3 etc.)\n')
        rows = r
        while rows > 0:
            rows-=1
            while True:
                try:
                    l =  list(map(int,input('  Enter the row for the second matrix (separated by spaces): ').split(" ")))
                    if len(l) != r: raise NameError(); break
                    else: rix.append(l); break
                except NameError: print('\n  Invalid Input (column limit is {})\n'.format(c))
                except ValueError: print('\n  Invalid Input (e.g. 1 2 3 etc.)\n')
        rows = r
        result = []
        for i in range(rows):
            row = []
            for j in range(c):
                row.append(0) 
            result.append(row)
        while True:
            print('\n[1 - addition | 2 - subtraction | 3 - multiplication | e - exit]\n')
            operation = input('Select operation: ')
            if operation == '1':
                print('\nOutput:\n')
                for i in range(r):
                    for j in range(c):
                        result[i][j] = mat[i][j] + rix[i][j]
                for ii in result:
                    print('  {}'.format(''.join(str(ii).split(','))[1:-1]))
            elif operation == '2':
                print('\nOutput:\n')
                for i in range(r):
                    for j in range(c):
                        result[i][j] = mat[i][j] - rix[i][j]
                for ii in result:
                    print('  {}'.format(''.join(str(ii).split(','))[1:-1]))
            elif operation == '3':
                print('\nOutput:\n')
                for i in range(r):
                    for j in range(c):
                        result[i][j] = mat[i][j] * rix[i][j]
                for ii in result:
                    print('  {}'.format(''.join(str(ii).split(','))[1:-1]))
            elif operation.lower() == 'e': break
            else: print('\nInvalid Input')
    
    def programs(self):
        match self.number:
            case 1: return '''  odd, even = 0, 0
  for i in l:
      if i%2==0: even+=1
      else: odd+=1
  print('Number of odd numbers: {}\\nNumber of even numbers: {}'.format(odd,even))'''
            case 2: return '''  digits, letters = 0, 0
  s = str(input('Enter the text: '))
  for i in s:
      if i.isdigit(): digits+=1
      elif i.isalpha(): letters+=1
      else: pass
  print('Number of digits: {}\\nNumber of letters: {}'.format(digits,letters))'''
            case 3: return '''  b = True
  s = str(input('Enter the password: '))
  while True:
      if not any(s.islower() for s in s): b = False; break
      elif not any(s.isupper() for s in s): b = False; break
      elif not any(s.isdigit() for s in s): b = False; break
      elif not any(s in ['$','#','@'] for s in s): b = False; break
      elif len(s) < 6: b = False; break
      elif len(s) > 16: b = False; break
      else: break
  if b: print('Valid Password')
  else: print('Invalid Password')'''
            case 4: return '''  count, sum = 0, 0
  i = int(input('Enter the number (0 to finish): '))
  if i != 0: 
      sum+=i
      count+=1
  while i !=0:
      i = int(input('  Enter the number (0 to finish): '))
      sum = sum+i
      count+=1
  if count == 0:
      print('Sum of the above numbers: 0\\nAverage of the above numbers: 0')
  else: print('Sum of the above numbers: {}\\nAverage of the above numbers: {}'.format(sum, sum/(count-1)))'''
            case 5: return '''  upper, lower = 0, 0
  s = str(input('Enter the text: '))
  for i in s:
      if i.isupper(): upper+=1
      elif i.islower: lower+=1
      else: pass
  print('Number of upper case letters: {}\\nNumber of lower case letters: {}'.format(upper, lower))'''
            case 6: return '''  x, y, l = 0, 1, []
  i = int(input('Enter the number: '))
  while y <= i:
      l.append(y)
      x, y = y, x+y
  print('Fibonacci series: {}'.format(str(l)[1:-1]))'''
            case 7: return '''  i = int(input('Enter the number: '))
  def recursion(i):
      if i == 1: return 1
      else: return i * (recursion(i-1))
  print('Factorial of {} is: {}'.format(i, recursion(i)))'''
            case 8: return '''  l = list(map(int,input('Enter the list (separated by spaces): ').split(' ')))
  low, high = 0, len(l)-1
  b = False
  i = int(input('Search: '))
  while(low <= high and not b):
      mid = (low + high)//2
      if l[mid] == i:
          b = True
      else:
          if i < l[mid]:
              high = mid - 1
          else: 
              low = mid + 1
  if b: print('Number {} is present at index {} in the list'.format(i, mid))
  else: print('Number {} is not present in the list'.format(i))'''
            case 9: return '''  import os
  s = str(input('Write (to file): '))
  file = open("text.txt", 'w')
  file.write(s)
  file = open("text.txt", 'r')
  word = " "
  freq = 0
  words = []
  for line in file:
      splitted_words = line.replace(',',' ').replace('.',' ').split(" ")
      for w in splitted_words:
          words.append(w)
  for i in range(0, len(words)):
      count = 1
      for j in range(i+1, len(words)):
          if words[i] == words[j]:
              count+=1
      if(count>freq):
          freq = count
          word = words[i]
  file.close()
  os.remove('text.txt')
  print("Frequent word: '{}' at {} times".format(word, freq))'''
            case 10: return '''  mat, rix = [], []
  r = int(input('Enter the number of rows: '))
  c = int(input('Enter the number of columns: '))
  rows, columns = r, c
  while rows > 0:
      rows-=1
      l =  list(map(int,input('Enter the row for the first matrix (separated by spaces): ').split(" ")))
      mat.append(l)
  rows = r
  while rows > 0:
      rows-=1
      l =  list(map(int,input('Enter the row for the second matrix (separated by spaces): ').split(" ")))
      rix.append(l)
  rows = r
  result = []
  for i in range(rows):
      row = []
      for j in range(c):
          row.append(0) 
      result.append(row)
  while True:
      print('\\n[1 - addition | 2 - subtraction | 3 - multiplication | e - exit]\\n')
      operation = input('Select operation: ')
      if operation == '1':
          for i in range(r):
              for j in range(c):
                  result[i][j] = mat[i][j] + rix[i][j]
          for ii in result:
              print('  {}'.format(''.join(str(ii).split(','))[1:-1]))
      elif operation == '2':
          for i in range(r):
              for j in range(c):
                  result[i][j] = mat[i][j] - rix[i][j]
          for ii in result:
              print('  {}'.format(''.join(str(ii).split(','))[1:-1]))
      elif operation == '3':
          for i in range(r):
              for j in range(c):
                  result[i][j] = mat[i][j] * rix[i][j]
          for ii in result:
              print('  {}'.format(''.join(str(ii).split(','))[1:-1]))
      elif operation.lower() == 'e': break
      else: print('\\nInvalid Input')'''
            
            
class Input(Program):
    def one(self):
        l = None
        while True:
            try:
                l = list(map(int,input('\nInput:\n\n  Enter the list (separated by spaces): ').split(' '))); break
            except: print('\n  Invalid Input (e.g. 1 2 3 etc.)')
        return super().one(l)
    def two(self):
        s = None
        while True:
            try:
                s = str(input('\nInput:\n\n  Enter the text: '))
                if s.isspace():
                    raise ValueError(); break
                else: break
            except: print('\n  Invalid Input (e.g. he110 wor1d)')
        return super().two(s)
    def three(self):
        s = None
        while True:
            try:
                s = str(input('\nInput:\n\n  Enter the password: ')); break
            except: pass
        return super().three(s)
    def four(self):
        i = None
        while True:
            try:
                i = int(input('\nInput:\n\n  Enter the number (0 to finish): ')); break
            except: print('\n  Invalid Input (e.g. 1 or 2 or 3 etc.)\n')
        return super().four(i)        
    def five(self):
        s = None
        while True:
            try:
                s = str(input('\nInput:\n\n  Enter the text: '))
                if any(s.isdigit() for s in s):
                    raise ValueError(); break
                elif s.isspace():
                    raise ValueError(); break
                else: break
            except: print('\n  Invalid Input (e.g. heLLO worLd)')
        return super().five(s)        
    def six(self):
        i = None
        while True: 
            try:
                i = int(input('\nInput:\n\n  Enter the number: ')); break
            except: print('\n  Invalid Input (e.g. 1 or 2 or 3 etc.)')
        return super().six(i)
    def seven(self):
        i = None
        while True:
            try:
                i = int(input('\nInput:\n\n  Enter the number: ')); break
            except: print('\n  Invalid Input (e.g. 1 or 2 or 3 etc.)')
        program = Program(self)
        return i, program.seven(i)
    def eight(self):
        l, i = None, None
        while True:
            try:
                l = list(map(int,input('\nInput:\n\n  Enter the list (separated by spaces): ').split(' ')))
                if not all(l[i] <= l[i+1] for i in range (len(l)-1)) | all(l[i] >= l[i+1] for i in range (len(l)-1)): raise NameError
                break
            except NameError: print('\n  Invalid Input (sorted values only)')
            except ValueError: print('\n  Invalid Input (e.g. 1 2 3 etc.)')
        while True:
            try:
                i = int(input('\n  Search: ')); break
            except: print('\n  Invalid Input (e.g. 1 or 2 or 3 etc.)')
        return super().eight(l, i), i
    def nine(self):
        s = None
        while True:
            try:
                s = str(input('\nInput:\n\n  Write (to file): ')); break
            except: pass
        return super().nine(s)
    def ten(self):
        r, c = None, None
        while True:
            try:
                r = int(input('\nInput:\n\n  Enter the number of rows: ')); break
            except: print('\n  Invalid Input (e.g. 1 or 2 or 3 etc.)')
        while True:
            try:
                c = int(input('\n  Enter the number of columns: ')); break
            except: print('\n  Invalid Input (e.g. 1 or 2 or 3 etc.)')
        return super().ten(r,c)

class Output(Input):
    def one(self):
        one = super().one()
        print('\nOutput:\n\n  Number of odd numbers: {}\n  Number of even numbers: {}'.format(one[0],one[1]))
    def two(self):
        two = super().two()
        print('\nOutput:\n\n  Number of digits: {}\n  Number of letters: {}'.format(two[0],two[1]))
    def three(self):
        s = ''
        three = super().three()
        match three[1]:
            case 'a': s = 'At least 1 letter between [a-z]'
            case 'b': s = 'At least 1 letter between [A-Z]'
            case 'c': s = 'At least 1 number between [0-9]'
            case 'd': s = 'At least 1 character from [$#@]'
            case 'e': s = 'Minimum length 6 characters'
            case 'f': s = 'Maximum length 16 characters'
        if s == '': print('\nOutput:\n\n  {}'.format(three[0]))
        else: print('\nOutput:\n\n  {} ({})'.format(three[0],s))
        while True:
            if str(three[0]) == 'Invalid Password': self.three(); break
            else: break
    def four(self):
        four = super().four()
        print('\nOutput:\n\n  Sum of the above numbers: {}\n  Average of the above numbers: {}'.format(four[0], four[1]))
    def five(self):
        five = super().five()
        print('\nOutput:\n\n  Number of upper case letters: {}\n  Number of lower case letters: {}'.format(five[0],five[1]))
    def six(self):
        six = super().six()
        print('\nOutput:\n\n  Fibonacci series: {}'.format(six))
    def seven(self):
        seven = super().seven()
        print('\nOutput:\n\n  Factorial of {} is: {}'.format(seven[0], seven[1]))
    def eight(self):
        eight = super().eight()
        if eight[0][0]: print('\nOutput:\n\n  Number {} is present at index {} in the list'.format(eight[1],eight[0][1]))
        else: print('\nOutput:\n\n  Number {} is not present in the list'.format(eight[1]))
    def nine(self):
        nine = super().nine()
        print("\nOutput:\n\n  Frequent word: '{}' at {} times".format(nine[0],nine[1]))
    def ten(self):
        ten = super().ten()
        return (ten)

class Result(Output):
    def result(self):
        return '  Thus the above code is executed successfully.'
class PPL(Result):
    def ppl(self):
        print('\nAim:\n\n{}'.format(Algorithm(self.number).aim()))
        print('\nAlgorithm:\n\n{}'.format(Algorithm(self.number).algorithm()))
        print('\nProgram:\n\n{}'.format(Program(self.number).programs()))
        match self.number:
            case 1: Result(self).one()
            case 2: Result(self).two()
            case 3: Result(self).three()
            case 4: Result(self).four()
            case 5: Result(self).five()
            case 6: Result(self).six()
            case 7: Result(self).seven()
            case 8: Result(self).eight()
            case 9: Result(self).nine()
            case 10: Result(self).ten()
        print('\nResult:\n\n{}'.format(Result(self).result()))
        
#ppl = PPL(7)
#ppl.ppl()
def main():

    if platform.system() == 'Windows':
        os.system('"cls"')
        os.system('"title Python Programing Lab"')
    elif platform.system() == 'Linux':
        os.system('"clear"')
        #os.system('"title Python Programing Lab"')
    else: pass #Mac - Darwin

    print('\nWelcome to Python Programing Lab!')

    while True:
        print('\n[lop - list of programs | 1 to 10 - number of programs | cls - clear screen | e - exit]')
        command = input('\nEnter your command: ')
        if str(command).lower() == 'lop':
            ppl = PPL(0)
            print(ppl.lop())
        elif str(command).lower() == 'e': break
        elif str(command).lower() == 'cls': 
            os.system('"cls"') if platform.system() == 'Windows' else os.system('"clear"')
            main(); break
        else: 
            ppl = PPL(int(command))
            ppl.ppl()

if __name__ == '__main__':
    main()

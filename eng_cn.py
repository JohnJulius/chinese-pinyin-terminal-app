import csv
import os

def clear_terminal():
  """Clears the terminal."""
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

def remove_numbers(string):
  """Removes all numbers from a string.

  Args:
    string: A string.

  Returns:
    A string without any numbers.
  """

  new_string = ""
  for char in string:
    if not char.isdigit():
      new_string += char
  return new_string
def extract_digits(text):
  """Extracts all digits from a string using the `isdigit()` function.

  Args:
    text: A string.

  Returns:
    A string containing all the digits in the input string.
  """
  digits = ''
  for char in text:
    if char.isdigit():
      digits += char
  return digits
             
is_done = False
while is_done:
    # Ask for user input
    word = input("Enter the word to search: ")
    #number = extract_digits(word)
    clear_terminal()
    with open("input.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        if word != "x":
            for row in reader:
                if word in row[2]: # checks column for pinyin
                    print(row[0] + ":" +row[1]+" = "+ row[2])
        else:
            is_done = False


def EN_CN(word):
    pinyin_list= []
    #number = extract_digits(word)
    #clear_terminal()
    with open("input.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        if word != "x":
            for row in reader:
                if word in row[2]: # checks column for pinyin
                    print(row[0] + ":" +row[1]+" = "+ row[2])
                    pinyin_list.append(row[0] + ":" +row[1]+" = "+ row[2])
    return pinyin_list

def PY_EN(word):
    pinyin_list= []
    #number = extract_digits(word)
    #clear_terminal()
    with open("input.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if word in row[1]: # checks column for pinyin

                pinyin = remove_numbers(word)
                print(pinyin)
                print("____________________________________")
                print("High - 1st Tone | Rising - 2nd Tone")
                print("Falling-Rising - 3rd Tone | Falling - 4th Tone")
                print("____________________________________")
                for scope in reader:
                    if  pinyin+"1" in scope[1]:
                        pinyin_list.append("1st :"+scope[0]+" = "+ scope[2])
                    if  pinyin+"2" in scope[1]:
                        pinyin_list.append("2nd :"+scope[0]+" = "+ scope[2])
                    if  pinyin+"3" in scope[1]:
                        pinyin_list.append("3rd :"+scope[0]+" = "+ scope[2])
                    if  pinyin+"4" in scope[1]:
                        pinyin_list.append("4th :"+scope[0]+" = "+ scope[2])
    return pinyin_list

def CN_PY(word):
    pinyin_list= []
    #number = extract_digits(word)
    with open("input.csv", encoding="utf-8") as f:
        #clear_terminal()
        reader = csv.reader(f)
        for row in reader:
            if word in row[0]: # checks column for pinyin
                remove_numbers(row[1])  
                for scope in reader:
                    if  remove_numbers(row[1])==remove_numbers(scope[1]):
                        pinyin_list.append(row)
    return pinyin_list
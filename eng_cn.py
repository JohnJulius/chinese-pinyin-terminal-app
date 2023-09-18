import csv
import os

def clear_terminal():
  """Clears the terminal."""
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
              
is_done = True
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
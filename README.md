# chinese-pinyin-terminal-app
Chinese Pinyin Python Terminal Application

# Pinyin
Pinyin is a system that uses the Latin alphabet to write Chinese words based on their pronunciation. 

Chinese character components, radicals and phonetics are three aspects of the Chinese writing system that help learners understand and memorize characters. Here is a brief explanation of each term:

Chinese character components are the smallest meaningful units that make up a character. They can be either radicals, semantic components or phonetic components.

Radicals are components of characters that index them so you can look them up in dictionaries. Every character in Chinese has one radical, usually on the left or top of the character. Radicals often provide a clue to the meaning of a character.

Phonetic components are components of characters that suggest the correct pronunciation. They are usually on the right or bottom of the character. 

Phonetic components often have a similar sound to the character they are part of.

- Character Structure Learning:
    - Character composition (Sound, Semantic, etc)
    - Radicals
    - Form and meaning

# Project 
1. Create an application to filter all pinyin without tone marking and store into a list

2. Create dictionary from the list to output the following structure
{
    word: {
        tone: "1/2/3/4/5"
        pinyin: "based on tone"
        chinese: "text"
        english: "word and meaning"
    }
}

3. Make into an API (FastAPI)

4. Gamification
## Packaging Your PySimpleGUI Application for Windows
python -m pip install pysimplegui
python -m pip install pyinstaller

pyinstaller --onefile img_viewer.py

To remove the console, you can use the --noconsole or the --windowed flag when running PyInstaller.


5. Display on APP


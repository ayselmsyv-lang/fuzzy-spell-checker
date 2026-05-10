# fuzzy-spell-checker

18. Fuzzy Spell Checker You are given a dictionary of correct words 
and a list of possibly misspelled words. Your task is to suggest likely 
corrections. Use a heuristic based on edit distance. For each misspelled 
word, compare it with dictionary words and return words with small edit 
distance. To make the program faster, you may first filter dictionary 
words by length or first letter. Your program should output the top 
correction suggestions for each input word. Rank suggestions by edit 
distance and then alphabetically or by frequency.

## Okay let's talk about what my code does

# Smart Fuzzy Spell Checker

This project is an interactive fuzzy spell checker built with Python and Streamlit.

The task is to take a dictionary of correct words and suggest likely corrections for misspelled words. The suggestions are ranked by edit distance and then alphabetically.

## What the project does

The user enters a possibly misspelled word, and the app compares it with words from the dictionary. If the word is close enough, the app returns the best correction suggestions.

Example:

```text
appel → apple
pyhon → python
progrmming → programming
```

#### In my code i used streamlit for web visual side:

```
app.py
```

#### For backend side i used :
```
spell_checker.py
words.txt
```
As i explained in my code, i used ```dp[Dynamic Programming] approach``` . It helped me find to compare user input and dictionary elements. 

And as a result i would find the 
most optimal solution which requires minimal change between words.

#### i used 3 functions:
```
edit_distance - Calculates the minimum number of operations needed to convert one word into another.

Allowed operations:

- insertion
- deletion
- substitution
```
```
get_suggestions - Compares the input word with dictionary words and returns the closest suggestions.

Suggestions are sorted by:

1.lowest edit distance
2.alphabetical order
```
```
load_words - Reads correct words from words.txt and stores them in a list.
```
### Technologies used
- Python
- Streamlit
- Dynamic Programming
- Edit Distance / Levenshtein Distance

 ### Project structure
 ```
fuzzy-spell-checker/
│
├── app.py              # Streamlit user interface
├── spell_checker.py    # Core spell checking logic
├── words.txt           # Dictionary words
├── requirements.txt    # Required packages
└── README.md
```


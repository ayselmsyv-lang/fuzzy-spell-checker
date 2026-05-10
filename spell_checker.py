#Via this function we find difference between input 
#word and original word from dictionary.
#word1 is input word and word2 is original word from dictionary.    
def edit_distance(word1, word2):

    rows=len(word1)+1
    cols=len(word2)+1

    #we use dp because we need minimum nuber of operations to convert user input to our dictionary word.
    dp=[[0 for i in range(cols)] for j in range(rows)]

    for i in range(rows):   # deletion of letters from the word1.
        dp[i][0]=i
    for j in range(cols):   # insertion of letters into the word1.
        dp[0][j]=j
    
    for i in range(1,rows):
        for j in range(1,cols):

            #if the letters are same then we will not do any 
            #operation and take the value from previous row and column.

            #if the letters are different then we will do one of the three 
            #operations and take the minimum value from previous row and column.

            if word1[i-1]==word2[j-1]:
                cost=0  

            else:
                cost=1
            
                #the purpose of cost here is diagonal element whether it will be zero(no change,full match) or 1(replacement,no match) 
                #and we will add it to the diagonal element of dp table.

            dp[i][j]=min(dp[i-1][j]+1,      #deletion
                        dp[i][j-1]+1,      #insertion
                        dp[i-1][j-1]+cost)   #substitution
    return dp[-1][-1]

def get_suggestions(word, dictionary, max_distance=2, top_n=5):
    word = word.lower() #our purpose here is preventing from case sensitivity between e.g. python and Python.
    suggestions = []    #this is the list of suggestions that we will return to the user.

    #This loop will find the minimal edit distance between user input and dictionary words.
    for correct_word in dictionary:
        if abs(len(word) - len(correct_word)) > max_distance:
            continue

    #we compare whether distance is less than or equal to max_distance or 
    #not because we want to return only those suggestions which are close to the user input.
        distance = edit_distance(word, correct_word)

        if distance <= max_distance:
            suggestions.append((correct_word, distance))
    #only choose the closest suggestions based on edit distance and sort them by distance and then alphabetically.
    suggestions.sort(key=lambda x: (x[1], x[0]))
    return suggestions[:top_n]



def load_words(file_path):
    with open(file_path, "r",encoding="utf-8") as file:
        return [line.strip().lower() for line in file if line.strip()] #this is the list of words from the dictionary.
if __name__ == "__main__":
    dictionary = load_words("words.txt")
    word = input("Enter the word: ")
    suggestions = get_suggestions(word, dictionary)

    for suggestion, distance in suggestions:
        print(suggestion, distance)
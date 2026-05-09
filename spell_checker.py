'''Via this function we find difference between input 
   word and original word from dictionary.
   word1 is input word and word2 is original word from dictionary.'''
def edit_distance(word1, word2):
    rows=len(word1)+1
    cols=len(word2)+1
'''we use dp because we need minimum nuber of operations to convert user input to our dictionary word.'''
    dp=[[0 for i in range(cols)] for j in range(rows)]

    for i in range(rows):   #rows represent insertion of letters in the word.
        dp[i][0]=i
    for j in range(cols):   #cols represent deletion of letters in the word.
        dp[0][j]=j
    
    for i in range(1,rows):
        for j in range(1,cols):
            '''if the letters are same then we will not do any 
            operation and take the value from previous row and column.'''
            if word1[i-1]==word2[j-1]:
                cost=0  
                dp[i][j]=dp[i-1][j-1]
            '''if the letters are different then we will do one of the three 
            operations and take the minimum value from previous row and column.'''
            else:
                cost=1
#the purpose of cost here is diagonal element whether it will be zero(no change,full match) or 1(swap,no match) 
#and we will add it to the diagonal element of dp table.
            dp[i][j]=min(dp[i-1][j]+1,      #deletion
                        dp[i][j-1]+1,      #insertion
                        dp[i-1][j-1]+cost)   #substitution
    return dp[-1][-1]

a=input("Enter the word: ") #this is the input word from user.
with open("words.txt", "r") as file:
    b=[line.strip() for line in file] #this is the list of words from dictionary.
for word in b:
    distance = edit_distance(a, word)
    print(word, distance)
print(f"our distance is: {edit_distance(a,b)}") #this will print the distance between input word and original word from dictionary.

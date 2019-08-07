"""
Case study 2 of Think Python 2e.
"""

"""
Exercise 9.1.
Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace).
"""

f = open("words.txt")

def print_long(f):
    for word in f:
        if len(f) > 20:
            print(word)
        else:
            pass


"""
Exercise 9.2.
Write a program that reads words.txt and prints only the words that have no “e”. 
Compute the percentage of words in the list that have no “e”.
"""
def print_no_e(f):
    count = 0
    all = 0
    for word in f:
        if 'e' not in word:
            print(word)
            count += 1
            all += 1
        else:
            all += 1
    print(str(count/all*100) + "% of words are without e!\n")

"""
Exercise 9.3.
Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.
Write a program that prompts the user to enter a string of forbidden letters and then prints the
number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?
"""
def avoids(f,s):
    for word in f:
        flag = True
        for letter in word:
            if letter in s:
                flag = False
                break
            else:
                pass
        if flag:
            print(word)

def avoids_count(f,s):
    c = 0
    for word in f:
        flag = True
        for letter in word:
            if letter in s:
                flag = False
                break
            else:
                pass
        if flag:
            c += 1
    return c            
            
                
if __name__ == "__main__":
    from itertools import permutations as pm

    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                 'o','p','q','r','s','t','u','v','w','x','y','z']
    s = pm(alpha,5)
#        forbidden = input("Please enter a 5 letter string of forbidden letters:\n")
#        print(avoids_count(f, forbidden))
    m = 1000000
    for perm in s:
        f = open("words.txt")
        n = avoids_count(f,perm)
        if n<m:
            m = n
            least_perm = perm
        print(perm,least_perm,m)

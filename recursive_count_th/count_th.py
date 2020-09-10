'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#Your function should take in a signle parameter (a string word)
def count_th(word):
#need to slice after every occurrence of "th"

    #need to include base case
    #if len(word) is less than 2:
    if len(word) < 2:
        return 0
    #if first two words == "th"
    if word[:2] == 'th':
    #return 1 and call count_the(word) again starting at index 2 as first 
    #two index's were 'th', start the function again to find more 'th' if possible
        return 1 + count_th(word[2:])
    else:
    #else look at 1st index of word to see if 'th' begins here
        return count_th(word[1:])

print(count_th("athththa"))


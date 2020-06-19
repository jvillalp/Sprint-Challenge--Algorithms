#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) o(n): As the size of the input increases, the runtime or the space used will grow at the same rate. 


b) O (n^2): As the size of the input increases, the runtime or space used will grow twice as fast


c) 0(n): As the size of the input increases, the runtime or the space used will grow at the same rate. 

## Exercise II

stories = n
#a lot of eggs
eggs = 
If egg dropped on floor f >= will break
else will survive

- we have to create a binary search strategy since we can assume that all floors of building are in order -
-  three options: 1. our guess is correct, 2. guess is too high, 3. guess is too low 


- PSEUDOCODE

start = 0
end = len of floor

while start < end:
    middle = (start + end) /2
    if not eggBreak(middle):
        if eggBreak(middle +1):
            return middle + 1
        else:
            start = middle + 1
    else:
        end = middle -1
        
return -1
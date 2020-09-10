#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) o(n): As the size of the input increases, the runtime or the space used will grow at the same rate. 
 - " while (a < n * n * n) " is o(n^3) and " a += n * n " is O(n^2) once we divide n^3 / n^2 = n which is the running time of this pseudocode.
  - outer loop is being cubed. 


b) O (2^n): As the size of the input increases, the runtime or space used will grow twice as fast
 - outer loop "for i in range(n): ..." is O(n) and inner loop " while j < n: ..." is O(n) so n * n = n^2 which is our running time in this pseudocode.
 - inner loop is being multipled by 2.


c) 0(n + 1): As the size of the input increases, the runtime or the space used will grow at the same rate. 
- Each time we run this code, we are increasing bunnyEars at the same rate of number of times we have a bunny plus the 0 bunnies in base case so O(n + 1) is our runtime. 

## Exercise II

- we have to create some type of a binary search strategy since we can assume that all floors of building are in order
-  three options: 1. our guess is correct, 2. guess is too high, 3. guess is too low 
- if guess results in the egg not breaking, we can add one more to the floor and see if it breaks there, if it does break, then we have found f floor in which the eggs start to break in every floor after that. 


- PSEUDOCODE -

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

- The runtime if O(log n) because the total number of times we check for the floor are divided by 2 until we reach our answer. 
# RegularExpressions
Regular expressions are the sequence of patterns that are used to find the patterns from the string and files etc. 

## Dot (.)</br>
>Dot (.) matches anything except the newline character in the string.</br>
>### TASK-1: </br>
>#### Question: abc.efg.ijk.mno</br>
>#### Solution: r'^...\\....\\....\\....$'

## \d and \D</br>
>'\d' matches all the digits [0-9].
>'\D' matches all the non-digit characters. 
>### TASK-2:</br> 
>#### Question: xxXxxXxxxx</br>
>where,</br>
>     x: digit</br>
>     X: on-digit</br>
>#### Solution: r'\d{2}\D\d{2}\d{4}'

## * 
>(*) mathces zero or more repetition of proceeding character/ group/  character class.
>### TASK-6:</br>
>#### Question: 
>You have a test string <i>S</i>.Your task is to write a regex that will match S using the following conditions:</br>

>* S should begin with 2 or more digits.</br>
>* After that, S should have 0 or more lowercase letters.</br>
>* S should end with 0 or more uppercase letters</br>
> #### Solution: r'^\\d{2}\\d*[a-z]\*[A-Z]\*$'

## +
>+ mathes 1 or more repetition of proceeding character/group/ character class.
>### TASK-7: </br>
>#### Question: 
>You have a test string S. Your task is to write a regex that will match S using the following conditions:

>* S should begin with 1 or more digits.
>* After that, S should have 1 or more uppercase letters.
>* S should end with 1 or more lowercase letters.
>#### Solution: r'^\\d+[A-Z]+[a-z]+$'

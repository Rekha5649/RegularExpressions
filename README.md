# RegularExpressions (Hackerrank Questions)
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

## $
> End string with the proceeding character/ group/ Character class. e.g. 123$
>### TASK-8: </br>
>#### Question: 
>Write a RegEx to match a test string, S, under the following conditions:

>* S should consist of only lowercase and uppercase letters (no numbers or symbols).
>* S should end in s.
>#### Solution: r'^[a-z A-Z]\*s$'

## Parenthesis ()
>Parenthesis ( ) around a regular expression can group that part of regex together. This allows us to apply different quantifiers to that group.These parenthesis also create a numbered capturing. It stores the part of string matched by the part of regex inside parentheses.These numbered capturing can be used for backreferences. ( We shall learn about it later )
>### TASK-9: </br>
>#### Question: 
>You have a test String S. Your task is to write a regex which will match S with the following condition:
>* S should have 3 or more consecutive repetitions of ok.
>#### Solution: r'(ok){3}\\1*'

>## Notes
>Alternations, denoted by the | character, match a single item out of several possible items separated by the vertical bar. When used inside a character class, it will match characters; when used inside a group, it will match entire expressions (i.e., everything to the left or everything to the right of the vertical bar). We must use parentheses to limit the use of alternations.
>### TASK-10: </br>
>#### Questions:
>Given a test string, s, write a RegEx that matches s under the following conditions:

>* s must start with Mr., Mrs., Ms., Dr. or Er..
>* The rest of the string must contain only one or more English alphabetic letters (upper and lowercase).
>>#### Solution: r'^(Mr|Mrs|Ms|Dr|Er)\\.[a-z A-Z]+$'

## Positive lookahead (regex1(?=regex2))

The positive lookahead (?=) asserts regex_1 to be immediately followed by regex_2. The lookahead is excluded from the match. It does not return matches of regex_2. The lookahead only asserts whether a match is possible or not.

>### TASK:
>#### Question: 
>Write a regex that can match all occurrences of o followed immediately by oo in String.
>#### Solution: Regex_Pattern = r'o(?=(oo))'

# RegularExpressions
Regular expressions are the sequence of patterns that are used to find the patterns from the string and files etc. 

## Dot</br>
>Dot (.) matches anything except the newline character in the string.</br>
>>###TASK-1: </br>
>>abc.efg.ijk.mno</br>
>> Solution: r'^...\\....\\....\\....$'

## Digit (\d and \D)</br>
>'\d' matches all the digits [0-9].
>'\D' matches all the non-digit characters. 
>>###TASK-2:</br> 
>>xxXxxXxxxx</br>
>>>where,
>>>     x: digit
>>>     X: on-digit
>>Solution: r'\d{2}\D\d{2}\d{4}'

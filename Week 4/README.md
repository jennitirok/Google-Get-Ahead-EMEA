# Technical Challenge 4
This is relevant for students that are in their first or second year of Bachelor's degree.

## Car Plates Dictionary
We need to find the shortest word from a vocabulary that includes all the letters from a given licence plate. The shorter the word, the better. The licence plates start with two or three letters, then they are followed by 5 characters, from which at most 2 are letters, the rest are digits.

Write a solution that will find the shortest words for 1000 licence plates.

You are given a vocabulary containing all valid words.

*   Keep duplicate letters
*   Ordering is irrelevant
*   Case is irrelevant
*   The vocabulary is sorted lexicographically
*   The vocabulary contains about 4 million entries

### Example 1
Given the vocabulary of valid words as ["Sort", "Google", "Get", "Ahead"]

For the licence plate ```RT 123 SO``` the shortest word would be SORT:

### Example 2
Given the vocabulary of valid words as ["What", "Is", "Google", "Car", "Waymo"]

For ```RC 10014``` the shortest word would be CAR.


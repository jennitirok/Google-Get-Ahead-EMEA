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

<img width="238" alt="Screen Shot 2021-08-10 at 09 39 57" src="https://user-images.githubusercontent.com/46791949/128800410-9bca383c-8f84-4b2d-aeb7-83313271c76b.png">

For the licence plate ```RT 123 SO``` the shortest word would be SORT.

### Example 2
Given the vocabulary of valid words as ["What", "Is", "Google", "Car", "Waymo"]

<img width="213" alt="Screen Shot 2021-08-10 at 09 40 13" src="https://user-images.githubusercontent.com/46791949/128800419-88960c5e-e201-4d76-9ff9-c86688c210e6.png">

For ```RC 10014``` the shortest word would be CAR.


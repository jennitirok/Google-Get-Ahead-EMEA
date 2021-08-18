# Technical Challenge 5
This is relevant for students that are in their first or second year of Bachelor's degree.

## Rectangle Sums
Given a list of lists of **positive** integers that represent arrangements of numbers as shown in the test cases below, find the rectangle containing the **largest** sum such that the rectangle doesn't contain any empty/missing cells.

Your program should **return the pair of array indices that represent the rectangle**. If there's more than one rectangle with an optimal sum, any arbitrary one may be returned.

### Test Cases
For the list ```[[1, 2], [3, 4, 5, 6], [7, 8], [9]]```, the arrangement would be as follows. The solution rectangle contains a sum of 25 and array indices **(0, 0) -- (2, 1)**:

<img width="913" alt="Screen Shot 2021-08-18 at 10 42 27" src="https://user-images.githubusercontent.com/46791949/129833832-6bbe5989-cb91-4dbc-bb46-a24ed419dcfd.png">

<br>

For the input list ```[[1, 3, 2, 2], [2, 1, 2, 3], [4, 2, 3], [1, 1, 2, 17, 14], [3, 1, 2, 2]]```, the solution rectangle contains a sum of 35 and has array indices **(3, 0) -- (3, 4)**.

<img width="910" alt="Screen Shot 2021-08-18 at 10 42 45" src="https://user-images.githubusercontent.com/46791949/129833854-0ea2db2a-94af-4953-8a04-47c7446876d7.png">

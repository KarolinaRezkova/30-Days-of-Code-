# Day 12: Inheritance

See the original assignment on 
[Day 12: Inheritance | HackerRank
]( https://www.hackerrank.com/challenges/30-inheritance/problem ).

## Objective
Today, we're delving into Inheritance.

## Task
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. 
Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student 
inherits all the properties of Person.

Complete the Student class by writing the following:

-  Student class constructor, which has  parameters:
    - A string, `firstName`.
    - A string, `lastName`.
    - An integer, `idNumber`.
    - An integer array (or vector) of test scores, `scores`.
- A char `calculate()` method that calculates a Student object's average and returns the grade character representative
of their calculated average:

| **Letter** | The average of the scores $a$ |
|:----------:|-------------------------------|
|   **O**    | $90 \leq a \leq 100$          |
|   **E**    | $80 \leq a < 90$              |
|   **A**    | $70 \leq a < 80$              |
|   **P**    | $55 \leq a < 70$              |
|   **D**    | $40 \leq a < 55$              |
|   **T**    | $a < 40$                      |

##### Input Format
The locked stub code in the editor reads the input and calls the Student class constructor with the necessary arguments.
It also calls the calculate method which takes no arguments.

The first line contains `firstName`, `lastName`, and `idNumber`, separated by a space. The second line contains 
the number of test scores. The third line of space-separated integers describes `scores`.

##### Constraints
- $1 \leq len(firstName) \leq 10$
- $1 \leq len(lastName) \leq 10$
- $len(idNumber) = 7$
- $0 \leq score \leq 100$

##### Output Format
Output is handled by the locked stub code. Your output will be correct if your Student class constructor and 
calculate() method are properly implemented.

###### Sample Input 
```
Heraldo Memelli 8135627
2
100 80
```

###### Sample Output 
```
Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
```

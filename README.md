# FSA Drawer and Checker
Object-oriented python program that reads  a file representing an FSA and a string of chars and reports if the string is legal or not according to the FSA.

# Project Instructions

## Introduction

Recall that we defined an FSA as an abstract machine that reads as input a string of symbols and decides whether to accept or reject the input string. We represented an FSA as a graph with directed, labeled arcs, two types of nodes (final and non-final states), and a unique start state. The FSA accepts a string if, starting from the start state, the automaton can be in a final state after having read the whole input string.

Consider the following FSA:

![fsa](https://user-images.githubusercontent.com/77580692/157102404-59133417-7b83-446d-bdcb-579a4eb86939.jpg)

It could be represented (for instance, in a data file) by the following:

```
5; x,y,z,a;(0:0:x),(0:1:y),(1:2:x),(2:2:x),(2:3:y),(3:3:x),(3:4:z),(4:4:x),(4:1:a);0;1,3;
```

where:

- 5; represents the number of states
- x,y,z; represents the alphabet
- (0:0:x),(0:1:y),(1:2:x),(2:2:x),(2:3:y),(3:3:x),(3:4:z),(4:4:x),(4:1:a); represent the state transitions
- 0; represents the start state
- 1,3; represent the accept states
- An example of a legal input string is: xxxxxyxxxyxxxzxxxa 

## Project specifications:

Your objective is to develop an object-oriented Python program running on Windows in Python 3, as follows:

A program that reads:

- a file representing an FSA in the format specified above
- a string of chars

and reports if the string is legal or not according to the FSA.

Additionally, your program must draw the FSA in a window using a simplified scheme that looks like this:

![FSADrawing](https://user-images.githubusercontent.com/77580692/157103185-e44f9251-a6e3-4115-a8ab-5af958bac592.png)

Your program does not have to show how the string is processed in the drawing.

> **NOTE:** Do not hard-code your program to solve the FSA above. It should be able to process any specified FSA.

## Error Checking
Your program should also check as it reads the fsa to process. It should properly handle characters in the input string to be checked which are not part of the grammar's alphabet, transitions to illegal or non-existent states, etc.


## Input and Output

Provide a script: run.bat. The .bat file will produce two runs of your program.
```
python fsa.py fsa.txt legal1.txt
python fsa.py fsa.txt illegal1.txt
```

where:

- python runs the python interpreter
- fsa.py is your program that reads fsa.txt and legal1.txt, draws the fsa and processes the string
- fsa.txt contains the fsa specification
- (il)legal1.txt would be a string of characters to be processed

Executing the script will cause your program to read the fsa specification into any representation you wish so long as your program is object-oriented. Your program will draw the graphical representation of the fsa and process the string, reporting success for the legal string and failure for the illegal one to the console. Understand that I will copy a diferent FSA and string file in as part of testing, so DO NOT hard-code your program.

## Design Considerations

This program will use Python to load and represent the FSA and to evaluate strings. Project 4 will extend this program. In project 4, you will still need to read the FSA using code you have developed here. However, that project will generate code in another programming language that will solve the FSA. Consequently, you should carefully consider how you will factor this program for reuse in project 4. 

Programming environment: We will work on Windows for this project. You may use a Python IDE if you wish but be sure your program can execute from the script as specified above.

## Deliverables

1. Python code for your program. It should adhere to good programming conventions.
2. The required files: fsa.txt, legal.txt, illegal.txt, and run.bat.

# QOSF mentorship application - Task 1 - Vatsal Kanoria

The task description is included at the bottom of this README for context.

## Learning Journey

Attempting this task has been a very interesting learning experience for me, which I felt would be interesting to record here. 

I began this task with knowing close to nothing about quantum computing apart from a vague idea of what a qubit was and knowing that to manipulate a qubit I needed to apply some kind of quantum logic gates, and a very rough understanding of some basic quantum mechanics. 

I struggled initially to understand what the task was asking, and so thought it would be best to read a book on quantum computing. Scanning through a few references I settled on reading 'Concise Guide to Quantum Computing' (Kurgalin, Borzunov) as it was the easiest book I could find to quickly get a grasp of some of the main concepts of Quantum Computing. It was particularly nice for me to read the book, as it is quite mathematical oriented and I come from a maths background, and doesn't spend time trying to teach the quantum mechanics or more physical/hardware aspects, so felt it was quite practical as an intro. 

After reading a few chapters of the book I went back to task 1 and had a slightly better understanding of what the problem was asking. I still wasn't sure how I would go about solving the problem on a quantum computer. At this stage, I felt it was important to get some hands on experience with Qiskit. I went to the Qiskit website and began a [tutorial on Qiskit](https://qiskit.org/textbook-beta/course/introduction-course). This really helped me to get a better understanding of how to implement the gates which I was reading about in the book, and get a better feeling for how quantum computations work and what is involved in quantum circuit design.   

Around half way through completing the Qiskit tutorial and reading the book, the problem started to make more theoretical sense to me. As I still wasn't sure how to write the relevant quantum algorithm at this stage, to get a better feeling for the problem, I decided to try and write a classical algorithm which would take any array of positive integers and output a string (to the console) which would reperesent the superposition of states which we want as a result. Although this doesn't solve the problem of desiging a quantum circuit, it did help me to understand a bit better as to what the problem was asking me to do. The code for this algorithm (although not perfectly correct, and currently does not work when tested with arrays of size larger than 4) can be found in the directory 'classical_implementation/classical_implementation.py' - note that it does seem to work correctly for the two input example cases `[1,5,4,2]` and `[1,5,7,10]` in task 1. This classical implementation is roughly what we want to achieve for the task 1 general case/extension problem, but with a quantum algorithm - not outputting a string representing what we would want, but actually create the desired quantum state.

After writing the classical algorithm, I decided to go back to finishing the qiskit tutorial, and in particular understand Grover's algorithm (as recommended in the task as a possible way to help with the problem). I think the hardest thing I found getting my head around when attempting some of the problems in this tutorial (before looking at the solutions) was just the different way of thinking in terms of not being able to use classical logic like 'if...else' conditional statements that I have become accustomed to in writing classical algorithms in high-level languages like python, which as far as I know doesn't really make sense to do when writing a quantum algorithm with qiskit, as the logical operations are more low level gate operations. (I do know from a conference I attended that there are systems where it is possible to write classical logic within quantum algorithms such as with D-Wave's Qua language for quantum orchestration).

I also decided to finish reading the book, to get an overview of the different techniques used in Quantum Computing and felt it was important to read the paper on QRAM, as suggested by the problem. I found [this article](https://quantaforbreakfast.com/2016/08/19/quantum-computing-and-its-models/) useful to understand what is meant by "fiduciary" states in the QRAM article, and understand what a computational basis is, amongst get an overview of different quantum computing models. I also came across a short article by chance on [superdense coding](https://quantumcomputinguk.org/tutorials/superdense) I thought was relevant, and read this article too to see if it would help. At this stage I felt ready to go all hands in and attempt tackling the problem in task 1. 

In the end, at this stage I haven't been able to understand well enough how to implement the QRAM article in practice, or have a full grasp of the theory. Hence I have not been able to do the quantum solution as yet. I will keep on working on it and send updates to this code base if I am able to get to the solution in the next few days.  

## Solution

The quantum circuit solution is saved as 'circuit.png' 

To run the program, first create a virtual env and install packages:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
Then run the program
```
python3 quantum_program.py
```

There was also a 'classical' implementation I wrote while experimenting/trying to learn which can be run, but was more of an experiment. 
```
python3 classical_implementation/classical_implementation.py
```

## Questions

A) I am not sure I understand the following statement in the QRAM article. 
"Now, when the qubits of the address register are sent through the graph, at each node they encounter a unitary encoding trans-formationU. If the qutrit is initially in the |wait〉state,the unitary swaps the state of the qubit in the two 
|left〉-|right〉levels of the qutrit (i.e.U|0〉|wait〉=|f〉|left〉andU|1〉|wait〉=|f〉|right〉, where |f〉is a fiduciary stateof the qubit)"

I had a few questions on the input array for task 1:

B) is the length of the input array always a power of 2?
C) are the values of the array always positive integers, and is there a limit to how big the integer can be? 
D) Do we take the number of bits in the binary representation of any integer in the array to be the size of the binary representation of the max integer? e.g. if we have [1, 2, 12] then 12 can be represented in binary by a minimum of 4 bits, so our binary representation of 3 would look like ‘0011’ instead of just ‘11’.
E) are we only supposed to do the task for the specific array [1, 5, 7, 10]?

## Task 1
(I have copied the task description here for reference).

Design a quantum circuit that considers as input the following vector of integers numbers: [1,5,7,10]
returns a quantum state which is a superposition of indices of the target solution, obtaining in the output the indices of the inputs where two adjacent bits will always have different values. In this case the output should be: 1/sqrt(2) * (|01> + |11>), as the correct indices are 1 and 3.
1 = 0001
5 = 0101
7 = 0111
10 = 1010
The method to follow for this task is to start from an array of integers as input, pass them to a binary representation and you need to find those integers whose binary representation is such that two adjacent bits are different. Once you have found those integers, you must output a superposition of states where each state is a binary representation of the indices of those integers.

**Example 1**
Consider the vector [1,5,4,2]
Pass the integer values to binary numbers that is [001,101,100,010]
Identifies which values whose binary representation is such that two adjacent bits are different, we can see that are 2 101 and 010, [001,101,100,010].
Returns the linear combination of the indices in which the values satisfying the criterion are found.
[001,101,100,010]
Indices 0, 1, 2, 3 are converted to binary states |00> |01> |10> |11>.
The answer would be the superposition of the states |01> and |11> or 1/sqrt(2) * (|01> + |11>).

**Context**
If you’re struggling to find a proper way to solve this task, you can find some suggestions for a possible solution below. This is one way to approach the problem, but other solutions may be feasible as well, so feel free to also investigate different strategies if you see fit!
The key to this task is to use the superposition offered by quantum computing to load all the values of the input array on a single quantum state, and then locate the values that meet the target condition. So, how can we use a quantum computer to store multiple values? A possible solution is using the QRAM (some references: https://arxiv.org/pdf/0708.1879.pdf, https://github.com/qsharp-community/qram/blob/master/docs/primer.pdf).
As with classical computers, in the QRAM information is accessed using a set of bits indicating the address of the memory cell, and another set for the actual data stored in the array.
For example, if you want to use a QRAM to store 2 numbers that have at most 3 bits, it can be achieved with 1 qubit of address and 3 qubits of data.
Suppose you have the vector input_2 = [2,7].
In a properly constructed circuit, when the value of the address qubit is |0> the data qubits have value 010 (binary representation of 2) and when it is |1> in the data qubits have value 111 (binary representation of 7).
Given such a structure, you should be able to use Grover’s algorithm in order to obtain the solution to the task.
You can assume that the input always contains at least two numbers that have alternating bitstrings.
Bonus:
Design a general circuit that accepts vectors with random values of size 2𝑛 with m bits in length for each element and finds the state(s) indicated above from an oracle.
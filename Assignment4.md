Pam Qian    
CS 330 Programming Languages    
Assignment 4: Control Flow    
Swift Programming Languages   

__1. What types of conditional statements are available in your language? 
Does it allow for statements other than "if"?__   
Siwft has "if", "if/else", "if/else if/else", and "switch" conditional statements.    

__2. Does your language use short-circuit evaluation? 
If so, make sure that your code includes an example.__   
*Short circuiting is when a statement stops evaluation as soon as an
outcome is determined.*   
For example, when using the logical AND operator (a && b), if the first value
is false, the second value won't even be evaluated, because it can't possibly make
the overall expression equate to true.    

Example:    
let enteredDoorCode = false   
let passedRetinaScan = false    
if enteredDoorCode && passedRetinaScan {    
    print("Welcome!")   
} else {    
    print("ACCESS DENIED")    
}   
// Prints "ACCESS DENIED"       

__3. How does your programming language deal with 
the “dangling else” problem?__    
*The dangling else problem occurs when an optional else cluase resuits in nested 
conditionals being ambiguous.*    
Swift used to force braces around conditional statements (early versions).
However, in Swift 5, the braces are not required if the statments do not cause confusions.    
Example:    
if (x < y) {
print ("x is less than y")
}

__4. Does your language include multiple types of loops?__    
1) For-In Loops   
For-in loops are used to iterate over a sequence, such as items
in an array, ranges of numbers, or characters in a string.
There are similar to the For-Each Loops in Python.    
2) While Loops    
While loops start by evaluating a single condition. If the 
condition is true, a set of statements is repeated until the condition 
becomes false.    
3) Repeat-While   
Repeat-While is a variation of the while loops, It performs
a single pass through the loop block first, before considering the 
loop's condition. It then continues to repeat the loop until the condition 
is false.   

__5. Can you use break or continue statements to control iteration?__   
Yes!    

__6. If your language supports switch or case statements, do you have to use 
"break" get out of them? Can you use "continue" to have all of them evaluated?__ 
Swift supports switch statements. A switch statement provides an alternative to the if statement 
for responding to multiple potential states. It does not have to use "break".   
The continue statement tells a loop to stop what it is doing and start again at the 
beginning of the next iteration through the loop.   
The break statement ends execution of an entire control flow statement immediately. 
The break statement can be used inside a switch or loop statement when you want to 
terminate the execution of the switch or loop statement earlier than would otherwise be the case.   

__7. Is there anything special in terms of control flow that your language 
does that isn't addressed in this assignment?__
1) Fallthrough. In Swift, switch statements don’t fall through the bottom of each case and into the next one. That is, the entire switch statement completes its execution as soon as the first matching case is completed. By contrast, C requires you to insert an explicit break statement at the end of every switch case to prevent fallthrough. If you need C-style fallthrough behavior, you can opt in to this behavior on a case-by-case basis with the fallthrough keyword.   
    
2) Early Exit: A guard statement, like an if statement, executes statements depending on the Boolean value of an expression. You use a guard statement to require that a condition must be true in order for the code after the guard statement to be executed. Unlike an if statement, a guard statement always has an else clause—the code inside the else clause is executed if the condition is not true.   

*Reference*   
(https://docs.swift.org/swift-book/LanguageGuide/ControlFlow.html#ID135)
















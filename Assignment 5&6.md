Pam Qian    
CS 330 Programming Languages    
PLP Assignments 5 & 6   
Functions, parameters, and scope    

__1. What is the syntax for declaring a function in Swift?__   
    
*Simple example:*      

	func name() {   
	    some code   
		}

	*Return values:*    
	func name() -> DataType {   
		  some code   
		  return someValue
	} 
    
*Using parameters:*  

	func name(argumentLabel parameterNmae: DataType){   
	}   

__2. Are there any rules about where the function has to be placed in your code file so that it can run?__    
No. You can declare a function anywhere in the code, even inside of another function, known as the nested functions.    
	  
__3. Does Swift support recursive functions? If so, write one.__    
Yes!    
*Example:*   

	func countDownToZero(num: Int) {    
	    print(num)    
	    if num > 0 {    
		countDownToZero(num: num - 1)   
	    }   
	}   
	print("Countdown:")   
	countDownToZero(num:3)    
    
*Output:*			
Countdown: 	   
3   
2   
1   
0   
    
__4. Can functions in Swift accept multiple parameters? Can they be of different data types?__    
Yes and yes!    
*Example:*  

	func greet(person: String, alreadyGreeted: Bool) -> String {    
	   if alreadyGreeted {    
	       return greetAgain(person: person)    
	   } else {   
	       return greet(person: person)   
	   }    
	}   
	
	print(greet(person: "Tim", alreadyGreeted: true))   
	// Prints "Hello again, Tim!"   

__5.Can functions in Swift return multiple values at the same time?__
Yes!    
*Example:*    

	func minMax(array: [Int]) -> (min: Int, max: Int) {   
	   var currentMin = array[0]    
	   var currentMax = array[0]    
	   for value in array[1..<array.count] {    
	       if value < currentMin {    
		   currentMin = value   
	       } else if value > currentMax {   
		   currentMax = value   
	       }    
	   }    
	   return (currentMin, currentMax)    
	}   

__6. Declare a variable (say, x) in the main body of your program. Then declare a variable of the same name inside of a loop. 
Is there a conflict? Is the old variable overwritten or do you now have two variables of the same name?__   
No, there is no conflict, meaning the code does not generate an error. There are two variables of the same name
    
	var x = 6   
	print(x)    
	for i in 1...10 {   
	    var x = 9   
	    print(x)    
	}   
	
	
	*Output:*
	*Before the for loop:*		
	6
	
	*Inside the for loop:*	
	9	
	9	
	9	
	9	
	9	
	9	
	9	
	9	
	9	
	9	
	(10 times)
	
	*After the loop:*		
	6	

__7. What if the other x inside a function?__   
Yes, you can declare another ‘x’ inside of a function and assign it a different value.    
    
	func printanInt(_ x:Int) {    
	    print(x)    
	    var x = 9   
	    print(x)    
	}   
	printanInt(x)   

__8. Can you have variables that are globally accessible? What are the rules for creating them?__   
Yes.    
*Declare the variable in main:*   

	let pi = 3.14   
	
This variable pi can be used in functions.    
    
__9. Are variables passed by value or by reference? (Hint: write a function that alters its input, but doesn’t return it. 
Pass it a variable, and see if the alteration is visible in main after you call the function)__   
Variables are passed by references.

	  char [] a = {'c','a','t'}     
	  char [] b = {'d','o','g'}   
	  a=b   
	  b[1] = 'u'    
	  print a   
	  print b   
    
__10. If you run this code (or the equivalent) in your language, what is the output? 
What does that tell you about how the language handles assignments?__

    var a: [Character] = ["c","a","t"]
    var b: [Character] = ["d","o","g"]
    a = b
    b[1] = "u"
    
    print(a)
    print(b)
    
Output:   
    ["d", "o", "g"]
    ["d", "u", "g"]
    
The first char array, “a”, stores “d”, “o”, “g” and the second char array “b” stores “d”, “u”, “g” because the alternation from o to u was made after assigning the original values of “b” to “a”. 

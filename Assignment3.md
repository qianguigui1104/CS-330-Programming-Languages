
__Discussion questions: (Swift)__
__1. What are the naming requirements for variables in your language? What about naming conventions? Are they enforced by the compiler/interpreter, or are they just standards in the community?__    
Apple gives general conventions and other style guide for Swift programming.    
- Names of types and protocols are UpperCamelCase.    
- Everything else (such as global constant) is lowerCamelCase.    
- Exampleq:    
  var enjoysScubaDiving = true    
  var radarDetector: RadarScanner     
    
_Reference: https://swift.org/documentation/api-design-guidelines/#naming_


__2. Is your language statically or dynamically typed?__    
Swift is static - very static. The compiler must have all information about all classes and functions at compile time. 
You can "extend" an existing class (with an extension), but even then you must define completely at compile time what that extension consists of.   

_Reference: https://stackoverflow.com/questions/29924477/is-swift-a-dynamic-or-static-language_


__3. Strongly typed or weakly typed?__    
Swift is strongly typed. Whenever you use a variable or pass something as function argument,
Swift checks that it is of the correct type. You can't pass a string to a function that expects an integer etc. Swift does this check at compile time (since it's statically typed).    

_Reference: https://www.aidanf.net/learn-swift/types_and_type_inference_   


__4. If you put this line (or something similar) in a program and try to print x, what does it do? If it
doesn't compile, why? Is there something you can do to make it compile?
x = "5" + 6__   
It does not compile because in Swift "+" cannot be applied to operands of type "String" and "Int". 
There is no strightforward way to convert a string to an integer.   
Possible solution:    
let s = "5"   
var n =Int(s)   
var x = s + 6   

_Reference: https://iswift.org/cookbook/convert-string-to-int_    


__5. Describe the limitations (or lack thereof) of your programming language as they relate to the
coding portion of the assignment (adding ints and floats, storing different types in lists, etc).
Are there other restrictions or pitfalls that the documentation mentions that you need to be
aware of?__   

- Swift supports most standard C operators and improves several capabilities to eliminate common coding errors.     
- The assignment operator (=) doesn’t return a value, to prevent it from being mistakenly used when the equal to operator (==) is intended.   
- Arithmetic operators detect and disallow value overflow, to avoid unexpected results when working with numbers that become larger or smaller than the allowed value range of the type that stores them.     
- Swift also provides range operators that aren’t found in C, such as a..<b and a...b, as a shortcut for expressing a range of values.    

_Reference: https://docs.swift.org/swift-book/LanguageGuide/BasicOperators.html_    


__6. How do type conversions work in your language? Are the conversions narrowing or widening,
and do they work by default or do they have to be declared by the programmer?__
- Type casting is a way to check the type of an instance, or to treat that instance as a different superclass or subclass from somewhere else in its own class hierarchy.   
- Type casting in Swift is implemented with the is and as operators. These two operators provide a simple and expressive way to check the type of a value or cast a value to a different type.    

**Downcasting (Two different forms)**
1. The conditional form, as?, returns an optional value of the type you are trying to downcast to.    
2. The forced form, as!, attempts the downcast and force-unwraps the result as a single compound action.      


**Type Casting for Any and AnyObject**    
Swift provides two special types for working with nonspecific types:    
- Any can represent an instance of any type at all, including function types.   
- AnyObject can represent an instance of any class type.    

Example:    
var things = Any ()   
things.append(0)  // integer    
things.append(0.0)  // float    
things.append("hello")  // string   

    















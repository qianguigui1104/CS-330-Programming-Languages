
// Pam Qian
//PLP 4
// Simple Statements

import UIKit

// Part 1 one-condition if-else statement

var happy:Bool = true
if happy {
    print("Fantastic!")
} else {
    print ("I hope you feel better!")
}


// Part 2 multi-conditions if-else statement
let gpa = 4.0
let myGrade = 3.8
if happy || gpa == 4.0 {
    print ("Well done!")
} else if !happy && gpa < 4.0 {
    print ("Feel better!")
} else if (gpa == 4.0 || myGrade > 3.9) && happy {
    print ("Good scores!")
} else {
    print ("You got this!")
}


// Part 3 different kinds of loops
// 1. For-In loop
for counter in 1...5 {
    print (counter)
}

for _ in 1...5 {
    print ("Hello")
}

// 2. While loop
let max = 20
var sum = 0
while sum < max {
    sum += 2
}
print (sum)

// 3. Repeat-While loop
sum = 0
repeat {
    print ("Hello")
    sum += 3
} while sum < max
print (sum)


// Part 4 Switch cases
var someCharacter: Character = "a"

switch someCharacter {
case "a":
    print("is an A")
case "b", "c":
    print ("is a B or C")
default:
    print ("Some fallback")
}


// Part 5 Break and Continue
let x = 0

switch x {
case 0:
    break;
case 1:
    print("One for the money...")
case 2:
    print("Two for the road...")
default:
    print("Any other values");
}
print("Finished")


outer: for i in 1...3 {
    inner: for j in 1...3 {
        if j > 2 {
            continue outer
        }
        print("i: \(i)  j: \(j)")
    }
}



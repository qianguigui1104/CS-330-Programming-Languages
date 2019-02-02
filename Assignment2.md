__1. Can this language be installed on any operating system? Which ones (Windows,
Mac, Unix/Linux)? If not, what are its limitations?__   

Swift can be installed on MacOS and Unix/Linux, but until now no 
official open source port to Windows is available or announced. However, Windows users
can either use a [SwiftForWindows compiler](https://swiftforwindows.github.io/) or run the MacOS on a virtual machine in order
to programin in Swift.

__2.Give instructions for how to install the language.__

Swift is available as part of Xcode (IDE for swift). For mac users, Xcode is pre-installed already so 
they do not need to download or install anything to use swift. 
For Linux users, they can download Swift for Ubuntu [here](https://swift.org/download/#releases).

__3. Where do you write programs in this language (e.g.: in: in a text editor, a special
editor just for that language, or something else?)__

As mentioned in the previous answer, Xcode is the recommended programming environment for Swift.
However, developers can also use Notepad++, Sublime, or other text editors to write in Swift but 
additional compilers are required. 

__4. How do you run programs that you write?__

Xcode provides a couple project options, including _playground_ projects and and Xcode projects. For now, I am sill 
using the _playground_ project. _Playgrounds_ execute automatically by default, meaning programmers can write code 
and immediately see the output. This control allows developers to execute the playground again. Holding down the ▶︎ (Execute) 
button to switch between automatic execution and manual execution modes. Alternatively, developers can force a 
re-execution by clicking Editor ▸ Run Playground in the menu bar.

I believe it will be different to build with Xcode projects. I expect I will need to use a virtual machine
(iOS) to run my mobile applications.


__5. Is there a lot of boiler-plate code needed to write a program (e.g. Java)? Or can you
just start writing (e.g. Python and Perl)?__

No. Swift is easy to use and allows developers to just start writing.

__6. How do you write comments in your language?__    
Single line comment:  
//this is a comment

Block comment:   
/*    
This  
is a  
multiple-line   
comment*/     

_(Reference for answers to problem 4 and 6:     
https://www.raywenderlich.com/6338-swift-tutorial-part-1-expressions-variables-and-constants)_

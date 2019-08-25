# General
This is an excercise where one puts their programming skills to the test. It can be used for any programming language, however here it is explained and solved in English & Python 3 ;).  
Note that this excercise should not take more than 20-25 minutes to finish by yourself.  


# Characterizing the excercise
Mimic an API for a counter program that receives a number and has two possible functionalities:  
1) Increment the number by 1, and if the number reaches 100 then the next increment should be 0.  
2) Reset the counter to the original number the user entered.  

Write several test cases that prove the functionality of the program.  


# Solution Workflow
* Define a class for the counter in order to mimic an API.  
* In the constructor method (__init__) define two members - current counter value and initial counter value. The current counter value represents a dynamically changing value according to the user's usage of the program while the initial counter value represents the original number inputted by the user into the program.  
* Create two methods - next() and reset(), each one with the required functionality as described in the characterization of the excercise.  
* Write several test cases using the "assert" statement checking the functionality of each method in the class.  

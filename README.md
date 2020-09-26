# linear_system
Simple python code written in order to solve linear system considering that it might be represented as a matrix equation Ax = b. So firstly the system's size has to be informed and then the user must enter with matrix's A coefficients and vector's b coefficients respectively. Sooner the program will output the result x as an array.

The code was developed by using python language and some of its packtes(libs). The most important one is numby because it is responsable to calculate the final result x as the coefficients from A and b are given as parameters to linalg.solve's method argument while this method is part of numpy packet and called by typing the follow syntax: numpy.linalg.solve().

Before passing A and b cofficients to linalg.solve's method they has to be transformed in variables with array type. So in order to do that another method from numpy is called: .array(). Its functionality allows to convert a list passed as a parameters in an array with the same elements and by doing that the method .linalg.solve() can receive the coefficients and gives as output the vector solution x.

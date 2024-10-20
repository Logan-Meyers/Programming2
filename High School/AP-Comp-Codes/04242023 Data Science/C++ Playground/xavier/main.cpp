// imports
#include <iostream>

// main function, tells c++ what to run
int main() {
    // set int prod to initial value, 1
    int prod = 1;
    // for loop:
        // int n set to 1
        // run for loop while n is less than/equal to 4
        // increment n by 1 after each run
    for ( int n=1; n<=4; n++ ) {
        // assign prod to itself, times (2 times n)
        prod *= 2*n;
        // print-outs
        std::cout << "For loop! N is: " << n << ", we're multiplying by: " << (2*n) << ", and sum is now: " << prod << "\n";
    }
    // final print-out
    std::cout << "Final sum: " << prod << "\n";
}
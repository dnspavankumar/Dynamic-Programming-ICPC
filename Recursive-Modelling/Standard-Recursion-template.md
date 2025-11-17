<h1>Recursion Modelling</h1>

```c++
int recursion(int argument){
    //pruning
    if(impossible_case)return a_value_that_doesnot_affect_result;
    //basecase
    if(base_case)return known_result;
    //f could be any function which has recursive call 
    //for example f(rec(new arg)) = rec(n-1)+rec(n-2)<--fibonacci
    return f(recursion(new argument));
}
```
****Pruning****:
Pruning refers to safely removing certain branches of the recursion tree when they cannot contribute to a valid result.

If a recursive function encounters a value that is impossible given the constraints, or one for which the result cannot be computed, that value should be pruned.
However, since a recursive function must return a value of its defined type, you return a placeholder that does not affect the final answer.

****Base-Case****:
A base case is a condition at which the recursion stops. It must directly return a known, computable result.
Ensuring correct base cases is crucial — without them, the recursion will never terminate.

***Base-Case when Exception***
Sometimes a recurrence relation does not apply under specific conditions. These exceptions should always be treated as base cases.
for example,
```cpp
    fib(1)!= fib(0) + fib(-1)
```
Even though this is not a mathematical exception, the recurrence relation fails here, so fib(1) and fib(0) must be base cases.

****Example****:

```c++  
int fibonacci(int n){
/*if n is negative there is no fibobnacci for negative number hence prune it by returning -1*/
    if(n<0)return -1;
    //base case
    if(n<2)return n;
    //recursive call 
    return fibonacci(n-1) + fibonacci(n-2);
}
<h1>4.Variations of Query</h1>
<h3>Problem Statement</h3>
You are standing at stair 0 and your goal is to reach the stair n and you are a tall guy who can take 1,2, or 3 steps at any stair 

1.return the total number of ways of reaching the nth stair(counting)

2.return whether you can ever reach the nth stair(validation)

3.if each step has a cost c[i] return the minimum cost to reach the nth stair(minimization)

4.if each step has a loot l[i] return the maximum loot you can grab reach the nth stair(maximization)

<h4>Counting</h4>

In counting problems to prune something we often return 0

And on reaching the goal we return 1

this is very naive but it works

now for this problem I just need to add all the choices to get the count of number of ways to reach the goal

```c++
int countWays(int n){
    if(n==0){
        return 1;
    }
    if(n<0){
        return 0;
    }
    return countWays(n-1)+countWays(n-2)+countWays(n-3);
}
```
<h4>Validation</h4>
In this if its a pruning case I would return false

And on reaching the goal we return true

```c++
bool canReach(int n){
    if(n==0){
        return true;
    }
    if(n<0){
        return false;
    }
    return canReach(n-1)||canReach(n-2)||canReach(n-3);
}
```

<h4>Minimization</h4>
In this if its a pruning case I would return INT_MAX

And on reaching the goal we return 0

```c++
int minCost(int n,vector<int>&costs){
    if(n==0){
        return 0;
    }
    if(n<0){
        return INT_MAX;
    }
    return costs[n]+min(minCost(n-1,costs)+minCost(n-2,costs)+minCost(n-3,costs));
}
```

<h4>Maximization</h4>
In this if its a pruning case I would return INT_MIN

And on reaching the goal we return 0

```c++
int maxLoot(int n,vector<int>&loots){
    if(n==0){
        return 0;
    }
    if(n<0){
        return INT_MIN;
    }
    return loots[n]+max(maxLoot(n-1)+maxLoot(n-2)+maxLoot(n-3));
}
```
And yeah since pruning and base case are independent they can be written in any order
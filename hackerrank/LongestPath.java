package hackerrank;

// Our chef lately has become quite good with shortest path problems. Dijkstra, 
// Floyd Warshall, Bellman Ford, you name it, he knows it all! You are designing a 
// contest for him and have been thinking of a difficult problem for days. Finally you 
// decide that you will have to surprise the chef by giving him the longest path problem instead.

// The problem consists of n cities and m roads of the form [a b c] which implies that 
// there is a one-way road from city a to city b having cost of travel c. 
// Also, a pair of cities [a,b] is called "friendly" if a is reachable from b and vica versa. 
// Whenever moving between a pair of friendly cities, we must travel without incurring any cost. 
// You ask the chef to find the maximum cost of travelling possible in your graph.

// Our chef, comes to you for help. Can you help him?

// Input Format

// First line contains T, the no. of test cases.

// Each test case consists of n amd m on the first line.

// Each of the next m lines consist of 3 space seperated integers of the form a b c implying there is an edge from a to b of cost c.

// Constraints

// T <= 10

// 2 <= n <= 10^5

// 1 <= m <= 10^6

// 1 <= c <= 10^8

// 0 <= a,b <= n-1

// Huge IO warning - Use appropriate input methods

// Output Format

// For each test case output a single line containing the answer to the problem.

// Sample Input

// 1

// 6 6

// 0 1 2

// 1 2 3

// 2 4 4

// 3 1 5

// 4 3 6

// 4 5 1

// Sample Output

// 3

// Explanation

// The maximum cost of traveling is between cities 0 and 5 having a value 3. Here is one of the possible paths -
// 0->1 (not frendly) cost = 2
// 1->2 (friendly) cost = 0
// 2->4 (friendly) cost = 0
// 4->5 (not friendly) cost = 1
// Total cost = 2+1 = 3

public class LongestPath {
    
}

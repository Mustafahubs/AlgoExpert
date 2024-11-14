## Three Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.
If no three numbers sum up to the target sum, the function should return an empty array.

### Sample Input
```python
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
```
### Sample Output
```python
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
```
### Hints
**Hint 1**
Using three for loops to calculate the sums of all possible triplets in the array would generate an algorithm that runs in O(n^3) time, where n is the length of the input array. Can you come up with something faster using only two for loops?

**Hint 2**
Try sorting the array and traversing it once. At each number, place a left pointer on the number immediately to the right of your current number and a right pointer on the final number in the array. Check if the current number, the left number, and the right number sum up to the target sum. How can you proceed from there, remembering the fact that you sorted the array?

**Hint3**
Since the array is now sorted (see Hint #2), you know that moving the left pointer mentioned in Hint #2 one place to the right will lead to a greater left number and thus a greater sum. Similarly, you know that moving the right pointer one place to the left will lead to a smaller right number and thus a smaller sum. This means that, depending on the size of each triplet's (current number, left number, right number) sum relative to the target sum, you should either move the left pointer, the right pointer, or both to obtain a potentially valid triplet.

**Optimal Space & Time Complexity**
O(n^2) time | O(n) space - where n is the length of the input array

## Tests
Test Case 1
```python
{
	"array":  [12,  3,  1,  2,  -6,  5,  -8,  6],
	"targetSum":  0 
}
```
Test Case 2
```python
{
	"array":  [1,  2,  3],  
	"targetSum":  6
}
```
Test Case 3
```python
{
	"array":  [1,  2,  3],
	"targetSum":  7
}
```
Test Case 4
```python
{
	"array":  [8,  10,  -2,  49,  14],
	"targetSum":  57
}
```
Test Case 5
```python
{
	"array":  [12,  3,  1,  2,  -6,  5,  0,  -8,  -1],
	"targetSum":  0
}
```
Test Case 6
```python
{
	"array":  [12,  3,  1,  2,  -6,  5,  0,  -8,  -1,  6],
	"targetSum":  0
}
```

## Solution
```python
def threeNumberSum(array, targetSum):
	# Write your code here.
	pass
```

## Video Explanation
**Link:**  
https://youtu.be/WbYRG6qpoKI

**Note:**
The first step in the solution is to sort the input array. Why is the  _O(nlog(n))_  runtime of the sorting step not reflected in the overall time complexity of the algorithm?
The nested loops in the solution run in  _O(n^2)_  time; this dwarfs the  _O(nlog(n))_  runtime of the sorting step and allows us to remove it from the final time complexity of the algorithm.
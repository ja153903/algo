from ...src.google_interview_prep.interview_process.fruits_into_baskets import Solution

solution = Solution()

def test_fruits_into_baskets_bf_case1():
    fruits = [1, 2, 1]
    assert solution.brute_force(fruits) == 3

def test_fruits_into_baskets_bf_case2():
    fruits = [0, 1, 2, 2]
    assert solution.brute_force(fruits) == 3

def test_fruits_into_baskets_bf_case3():
    fruits = [1, 2, 3, 2, 2]
    assert solution.brute_force(fruits) == 4

def test_fruits_into_baskets_case1():
    fruits = [1, 2, 1]
    assert solution.totalFruit(fruits) == 3

def test_fruits_into_baskets_case2():
    fruits = [0, 1, 2, 2]
    assert solution.totalFruit(fruits) == 3

def test_fruits_into_baskets_case3():
    fruits = [1, 2, 3, 2, 2]
    assert solution.totalFruit(fruits) == 4

def test_fruits_into_baskets_case3():
    fruits = [3,3,3,1,2,1,1,2,3,3,4]
    assert solution.totalFruit(fruits) == 5

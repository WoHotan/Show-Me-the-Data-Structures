1. Use recursion to find the user in group, because each group may contain a different number of subgroups.Assuming that a goup have m users, and have n subgoups.And the recursion depth is k, time complexity is (m + n) * k, when the 
recursion depth k is close to n, the worst time complexity is O(n^2).
2. In this function, we only search the files and return value, so the space complexity is O(1).

1. Use double linked list to store LRU cache info.
2. Because double linked list search time complexity is not O(1),
   use a dict handle it, and then, we can get the element in O(1).
3. The time complexityof get() and set() function are O(1).
4. The linked list need linear space, assuming the length of the linked list is n,
   space complexity is O(n).
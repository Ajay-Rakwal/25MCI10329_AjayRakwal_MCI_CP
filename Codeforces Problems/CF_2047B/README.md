## Submission

<img width="361" height="248" alt="Screenshot 2026-02-05 191752" src="https://github.com/user-attachments/assets/dc885bda-3bc6-4946-af26-728ef5da3eae" />


## Thought Process

1. For each test case, I first read the value of n and the string s.

2. I created a list called seen to store all unique characters of the string in the order in which they appear.

3. If the number of unique characters is less than two, then no useful replacement can be made, so I print the string as it is and move to the next test case.

4. I initialized the maximum frequency using the first unique character and the minimum frequency using the second unique character from the seen list, along with their corresponding indices.

5. I then traversed the string from left to right and calculated the frequency of each character.

6. During traversal, if a character with a higher frequency than the current maximum was found, I updated the maximum frequency and its index.

7. Similarly, if a character with a lower frequency than the current minimum was found, I updated the minimum frequency and its index.

8. After identifying the characters with maximum and minimum frequencies, I replaced the character at the minimum-frequency index with the character at the maximum-frequency index.

9. Finally, I printed the modified string, which minimizes the number of distinct permutations after performing exactly one operation.

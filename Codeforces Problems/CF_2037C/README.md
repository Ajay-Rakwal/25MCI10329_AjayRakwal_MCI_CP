
## Submission 
<img width="390" height="196" alt="image" src="https://github.com/user-attachments/assets/f09548f9-7cbb-4bd6-85b8-76bd5417f7cd" />




## 🧠 Thought Process

1. First, I observed that for very small values of n (less than 5), it is not possible to form a valid arrangement using the intended pattern, so I directly output -1 for these cases.

2. Initially, I tried printing all even numbers first followed by all odd numbers. However, this approach failed for certain values of n because the required condition was not satisfied in some edge cases.

3. On analyzing the failing cases, I noticed that the numbers 4 and 5 were causing the issue when placed in the general even–odd order.

4. To fix this, I decided to handle 4 and 5 separately by placing them together in the sequence.

5. I then printed all even numbers except 4, followed by the pair 4 5, and finally printed all odd numbers except 5.

6. This adjustment resolved the errors in the failing cases and ensured that all numbers from 1 to  n appeared exactly once in a valid order.

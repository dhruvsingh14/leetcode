"""
Number of Students Unable to Eat Lunch

Problem: LeetCode 1700 - Number of Students Unable to Eat Lunch
Pattern: Queue + Stack Simulation

Key Insights:
- Students form a queue (FIFO) - front student tries to take sandwich first
- Sandwiches form a stack (LIFO) - only top sandwich is accessible
- If front student likes top sandwich: both removed (student eats)
- If front student doesn't like it: student goes to back of queue
- Deadlock occurs when all remaining students have cycled through once
  without anyone taking a sandwich (no one wants the current top sandwich)

Stopping Condition:
- Use a counter to track consecutive rejections
- If counter reaches queue length, all students have rejected current sandwich
- This means remaining students will never match remaining sandwiches
- Return the number of students still in queue

Why This Approach Works:
- Simulates the actual process described in the problem
- Counter prevents infinite loops (detects when no progress is possible)
- When a match is found, counter resets (progress made, keep trying)
- When counter == queue length, we've gone full circle with no matches

Time Complexity: O(n²) worst case - each student might cycle through queue multiple times
Space Complexity: O(n) - storing queue and stack

Alternative Approach:
- Could use counting: count preferences in students vs what's needed in sandwiches
- If a sandwich type is needed but no students want it, those students can't eat
- Would be O(n) time, but this simulation approach is more intuitive
"""

'''
Approach:
Well, first for the data structure. It says in the question that the sandwiches are placed in a stack. Therefore that's how I'll store the sandwiches, in a stack. The student I believe are in a queue, since this question is part of the section on queues, of a DSA practice course.
So, stack will be implemented using a list. Queue will be implemented using a singly linked list.
Next, for each element: at the top of the stack, and at the left most side of the queue, we compare for equality. If it's a match, we dequeue from the queue and detach, and pop from the stack.
If it's not a match, we dequeue from the queue anyway, but enqueue the same person to the end of the queue. 
As for our stopping condition. Well, we'll want to loop through the queue at least once. But we'll also want to loop through it again. The key is figuring out the stopping condition. I'm not quite sure how to ensure that all elements in the queue have been exposed to all options in the stack. But that's what we'll want to do to ensure there's nothing left remaining to check.
Lastly, if there are any elements remaining in the queue or in the stack, unmatched, should be the same length, we return the length, and say that many students were unable to eat.

reference
q = deque(list) — create a deque from a list
q.append(x) — add to the right end
q.popleft() — remove and return from the left end
q.appendleft(x) — add to the left end
q.pop() — remove and return from the right end
len(q) — get the length
'''


from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Count how many students are unable to eat lunch.
        
        Time Complexity: O(n²) - worst case, students cycle through queue multiple times
        Space Complexity: O(n) - storing queue and reversed stack
        
        Args:
            students: List[int] - preferences of students in queue order (0 or 1)
            sandwiches: List[int] - types of sandwiches in stack order (0 or 1)
            
        Returns:
            int - number of students unable to eat
            
        Strategy:
            1. Convert students to deque (queue) for efficient front/back operations
            2. Reverse sandwiches list to treat it as a stack (last element = top)
            3. Use counter to track consecutive students who rejected sandwich
            4. If front student wants top sandwich:
               - Remove both (student eats)
               - Reset counter (progress made)
            5. If front student doesn't want it:
               - Move student to back of queue
               - Increment counter
            6. If counter == queue length:
               - Full cycle with no matches = deadlock
               - Return remaining students
               
        Example Walkthrough:
            students = [1,1,0,0], sandwiches = [0,1,0,1]
            
            Queue: [1,1,0,0], Stack top: 0, counter: 0
            - Student 1 doesn't want 0 → move to back → [1,0,0,1], counter: 1
            
            Queue: [1,0,0,1], Stack top: 0, counter: 1
            - Student 1 doesn't want 0 → move to back → [0,0,1,1], counter: 2
            
            Queue: [0,0,1,1], Stack top: 0, counter: 2
            - Student 0 wants 0 → both removed → [0,1,1], Stack: [1,0,1], counter: 0
            
            ... continues until all matched ...
            
            Result: 0 students unable to eat
        """

        stu_q = deque(students)  # Convert students list to deque (queue)
        sand_st = sandwiches[::-1]  # Reverse sandwiches to treat as stack (pop from end)
        counter = 0  # Track consecutive students who rejected current sandwich
        
        # Continue while students remain AND we haven't gone full circle without a match
        while stu_q and counter < len(stu_q):
            # Check if front student wants top sandwich
            if stu_q[0] == sand_st[-1]:  # Match found!
                stu_q.popleft()  # Remove student from front (they eat)
                sand_st.pop()  # Remove sandwich from top of stack
                counter = 0  # Reset counter (progress made, keep trying)
            else:  # No match
                stu_unmatched = stu_q.popleft()  # Remove student from front
                stu_q.append(stu_unmatched)  # Add same student to back of queue
                counter += 1  # Increment counter (one more rejection in a row)
                
        # When loop exits, either:
        # 1. stu_q is empty (all students ate) → return 0
        # 2. counter == len(stu_q) (deadlock) → return remaining students
        return len(stu_q)  # Number of students unable to eat
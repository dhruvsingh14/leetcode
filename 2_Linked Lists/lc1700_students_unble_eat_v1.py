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

        stu_q = deque(students)
        sand_st = sandwiches[::-1]
        counter = 0
        while stu_q and counter < len(stu_q):
            if stu_q[0] == sand_st[-1]:
                stu_q.popleft()
                sand_st.pop()
                counter = 0
            else:
                stu_unmatched = stu_q.popleft()
                stu_q.append(stu_unmatched)
                counter += 1
        return len(stu_q)









        
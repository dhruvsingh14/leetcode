"""
Browser History Implementation Using Doubly Linked List

Problem: LeetCode 1472 - Design Browser History
Pattern: Doubly Linked List with Current Pointer

Key Design Decisions:
- Uses doubly linked list for bidirectional navigation
- Dummy head and tail sentinels to simplify boundary checks
- 'curr' pointer tracks current webpage position
- visit() clears forward history by breaking the chain

Why Doubly Linked List:
- Need to traverse both forward (next) and backward (prev)
- Perfect match for browser forward/back navigation
- O(1) insertion when visiting new page
- O(min(steps, history_length)) for back/forward operations

Structure Example:
    head <-> leetcode.com <-> google.com <-> facebook.com <-> tail
             ^                ^               ^
             page1            page2           curr (current page)

After visit("linkedin.com"):
    head <-> leetcode.com <-> google.com <-> facebook.com <-> linkedin.com <-> tail
                                             ^                 ^
                                             old curr          new curr
    (Everything after old curr is cleared/unreachable)

Operations Time Complexity:
- __init__: O(1) - initialize with homepage
- visit(url): O(1) - insert new node and update curr
- back(steps): O(min(steps, pages_back)) - traverse backward
- forward(steps): O(min(steps, pages_forward)) - traverse forward

Space Complexity: O(n) where n is number of unique pages visited

Real-World Application:
- Actual browser history implementation
- Undo/redo functionality in text editors
- Music player navigation (previous/next track)
- Any sequential navigation with bidirectional movement

Alternative Approaches:
1. Array/List with index pointer (simpler but less elegant)
2. Two stacks (back stack + forward stack)
This solution uses doubly linked list for natural forward/back semantics
"""


class ListNode:
    """
    A node in the browser history doubly linked list.
    
    Each node represents a webpage (URL) in the browsing history.
    """
    
    def __init__(self, url: str):
        """
        Initialize a history node with a URL.
        
        Args:
            url: str - the webpage URL (or None for dummy nodes)
        """
        self.val = url  # URL of the webpage (None for dummy head/tail)
        self.next = None  # Pointer to next page in history (forward)
        self.prev = None  # Pointer to previous page in history (back)


class BrowserHistory:
    """
    Browser history implementation using doubly linked list.
    
    Maintains current position and allows forward/backward navigation.
    Visiting a new page clears all forward history.
    """

    def __init__(self, homepage: str):
        """
        Initialize browser history with a homepage.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Args:
            homepage: str - the initial page to start on
            
        Initial Structure:
            head <-> homepage <-> tail
                     ^
                     curr
        """
        '''
        Approach: 
        If we use a doubly linked list. 
        nodes can store url's as value.
        .next can navigate forward
        and .prev can navigate back
        we will also need a pointer to track which webpage we are on
        '''
        self.head = ListNode(None)  # Dummy head sentinel
        self.tail = ListNode(None)  # Dummy tail sentinel
        self.curr = ListNode(homepage)  # Current page pointer (starts at homepage)

        # Link head -> curr
        self.head.next = self.curr
        self.curr.prev = self.head

        # Link curr -> tail
        self.curr.next = self.tail
        self.tail.prev = self.curr

    def visit(self, url: str) -> None:
        """
        Visit a new URL from the current page. Clears all forward history.
        
        Time Complexity: O(1) - constant pointer updates
        Space Complexity: O(1) - creating one new node
        
        Args:
            url: str - the new page to visit
            
        Strategy:
            1. Create new node for the URL
            2. Insert it after current page
            3. Point it to tail (clearing any forward history)
            4. Update curr to the new page
            
        Example:
            Current state: head <-> A <-> B <-> C <-> tail (curr at B)
            After visit("D"): head <-> A <-> B <-> D <-> tail (curr at D)
            Note: C is now unreachable (forward history cleared)
            
        Key Behavior:
            This mimics real browser behavior - when you visit a new page
            while in the middle of history, all forward pages are lost.
        """
        newNode = ListNode(url)  # Create new page node
        
        # Insert new node after current page
        self.curr.next = newNode
        newNode.prev = self.curr

        # Point new node to tail (no forward history beyond this)
        newNode.next = self.tail
        self.tail.prev = newNode

        # Move current pointer to the new page
        self.curr = newNode

    def back(self, steps: int) -> str:
        """
        Move back in history by the specified number of steps.
        
        Time Complexity: O(min(steps, pages_available)) - traverse backward
        Space Complexity: O(1) - no additional space
        
        Args:
            steps: int - number of pages to go back
            
        Returns:
            str - URL of the page after moving back
            
        Strategy:
            1. Move curr pointer backward 'steps' times
            2. Stop early if we hit the dummy head (no more history)
            3. Return the URL we land on
            
        Example:
            History: head <-> A <-> B <-> C <-> D <-> tail (curr at D)
            back(2): moves to B, returns "B"
            back(10): moves to A (only 3 steps available), returns "A"
            
        Edge Cases:
            - steps > available history: goes back as far as possible
            - already at oldest page: stays at same page
        """
        i = 0  # Counter for steps taken
        
        # Move backward 'steps' times or until we hit the head dummy
        while i < steps and self.curr.prev != self.head:
            self.curr = self.curr.prev  # Move back one page
            i += 1
            
        return self.curr.val  # Return URL of current page

    def forward(self, steps: int) -> str:
        """
        Move forward in history by the specified number of steps.
        
        Time Complexity: O(min(steps, pages_available)) - traverse forward
        Space Complexity: O(1) - no additional space
        
        Args:
            steps: int - number of pages to go forward
            
        Returns:
            str - URL of the page after moving forward
            
        Strategy:
            1. Move curr pointer forward 'steps' times
            2. Stop early if we hit the dummy tail (no more forward history)
            3. Return the URL we land on
            
        Example:
            History: head <-> A <-> B <-> C <-> D <-> tail (curr at A)
            forward(2): moves to C, returns "C"
            forward(10): moves to D (only 3 steps available), returns "D"
            
        Edge Cases:
            - steps > available forward history: goes forward as far as possible
            - already at newest page: stays at same page
            - no forward history (just visited a page): stays at current page
        """
        i = 0  # Counter for steps taken
        
        # Move forward 'steps' times or until we hit the tail dummy
        while i < steps and self.curr.next != self.tail:
            self.curr = self.curr.next  # Move forward one page
            i += 1
            
        return self.curr.val  # Return URL of current page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
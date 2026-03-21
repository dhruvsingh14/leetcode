"""
Encode and Decode Strings

Problem: LeetCode 271 - Encode and Decode Strings (Premium)
Pattern: String Manipulation + Length Prefix Protocol
Concept: Serialization and Deserialization

Problem Statement:
Design an algorithm to encode a list of strings to a single string, and decode 
that single string back to the original list of strings.

Challenge:
- Strings can contain ANY characters (including delimiters like commas, spaces)
- Strings can be empty
- Need to unambiguously encode/decode without information loss

Why Simple Delimiters Don't Work:
❌ Join with comma: ["abc", "d,ef"] → "abc,d,ef" → ambiguous!
❌ Join with newline: ["abc", "d\nef"] → same problem
❌ Any single delimiter: string might contain that delimiter

Solution: Length-Prefix Protocol
✓ Format: <length>#<string><length>#<string>...
✓ Example: ["abc", "de"] → "3#abc2#de"
✓ Length tells us exactly how many characters to read
✓ Works even if strings contain '#' or numbers!

Encoding Format Explanation:
    ["hello", "world"] → "5#hello5#world"
     ^                    ^^    ^^
     string               length  length
                          prefix  prefix

Example with Special Characters:
    ["a#b", "cd"] → "3#a#b2#cd"
                     ^^^^^
                     The # inside "a#b" is part of data, not delimiter
                     We know to read exactly 3 characters after first #

Example with Empty Strings:
    ["", "a", ""] → "0#1#a0#"
                     ^^    ^^
                     empty empty

Time Complexity:
- encode(): O(n) where n = total characters across all strings
- decode(): O(n) where n = length of encoded string
- Both are linear and optimal (must touch each character)

Space Complexity:
- encode(): O(n) for building result string
- decode(): O(n) for building result list
- Both use linear space (unavoidable for output)

Why This Encoding Works:
1. Length prefix tells us EXACTLY how many chars to read
2. The '#' delimiter separates length from actual string data
3. No ambiguity: even if string contains '#' or numbers, we know the length
4. Deterministic: same input always produces same encoding

Algorithm Visualization for encode(["abc", "de"]):
    
    Start: res = ""
    
    Process "abc":
    - Length = 3
    - res = "3#abc"
    
    Process "de":
    - Length = 2
    - res = "3#abc2#de"
    
    Return: "3#abc2#de"

Algorithm Visualization for decode("3#abc2#de"):
    
    i=0: Find # at j=1
    - Length = int("3") = 3
    - Read 3 chars starting after #: "abc"
    - res = ["abc"]
    - Move i to position after "abc"
    
    i=5: Find # at j=6
    - Length = int("2") = 2
    - Read 2 chars starting after #: "de"
    - res = ["abc", "de"]
    
    Return: ["abc", "de"]

Edge Cases Handled:
✓ Empty list: encode([]) → "" → decode("") → []
✓ Empty strings: encode(["", ""]) → "0#0#" → decode → ["", ""]
✓ Strings with numbers: encode(["123"]) → "3#123" (unambiguous)
✓ Strings with #: encode(["#"]) → "1##" (first # is delimiter)
✓ Very long strings: length prefix can be multi-digit ("100#...")

Interview Discussion Points:
- Why we need length prefix (delimiters fail for arbitrary strings)
- How this is similar to network protocols (HTTP Content-Length header)
- Alternative: escape characters (more complex, less efficient)
- This pattern appears in file formats, serialization, network protocols

Real-World Applications:
- Network protocols (TCP, HTTP use similar techniques)
- File formats (many binary formats use length prefixes)
- Database serialization
- Message queuing systems
- Any system that needs to transmit strings with arbitrary content

Common Mistakes to Avoid:
❌ Using simple delimiter without escaping
❌ Not handling empty strings
❌ Off-by-one errors in decode (pointer arithmetic is tricky!)
❌ Not considering strings that contain the delimiter
"""


class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encode a list of strings into a single string using length-prefix protocol.
        
        Time Complexity: O(n) where n = total characters in all strings
        Space Complexity: O(n) for building result string
        
        Args:
            strs: List[str] - list of strings to encode (can contain any characters)
            
        Returns:
            str - encoded string in format: <length>#<string><length>#<string>...
            
        Encoding Format:
            Each string is prefixed with its length and a '#' delimiter
            Example: ["abc", "de"] → "3#abc2#de"
            
        Why This Works:
            - Length prefix tells decoder exactly how many chars to read
            - '#' separates length from actual string data
            - Even if string contains '#', we know to read <length> chars
            
        Examples:
            encode(["abc", "de"]) → "3#abc2#de"
            encode([""]) → "0#"
            encode(["#", "a#b"]) → "1##3#a#b"
            encode([]) → ""
            
        Edge Cases:
            - Empty list: returns ""
            - Empty strings: encoded as "0#"
            - Strings with special chars: handled correctly
        """
        res = ""  # Result string to build
        
        # Process each string in the list
        for s in strs:
            # Append length + delimiter + actual string
            # Format: <length>#<string>
            # str(len(s)) converts length to string
            # "#" is the delimiter between length and data
            res += str(len(s)) + "#" + s
            
        return res  # Return the encoded string
    
    def decode(self, s: str) -> List[str]:
        """
        Decode a single encoded string back into a list of strings.
        
        Time Complexity: O(n) where n = length of encoded string
        Space Complexity: O(n) for building result list
        
        Args:
            s: str - encoded string in format: <length>#<string><length>#<string>...
            
        Returns:
            List[str] - original list of strings
            
        Decoding Algorithm:
            1. Find the '#' delimiter to extract length
            2. Parse length as integer
            3. Read exactly <length> characters after '#'
            4. Append to result list
            5. Move pointer past the string we just read
            6. Repeat until end of encoded string
            
        Examples:
            decode("3#abc2#de") → ["abc", "de"]
            decode("0#") → [""]
            decode("1##3#a#b") → ["#", "a#b"]
            decode("") → []
            
        Pointer Movement:
            i: marks start of current length prefix
            j: scans forward to find '#' delimiter
            After finding '#':
            - Parse length from s[i:j]
            - Read string from s[j+1:j+1+length]
            - Move i past the string we just read
            
        Edge Cases:
            - Empty encoded string: returns []
            - Encoded empty strings: correctly extracts ""
            - Multi-digit lengths: correctly parses
        """
        res = []  # Result list to build
        i = 0  # Pointer to start of current segment
        
        # Process the entire encoded string
        while i < len(s):
            j = i  # j will scan forward to find '#'
            
            # Find the '#' delimiter
            # Everything from i to j is the length prefix
            while s[j] != '#':
                j += 1  # Move j forward until we hit '#'
            
            # Extract and parse the length
            # s[i:j] is the length as a string (e.g., "3")
            # Convert to integer to know how many chars to read
            length = int(s[i:j])
            
            # Move i past the '#' delimiter
            # Now i points to the start of the actual string data
            i = j + 1
            
            # Calculate end position of current string
            # We need to read exactly 'length' characters
            j = i + length
            
            # Extract the string and append to result
            # Read from position i for 'length' characters
            res.append(s[i:j])
            
            # Move i past the string we just extracted
            # Position i for the next length prefix
            i = j
            
        return res  # Return the decoded list of strings
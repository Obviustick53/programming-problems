# Valid parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Solution:
    def isValid(self, s: str) -> bool:

        # String of odd length is invalid
        if len(s) % 2 != 0:
            return False

        closing_to_opening = {")": "(", "]": "[", "}": "{"}

        stack = []

        for char in s:
            if char in closing_to_opening:
                # There are not a opening available o the type is incorrect.
                if not stack or stack.pop() != closing_to_opening[char]:
                    return False
            else:
                stack.append(char)

        return not stack


solution = Solution()

print(solution.isValid("([)]"))

# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((i, next))
            pass

        if next in ")]}":
    
            if not len(opening_brackets_stack):
                return i+1
            
            _, top = opening_brackets_stack.pop()
            if not(are_matching(top, next)):
                return i+ 1
            # Process closing bracket, write your code here
            pass
    if len(opening_brackets_stack):
        return opening_brackets_stack[-1][0] + 1
    return 'Success'

def main():
 
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()

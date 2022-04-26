from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    for i in range(len(pattern)):
        table[pattern[i]] = max(1, len(pattern) - i - 1)
    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)

    def decide_slide_width(self, c: str) -> int:
        assert len(c) == 1
        raise Exception("TODO")
        return -1

    def search(self) -> int:
        # Set the search initial value i to be the len of pattern.
        i = len(self.pattern) - 1 
        while i < len(self.text):
            match = True 
            # Compare one character of the pattern at a time
            for j in range(len(self.pattern)):
                if self.text[i - j] != self.pattern[-1 - j]:
                    match = False  
                    # The search location will be moved to the next, so no further search will be performed.
                    break   
                    
            if match:   
                # Since the search is performed from the end, return the beginning position is performed.
                return i - len(self.pattern) + 1
            
            if self.text[i] in self.table:
                # Add up the amount of shifting the search location obtained from the previous result
                i += self.table[self.text[i]] 
            else:
                # If there is no particular target to shift, shift by the number of characters in the pattern
                i += len(self.pattern)
        return -1

from typing import List

def in_array(array1: List[str], array2: List[str])-> List[str]:
    return sorted(list({s1 for s1 in array1 if any(s1 in s2 for s2 in array2)}))
    
a1 = ["arp", "live", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))
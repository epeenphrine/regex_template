#%%

# check if words contain a string / string pattern
# returns None if match, returns re object if match

test = 'something 12345 yoyo'
message = 'nabbar'

import re

pattern_match1 = re.search('n[a-i0-9][a-g0-5][a-g0-5][a-e0-4]r', message.lower())
pattern_match2 = re.search('n[a-i0-9][a-g0-5][a-g0-5][a4]',test) 

print(pattern_match2)


#%%

# replace / substitute strings or string patternss
test = 'something 12345 yoyo'

import re
string_pattern = re.compile(r'[\n\t\r\s]') ## <- find spaces, tabs, newlines, and etc 
string_pattern2 = re.compile(r'something') 

new_string1 = string_pattern.sub("", test )
new_string2 = string_pattern2.sub("", test )

print(new_string1)
print(new_string2)
def _find_longest_match(string, window, index): 

    longest_match, window_index = 0, index

    if len(string) == 2: return 1
    
    for char in string: 

        if char != window[window_index]: break
        
        window_index  += 1
        longest_match += 1
        window = window + char
        
    return longest_match

def _find_triplet(string, search_buffer):
    
    length, offset = 0, 0
    search_buffer_size = len(search_buffer)

    for index, char in enumerate(search_buffer):
        
        if char != string[0]: continue
        
        actual_offset = search_buffer_size - index
        actual_length = _find_longest_match(string, search_buffer, index)

        if actual_length > length: 
            offset, length = actual_offset, actual_length

    length = min(len(string) - 1, length)  
    
    if length == 0: 
        offset = 0
    
    return offset, length, string[length]

def compress(string, windows_size = 22, lookahead_buffer_size = 7):

    search_buffer_size = windows_size - lookahead_buffer_size

    output        = [ (0, 0, string[0]) ]
    search_buffer = string[0]
    string        = string[1: ]

    while string: 
        offset, length, character = _find_triplet(string, search_buffer)
    
        search_buffer += string[ :length + 1]

        string = string[length + 1: ]
    
        output.append( (offset, length, character) )
        
        if len(search_buffer) <= search_buffer_size:  continue
        
        search_buffer = search_buffer[-search_buffer_size: ]
    
    return output


def decompress(compress_list):
    output = str()

    for element in compress_list:
        offset, length, character = element
        
        for _ in range(length):
            output += output[-offset]
        
        output += character
    
    return output 
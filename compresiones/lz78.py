def compress(string): 
    
    dictionary, key, output = dict(), str(), list()
    index = 1
    
    for i, char in enumerate(string, start=1):  
        key += char

        if key not in dictionary: 
            dictionary[key] = index    
        
            if len(key) > 1: 
                pos = dictionary[key[:-1]]
            else:
                pos = 0
        
            output.append( (pos, char) )

            key = str()
            index += 1

        elif i == len(string): 
            output.append( (dictionary[key], ) )
        
    return output

def decompress(compress_list):
    
    output = list()
    
    for element in compress_list: 
        
        try: 
            index, char = element
       
            if index == 0: 
                output.append(char)
            else: 
                output.append(output[index - 1] + char)
       
        except: 
            index = element[0]
            output.append(output[index - 1])

    return "".join(output)
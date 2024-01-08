from math  import log2, ceil

def histogram(string):
    output = dict()
    probability_unit = 1/len(string)
    
    for char in string:
        if char not in output: 
            output[char] = probability_unit
        else:
            output[char] += probability_unit
    
    return output


def codeword(word, length):
    binary_decimal = bin( int( word * (1 << length) ) )[2:]
    size_binary    = len(binary_decimal)

    if size_binary == length: return binary_decimal

    return "0" * (length - size_binary) + binary_decimal


def shannon_fano_elias(string):
    shanon_table        = histogram(string)
    frecuency_acc, prev = [0], 0
    output              = list()
    probability_list    = list()
    
    for _, prob in shanon_table.items(): 
        frecuency_acc   .append(prev + prob)
        probability_list.append(prob)
        prev += prob
    
    frecuency_acc = frecuency_acc[:-1]

    for acc, prob in zip(frecuency_acc, probability_list):
        word   = acc + prob/2
        length = ceil( log2(1/prob) ) + 1
        output.append( codeword(word, length) )
    
    return list( zip(shanon_table.keys(), output) )




def transpose_strings(strings_list):
    """
    ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
    →
    ['abc jkl stu', 'def mno vwx', 'ghi pqr yz']
    """
    
    word_lists = [s.split() for s in strings_list]
    transposed = list(zip(*word_lists))
    return [' '.join(words) for words in transposed]


result = transpose_strings(['abc def ghi', 'jkl mno pqr', 'stu vwx yz'])
print(result)

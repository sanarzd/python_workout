def hex_output_ord():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ').upper()
    
    for power, digit in enumerate(reversed(hexnum)):
        if '0' <= digit <= '9':
            value = ord(digit) - ord('0')
        elif 'A' <= digit <= 'F':
            value = ord(digit) - ord('A') + 10
        else:
            print(f"Error: {digit} is not valid")
            return
        
        decnum += value * (16 ** power)
    
    print(f"Result: {decnum}")

hex_output_ord()
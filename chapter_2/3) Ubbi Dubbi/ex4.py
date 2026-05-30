def url_encode(text):
    output = []
    for char in text:
        if char.isalnum():
            output.append(char)
        else:
            output.append(f'%{ord(char):02x}')
    return ''.join(output)

print(url_encode("Hello world!"))

import re

def main():
    fh = open('sparrow.text')
    #opens the text sparrow and reads it line by line
    for line in fh:
        match = re.search('sparrow', line)
        if match:
            #regex search...searching for regular expressions
            print(match.group())
if __name__ == "__main__":main()

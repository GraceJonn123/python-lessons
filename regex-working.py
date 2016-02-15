import re

def main():
    fh = open('sparrow.text')
    #opens the text sparrow and reads it line by line
    for line in fh:
            #regex search...searching for regular expressions
            match = (re.sub('sparrow', line), end =' ')
            if match:
                print (line.replace(match.group(), 'grcaey'), end = ' ')
if __name__ == "__main__":main()

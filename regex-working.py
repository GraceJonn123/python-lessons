import re

def main():
    fh = open('sparrow.text')
    #opens the text sparrow and reads it line by line
    for line in fh:
            #regex search...searching for regular expressions
            print(re.sub('sparrow','Gracey' line), end =' ')
if __name__ == "__main__":main()

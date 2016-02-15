import re

def main():
    fh = open('sparrow.text')
    for line in fh:
        if re.search('sparrow', line):
            print(line, end=' ')
if __name__ == "__main__":main()

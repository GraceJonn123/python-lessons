import re

def main():
    fh = open('sparrow.text')
    pattern = re.compile('sparrow', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(pattern.sub("Grace", line), end = ' ')
if __name__ == "__main__":main()

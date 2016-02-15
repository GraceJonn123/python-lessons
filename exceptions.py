def main():
    try:
        fh = open('lnes.txt')
    except FileNotFoundError as e:
        print("couldn't open this file...yaaaay you did t", e)
    else:
        for line in fh: print(line.strip())
def readfile(filename):
    fh = open(filename)
    return fh.readlines()


if __name__=="__main__":main()

def main():
    testfunc(1, 2, 3, 34, 45, 56)
def testfunc(this, that, other, *args):
    #asterisk means you can have any form of lists as arguments
    print(this, that, other)
    #here what i'll get is a normal tuple
    for n in args: print(n, end=' ')
if __name__=="__main__": main()

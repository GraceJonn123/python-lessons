def main():
    testfunc(1, 2, 3, 34, 45, 56)
def testfunc(this, that, other, *args):
    print(this, that, other, args)
    #here what i'll get is a normal tuple
    for n in args: print(n, end=' ')
if __name__=="__main__": main()

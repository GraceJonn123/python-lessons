def main():
    testfunc(1, 2, 3, 34, 45, 56)
def testfunc(this, that, other, *args):
    #asterisk means you can have any form of lists as arguments
    try:
        print(this, that, other)(args)
    except TypeError:
        print(that, other, this)
        print(other, args, this, that)
    try:
        print(ars)
    except NameError:
        print("OOps! Too many mistakes..try again")

        #here what i'll get is a normal tuple
if __name__=="__main__": main()

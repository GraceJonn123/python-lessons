def main():
    testfunc(2, 3, 7, 34, 78, 45, 46, fourty=45, thar=56, two = 3)

def testfunc(a, b, c, *args, **kwargs):
    try:
        for k in args: print(k, args[k])
    except IndexError:
            print ("Whatever")
if __name__=="__main__": main()

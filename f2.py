#kwargs... its a dictionary, and accessed by a double asterisk. (**)
def main():
    testfunc(2, 3, 7, 34, 78, 45, 46, fourty=45, thar=56, two = 3)

def testfunc(a, b, c, *args, **kwargs):
    print(a, c, b, args, kwargs['fourty'],kwargs['thar']),kwargs['two']

if __name__=="__main__": main()

__author__ = 'gideon'


def fibo(n):

    if n < 1:

        return False

    elif n == 1 or n==2:

        return 1

    else:

        an_1 = 1
        an_2 = 1

        print an_1
        print an_2

        for i in range(n-2):

            an = an_1 + an_2
            print str(an)

            an_1 =  an_2
            an_2 =  an

        return an_2


fibo(20)
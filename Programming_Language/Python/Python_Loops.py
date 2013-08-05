"""
varies between those following two pieces of codes

"""

# 1st version
    import random
    boolResult = True

    for i in range(30):
        if boolResult:
            print '-' * 20 + '>', i
            boolResult = random.choice([True, False])
            print 'The current boolResults are: %s'%boolResult

"""Outputs as following

C:\apps\python27\python.exe C:/test/test_data/for_loops.py
--------------------> 0
The current boolResults are: True
--------------------> 1
The current boolResults are: False

Process finished with exit code 0
"""




#2nd version


# 1st version
    import random
    boolResult = True

    for i in range(30):
        if boolResult:
            print '-' * 20 + '>', i
        boolResult = random.choice([True, False])
        print 'The current boolResults are: %s'%boolResult


""" Outputs as following:
C:\apps\python27\python.exe C:/test/test_data/for_loops.py
--------------------> 0
The current boolResults are: True
--------------------> 1
The current boolResults are: False
The current boolResults are: True
--------------------> 3
The current boolResults are: True
--------------------> 4
The current boolResults are: False
The current boolResults are: True
--------------------> 6
The current boolResults are: False
The current boolResults are: True
--------------------> 8
The current boolResults are: True
--------------------> 9
The current boolResults are: False
The current boolResults are: False
The current boolResults are: True
--------------------> 12
The current boolResults are: True
--------------------> 13
The current boolResults are: False
The current boolResults are: False
The current boolResults are: True
--------------------> 16
The current boolResults are: False
The current boolResults are: True
--------------------> 18
The current boolResults are: True
--------------------> 19
The current boolResults are: True
--------------------> 20
The current boolResults are: True
--------------------> 21
The current boolResults are: True
--------------------> 22
The current boolResults are: False
The current boolResults are: False
The current boolResults are: True
--------------------> 25
The current boolResults are: True
--------------------> 26
The current boolResults are: True
--------------------> 27
The current boolResults are: True
--------------------> 28
The current boolResults are: True
--------------------> 29
The current boolResults are: True

Process finished with exit code 0
"""
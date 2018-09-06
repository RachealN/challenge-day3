def missing_number(testlist):
    missing = []
    if not isinstance(testlist,list):
        return 'invalid input'
    else:
        for i in range(1,10):
            if i not in testlist:
                missing.append(i)

        return missing 

missing_number([1,2,3,5,6,7,9])       



while True:

    test = input()

    if not test:
        break

    length = len(test)
    start = 0
    end = length-1
    stop = length-1  # We will use this to stop the iteration
    words = list()    # This is the list of cycle shift words 
    words.append(test)
    while start < stop:
        start += 1
        end += 1
        result = ""
        result += test[start:]
        result += test[0:(end%length)+1]
        words.append(result)
        
    words.sort()
    final = ""
    for word in words:
        final += word[-1]
    
    print(final)
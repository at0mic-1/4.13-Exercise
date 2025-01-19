def compress(input):
    times_run = 1
    count = 1
    result = ""
    for i in input:
        if times_run == len(input):
            result += i
            result += str(count)
        else:
            if i == input[times_run]:
                count += 1
            else:
                result += i
                result += str(count)
                count = 1
                
        times_run += 1

    return result
#this will let the reader know this is were they are supposed to put the message.
print(compress(input("Enter coordinates here: ")))

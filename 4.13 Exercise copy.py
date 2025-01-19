"""This is the coordinate to enter
NNNEENNWNNEEEENNWWNNEEEESSSEEENNEEESSWSSWWWSSSSWWW"""
def shorten(input):
    times_run = 1
    count = 1
    result = ""
    for i in input:
        if times_run == len(input):
            result += i
            result += str(count)
        elif i == input[times_run]:
            count += 1
        else:
            result += i
            result += str(count)
            count = 1
                
        times_run += 1

    return result
#this will let the reader know this is were they are supposed to put the message.
coordinates = shorten(input("Enter coordinates here: "))
print(coordinates)
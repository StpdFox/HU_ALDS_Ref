# 1.6


def hairyGroupsOf3(arr):
    result = [(), (), ()]
    m = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                tup = (arr[i], arr[j], arr[k])
                relativeHair = avgHairLength(
                    tup) - (avgHairLength(arr)/avgHairLength(tup))
                result[m] = (tup, relativeHair)
                m += 1
    return result


hairyGroupsOf3.avgHairLength = 0


# Time complexity = O(n^4), assuming that avgHairLength() == O(n)

# result <- an empty array of 3-tuples of length (l over 3)
#m <- 0
#avgHair <- avgHairLength(arr)
# for i $ 0..L-1 do
#    for j $ i+1..L-1 do
#	    for k $ j+1..L-1 do
#		    tup <- (arr[i],arr[j],arr[k]
#			relativeHair <- avgHairLength(tup) - (avgHair/avgHairLength(tup))
#			result[m] <- (tup, relativeHair)
#			m++
#		end for
#	end for
# end for
# return result

# Now it's O(n^3)

# 5

def hairyGroupsOf3New(arr):
    result = [(), (), ()]
    m = 0
    avgHair = avgHairLength(arr)
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                tup = (arr[i], arr[j], arr[k])
                relativeHair = avgHairLength(
                    tup) - (avgHair/avgHairLength(tup))
                result[m] = (tup, relativeHair)
                m += 1
    return result
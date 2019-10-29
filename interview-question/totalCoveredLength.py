# LinkedIn's interview question on 10/21/2019 fro 1pm - 2p
# I was not able to solve this proble. The interview lasted only 30 minutes instead of 1 hour.

# Returns a total length covered by the addedd intervals.
# If several intervals intersect, their intersection should be counted only once.
# Example:
#   addInterval(3, 6)
#   addInterval(8, 9)
#   addInterval(1, 5)
# 
#   getTotalCoveredLength() -> 6
#
# i.e. [1, 5] and [3, 6] intersect and give a total covered interval [1, 6] with a length of 5.
#      [1, 6] and [8, 9] don't intersect, so the total coveredlength is a sum of both intervals, that is 5+1=6
#
#           |__|__|__|               (3,6)
#                          |__|      (8,9)
#     |__|__|__|__|                  (1,5)
# 
#   0 1  2  3  4  5  6  7  8  9  10

class Interval:
    #[[1, 6], [8, 9], [10, 15]]

    #addaninterval [from, to] into an internal structure.

    def addInterval(begin, to):
        #implement here

    def getTotalCoveredLength():
        #implement here

a = [1, 2, 3, 4, 5, 6

print(len(a))

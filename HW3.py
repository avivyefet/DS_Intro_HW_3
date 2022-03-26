
# Assignment 3

# Aviv yefet

# QA
def read_line(n, file):
    if isinstance(n, int) and isinstance(file, str):
        try:
            fhand = open(file)
            count = 0
            for line in fhand:
                count = count + 1
                if count == n:
                    return line
            return "line " + str(n) + " doesn't exist"  # if the for loop ends it means that the line dosen't exist
        except:
            return "file not found"
    else:
        return "invalid input detected"


# Test QA:
# print(read_line(4, "ex3_text.txt"))      #should return: " There is much more to black holes than meets the eye. In fact,".
# print(read_line(9, "ex3_text.txt"))     #should return: " ".
# print(read_line(29, "ex3_text.txt"))    #should return: "line 29 doesn't exist".
# print(read_line("c", "ex3_text.txt"))   #should return: "invalid input detected".
# print(read_line(9, "ex4_text.txt"))     #should return: "file not found".
# print(read_line(2, 3))                  #should return: "invalid input detected".

import re

# QB
def longest_words(file):
    if isinstance(file, str):
        try:
            dic = dict()
            fhand = open(file)
            for line in fhand:
                line = re.sub('[^0-9a-zA-Z]+', ' ', line)  # replaced all of the non-alphanumeric characters in space.
                line = line.rstrip().split()

                for word in line:
                    if word not in dic:
                         dic[word] = len(word)

            lst = list()
            for k, v in dic.items():
                lst.append((v, k))

            lst = sorted(lst, reverse=True)

            longest_five = list()
            for v, k in lst[:5]:
                longest_five.append(k)
            return longest_five

        except:
            print("file not found")
            return list()
    else:
        print("file not found")
        return list()

# Test QB
# print(longest_words("ex3_text.txt"))     # should return: ['electromagnetic', 'gravitational', 'Consequently', 'calculations', 'ultraviolet'].
# print(longest_words("ex4_text.txt"))     # should print: "file not found" and return an empty list.
# print(longest_words(2))                  # should print: "file not found" and return an empty list.
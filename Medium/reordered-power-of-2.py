class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """

        minN = maxN = ""
        
        strN = str(n)
        listN = []

        ## Find the smallest and largest permutations of the given number ##
        listN = list(strN)

        # Sort digits in ascending and descending order
        minListN = sorted(listN)
        maxListN = sorted(listN, reverse=True)

        # Build smallest permutation as a string
        for digit in minListN:
            minN = minN + digit

        # Build largest permutation as a string
        for digit in maxListN:
            maxN = maxN + digit

        # Convert the strings to integers
        minN = int(minN)
        maxN = int(maxN)
        ## ./Find the smallest and largest permutations of the given number ##


        # Get binary representation of min and max values (without '0b' prefix)
        minN = bin(minN)[2:]
        maxN = bin(maxN)[2:]

        # Get the lengths of the binary strings
        minN = len(minN)
        maxN = len(maxN)

        # List to store all binary values of 2^n between min and max
        list2N = []

        # Create the largest 2^n value in binary according to max length
        max2N = "1"
        for x in range(maxN - 1):
            max2N = max2N + "0"
        
        list2N.append(max2N)

        # Generate all 2^n binary strings from max down to min
        while maxN > minN:
            maxN = maxN - 1

            temp2N = "1"
            for x in range(maxN - 1):
                temp2N = temp2N + "0"

            list2N.append(temp2N)

            temp2N = ""

        # Create the smallest 2^n value in binary according to min length
        min2N = "1"
        for x in range(minN - 1):
            min2N = min2N + "0"

        # Add the min value to the list
        list2N.append(min2N)


        # List to store decimal values of the binary 2^n numbers
        list2NDec = []

        for binary in list2N:
            # Convert binary string to decimal integer
            list2NDec.append(int(binary, 2))

        # Sort the digits of the original number for comparison
        listN = list(str(n))
        sortListN = sorted(listN)

        # For each 2^n candidate, convert to string, sort digits, and compare
        for bk in list2NDec:
            bk = sorted(str(bk))

            if bk == sortListN:
                return True

        return False

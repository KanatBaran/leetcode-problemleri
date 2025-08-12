class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # VI = 6
        # IV = 4

        # Degiskenler #
        listNumber = []
        result = 0
        # ./Degiskenler #
        
        listRoman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # Girilen roman sayisinin degerini listeye ekliyoruz.
        for cha in s:
            listNumber.append(listRoman[cha])

        # Karakterlerden elde ettigimiz sayinin bir sonraki degere bakip toplanacak mi cıkartılacak mi onu kontrol ediyoruz.
        for index in range(len(listNumber) - 1):
            if listNumber[index] < listNumber[index + 1]:
                listNumber[index] = -listNumber[index] 

        for number in listNumber:
            result = result + number

        return result


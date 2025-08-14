class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        
        threeList = []  # 3 tane aynı rakamdan oluşan alt dizgileri tutmak için liste

        # Dizgi üzerinde 3 karakterlik kontrol yaparak ilerle
        for index in range(len(num) - 2):
            # İlk iki karakter aynı mı?
            if(num[index] == num[index + 1]):
                # Üçüncü karakter de aynı mı?
                if(num[index] == num[index + 2]):
                    # Aynıysa bu karakterden oluşan 3 uzunluklu string'i listeye ekle
                    threeList.append(num[index] * 3)
        
        # Eğer hiç uygun alt dizgi yoksa boş string döndür
        if(len(threeList) == 0):
            return ""
        else:
            # Listeyi büyükten küçüğe sırala
            threeList.sort(reverse=True)
            # En büyük olanı döndür
            return threeList[0]

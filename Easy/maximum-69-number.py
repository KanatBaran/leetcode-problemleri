class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        # Sayıyı stringe çevirip listeye dönüştürüyoruz
        # Çünkü string doğrudan değiştirilemez (immutable), ama liste değiştirilebilir
        numList = list(str(num))

        # Soldan sağa tüm karakterleri geziyoruz
        for index in range(len(numList)):
            # İlk gördüğümüz '6' karakterini bulunca
            if numList[index] == "6":
                # Onu '9' yapıyoruz
                numList[index] = "9"
                # Sadece 1 tane değiştirebileceğimiz için döngüyü bitiriyoruz
                break
        
        # Listeyi tekrar stringe çeviriyoruz ve integer'a dönüştürüp geri döndürüyoruz
        return int("".join(map(str, numList)))

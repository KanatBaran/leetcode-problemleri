class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # String'i listeye çeviriyoruz
        listS = list(s)

        # Stack (yığın): açılış parantezleri burada tutulacak
        stack = []

        # Kapanış -> Açılış eşleştirme tablosu
        matchS = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        # Tüm karakterleri sırayla dolaş
        for cha in listS:
            if (cha == "[" or cha == "(" or cha == "{"):
                # Açılış parantezi ise yığına ekle
                stack.append(cha)
            else:
                # KONTROL #1: Yığın boşsa, ilk/şu anki karakter kapanış olamaz 
                if not stack:
                    return False

                # Tepedeki açılış parantezi doğru tip mi?
                if (matchS[cha] == stack[-1]):
                    # Eşleştiyse tepedekini çıkar
                    stack.pop()
                else:
                    # Tip uyumsuzluğu varsa geçersiz
                    return False

        # KONTROL #2: Döngü bittiğinde yığın tamamen boş olmalı
        # (Aksi halde kapanmamış açılış parantezleri var demektir.)
        return len(stack) == 0

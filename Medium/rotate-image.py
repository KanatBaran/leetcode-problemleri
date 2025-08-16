class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None  # Do not return anything, modify matrix in-place instead.
        """

        # 1) MATRİSİN TRANSPOZUNU AL
        # Yani satır-sütun yerlerini değiştiriyoruz.
        # Ama her elemanı 2 defa değiştirmemek için sadece üst üçgende (col > row) dolaşıyoruz.
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix)):
                # (row, col) ile (col, row) elemanlarını yer değiştiriyoruz
                swap = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = swap

        # 2) SATIRLARI TERS ÇEVİR
        # Transpozdan sonra her satırı sağdan sola çevirince
        # matris saat yönünde 90° dönmüş oluyor.
        for row in matrix:
            row.reverse()

        return matrix
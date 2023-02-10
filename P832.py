from typing import List
def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    m = len(image)
    for i in range(m):
        n = len(image[i])
        for j in range(n):
            image[i][j], image[i][n-1-j] = image[i][n-1-j], image[i][j]

    for i in range(m):
        n = len(image[i])
        for j in range(n):
            image[i][j] = 1 - image[i][j]
    
    return image


    
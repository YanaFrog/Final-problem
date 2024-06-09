import numpy as np
def GetNumGlowPixelsOnPhoto(image):
    glowPixels = np.sum(image > 200)
    return glowPixels

def GetGlowPointsForGraph(images):
    result = []
    for i in images:
        result.append(GetNumGlowPixelsOnPhoto(i))
    return result

def GetNumLightPixel(images):
    answer = []
    for image in images:
        for i in range(len(image)):
            for j in range(len(image[0])):
                if (image[i][j] > 200): 
                    answer.append(i*len(image[0]) + j)
    return answer
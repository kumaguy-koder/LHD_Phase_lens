import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

if __name__ == "__main__":
    width = 256  # CGH width (pixels)
    height = 256  # CGH height (pixels)
    focal_length = 1000  # focal length (mm)
    wave_length = 633*10**-6   # wave length (mm)
    pixel_pitch = 20*10**-3  # Pixel pitch of CGH（mm）

    # Array containing the distance to each pixel from the center of the image
    xlist = np.array([[i for i in range(width)] for j in range(height)], dtype=int)
    ylist = np.array([[j for i in range(width)] for j in range(height)], dtype=int)
    r = np.sqrt((height/2 - ylist) ** 2 + (width/2 - xlist) ** 2)

    # Converting to the distance on SLM
    r_SLM = r * pixel_pitch

    # Calculating of Phase Fresnel lens
    l_phase = -1 * (np.pi * (r_SLM ** 2) / (focal_length * wave_length))
    l_phase = np.fmod(l_phase, 2 * np.pi) + np.pi
    l_phase = np.uint8(l_phase / np.max(l_phase) * 255)

    # Showing an image
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_title("Phase Fresnel lens")
    ax1.imshow(l_phase, cmap='gray')
    plt.show()

    # Saving an image
    l_phase = Image.fromarray(l_phase)
    l_phase.save("lphase.bmp")



import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

# 位相型フレネルレンズの計算
if __name__ == "__main__":
    width = 256  # SLMの横サイズ (pixel)
    height = 256  # SLMの縦サイズ (pixel)
    focal_length = 1000  # 焦点距離 (mm)
    wave_length = 633*10**-6   # 波長 (mm)
    pixel_pitch = 20*10**-3  # SLMの画素ピッチ（mm）

    # 画像の中心からの各画素までの距離が格納された配列 r
    xlist = np.array([[i for i in range(width)] for j in range(height)], dtype=int)
    ylist = np.array([[j for i in range(width)] for j in range(height)], dtype=int)
    r = np.sqrt((height/2 - ylist) ** 2 + (width/2 - xlist) ** 2)

    # SLM上での距離に変換
    r_SLM = r * pixel_pitch

    # レンズパターンを計算
    l_phase = -1 * (np.pi * (r_SLM ** 2) / (focal_length * wave_length))
    l_phase = np.fmod(l_phase, 2 * np.pi)

    # 出力
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_title("Phase Fresnel lens")
    ax1.imshow(l_phase, cmap='gray')
    plt.show()



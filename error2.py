# ライブラリのインポート
import cv2
import sys
import matplotlib.pyplot as plt
import numpy as np

# カメラの場合
camera_path = 0

# 動画の場合
camera_path = 'c:/tmp001/video_sample_01.mp4'

capture = cv2.VideoCapture(camera_path)

# 閾値
threshold_value = 127

#########################################
# 追加部分
#########################################
# カメラ・動画画像の横幅、縦幅を取得
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# カメラ・動画のFPSを取得
fps = capture.get(cv2.CAP_PROP_FPS)
# print("fps:", fps)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # aviファイルで出力する場合
# fourcc = cv2.VideoWriter_fourcc(*'MP4V') # mp4ファイルで出力する場合

outvideopath = 'output.avi'
out = cv2.VideoWriter(outvideopath, fourcc, fps, (width, height))

# 閾値
# threshold_value = 127


while True:
    # カメラ/動画の画像を1フレーム分取得
    ret, img = capture.read()
    if not ret:
        print("capture error!!")
        break

    ########################################
    # このあたりに1フレームごとに処理を加えたりする
    ########################################

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    threshold_img = gray.copy()
    # 方法1（NumPyで実装）
    threshold_img[gray < threshold_value] = 0
    threshold_img[gray >= threshold_value] = 255

    cv2.imshow('camera', threshold_img)
    #########################################
    # 追加部分
    #########################################
    out.write(img)

    # qキーを押したら処理を終了する
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# いろいろ閉じる
capture.release()
out.release()
cv2.destroyAllWindows()
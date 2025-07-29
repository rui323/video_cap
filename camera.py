import cv2
import os

# 保存ディレクトリ
save_folder = "distance-30" # 30cm離した画像
# クラックの場合 save_folder = "distance-30-45" 30cm離して、斜め45度の角度で撮影 etc

# ディレクトリが存在しなければ作成
os.makedirs(save_folder, exist_ok=True)
# カメラを初期化
cap = cv2.VideoCapture(0)

count = 0
if not cap.isOpened():
    print("カメラが開けません")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("フレームが取得できません")
        break

    cv2.imshow('USB Camera', frame)

    key = cv2.waitKey(1) & 0xFF  # 押されたキーを取得（& 0xFFで下位8ビットにする）

    if key == ord('p'):
        filename = os.path.join(save_folder, f"pic_{count}.png")
        count += 1
        cv2.imwrite(filename, frame)
        print(f"{filename} を保存しました")
    elif key == ord('q'):
        print("終了します")
        break

cap.release()
cv2.destroyAllWindows()

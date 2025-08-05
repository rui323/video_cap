# video_cap
## 内容
 - ローカルの環境でUSBカメラを使用することができる
 - 実行前に画像を保存するフォルダのパスを作成する
   - もし、存在しなければ新しく作成するようになっている
 - 実行時、opencvのウィンドウが開きカメラ映像が流れる
 - 「ｐ」ボタンを押すことでそのフレームを指定したフォルダに保存
 - 「ｑ」ボタンを押すことで処理を終える
## 環境構築
 - powershellを開く
~~~bash!
mkdir DataSet # ワークスペースを作成
cd DataSet
pip install opencv-python
~~~
 - VScodeでこのレポジトリに書かれているファイルを複製
## 実行
~~~bash!
python3 camera.py
~~~
## もしPC内蔵のカメラが起動した場合
 - 以下のコマンドを実行
~~~bash!
pip install cv2_enumerate_cameras
python -m cv2_enumerate_cameras
~~~
 - 出力結果からRealSense RGBのindex番号を確認
 - cap = cv2.VideoCapture(ここの番号を変更)

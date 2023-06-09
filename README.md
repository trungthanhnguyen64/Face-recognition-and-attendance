# Face recognition and attendance
企業や学校が集合住宅の出退勤管理や入退室管理に顔認証を活用することで、感染拡大のリスクが軽減されます。 ユーザーはカメラの前に数秒間顔を向けるだけで、システムが処理して識別します。 そのおかげで、管理は便利で速くなります 迅速かつ安全に。
これらの理由から、実用的なニーズを満たし、今日のわが国の人工知能の開発プロセスに貢献するために、「スマート大学に適用される多対象顔認識プログラムに関する研究」というトピックを選択しました。

プロジェクトの手順は次のとおりです。
+ ステップ 1: データを収集する
この機能を使用すると、ユーザーはカメラを起動して、元のデータの顔の角度の画像を 100 枚キャプチャできます。 キャプチャされた画像は、コンピューターが処理するために OpenCV ライブラリを介してグレースケールに変換され、「dataSet」フォルダーに保存されます。 顔を正確にキャプチャできるようにするために、OpenCV ライブラリを介して Haar Cascade アルゴリズムを使用しました。 これはオブジェクト検出アルゴリズムであり、顔を正確にキャプチャして周囲のコンポーネントから分離することができます。
そして、プログラムはユーザーに、キャプチャされた画像に対応する情報 MSSV (ID)、フルネーム、クラスを入力するように求めます。 これらの情報は、Python の sqlite3 ライブラリを介して SQLite データベースに保存されます。
+ ステップ 2: トレーニング データ
この関数は、LBPH (Local Binary Pattern Histograms) アルゴリズムを使用して、OpenCV ライブラリを通じてキャプチャされた画像データをトレーニングします。 このアルゴリズムは、元の画像を ID に対応するローカル バイナリ パターン ヒストグラムに変換して、他の顔と区別します。 トレーニング後のデータは、ファイルの下に保存されます
識別用の「TrainingData.yml」。
+ ステップ 3: 顔認識
この関数は、カメラを使用して顔をスキャンし、OpenCV ライブラリを使用してファイル「TrainingData.yml」を読み取り、データを比較します。 一致すると、その顔の名前が画面に表示されます。 そうしないと、顔が一致せず、「Unknown」という単語が画面に表示され、顔がシステムによって認識されません。
+ ステップ 4: 出欠を取る
この関数は、スキャンした顔の ID、姓名、クラスを Excel ファイルに保存します。
認識されていない顔はファイルに保存されません。

結果: 以下の機能を備えた顔認識および出席プログラムを完了しました。
+ 得られた画像を分析して処理します。
+ 元のデータに基づく顔認識。
+ 出席を取って、リストを Excel ファイルに保存します。

レポートのリンク:https://docs.google.com/document/d/1wom4wipxWweVWBXx99gpQDlBfc8EO4lJ/edit

結果：
+ ![alt text](https://github.com/trungthanhnguyen64/Face-recognition-and-attendance/blob/main/result1.png)

+ ![alt text](https://github.com/trungthanhnguyen64/Face-recognition-and-attendance/blob/main/result2.png)

また、出席アプリの開発にも取り組んでいます。 製品は研究中であり、将来的にリリースされる予定です。
アプリケーションのインターフェースは次のとおりです。

![alt text](https://github.com/trungthanhnguyen64/Face-recognition-and-attendance/blob/main/app..png)
![alt text](https://github.com/trungthanhnguyen64/Face-recognition-and-attendance/blob/main/app.png)


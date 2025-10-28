# Googleスプレッドシート連携スクリーンショット自動化ツール


## 概要
このPythonスクリプトは、Googleスプレッドシートに記載されたURLリストにアクセスし、各ページのスクリーンショットを自動で取得・保存するツールです。
- Seleniumでブラウザ操作
- Google Sheets APIでURLリスト取得
- 取得したスクリーンショットを指定フォルダに保存


主に **Webサイトの監視や資料作成の自動化** に活用できます。


---


## ポートフォリオ用アピールポイント
- Pythonを使用したWeb自動化の実務経験を示せます
- Googleスプレッドシートとの連携によるデータ操作が可能
- Seleniumを用いたブラウザ操作・スクリーンショット取得を自動化
- 実務に応用可能な小規模プロジェクトとしてクライアントに提示可能


---


## 使用方法


### 1. 必要なライブラリをインストール
```bash
pip install gspread oauth2client selenium
```


### 2. Google API認証情報の準備
1. [Google Cloud Console](https://console.cloud.google.com/)でサービスアカウントを作成
2. JSON形式の認証ファイルをダウンロード
3. スクリプト内の `credentials.jsonが格納してある階層指定` を認証ファイルのパスに置き換え


### 3. Googleスプレッドシートの準備
- URLやサイト名を含むスプレッドシートを作成
- スプレッドシートIDをスクリプト内の `spreadsheet_id` に設定


### 4. 保存先ディレクトリの設定
- `save_dir` にスクリーンショット保存先フォルダを指定


### 5. スクリプト実行
```bash
python main.py
```
- スクリーンショットが `save_dir` に順次保存されます


---


## 注意点
- 空のタイトルや無効なURLはスキップされます
- 実行時にブラウザが立ち上がります（Selenium ChromeDriver 必須）
- スクリプト内の `time.sleep(2)` はリクエスト間隔を制御しています。必要に応じて調整可


---


## 使用技術
- Python 3.13
- gspread（Google Sheets API連携）
- oauth2client（認証）
- Selenium（ブラウザ操作・スクリーンショット）
- 正規表現（ファイル名の安全化）

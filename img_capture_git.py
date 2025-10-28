import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import sys
import re

# 行カウント変数（スプレッドシートの2行目から開始）
i = 2
error = 0
processed = 0

###########最初の準備　ここから##########
# Google APIのスコープを設定
scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/drive']

# 認証情報を読み込む
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.jsonが格納してある階層指定", scope)
# Googleスプレッドシートに接続
client = gspread.authorize(credentials)
# スプレッドシートID設定
spreadsheet_id = "URL、サイト名が記載してあるGoogleスプレッドシートのID記載"
# スプレッドシートを開く
spreadsheet = client.open_by_key(spreadsheet_id)

# オプションを設定する
options = Options()
options.add_argument(
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")

# Google ChromeのWebdriverを設定
driver = webdriver.Chrome(options=options)
###########最初の準備　ここまで##########

# 保存先ディレクトリ
save_dir = "保存先のディレクトリを指定"
os.makedirs(save_dir, exist_ok=True)

# シートを一括取得（APIコールはここだけ）
rows = spreadsheet.sheet1.get_all_values()  # 2次元リスト。1行目がヘッダーなら rows[1:] から処理

try:
    for row in rows[1:]:  # ヘッダーが1行ある前提。ヘッダーが無い場合は rows[:] に変更
        # row の長さチェック
        title_raw = row[0] if len(row) > 0 else ""
        url_raw = row[1] if len(row) > 1 else ""

        title = title_raw.strip() if title_raw is not None else ""
        url = url_raw.strip() if url_raw is not None else ""

        # 空のタイトルが来たら終了（運用に合わせて continue に変更可）
        if not title:
            print("空のタイトルを検出したため処理を終了します。")
            break

        # ファイル名に使えない文字を安全化
        title_safe = re.sub(r'[\\/:*?"<>|]', '_', title)

        print(f"[{i}] アクセス中: {url}")
        try:
            driver.get(url)
            # 指定された画像サイズに変更
            w = 1000
            h = 1000
            driver.set_window_size(w, h)

            FILENAME = f"{save_dir}/{title_safe}.jpg"
            driver.save_screenshot(FILENAME)
            print(f" 保存完了: {FILENAME}")
            processed += 1

        except Exception as e:
            error += 1
            print(f" エラー（スキップ）：{e}")

        finally:
            i += 1
            time.sleep(2)

finally:
    driver.quit()
    print(f"処理完了: 成功={processed}, エラー={error}")
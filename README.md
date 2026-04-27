# py-komatsu-lcd-timetable

IRいしかわ鉄道小松駅改札内中2階のLCD発車標を Python / pygame で再現するプロジェクトです。

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![pygame](https://img.shields.io/badge/pygame-2.x-green?logo=python)
![License](https://img.shields.io/badge/license-MIT-yellow)

> [!WARNING]
> **現在は静的データのみ対応しています。**
> リアルタイムのダイヤ取得・自動更新機能は未実装です。時刻・行先・のりばを変更するにはソースコードを直接編集してください。

---

<img src="py-komatsu-lcd-timetable_screenshot.gif" width="50%">

## 必要環境

| 項目 | バージョン |
|------|-----------|
| Python | 3.x |
| pygame | 最新推奨 |
| OS | Windows, *nix |
| フォント | メイリオ |

## インストール

```zsh
git clone https://github.com/awazustamin/py-komatsu-lcd-timetable.git
cd py-komatsu-lcd-timetable
pip install -r requirements.txt
```

## 使い方

```zsh
python main.py
```

起動するとウィンドウが開き、発車標が表示されます。

| 操作 | 動作 |
|------|------|
| ウィンドウリサイズ | 16:9 を維持してスケーリング |
| ウィンドウを閉じる | アプリ終了 |

### 時刻・行先・のりばを変更する

現在はデータが `main.py` にハードコードされています。変更したい場合は該当箇所を直接編集してください。

```python
# 例: 1段目の時刻を変更する
text_time1 = main_font.render("16：53", True, YELLOW_TEXT)  # ← 時刻文字列を書き換える
```

## ライセンス

[MIT License](LICENSE)

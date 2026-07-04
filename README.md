# py-komatsu-lcd-timetable

IRいしかわ鉄道小松駅改札内中2階のLCD発車標を Python / pygame で再現するプロジェクトです。

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![pygame](https://img.shields.io/badge/pygame-2.x-green?logo=python)
![Requests](https://img.shields.io/badge/Requests-2.x-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-yellow)

---

<img src="py-komatsu-lcd-timetable_screenshot.gif" width="60%">

## 必要環境

| 項目 | バージョン |
|------|-----------|
| Python | 3.x |
| pygame | 最新推奨 |
| Requests | 最新推奨 |
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
また、--debugオプションを追加すると時刻の変更ができます。   

| 操作 | 動作 |
|------|------|
| ウィンドウリサイズ | 16:9 を維持してスケーリング |
| ウィンドウを閉じる | アプリ終了 |
| Bキー | 時間を10分送る |
| Gキー | 時間を10分戻す |
| Nキー | 時間を60分送る |
| Hキー | 時間を60分戻す |

### 時刻・行先・のりばを変更する

main.pyがあるディレクトリー内にkomatsu.jsonが追加されているので、それを複製し書き換えてください。  
書き換えたファイルの読み込みは```--file ディレクトリー``` です


## ライセンス

[MIT License](LICENSE)

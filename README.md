# Overview / 概要

badger2040_soundbadge is a wearable e-paper badge that helps individuals with auditory hypersensitivity express their needs in noisy environments, such as public spaces.  It uses the [Badger 2040](https://shop.pimoroni.com/products/badger-2040) .

\[日本語\]

badger2040_soundbadge プロジェクトは聴覚過敏の方々のための電子ペーパーバッジです。[Badger 2040](https://shop.pimoroni.com/products/badger-2040)を使っています。

# Hardware / ハードウェア

| Component | Product Name | Description |
|----------|---------------|-------------|
| Main Board | [Pimoroni Badger 2040](https://shop.pimoroni.com/products/badger-2040) | An e-paper badge based on the Raspberry Pi RP2040 |
| Sound Sensor | [Zio Qwiic Loudness Sensor](https://www.sparkfun.com/products/17350) | Detects ambient sound levels |
| LED Indicator | [SparkFun Qwiic Button](https://www.sparkfun.com/products/15586) | Used only for its built-in RGB LED, not as a button |

All components are connected via Qwiic (I2C) for solderless assembly.

\[日本語\]

| パーツ | 製品名 | 説明 |
|-------|---------------|------|
| 本体 | [Badger 2040](https://shop.pimoroni.com/products/badger-2040) | Raspberry Pi RP2040搭載の電子ペーパーバッジ |
| 音量センサー | [Zio Qwiic Loudness Sensor](https://www.sparkfun.com/products/17350) | 周囲の音量をリアルタイムで測定 |
| ステータスLED | [SparkFun Qwiic Button](https://www.sparkfun.com/products/15586) | ボタンとしては使用せず、内蔵LEDをステータス表示に使用 |

Qwiic（I2C）接続で、はんだづけなしで配線できます。

# How It Works / 動作概要

The device measures ambient sound in real time using a loudness sensor.  
If the sound level exceeds the defined threshold, it activates the LED (red) and displays a warning message on the e-paper display.

\[日本語\]

本デバイスはラウドネスセンサーを使って、周囲の音量をリアルタイムに計測します。  
音量が設定したしきい値を超えると、LEDが赤く点灯し、電子ペーパーにメッセージを表示します。

# Video / 動画

![video](video.gif)

# Installation / インストール方法

Follow these steps to set up your Badger 2040 and run the Sound Sensitive Badge software:

1. Clone the repository:
    ```sh
    git clone https://github.com/cubic9com/badger2040_soundbadge.git
    ```

1. Download the latest version of [Thonny](https://thonny.org).

1. Open Thonny.

1. In the bottom-right corner, make sure the interpreter is set to `MicroPython (Raspberry Pi Pico)`. If not, go to `Tools > Options > Interpreter` and select it from the dropdown.

1. Plug the Badger 2040 into your computer using a USB cable.

1. In Thonny, click the red square Stop button to interrupt the running program. In recent versions of Thonny, you can enable automatic interruption on connect: Go to `Tools > Options > Interpreter > Interrupt working program on connect`.

1. After pressing Stop, you should see a prompt like this in the Shell:
     ```
     >>> 
     ```
   This means the Badger is ready to receive commands from your computer.

1. Once connected, copy the `soundbadge.py`, `loudness_normal.bin`, `loudness_abnormal.bin` to the Badger 2040.

\[日本語\]

1. リポジトリをクローンします:
    ```sh
    git clone https://github.com/cubic9com/badger2040_soundbadge.git
    ```

1. [Thonny](https://thonny.org) をダウンロードし、インストールします。

1. Thonnyを起動します。

1. 画面右下の「インタプリタ」欄で「MicroPython (Raspberry Pi Pico)」を選択します。選択できない場合は、`Tools > Options > Interpreter` から選択できます。

1. USB ケーブルで Badger 2040 をパソコンに接続します。

1. Thonny の「停止ボタン（■）」をクリックして実行中のプログラムを中断します。Thonnyの最新版では、接続時に自動でプログラムを中断するオプションもあります： `Tools > Options > Interpreter > Interrupt working program on connect` にチェックを入れてください。

1. プログラムを停止すると、Shellウィンドウに以下のようなプロンプトが表示されます：
     ```
     >>> 
     ```
   これが表示されていれば、Badger が正常に接続されており、コマンドの受け付け準備ができています。

1. Thonnyで`soundbadge.py`、`loudness_normal.bin`、`loudness_abnormal.bin`をBadger 2040に転送します。

# ライセンス / License

Copyright (C) 2025, cubic9com All rights reserved.

This project is licensed under the MIT license.

See file `LICENSE` file for details.

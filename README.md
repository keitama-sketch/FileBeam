# FileBeam
PeerJSでHostとClientがP2P接続し、ファイルを直接送受信します。
HostはUint8Arrayで送信し、ClientはBlobに戻してダウンロードします。
システム構成
PeerJSを使って、ブラウザ同士が直接つながり、ファイルを送る仕組みです。 サーバーにファイルを置かず、** P2P（直接通信）** で転送します。

** ＜仕組み＞ **

Host ──(PeerJSで接続)── Client ↑ ※仲介だけ PeerJSサーバー

PeerJSサーバー →「つなぐ」役だけ

ファイルデータ → Host と Client で直接やりとり

** ＜流れ＞ **

① Host

　ID（SessionID）を決める 　Clientからの接続を待つ 　ファイルを選ぶ 　ファイルを Uint8Array に変換して送信

② Client

　SessionIDを入力して接続 　データを受信 　Blob に戻す 　ダウンロードリンクを作る

** ＜なぜ Uint8Arrayにしたか？＞ **

ファイルはそのまま送れないので、 File → ArrayBuffer → Uint8Array にすると 安全にバイナリ送信できる

** ＜送っているデータの中身＞ **
```
{
name: "sample.png", // ファイル名
type: "image/png", // 種類
data: Uint8Array // 中身
}
```

** ＜Client側でやってること＞ **

Uint8Array → Blob → URL → ダウンロード → だから 元のファイルがそのまま保存できる。

** ＜この方式の特徴＞ **

・サーバーに保存しない ・高速 ・簡単

ただし、 大きいファイルは不安定になる（分割が必要）(Githubのbataブランチで解決済み)

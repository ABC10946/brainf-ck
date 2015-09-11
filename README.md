#Brainfuck Interpreter

##brainfuck.py

python製のbrainfuckインタプリタです。

python brainfuck.py ファイル名 ステップの有無(0または指定しない:なし,1:あり)

ステップは処理を一回ずつ進めることができ、エンターで進めます。

##test.bf

brainfuckのテスト用コードです。

「Hello, world!」と出力します。

##使用例

実行コマンド
```
python brainfuck.py test.bf
```

brainfuckプログラム
```
+++++++++[>++++++++>+++++++++++>+++++<<<-]>.>++.+++++++..+++.>-.------------.<++++++++.--------.+++.------.--------.>+.
```

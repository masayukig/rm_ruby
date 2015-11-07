Remove ruby from Aozora bunko's text
====================================

This program is for removing rubies from Aozora bunko's[1] text.

How to use (Quick start)
------------------------

$ wget http://www.aozora.gr.jp/cards/000329/files/3390_ruby_6090.zip
$ unzip 3390_ruby_6090.zip
$ cat urashima_taro.txt | PYTHONIOENCODING=utf-8 ./rm_ruby.py > urashima_taro_rm_ruby.txt

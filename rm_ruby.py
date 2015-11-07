#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

regex_ruby = re.compile(u'《[^》]*》')
regex_note = re.compile(u'［＃[^］]*］')
regex_split = re.compile(u'｜')

for line in sys.stdin.readlines():
    res = regex_note.sub('', unicode(line, 'shift-jis'))
    res = regex_ruby.sub('', res)
    res = regex_split.sub('', res)
    print res

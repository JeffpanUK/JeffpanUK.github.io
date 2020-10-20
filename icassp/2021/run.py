#!/usr/bin/env python
# -*- coding:utf-8 -*-
#***********************************************
#      Filename: run.py
#        Author: Jeff Pan
#         Email: panjunjie.jeff@bytedance.com
#   Description: --
#        Create: 2020-10-16 11:11:28
# Last Modified: 2020-10-16
#***********************************************

import os
import sys
import re
from collections import defaultdict

def main(options):
    with open(options["inputs"], "r", encoding='utf-8') as fi, \
            open(options["output"], "w", encoding='utf-8') as fo:
        for line in fi:
            line = line.strip().split("\t")
            text, speaker, emotion = line
            if speaker == "旁白" or speaker.lower() == "narrator":
                speaker = "narrator"
                color = "#666666"
            elif speaker == "余淮":
                color = "#003399"
            else:
                color = "#CC0033"
            fo.write(f'<p><font color="{color}">[{speaker}\t{emotion}]</font> {text}</p>\n')

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",
        default="",
        dest="output", help="")
    parser.add_argument("--inputs",
        default="",
        dest="inputs", help="")
    args = parser.parse_args()
    options = vars(args)
    main(options)

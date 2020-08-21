#!/usr/bin/env python

'''
usage:   unspread.py my.pdf
Creates unspread.my.pdf
Chops each page in half, e.g. if a source were
created in booklet form, you could extract individual
pages.
'''

import sys
import os

from pdfrw import PdfReader, PdfWriter, PageMerge

def splitpage(src):
    ''' Split a page into two (left and right)
    '''
    # Yield a result for each half of the page
    for x_pos in (0, 0.5):
        yield PageMerge().add(src, viewrect=(x_pos, 0, 0.5, 1)).render()


inpfn = sys.argv[1]
outfn = sys.argv[2] 
writer = PdfWriter(outfn)
page_num = 0
for page in PdfReader(inpfn).pages:
    if page_num == 0:
        writer.addpage(page)
    else:
        writer.addpages(splitpage(page))
    page_num = page_num + 1
writer.write()

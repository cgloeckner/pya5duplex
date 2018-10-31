#!/usr/bin/python3

import sys
import PyPDF2 as pdf

def copyPage(index, inpdf, outpdf, mirror=False):
	try:
		p = inpdf.getPage(index)
	except IndexError:
		# source pdf exhausted
		return
		
	if mirror:
		p = p.rotateClockwise(180)
	outpdf.addPage(p)

if __name__ == '__main__':
	dst = pdf.PdfFileWriter()
	src = pdf.PdfFileReader(open(sys.argv[1], 'rb'))

	num_pages = src.getNumPages()

	for i in range(num_pages // 4 + 1):
		copyPage(4 * i    , src, dst) # 1
		copyPage(4 * i + 2, src, dst) # 3
		copyPage(4 * i + 1, src, dst, mirror=True) # 2
		copyPage(4 * i + 3, src, dst, mirror=True) # 4

	h = open('output.pdf', 'wb')
	dst.write(h)

	print('Done.')

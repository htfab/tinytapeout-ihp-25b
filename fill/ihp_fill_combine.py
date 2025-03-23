#!/usr/bin/env python3

import sys
import gdstk


def main(argv0, main_gds, fill_gds, out_gds):

	lib_main = gdstk.read_gds(main_gds)
	lib_fill = gdstk.read_gds(fill_gds)

	top_main = lib_main.top_level()[0]
	top_fill = lib_fill.top_level()[0]

	c = set()
	for r in top_fill.references:
		if r.cell_name.endswith('_FILL_CELL'):
			if r.cell_name not in c:
				lib_main.add(r.cell)
				c.add(r.cell_name)
			top_main.add(r)

	lib_main.write_gds(out_gds)


if __name__ == '__main__':
	main(*sys.argv)

#!/usr/bin/env python3

import sys
import gdstk


def main(argv0, in_gds, out_gds):

	LY = [
		1,	# Activ
		8,	# Metal1
	]

	DT_DRAWING =  0
	DT_NOFILL  = 23

	l = gdstk.read_gds(in_gds)

	top = l.top_level()[0]


	def simplify_cell(cell):
		# Get boundary
		bbox = cell.get_polygons(layer=189, datatype=4)[0].bounding_box()

		# Create corners
		c1 = ( bbox[0][0] + 2.0, bbox[0][1] + 2.0 )
		c2 = ( bbox[1][0] - 2.0, bbox[1][1] - 2.0 )

		# Create a new cell
		new_cell = gdstk.Cell(cell.name + '_bb')

		# Iterare over layers
		for ly in LY:
			# Check if cell has nofill zones
			nofill = cell.get_polygons(layer=ly, datatype=DT_NOFILL)

			# Yes: Use them
			if nofill:
				for p in nofill:
					p.datatype = DT_DRAWING
					new_cell.add(p)

			# No: Create our own
			else:
				new_cell.add( gdstk.rectangle(c1,c2, layer=ly, datatype=DT_DRAWING) )

		return new_cell

	def simplify_subcells(cell):
		sc = {}
		for r in cell.references:
			if not r.cell_name.startswith('tt_') and not r.cell_name.startswith('sg13g2_'):
				continue
			if r.cell_name not in sc:
				sc[r.cell_name] = simplify_cell(r.cell)
			r.cell = sc[r.cell_name]

	simplify_subcells(top)

	out_lib = gdstk.Library()

	out_lib.add(top)
	for sc in top.dependencies(recursive=True):
		out_lib.add(sc)

	out_lib.write_gds(out_gds)


if __name__ == '__main__':
	main(*sys.argv)

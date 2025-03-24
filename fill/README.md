# TopMetal2 Logo + Fill Generator

## Overview

We generate the fill geometry by running the following steps:

1. Generate a GDS with simplified geometry for Active+Poly
2. Run Activ+Poly fill on that simplified geometry
3. Run Metal 1-5 / TopMetal 1-2 on the real geometry
4. Combine both results.

This speeds up the fill process and reduces the amount of memory used.

The Active+Poly fill step still needs a large amount of memory, somewhere between 16GB and 32GB.

## Usage

Export `PDK_ROOT` and `PDK` environment variables:

```bash
export PDK_ROOT=<path-to-pdk>
export PDK=ihp-sg13g2
```

Then run the following command to generate the fill geometry:

```bash
make
```

This will generate the fill geometry and save it to `../ihp/gds/tt_ihp_wrapper_final.gds`.

If your machine has a enough memory (40GB), you can use the `-j` flag to speed up the fill process:

```bash
make -j4
```

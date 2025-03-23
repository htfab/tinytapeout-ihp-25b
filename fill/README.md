# TopMetal2 Logo + Fill Generator

## Overview

We generate the fill geometry by running the following steps:

1. Generate a GDS with simplified geometry for Active / Metal1
2. Run Activ+Poly / Metal1 fill on that simplified geometry
3. Run Metal 2-5 / TopMetal 1-2 on the real geometry
4. Combine both results.

This speeds up the fill process and reduces the amount of memory used.

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

# Médongaule Image Archive

The web-size photographs of Médongaule, Yangpyeong, set as collage spreads after the Médongaule homepage.

- **Front**: the building from above at full width, the address on a strip beneath it. The logo box and menu stay in place as it scrolls away.
- **Filters**: All, Gardens, People, Build-up.
- **Index**: every photograph at once (the menu icon).
- **Colour Match**: groups photographs whose palettes sit together, with a colour strip over each spread. In the viewer, each photograph shows its five main colours and the eight photographs closest to them.
- Tall frames use each photograph's own mobile crop where one exists.

## Build

```
python3 build.py
```

`template.html` + `.tree.path` (the tree, traced from the supplied logo) + `manifest.json` (photographs, sizes, mobile crops) + `palettes.json` (five CIELAB colours per photograph) → `index.html`.

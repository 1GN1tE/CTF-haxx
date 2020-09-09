
# PNG Corruption Fix Guidelines

## Identifying a PNG from Data
Usually we do a `file` command on the file to see if its a PNG or not. But sometimes the headers maybe changed. So we should open it in some Hex Editors like ghex and find for strings like IHDR, IDAT, IEND. If we find these then we can be sure that it's a PNG file. `pngcheck` is a useful tool for this purpose.
### PNG Header
Every PNG file starts with a header or magic bytes as follows:
>`89 50 4E 47 0D 0A 1A 0A` --> `. P N G . . . .`

## PNG Chunks
After the header comes a series of chunks each of which conveys certain information about the image.
A chunk consists of four parts:
>Length &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--> 4 bytes 			E.g.--> `00 00 FF A9`<br />
Chunk type &nbsp;--> 4 bytes 			E.g.--> `49 44 41 54` --> `IDAT`<br />
Chunk Data &nbsp;--> Length bytes<br />
CRC &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--> 4 bytes			E.g.-->`b0 49 20 69`<br />

## Critical Chunks
### IHDR
The  IHDR  chunk must appear FIRST. It contains:
>Width: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4 bytes<br />
 Height: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4 bytes<br />
 Bit depth: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 byte<br />
 Color type: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 byte<br />
 Compression method: 1 byte<br />
 Filter method: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 byte<br />
 Interlace method: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 byte<br />
 **_Total of 13 bytes_**<br />
   
Sometimes the CRC following the IHDR chunk is changed, we can fix it by replacing the original CRC to the computed CRC on the tool `pngcheck`<br />
Sometimes the dimensions of the image are changed, then we can bruteforce the dimensions and see if it matches the original CRC.<br />
### IDAT
The IDAT chunk contains the actual image data of any length. It starts with: `49 44 41 54` and follows the data of length as described at the start of the chunk.
### IEND 
The IEND chunk must appear LAST. It marks the end of the PNG datastream. The chunk's data field is empty.

## Ancillary Chunks
The  pHYs  chunk specifies the intended pixel size or aspect ratio for display of the image. It contains:
>Pixels per unit, X axis: 4 bytes<br />
Pixels per unit, Y axis: 4 bytes<br />
Unit specifier:	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 byte<br />
**_Total of 9 bytes_**<br />

The following values are defined for the unit specifier:
>`00`: unit is unknown<br />
`01`: unit is the meter<br />

Preferably we should use `00` if the Unit specifier was changed. If present, this chunk must precede the first  IDAT  chunk.

## Important links
### Wiki material
1: [PNG Specification](http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html)<br />
2: [Wikipedia](https://en.wikipedia.org/wiki/Portable_Network_Graphics)<br />
### Tools
1: [pngtools](https://manpages.debian.org/jessie/pngtools/index.html)<br />
2: [Automated Tool](https://github.com/sherlly/PCRT) >>> Won't work if multiple changes are done in the data.<br />
3: [GUI Hex Editor](https://wiki.gnome.org/Apps/Ghex)

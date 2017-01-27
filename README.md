# diacritic-removal

This project provides definitions, scripts and documentation for removal of
diacritics on characters for the Dutch language. However, the project is also
useful for other languages. For all applications, also in Dutch, please review
exactly what the implications are of using the files and software offered here.

This functionality is also provided by certain software libraries. However,
the definitions here can be used for making a simple implementation or can be
for used for testing implementations.

Examples of results obtained with diacritic removal are:
* `café` → `cafe`
* `reünie` → `reunie`
* `enquête` → `enquete`

Note that the list with definitions also holds mappings for characters in
superscript and subscript to normal characters. These are also many-to-one
mappings for letters and numerails. Therefore, `e` cannot be converted back to
`ë`, because the `a` could also originate from `ê`. The same applies for `2`
with respect to `₂` and `²`. For this reason the converting of subscript and
superscript is not part of case casting.

Examples for when this relates to the Dutch language are:
* H₂O → H2O
* CO₂-emissie → CO2-emissie
* 16m² → 16m2
* HNO₃-oplossing → HNO3-oplossing

In the examples above, 16m² is a type of sailing boat and not sixteen square
meters, which is properly written as 16 m² with a space between the number and
the unit.

Even though in these example no ambiguity is created, converting back on the
basis of only inspecting separate characters is not possible.

The definitions are found in [diacritic-removal.tsv](diacritic-removal.tsv) and
counter examples, of where nothing changes, are found in
[non-diacritic-removal.tsv](non-diacritic-removal.tsv). Documentation of the
mapping is found in [diacritic-removal.png](diacritic-removal.png). Generated
regular expressions, for usage in for example sed, are found in
[diacritic-removal.sed](diacritic-removal.sed). A reference implementation for
Python with testing functionality is in [implementation.py](implementation.py).

![Diacritic removal](diacritic-removal.png?raw=true "Diacritic removal")

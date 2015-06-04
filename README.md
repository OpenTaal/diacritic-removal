# diacritic-removal

This project provides definitions, scripts and documentation for removal of
diacritics on characters for the Dutch language.

This functionality is also provided by certain software libraries. However,
the definitions here can be used for making a simple implementation or for
testing other implementations.

Example usage is:
* café → cafe
* reünie → reunie
* enquête → enquete

Note that the list with definitions also holds mappings for characters in
superscript and subscript to normal characters. These are also many-to-one
mappings and concern mainly numerals. For example, 2 cannot be mapped back to ₂
or ². Examples for when this relates to the Dutch language are:
* H₂O → H2O
* CO₂-emissie → CO2-emissie
* 16m² → 16m2
* HNO₃-oplossing → HNO3-oplossing

In the examples above, 16m² is a type of sailing boat and not sixteen square
meters, which is properly written as 16 m² with a space between the number and
the unit.

The definitions are found in [diacritic-removal.tsv](https://github.com/OpenTaal/diacritic-removal/blob/master/diacritic-removal.tsv). Documentation of the mapping is found in [diacritic-removal.png](https://github.com/OpenTaal/diacritic-removal/blob/master/diacritic-removal.png). Regular expressions, for usage in for example sed, are found
in [diacritic-removal.sed](https://github.com/OpenTaal/diacritic-removal/blob/master/diacritic-removal.sed).

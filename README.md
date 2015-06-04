# diacritic-removal

This project provides definitions, scripts and documentation for removal of
diacritics on characters for the Dutch language.

This functionality is also provided by certain software libraries. However,
the definitions here can be used for making a simple implementation or for
testing other implementations.

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

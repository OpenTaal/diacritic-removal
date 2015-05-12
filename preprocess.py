#!/usr/bin/env python3


import unicodedata

if __name__ == '__main__':
    src_nodes = []
    dst_nodes = []
    edges = []
    gv_file = open('diacritic-remove.gv', 'w')
    gv_file.write('''digraph G {
layout="twopi"
ranksep=1.5
fontsize=32
label="Remove diacritics"
labelloc="c"
node [shape="box" fontsize=24 ]
''')
    with open('diacritic-remove.tsv', 'r') as input_file:
        for line in input_file:
            if line != '\n' and line[0] != '#':
                (char_src, char_dst) = line[:-1].split('	')
                if char_src not in src_nodes:
                    src_nodes.append(char_src)
                if char_dst not in dst_nodes:
                    dst_nodes.append(char_dst)
                edge = '"{}" -> "{}"\n'.format(char_src, char_dst)
                if edge in edges:
                    print('ERROR')
                    exit(1)
                else:
                    edges.append(edge)

    for node in dst_nodes:
        gv_file.write('"{}" [label=<<b>{}</b><br/><font point-size="8">{}</font>> ]\n'.format(node, node, unicodedata.name(node).replace('LETTER ', 'LETTER_').replace(' ', '<br/>').replace('LETTER_', 'LETTER ').lower()))
    gv_file.write('''node [style="rounded" ]
''')
    for node in src_nodes:
        gv_file.write('"{}" [label=<<b>{}</b><br/><font point-size="8">{}</font>> ]\n'.format(node, node, unicodedata.name(node).replace('LETTER ', 'LETTER_').replace(' ', '<br/>').replace('LETTER_', 'LETTER ').lower()))
    for edge in edges:
        gv_file.write('{}\n'.format(edge))

    gv_file.write('''}
''')

#!/usr/bin/env python3

from unicodedata import category, name, normalize

def desc(char):
    return name(char).lower()

def remove_diacritics(s):
    return ''.join(c for c in normalize('NFKD', s.replace('ø', 'o').replace('Ø', 'O').replace('⁻', '-').replace('₋', '-'))
                  if category(c) != 'Mn')

if __name__ == '__main__':
    with open('diacritic-removal.tsv', 'r') as input_file:
        for line in input_file:
            if line == '\n' or line[0] == '#':
                continue
            (char_src, char_dst) = line[:-1].split('	')
            char = remove_diacritics(char_src)
            if char != char_dst:
                print('ERROR: character {} "{}"\t\tconverses to {} "{}" instead of {} "{}"'.format(char_src, desc(char_src), char, desc(char), char_dst, desc(char_dst)))
                exit(1)
            else:
                print('INFO: character {} "{}"\t\tconverses to {} "{}"'.format(char_src, desc(char_src), char_dst, desc(char_dst)))
                                
    with open('non-diacritic-removal.tsv', 'r') as input_file:
        for line in input_file:
            if line == '\n' or line[0] == '#':
                continue
            (char_src, char_dst) = line[:-1].split('	')
            char = remove_diacritics(char_src)
            if char != char_dst:
                print('ERROR: character {} "{}"\t\tconverses to {} "{}" instead of {} "{}"'.format(char_src, desc(char_src), char, desc(char), char_dst, desc(char_dst)))
                exit(1)
            else:
                print('INFO: character {} "{}"\t\tconverses to {} "{}"'.format(char_src, desc(char_src), char_dst, desc(char_dst)))

import argparse
from bcinfo.search import snp_pos2rsid


def main():
    print('Welcome to BCinfo')


def snp_pos2rsid_main():
    parser = argparse.ArgumentParser(description='convert SNP position to rsid')
    parser.add_argument('-org', help='organism', default='HUMAN')
    parser.add_argument('snp_position', type=str, help='snp position in <chr num>:<position> format')
    args = parser.parse_args()
    chr_id, chr_pos = args.snp_position.split(':')
    chr_id = chr_id.lstrip('chr')
    print(snp_pos2rsid(chr_id, chr_pos, args.org))

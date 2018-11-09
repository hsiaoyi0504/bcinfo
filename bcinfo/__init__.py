import argparse
from subprocess import Popen, PIPE
import xml.etree.ElementTree as ET


def main():
    print('Welcome to BCinfo')


def snp_pos2rsid():
    parser = argparse.ArgumentParser(description='convert SNP position to rsid')
    parser.add_argument('-org', help='organism', default='HUMAN')
    parser.add_argument('snp_position', type=str, help='snp position in <chr num>:<position> format')
    args = parser.parse_args()
    chr_id, chr_pos = args.snp_position.split(':')
    chr_id = chr_id.lstrip('chr')
    esearch = Popen(['esearch', '-db', 'snp', '-query', '"{}[CHR]" AND {}[ORGN] AND {}[CPOS]'.format(chr_id, args.org, chr_pos)], stdout=PIPE)
    efetch_command = ['efetch', '-format', 'docsum']
    efetch_snp_report = Popen(efetch_command, stdin=esearch.stdout, stdout=PIPE)
    root = ET.fromstring(efetch_snp_report.stdout.read().decode('utf-8'))
    result = root.findall('./DocumentSummary/SNP_ID')
    result = ['rs' + r.text for r in result]
    print(','.join(result))

from subprocess import Popen, PIPE
import xml.etree.ElementTree as ET


def snp_pos2rsid(chr_id, chr_pos, org='HUMAN'):
    esearch = Popen(['esearch', '-db', 'snp', '-query', '"{}[CHR]" AND {}[ORGN] AND {}[CPOS]'.format(chr_id, org, chr_pos)], stdout=PIPE)
    efetch_command = ['efetch', '-format', 'docsum']
    efetch_snp_report = Popen(efetch_command, stdin=esearch.stdout, stdout=PIPE)
    root = ET.fromstring(efetch_snp_report.stdout.read().decode('utf-8'))
    result = root.findall('./DocumentSummary/SNP_ID')
    result = ['rs' + r.text for r in result]
    return ','.join(result)
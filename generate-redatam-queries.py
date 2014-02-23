# coding: utf-8
import parse_variables

QUERY_TEMPLATE = u"""
// %(label)s
TABLE %(tablename)s
       AS AREALIST
       OF RADIO, %(variable)s 10.0
       OUTPUTFILE DBF 'C:\%(outfile)s.dbf'
       OVERWRITE
"""

def generate_query_for_variable(variable_name, config):
    vdef = parse_variables.variable_definition(variable_name, config)
    if vdef is None:
        return None
    q = QUERY_TEMPLATE % { 'tablename': (vdef['entname'] + vdef['name']).decode('windows-1252'),
                           'variable': (vdef['entname'] + '.' + vdef['name']).decode('windows-1252'),
                           'outfile': (vdef['entname'] + '-' + vdef['name']).decode('windows-1252'),
                           'label': vdef['label'].decode('windows-1252')  }
    return q


def generate_queries(config):
    for variable in [s for s in config.sections() if s.startswith('Variable')]:
        # print config.options(variable)
        # print config_section_map(variable, config)
        q = generate_query_for_variable(variable, config)
        if q is not None:
            print q.encode('utf-8')

if __name__ == '__main__':
    config = parse_variables.parse_ini('variables.ini')
    generate_queries(config)

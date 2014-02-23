# coding: utf-8
import ConfigParser, sys

QUERY_TEMPLATE = """
// %(label)s
TABLE %(tablename)s
       AS AREALIST
       OF RADIO, %(variable)s 10.0
       OUTPUTFILE DBF 'C:\%(outfile)s.dbf'
       OVERWRITE
"""


def config_section_map(section, config):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
        except:
            dict1[option] = None
    return dict1

def variable_definition(variable_name, config):
    rv = config_section_map(variable_name, config)
    if 'valuelabels' not in rv:
        print >>sys.stderr, "---- %s " % rv['name']
        return None
    rv['value_labels_list'] = []
    for i in range(1, int(rv['valuelabels']) + 1):
        rv['value_labels_list'].append(rv['vl' + str(i)])
    return rv


def parse_ini(fname):
    config = ConfigParser.ConfigParser()
    config.read(fname)
    return config

def generate_query_for_variable(variable_name, config):
    vdef = variable_definition(variable_name, config)
    if vdef is None:
        return None
    q = QUERY_TEMPLATE % { 'tablename': vdef['entname'] + vdef['name'] ,
                           'variable': vdef['entname'] + '.' + vdef['name'],
                           'outfile': vdef['entname'] + '-' + vdef['name'],
                           'label': vdef['label'].decode('windows-1252')  }
    return q


def generate_queries(config):
    for variable in [s for s in config.sections() if s.startswith('Variable')]:
        # print config.options(variable)
        # print config_section_map(variable, config)
        q = generate_query_for_variable(variable, config)
        if q is not None:
            print q

if __name__ == '__main__':
    config = parse_ini('variables.ini')
    generate_queries(config)

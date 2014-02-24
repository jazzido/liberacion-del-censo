# coding: utf-8
import ConfigParser, sys

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
        if rv['type'] == 'INTEGER':
            rv['value_labels_list'] = list(range(int(rv['rangemin']),
                                                 int(rv['rangemax']) + 1))
        else:
            print >>sys.stderr, "---- %s " % rv['name']
            return None
    else:
        rv['value_labels_list'] = []
        for i in range(1, int(rv['valuelabels']) + 1):
            rv['value_labels_list'].append(rv['vl' + str(i)])
    return rv


def parse_ini(fname):
    config = ConfigParser.ConfigParser()
    config.read(fname)
    return config

if __name__ == '__main__':
    config = parse_ini('variables.ini')

    print "Variable | Descripcion | Alias | Grupo"

    for variable in [s
                     for s in config.sections()
                     if s.startswith('Variable')]:

        vdef = variable_definition(variable, config)

        if vdef is None:
            continue

        if vdef['entname'] not in ('VIVIENDA', 'HOGAR', 'PERSONA'):
            continue

        print "%s.%s | %s | %s | %s " % (vdef['entname'], vdef['name'], vdef['label'].decode('windows-1252'), vdef.get('alias', ''), vdef.get('group', ''))

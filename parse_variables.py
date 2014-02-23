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

# coding: utf-8
import os
import parse_variables
import dbf

DBF_PATH = 'dbfs'

def dbf_csv(variable_name, config):
    vdef = parse_variables.variable_definition(variable_name, config)

    table = dbf.Table(os.path.join(DBF_PATH,
                                   vdef['entname'] + '-' + vdef['name'] + '.dbf'))

    return table

if __name__ == '__main__':
    config = parse_variables.parse_ini('variables.ini')
    # print dbf_csv('Variable37', config)
    raise Exception, "Falta terminar"

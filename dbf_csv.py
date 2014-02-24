# coding: utf-8
import os, sys, unicodecsv
import dbf
import parse_variables

DBF_PATH = 'dbfs'
CSV_PATH = 'csvs'

dbf_fname = lambda entname, name: entname + '-' + name + '.dbf'
csv_fname = lambda entname, name: entname + '-' + name + '.csv'

def dbf_csv(variable_name, config):
    vdef = parse_variables.variable_definition(variable_name, config)

    table = dbf.Table(os.path.join(DBF_PATH,
                                   dbf_fname(vdef['entname'], vdef['name'])))
    table.open()

    with open(os.path.join(CSV_PATH, csv_fname(vdef['entname'], vdef['name'])), 'w') as f:
        w = unicodecsv.writer(f)
        w.writerow(['radio'] + vdef['value_labels_list'] + ['TOTAL'])

        for row in table:
            w.writerow(row)


if __name__ == '__main__':
    config = parse_variables.parse_ini('variables.ini')

    for variable in [s
                     for s in config.sections()
                     if s.startswith('Variable')]:

        vdef = parse_variables.variable_definition(variable, config)

        if vdef is None:
            continue

        dbf_path = os.path.join(DBF_PATH,
                                dbf_fname(vdef['entname'],
                                          vdef['name']))

        if not os.path.exists(dbf_path):
            continue

        if vdef['entname'] not in ('VIVIENDA', 'HOGAR', 'PERSONA'):
            continue

        print >>sys.stderr, "Exportando tabla %s.%s" % (config.get(variable, 'entname'), config.get(variable, 'name'))

        dbf_csv(variable, config)




    #print dbf_csv('Variable37', config)
    ##raise Exception, "Falta terminar"

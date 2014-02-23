liberacion-del-censo
====================

Convertir los datos del Censo 2010 a un formato abierto

## Uso

Para generar consultas REDATAM:

```
python generate-redatam-queries.py

```

Salida (ejemplo):

```
// Tipo de vivienda agrupado
TABLE VIVIENDATIPVV
       AS AREALIST
       OF RADIO, VIVIENDA.TIPVV 10.0
       OUTPUTFILE DBF 'C:\VIVIENDA-TIPVV.dbf'
       OVERWRITE


// Tipo de vivienda particular
TABLE VIVIENDAV01
       AS AREALIST
       OF RADIO, VIVIENDA.V01 10.0
       OUTPUTFILE DBF 'C:\VIVIENDA-V01.dbf'
       OVERWRITE

```

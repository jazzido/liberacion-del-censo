liberacion-del-censo
====================

Conjunto de scripts para convertir a CSV datos almacenados en bases de datos confeccionadas con el sistema [REDATAM](http://www.eclac.cl/redatam/default.asp?idioma=IN).

  - `generate-redatam-queries.py`: Genera consultas REDATAM para exportar a formato DBF las variables definidas en `variables.ini` (se obtiene exportando el *diccionario* de REDATAM a formato ASCII)
  - `dbf_csv.py`: Convierte los DBFs generados por REDATAM a formato CSV.

## Uso

### Generar consultas REDATAM:

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

.....
```

Las consultas generadas deben ser copiadas al *Procesador Estadístico (R+Process)* de REDATAM. Una vez ejecutadas, generarán archivos DBF (uno por cada variable definida en `variables.ini`) en el directorio raíz del disco `C:`.

### Convertir DBFs a CSV

Los DBFs generados en el paso anterior, deben ser copiados al directorio `dbfs`.

```
python dbf_csv.py
```

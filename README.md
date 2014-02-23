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

.....
```

Las consultas generadas deben ser copiadas al *Procesador Estadístico (R+Process)* de REDATAM. Una vez ejecutadas, generarán archivos DBF (uno por cada variable definida en `variables.ini`, desagregado al nivel de *radio censal*) en el directorio raíz del disco `C:`.

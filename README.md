liberacion-del-censo
====================

Conjunto de scripts para convertir a CSV los datos del Censo Nacional de Población, Hogares y Viviendas 2010 publicados por INDEC mediante el sistema [REDATAM](http://www.eclac.cl/redatam/default.asp?idioma=IN).

  - `generate-redatam-queries.py`: Genera consultas REDATAM para exportar a formato DBF las variables definidas en `variables.ini`.
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

Las consultas generadas deben ser copiadas al *Procesador Estadístico (R+Process)* de REDATAM. Una vez ejecutadas, generarán archivos DBF (uno por cada variable definida en `variables.ini`, desagregado al nivel de *radio censal*) en el directorio raíz del disco `C:`.

### Convertir DBFs a CSV

```
python dbf_csv.py
```

## Variables extraídas

Variable | Descripcion | Alias | Grupo
--- | --- | --- | ---
VIVIENDA.INCALCONS | Calidad constructiva de la vivienda |  |
VIVIENDA.INCALSERV | Calidad de Conexiones a Servicios Básicos |  |
VIVIENDA.INMAT | Calidad de los materiales |  |
VIVIENDA.LOCAL | Localidad |  |
VIVIENDA.MUNI | Municipio |  |
VIVIENDA.TIPVV | Tipo de vivienda agrupado | TVAG | ESTRUCTURA
VIVIENDA.TOTHOG | Cantidad de Hogares en la Vivienda |  |
VIVIENDA.URP | Area Urbano - Rural | AREA | UBIGEO
VIVIENDA.V00 | Tipo de vivienda colectiva | TIPOVIVC | ESTRUCTURA
VIVIENDA.V01 | Tipo de vivienda particular | TIPOVIVP | ESTRUCTURA
VIVIENDA.V02 | Condición de ocupación | CONDOCUP | OCUPACION
HOGAR.ALGUNBI | Al menos un indicador NBI |  |
HOGAR.H05 | Material predominante de los pisos | PISO | ESTRUCTURA
HOGAR.H06 | Material predominante de la cubierta exterior del techo | TECHO | ESTRUCTURA
HOGAR.H07 | Revestimiento interior o cielorraso del techo | CIELO | ESTRUCTURA
HOGAR.H08 | Tenencia de agua | ABAGUA | FACILIDADES
HOGAR.H09 | Procedencia del agua para beber y cocinar | FUENAGUA | FACILIDADES
HOGAR.H10 | Tiene baño / letrina | SANITAR | FACILIDADES
HOGAR.H11 | Tiene botón, cadena, mochila para limpieza del inodoro | INODORO | FACILIDADES
HOGAR.H12 | Desagüe del inodoro | DESAGUE | FACILIDADES
HOGAR.H13 | Baño / letrina de uso exclusivo | USOSANIT | FACILIDADES
HOGAR.H14 | Combustible usado principalmente para cocinar | COMBUS | FACILIDADES
HOGAR.H15 | Total de habitaciones o piezas para dormir | TOTDOR | FACILIDADES
HOGAR.H16 | Total de habitaciones o piezas | TOTPIEZA | FACILIDADES
HOGAR.H19A | Heladera | HELADERA | EQUIPAMIENTO
HOGAR.H19B | Computadora | PC | TICS
HOGAR.H19C | Teléfono celular | CELULAR | TICS
HOGAR.H19D | Teléfono de línea | TELEFONO | TICS
HOGAR.INDHAC | Hacinamiento |  |
HOGAR.NHOG | Número del hogar en la vivienda |  | UBIGEO
HOGAR.PROP | Régimen de tenencia |  |
HOGAR.TOTPERS | Total de Personas en el Hogar |  |
PERSONA.CONDACT | Condición de actividad |  |
PERSONA.EDADAGRU | Edad en grandes grupos |  |
PERSONA.EDADQUI | Edades quinquenales |  |
PERSONA.P01 | Relación o parentesco con el jefe(a) del hogar | PARENT | GENERAL
PERSONA.P02 | Sexo | SEXO | GENERAL
PERSONA.P03 | Edad | EDAD | EDADES
PERSONA.P05 | En que país nació | LUGNAC | MIGRACION
PERSONA.P06 | Pais de nacimiento | PAISNAC | MIGRACION
PERSONA.P07 | Sabe leer y escribir | ALFAB | EDUCACION
PERSONA.P08 | Condición de asistencia escolar |  |
PERSONA.P09 | Nivel educativo que cursa o cursó |  |
PERSONA.P10 | Completó el nivel |  |
PERSONA.P12 | Utiliza computadora | PC | TICS

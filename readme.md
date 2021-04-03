Si se desea utilizar este software

-Debe contar con un usuario en Oracle llamado MEDISYSTEMADMIN con password root

-Para utilizar los triggers y auditoria debe correr en su base los scripts en la raíz del directorio
"MediSystemAuditorias.sql" y "MediSystemFuncionDelSistema.sql"

-Para poder replicar el uso de las multiples bases de datos
    -Tener en databases en sentings como default la base mongo
    -Se necesita elminar los archivos menos el init en migrations dentro de appMediSystem
    -Comentar en models.py(dentro de appMediSystem) todos los modelos en excepto el ebais(que será el que se guarde en mongo) y cualquier lugar en el programa donde se llamen 
    -Hacer las migraciones y migrar 
    -Descomentar los modelos 
    -Poner en default la base relacional 
    -Hacer las migraciones y migrar
    /Con esto queda en mongo las tablas no relacionales y en Oracle las relacionales

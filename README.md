# Manipulación de objetos Amazon S3 con Python
- Es necesario crear sus buckets en su cuenta de AWS
- Puede modificar el código por el nombre de los archivos para los cuales va a trabajar.
- Es muy importante que genere su propia credencial para hacer código desde la cuenta IAM de AWS


# Preparación del ambiente de trabajo


## Crear ambiente virtual

En una carpeta vacía crea el ambiente virtual con el siguiente código. 
Pégalo en la terminal y presionar enter para ejecutarlo.
<pre>
 python3 -m venv myenv
</pre>

Para Linux y mac activamos el ambiente creado con:
<pre>
source myenv/bin/activate
</pre>

Si estás trabajando en windows:
<pre>
myenv/Scripts/activate
</pre>

## Instalando librerias

En el archivo requirements.txt se listan las librerias necesarias para poder trabajar correctamente.
<pre>
pip install -r requirements.txt
</pre>
Para visualizar las librerias instaldas podemos hacerlo con:

Para Linuxy mac activamos el ambiente creado con:
<pre>
pip freeze
</pre>

## Respecto a AWS

1. Es necesatio que en tu cuenta de AWS crees un grupo de usuarios IAM
2. Otorgar a ese grupo los permisos "AmazonS3FullAccess".
3. Crear usuario y añadirlo al grupo creado anteriormente.
4. Crear las credenciales para código local para ese usuario y mantenerlas segura en el root del sistema operativo.


# Temario
                
1. Listar buckets de S3
2. Cargar archivos (objetos) a un bucket en S3
3. Crear bucket en S3 desde Python
4. Crear Subcarpetas en el bucket de S3
5. Descargar objectos (archivos) del bucket con python
6. Eliminar objectos
7. Eliminar buckets

# Repositorio de Conexiones a Redis y MongoDB

Este repositorio contiene scripts en Python para establecer conexiones tanto a Redis como a MongoDB, además de insertar datos simulados de publicaciones de Instagram.

## Prerequisitos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes:

- [Redis](https://redis.io/download) - Un servidor de almacenamiento en memoria
- [MongoDB Compass](https://www.mongodb.com/try/download/compass) - Una interfaz gráfica para MongoDB

## Configuración de MongoDB Atlas

Para utilizar MongoDB Atlas como base de datos, debes seguir estos pasos:

1. Crea una cuenta en [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) si aún no tienes una.
2. Inicia sesión en tu cuenta de MongoDB Atlas.
3. Crea un nuevo perfil en MongoDB Atlas para configurar tus bases de datos.

## Uso

1. Clona este repositorio en tu máquina local:

   bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   

2. Ejecuta los siguientes comandos para configurar las conexiones y agregar datos simulados a Redis y MongoDB:

   bash
   # Para Redis
   python redis_connection.py
   python insert_simulated_data_to_redis.py

   # Para MongoDB
   python mongodb_connection.py
   python insert_simulated_instagram_posts.py
   

## Notas adicionales

- Asegúrate de que Redis y MongoDB estén en funcionamiento antes de ejecutar los scripts.
- Ajusta la configuración de conexión en los scripts según tus necesidades y credenciales de MongoDB Atlas.
- Los datos insertados son simulados y pueden personalizarse según tus preferencias.

¡Disfruta explorando las conexiones a Redis y MongoDB en Python y la inserción de datos simulados de Instagram!

Si tienes alguna pregunta o problema, no dudes en [crear un issue](https://github.com/tu-usuario/tu-repositorio/issues) en este repositorio para que podamos ayudarte.


Asegúrate de reemplazar "tu-usuario" y "tu-repositorio" con tu nombre de usuario y nombre de repositorio en GitHub. También, personaliza cualquier otra información necesaria en el README.

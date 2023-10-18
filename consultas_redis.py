import redis

# Conectar al servidor
redis_host = '127.0.0.1' 
redis_port = 6379         
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)


# ID de la cuenta de Instagram qque vamos a usar
account_id = 'imperial'
post_id = 'post_2794'  # Post a analizar

# Queremos ver los likes de la publicacion anterior
likes = redis_client.hget(f'{account_id}:{post_id}', 'likes')

if likes is not None:
    print(f" El {post_id}, tiene {likes.decode('utf-8')} Likes")
else:
    print(f"El post {post_id} no se encontró en Redis.")


#Lo mismo pero con los shares

shares = redis_client.hget(f'{account_id}:{post_id}', 'shares')

if shares is not None:
    print(f" El {post_id}, tiene {shares.decode('utf-8')} Shares")
else:
    print(f"El post {post_id} no se encontró en Redis.")


##Total de likes de la cuenta Imperial

total_likes = 0

# Obtener todas las claves (IDs de publicaciones) en Redis para la cuenta
post_keys = redis_client.keys(f'{account_id}:post_*')

# Iterar a través de las claves y sumar los likes
for key in post_keys:
    post_data = redis_client.hgetall(key)
    likes = int(post_data.get(b'likes', 0))  # Enteros
    total_likes += likes

print(f"Likes de la cuenta {account_id}: {total_likes}")


##Ahora para ver las publicaciones con mas de 500 likes

# Obtener todas las claves (IDs de publicaciones) en Redis para la cuenta
post_keys = redis_client.keys(f'{account_id}:post_*')

# Crear un conjunto ordenado para almacenar la cantidad de "likes" y las claves de las publicaciones
orden = f'{account_id}:posts_sorted_by_likes'

# Iterar a través de las claves y agregar los "likes" y las claves al conjunto ordenado
for key in post_keys:
    post_data = redis_client.hgetall(key)
    likes = int(post_data.get(b'likes', 0))  # Pasar likes a enteros para analizarlos mejor
    if likes > 500:
        redis_client.zadd(orden, {key: likes})

# Obtener las claves de las publicaciones con más de 500 "likes"
top_posts = redis_client.zrevrange(orden, 0, -1, withscores=True)

print("Publicaciones con mas de 500 likes")


#Publicaciones con más de 500 "likes" y la cantidad de "likes" para cada una
for key, score in top_posts:
    print(f"Publicación: {key.decode('utf-8')}, Likes: {int(score)}")



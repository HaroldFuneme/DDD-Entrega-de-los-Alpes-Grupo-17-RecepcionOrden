# DDD-Entrega-de-los-Alpes-Grupo-17-RecepcionOrden
Microservicio de recepción de orden: Este microservicio se encargaría de recibir la orden del usuario y notificarla cuando identifique que la orden es consistente


### Crear imagen docker
docker build -t recepcion-orden .

### Correr servicio con docker
docker run -p 5000:5000 recepcion-orden

### Correr servicio con flask
 flask --app api run

### Docker build image
```bash
docker build . -f eda.Dockerfile -t orden/flask 
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run -p 5000:5000 orden/flask
```

### Docker compose
```bash
docker-compose up
```

Si desea detener el ambiente ejecute:

```bash
docker-compose stop
```
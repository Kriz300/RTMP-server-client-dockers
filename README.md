# RTMP Server-Client en Dockers

_Este proyecto trata de crear dos contenedores docker uno que transmita usando el protocolo rtmp en base a un servidor NGINX y otro con un cliente que reciba el streaming con el programa VLC._

### Instalación 🔧

_Basta con buildear los contenedores docker en sus carpetas correspondientes y runearlos._

**Build:**

```
$ sudo docker build .
```

_**Run:**_

* Server:

_Debe ser ejecutado al principio con el fin de que posea la ip 172.17.0.2 y comience la transmicion de forma automatica._

```
$ sudo docker run -it <imageid>
```

* Client:

_Se debe ingresar al contenedor para poder iniciar la captura de los datos enviados por el servidor, se espera arreglar esto en futuras actualizaciones._

```
$ sudo docker run -it <imageid>
root@xxxxxxxxxxxx:/tmp# ldconfig
root@xxxxxxxxxxxx:/tmp# cvlc --x11-display :0 rtmp://172.17.0.2/prueba/stream &
```

_Ahora toca abrir wireshark y captar los paquetes correspondientes al trafico entre ambos contenedores._

## Construido con 🛠️

**Servidor:**
* [Nginx](http://nginx.org/) - Sitio Web
* * [github](http://nginx.org/) - Github oficial
* * [nginx-http-flv-module](https://github.com/winshining/nginx-http-flv-module) - Modulo de protocolos
* * [nginx-rtmp-module](https://github.com/arut/nginx-rtmp-module) - Sub Modulo de protocolos

**Cliente:**
* [VLC](https://www.videolan.org/) - Sitio Web
* * [github](https://www.videolan.org/) - Github oficial

## Autores ✒️

* **Christian Muñoz I.** [Kriz](https://github.com/Kriz300)
* **Camilo Rubilar** [Niyet](#https://github.com/)

## Licencia 📄

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para detalles
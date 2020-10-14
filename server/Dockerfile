FROM ubuntu:latest
MAINTAINER camilo.rubilar@mail.udp.cl | christian.munoz@mail.udp.cl

WORKDIR /tmp
ENV TZ=America/Santiago

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get -yqq update \
    && apt-get -yqq upgrade \
    && apt-get clean \
    && apt-get install -yqq build-essential \
    && apt-get install ffmpeg -yqq \
    && apt-get install wget -yqq \
    && apt-get install git-all -yqq 
    
RUN git clone https://github.com/nginx/nginx.git \
    && wget https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.gz \
    && tar xzvf pcre-8.44.tar.gz \
    && wget https://www.zlib.net/zlib-1.2.11.tar.gz \
    && tar xzvf zlib-1.2.11.tar.gz \
    && wget https://www.openssl.org/source/openssl-1.1.1h.tar.gz \
    && tar xzvf openssl-1.1.1h.tar.gz \
    && rm -rf *.tar.gz \
    && cd /tmp/nginx \
    && git clone https://github.com/winshining/nginx-http-flv-module.git \
    && cd /tmp/nginx/auto \
    && mv configure /tmp/nginx \
    && cd .. \
    && ./configure --prefix=/usr/share/nginx \
            --sbin-path=/usr/sbin/nginx \
            --modules-path=/usr/lib/nginx/modules \
            --conf-path=/etc/nginx/nginx.conf \
            --error-log-path=/var/log/nginx/error.log \
            --http-log-path=/var/log/nginx/access.log \
            --pid-path=/run/nginx.pid \
            --lock-path=/var/lock/nginx.lock \
            --user=www-data \
            --group=www-data \
            --build=Ubuntu \
            --add-module=nginx-http-flv-module \
            --http-client-body-temp-path=/var/lib/nginx/body \
            --http-fastcgi-temp-path=/var/lib/nginx/fastcgi \
            --http-proxy-temp-path=/var/lib/nginx/proxy \
            --http-scgi-temp-path=/var/lib/nginx/scgi \
            --http-uwsgi-temp-path=/var/lib/nginx/uwsgi \
            --with-openssl=../openssl-1.1.1h \
            --with-openssl-opt=enable-ec_nistp_64_gcc_128 \
            --with-openssl-opt=no-nextprotoneg \
            --with-openssl-opt=no-weak-ssl-ciphers \
            --with-openssl-opt=no-ssl3 \
            --with-pcre=../pcre-8.44 \
            --with-pcre-jit \
            --with-zlib=../zlib-1.2.11 \
            --with-compat \
            --with-file-aio \
            --with-threads \
            --with-http_addition_module \
            --with-http_auth_request_module \
            --with-http_dav_module \
            --with-http_flv_module \
            --with-http_gunzip_module \
            --with-http_gzip_static_module \
            --with-http_mp4_module \
            --with-http_random_index_module \
            --with-http_realip_module \
            --with-http_slice_module \
            --with-http_ssl_module \
            --with-http_sub_module \
            --with-http_stub_status_module \
            --with-http_v2_module \
            --with-http_secure_link_module \
            --with-mail \
            --with-mail_ssl_module \
            --with-stream \
            --with-stream_realip_module \
            --with-stream_ssl_module \
            --with-stream_ssl_preread_module \
            --with-debug \
            --with-cc-opt='-g -O2 -fPIE -fstack-protector-strong -Wformat -Werror=format-security -D_FORTIFY_SOURCE=2' \
            --with-ld-opt='-Wl,-Bsymbolic-functions -fPIE -pie -Wl,-z,relro -Wl,-z,now' \
    && make \
    && make install

RUN cd /tmp/ \
    rm -r nginx-1.19.2/ openssl-1.1.1h/ pcre-8.44/ zlib-1.2.11/
    
RUN cd /etc/nginx/ \
    && chmod 775 nginx.conf
	    
RUN echo "rtmp{\n	server{\n		listen 1935;\n 		application prueba{\n			live on;\n			record off;\n		}\n	}\n}" >> /etc/nginx/nginx.conf

RUN chmod u=rwx,g=rx,o=r /etc/nginx/nginx.conf
    
RUN mkdir -p /var/lib/nginx \
    && echo "[Unit]\nDescription=A high performance web server and a reverse proxy server\nAfter=network.target\n\n[Service]\nType=forking\nPIDFile=/run/nginx.pid\nExecStartPre=/usr/sbin/nginx -t -q -g 'daemon on; master_process on;'\nExecStart=/usr/sbin/nginx -g 'daemon on; master_process on;'\nExecReload=/usr/sbin/nginx -g 'daemon on; master_process on;' -s reload\nExecStop=-/sbin/start-stop-daemon --quiet --stop --retry QUIT/5 --pidfile /run/nginx.pid\nTimeoutStopSec=5\nKillMode=mixed\n\n[Install]\nWantedBy=multi-user.target" >> /etc/systemd/system/nginx.service \
    && echo "[Nginx HTTP]\ntitle=Web Server (Nginx, HTTP)\ndescription=Small, but very powerful and efficient web server\nports=80/tcp\n\n[Nginx HTTPS]\ntitle=Web Server (Nginx, HTTPS)\ndescription=Small, but very powerful and efficient web server\nports=443/tcp\n\n[Nginx Full]\ntitle=Web Server (Nginx, HTTP + HTTPS)\ndescription=Small, but very powerful and efficient web server\nports=80,443/tcp" >> /etc/ufw/applications.d/nginx

CMD nginx \
    && ffmpeg -f lavfi -i testsrc=duration=60:size=1280x720:rate=30 testsrc.mpg -f flv rtmp://172.17.0.2/prueba/stream
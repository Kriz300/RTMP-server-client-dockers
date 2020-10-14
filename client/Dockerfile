FROM ubuntu:latest
MAINTAINER camilo.rubilar@mail.udp.cl | christian.munoz1@mail.udp.cl

WORKDIR /tmp/
ENV TZ=America/Santiago

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get -yqq update \
    && apt-get -yqq upgrade \
    && apt-get clean \
    && apt-get install -yqq build-essential \
    && apt-get install wget -yqq \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        libgl1-mesa-dri \
        libgl1-mesa-glx \
        pulseaudio \
        alsa-utils \
        dbus*
    
RUN wget http://get.videolan.org/vlc/3.0.11/vlc-3.0.11.tar.xz \
    && tar -xvf vlc-3.0.11.tar.xz
    
RUN cd /tmp/vlc-3.0.11 \
    && cp /etc/apt/sources.list /etc/apt/sources.list~ \
    && sed -Ei 's/^# deb-src /deb-src /' /etc/apt/sources.list \
    && apt-get update \
    && apt-get --no-install-recommends build-dep vlc -yqq
    
RUN cd /tmp/vlc-3.0.11 \
    && ./configure --enable-run-as-root\
    && make \
    && make install

RUN apt-get -y -f install \
    && apt-get -y install libvlc5 \
    && useradd -m vlc \
    && usermod -a -G audio,video vlc \
    && rm -rf /var/lib/apt/lists/*
     
USER vlc

WORKDIR /home/vlc/media

ENTRYPOINT ["vlc", "--no-qt-privacy-ask", "--no-metadata-network-access", "--snapshot-path=/home/vlc/snapshots"]
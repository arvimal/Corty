FROM fedora:latest

LABEL MAINTAINER="Vimal A R <arvimal81@gmail.com>"

RUN dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm && dnf clean all
RUN dnf -y update && dnf -y install poetry git && dnf clean all
RUN useradd corty && cd ~corty
RUN git clone https://github.com/arvimal/corty

CMD [ "/usr/bin/bash" ]
FROM openjdk:8

WORKDIR /opt/app

COPY log-viewer/log-viewer-1.0.3 .

CMD /bin/bash logviewer.sh

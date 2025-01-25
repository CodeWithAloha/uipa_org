FROM eclipse-temurin:8-jdk-alpine

RUN mkdir /usr/share/elasticsearch
WORKDIR /usr/share/elasticsearch

# su-exec is for interactive use in the container.
RUN apk add --no-cache su-exec curl && \
    addgroup -S -g 1000 elasticsearch && \
    adduser -S elasticsearch -u 1000 -G elasticsearch -h /usr/share/elasticsearch && \
    curl --retry 3 -S -L -o /tmp/elasticsearch.tar.gz https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.4.6/elasticsearch-2.4.6.tar.gz && \
    tar -zxf /tmp/elasticsearch.tar.gz --strip-components=1 && \
    rm /tmp/elasticsearch.tar.gz && \
    mkdir data logs config/scripts plugins && \
    chown -R elasticsearch:elasticsearch bin config data lib logs modules plugins

# cluster.name and network.host configured for our purposes.
COPY es.2_4_6_config.yml /usr/share/elasticsearch/config/elasticsearch.yml
RUN chown elasticsearch:elasticsearch /usr/share/elasticsearch/config/elasticsearch.yml

# Run the server as a regular user.
USER elasticsearch

ENV PATH=$PATH:/usr/share/elasticsearch/bin

CMD ["elasticsearch"]

EXPOSE 9200 9300


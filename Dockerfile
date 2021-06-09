FROM alpine:3.13
ADD startserver.py /startserver.py
RUN apk --no-cache add bash python3 py-pip && \
    ln -sf /usr/bin/python3 /usr/bin/python && \
    pip install -U jedi-language-server
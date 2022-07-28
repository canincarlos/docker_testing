FROM python:3

# https://www.youtube.com/watch?v=jyapP2Yy0AQ
# https://www.youtube.com/watch?v=p28piYY_wv8
# https://stackoverflow.com/questions/35931579/how-can-i-install-lxml-in-docker
# 



ENV PYTHONBUFFERED=1
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONIOENCODING 'utf-8'
ENV LANG 'C.UTF-8'

WORKDIR /django
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y \
        fonts-liberation \
        libasound2 \
        libatk-bridge2.0-0 \
        libatk1.0-0 \
        libatspi2.0-0 \
        libcups2 \
        libdbus-1-3 \
        libdrm2  \
        libgbm1 \
        libgtk-3-0\
        libnspr4 \
        libnss3 \
        libwayland-client0 \
        libxcomposite1 \
        libxdamage1 \
        libxfixes3 \
        libxkbcommon0 \
        libxrandr2 \
        xdg-utils \
        libu2f-udev \
        libvulkan1 \
        libgdal-dev \
        poppler-utils \
        antiword \
        tesseract-ocr \
        git \
        python3-lxml gcc libc-dev libxslt-dev \
        libxslt-dev && \
        pip install --no-cache-dir lxml>=4.5.0 \
    && pip install -r requirements.txt \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y -f ./google-chrome-stable_current_amd64.deb \
    && apt-get clean \
    && wget https://chromedriver.storage.googleapis.com/103.0.5060.134/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip
COPY . .
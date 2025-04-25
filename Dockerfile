FROM python:3.12

# Tạo user system "odoo"
RUN useradd -m -d /opt/odoo -U -r -s /bin/bash odoo

# Cài các packages cần thiết
RUN apt-get update && apt-get install -y \
    git build-essential wget \
    libpq-dev libxml2-dev libxslt1-dev libjpeg-dev \
    libldap2-dev libsasl2-dev libtiff5-dev libjpeg62-turbo-dev \
    liblcms2-dev libblas-dev libatlas-base-dev libssl-dev \
    python3-dev node-less npm \
    && rm -rf /var/lib/apt/lists/*

# Copy source Odoo
COPY . /opt/odoo

# Cài dependencies Python
RUN pip3 install --upgrade pip
RUN pip3 install -r /opt/odoo/requirements.txt

# Phân quyền
RUN chown -R odoo:odoo /opt/odoo

USER odoo
WORKDIR /opt/odoo

EXPOSE 8069

CMD ["python3", "odoo-bin", "-c", "/etc/odoo.conf"]
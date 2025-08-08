FROM mysql:latest

# Install nano, git, wget using microdnf
RUN microdnf update -y && \
    microdnf install -y nano git wget && \
    microdnf clean all

# Create log directory and set permissions
RUN mkdir -p /var/log/mysql && \
    chown -R mysql:mysql /var/log/mysql

# Overwrite the default my.cnf
COPY my.cnf /etc/my.cnf

# Ensure proper permissions
RUN chmod 644 /etc/my.cnf

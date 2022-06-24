# Run as root
if (( $EUID != 0 )); then
    echo "Please run as root"
    exit
fi

# Require internet
if ! ping -c 1 -q google.com > /dev/null; then
    echo "No internet connection"
    exit
fi

# Install dependencies

# update and upgrade
apt-get update -y && apt-get upgrade -y

# install pandoc
apt-get install pandoc -y

apt-get install pip -y
pip install sense_hat

# Copy program to /usr/local/sense-binary-watch
cp -r ../../sense-binary-watch /usr/local/sense-binary-watch

# Create system user
useradd -r -s /usr/sbin/nologin binary-watch-usr
chown -R binary-watch-usr:binary-watch-usr /usr/local/sense-binary-watch
# chmod +x /usr/local/sense-binary-watch/program/binary_watch.py
chmod 777 /usr/local/sense-binary-watch/program/binary_watch.py


# make program available global
# if file not exist 
if [ ! -f /usr/bin/binary_watch ]; then
    cp /usr/local/sense-binary-watch/program/binary_watch.py /usr/bin/binary_watch
fi



# Create pandoc file
# if file exist
if [ -f ./binary-watch.1]; then
    rm ./binary-watch.1
fi
pandoc binary-watch.1.md -s -t man -o binary-watch.1
gzip binary-watch.1
yes | cp -rf ./binary-watch.1.gz /usr/share/man/man1/
mandb


# Create systemd service
# if /etc/systemd/system/binary-watch.service
# if file exist
if [ -f /etc/systemd/system/binary-watch.service]; then
    rm /etc/systemd/system/binary-watch.service
fi
cp binary-watch.service /etc/systemd/system/binary-watch.service
systemctl daemon-reload

# Enable service
systemctl enable binary-watch.service

# Start service
systemctl start binary-watch.service



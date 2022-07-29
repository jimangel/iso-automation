# Update Ubuntu ISO's to autoinstall with Docker

This small Docker container modifies bootable ISO's to auto-install based on a GRUB config.

## How to use

```
git clone <this repo>

docker build --no-cache -t iso-automation:latest .

wget or curl the <ISO> to modify

docker run -e INPUT_ISO_NAME='ubuntu-22.04-live-server-amd64.iso' -v $PWD:/app iso-automation:latest
```

It takes about 5 minutes to run on an M1 mac, it would be great to add a progress bar or status output at somepoint...
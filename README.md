# Gezu Gandi Zone Updater

Gezu is a python3 script allowing to update a Gandi zone "A" record with the provided ip v4 address.

Private settings are stored in a rc file:
- gandi API key
- gandi zone id

The gezu script use the gzu package, provided under the packages folder.
The gzu package can be installed locally with pip:
pip3 install --upgrade packages/gzu

Sample command line (fake address):
./gezu --v4-addr 10.0.0.1

# base-station

A base station to run a rocket, and display some pretty graphs

## How to run
### Hardware code
* Construct circuit shown in schematic
* Move folders in ```hardware/src/libs``` to global Arduino library directory (usually ```Documents/Arduino/libraries```)
* Download libraries and install libraries found in the following repos
  * https://github.com/itead/ITEADLIB_Arduino_WeeESP8266 - ESP8266 library
* Build and upload

### Softare code

Each individual component requires a few minor setup steps:

* For the Google Static Maps downloader, you must set your Google maps api token as an environment variable with the key `google_maps_api_key`. (To do this using a unix based system, at the project root enter the following into your terminal: `export google_maps_api_key=YOUR_API_KEY`
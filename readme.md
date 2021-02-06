[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d0d4ba2150274a66b9871a7f071fae39)](https://www.codacy.com/app/pegasus.ict/AMM?utm_source=github.com&utm_medium=referral&utm_content=pegasusict/AMM&utm_campaign=badger)  
![GPL v3+](img/gplv3-or-later.svg)
# Audiophiles' Music Manager - Core V0.0.0-DEV
Updated: 2021-02-06   
Copyleft: 2017-2021 Mattijs Snepvangers  
Licence: GPL v3+ 

## GOAL
My goal is to write a suite that can REALLY _manage_ ALL aspects of a digital Music Collection of ANY size (my
collection consists of a little over 500k songs...)

## Currently, the suite will consist of:
 * Core `Python 3.9+`  
   This consists of a set of daemons which keep an eye on incoming files, processing them and storing them in the database.
 * Server `Php8 / Laravel8`  
   This will be a web/rpc server providing an interface to search the collection, creating and maintaining playlists and requests, as well as administering the settings for the 'core'; file naming conventions, black/whitelists etc.
 * Admin  
   python based multiplatform GUI
 * Client  
   python based multiplatform GUI

### (planned) REQUIREMENTS:
* Core:
    * Python 3.x
    * MySQL/MariaDB Server
* Server/webUI
    * PHP8/Laravel8

### Planned Functionality (MoSCoW prioritizing):
![Must](https://via.placeholder.com/60x40/ff0000/000000?text=Must) ![Should](https://via.placeholder.com/80x40/ff6600/000000?text=Should) ![Could](https://via.placeholder.com/80x40/ffff00/000000?text=Could) ![Would](https://via.placeholder.com/80x40/00ff00/000000?text=Would)
 -[ ] ![Must](https://via.placeholder.com/15/f00?text=+) `Must` Index files
 -[ ] ![Must](https://via.placeholder.com/15/f00?text=+) `Must` Purge Non-Audio files 
 -[ ] ![Must](https://via.placeholder.com/15/f00?text=+) `Must` Parse & Purge Tags
 -[ ] ![Must](https://via.placeholder.com/15/f00?text=+) `Must` Store File- & Tag-Data in DB
 -[ ] ![Must](https://via.placeholder.com/15/f00?text=+) `Must` Generate Audio-Fingerprint
 -[ ] ![Must](https://via.placeholder.com/15/f00?text=+) `Must` Calculate Audio Quality(bitrate/channels/sampling)
 -[ ] ![Must](https://via.placeholder.com/15/f00?text=+) `Must` Remove Duplicates Based on Quality
 -[ ] ![Must](https://via.placeholder.com/15/f00?text=+) `Must` Integrate Tags & Art in database, Fix (& Merge) Artist names & Titles
 -[ ] ![Must](https://via.placeholder.com/15/f00?text=+) `Must` Insert Tags in Files
 -[ ] ![Must](https://via.placeholder.com/15/f00?text=+) `Must` Rename & Move Files to target dir structure

 -[ ] ![Should](https://via.placeholder.com/15/f60?text=+) `Should` Transcode
 -[ ] ![Should](https://via.placeholder.com/15/f60?text=+) `Should` Normalize
 -[ ] ![Should](https://via.placeholder.com/15/f60?text=+) `Should` Retrieve Artist names, Album titles, ft. Artists, Composer/writer, Album art, Lyrics
 -[ ] ![Should](https://via.placeholder.com/15/f60?text=+) `Should` AJAX Interface
  
 -[ ] ![Would](https://via.placeholder.com/15/ff0?text=+) `Could` GUI 

 -[ ] ![Could](https://via.placeholder.com/15/0f0?text=+) `Would` Android Client
 -[ ] ![Could](https://via.placeholder.com/15/0f0?text=+) `Would` DLNA media server, audio player integration(?)

### Future ideas (still under debate):

* Acoustic Optimisation
* Automagic searching & downloading of missing songs

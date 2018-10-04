# NITT-Results-Scraper

[![PRs Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](http://makeapullrequest.com) [![made-with-python](https://img.shields.io/badge/made%20with-python-blue.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-BSD-green.svg)](LICENSE)

NITT-Results-Scraper is a simple python tool to check any student CGPA with their Octa credentials.

### Installation
##### Build from source
* ```
    $ git clone https://github.com/BharathKumarRavichandran/NITT-Results-Scraper.git
  ```
* ```
    $ cd NITT-Results-Scraper
  ```
*   Install required packages :
    ```
        $ python setup.py install
    ```
* Setting geckodriver :
    * Go to `https://github.com/mozilla/geckodriver/releases`
    * Download appropriate geckodriver file for your environment.
    * Extract the file and open the extracted folder.
    * Copy the executable file and paste it in suitable folder :
        * Example directory `/usr/local/bin` for ubuntu.
    * Give executable file permission for the pasted file named 'geckodriver' : 
    ```
        $ sudo chmod +x /usr/local/bin/geckodriver
    ```
    * Setting environment variable : 
    ```
        $ export PATH = $PATH:/usr/local/bin/geckodriver
    ```
    * Create a file named : `config.py`.
    * Copy the contents of `config.py.example` to `config.py`.
        * Replace `Enter-your-geckodriver-file-path-here` with your geckodriver file path in `config.py`.

### Requirements
* The application needs Firefox.
* The user should be connected to NITT Wifi (HP) for this application to work.

## Technologies used
* [Python](https://www.python.org/) 

## License
[BSD-3-Clause](LICENSE)

![Built with love](http://forthebadge.com/images/badges/built-with-love.svg)
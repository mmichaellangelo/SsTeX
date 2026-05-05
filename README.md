# <img src="external/graphics/icon/sstex_icon.png" style="height: 1em;"> SsTeX

## About
SsTeX is an AI-powered tool for Windows that helps convert screenshots of math equations into LaTeX. It is designed to be run in the background and appears as a system tray icon. Simply screenshot an equation and left-click the icon. Once complete, a notification will appear and the LaTeX code will be copied to your clipboard for easy access.  

## Installation
To install SSTeX, run the guided installer: `SsTeXSetup.exe`.  

## Usage
On the first run, SsTeX will ask you for your Gemini API key (this is required). You'll see the logo pop up in your system tray.  

## Building
If you'd like to build SsTeX from scratch, I've included some powershell scripts in the `scripts` folder which include the necessary build commands.  
*Scripts must be run from the project's root directory* (e.g. `.\scripts\build_all.ps1`)  

**`build_exec.ps1`** uses [PyInstaller](https://pyinstaller.org/) to bundle the program as a Windows executable.  

**`build_installer.ps1`** uses [InnoSetup](https://jrsoftware.org/isinfo.php) to create an installer. You'll need to run the `build_exec.ps1` script before running this. You must have InnoSetup (v6) installed and `INNO.exe` must be added to your system PATH.  

**`build_all.ps1`** simply runs `build_exec.ps1` followed by `build_installer.ps1` as an all-in-one build script.  

## Directories
During the installation process, you'll provide a location for the program's binary executable. Data and configuration files will be stored in the `%APPDATA%\SsTeX\` directory.

## Gemini
SsTeX uses Google's Gemini API to convert screenshots into code. Please review the [Gemini Terms of Service](https://ai.google.dev/gemini-api/terms) and Google's [Privacy Policy](https://policies.google.com/privacy) before installing or using the program. Gemini was selected because it offers a generous free tier for API usage and does not require you to enter credit card information.  

You'll need a [Gemini API Key](https://ai.google.dev/gemini-api/docs/api-key) to use the program. On the program's first run, you'll be prompted for this API key.   

## License
SSTeX is distributed under the [GNU GPLv3 License](LICENSE). See third party license information [here](THIRD-PARTY-NOTICES.txt).  

## AI Disclosure
Some of the program's code was written using AI tools.  

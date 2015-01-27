Sublime Text 2/3 - Macdown App Menu plugin
=========================================

Adds a handy menu item that opens [Macdown.app](http://macdown.uranusjr.com/)

**Issues:** https://github.com/diimdeep/sublime-text-macdown-app-menu/issues

![screenshot](http://i.imgur.com/oCEb7.jpg)

Adapted from [Marked App Menu](https://github.com/icio/sublime-text-marked) plugin for Sublime Text by Chris Tan. Originally developed by [jocelynmallon](https://github.com/jocelynmallon) and [icio](https://github.com/icio).


## Installation Instructions

**Package Installer:**

* Install [Sublime Package Control](http://wbond.net/sublime_packages/package_control)
* Select "Package Control: Install Package" from the Command Palette (⌘⇧P)
* Find "Macdown App Menu" and select

**Manually:**

* Install [Macdown 2.app](http://macdown.uranusjr.com/)  `brew cask install macdown.`
* Download [sublime-text-macdown-app-menu](https://github.com/diimdeep/sublime-text-macdown-app-menu/zipball/master) and copy unzipped folder to your Sublime Text packages folder (Sublime Text (2) → Preferences → Browse Packages...)
* Restart Sublime Text

```bash
# For Sublime Text 2
cd ~/Library/Application Support/Sublime Text 2/Packages
mkdir Macdown.app\ Menu
curl -L https://github.com/diimdeep/sublime-text-macdown/tarball/master | tar --strip-components 1 -C Macdown.app\ Menu -xvf -
```


## Usage

With the view selected containing the file you wish to preview in Macdown:

**Command Palette:**

* Select "Macdown" from the Command Palette (⌘⇧P)

**Keyboard Shortcut:**

* Add the following to your User Key Binding, adjusting the key configuration to taste:

    ```json
    { "keys": ["super+alt+m"], "command": "macdown" }
    ```

**Menus:**

* Select Tools → Macdown

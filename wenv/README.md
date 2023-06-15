# First, install wine and configure. In the terminal run:
brew install --cask xquartz
brew install --cask --no-quarantine wine-stable
brew install winetricks

# Create the alias and symbolic links:
echo "alias wine=/Applications/Wine\ Stable.app/Contents/Resources/wine/bin/wine64" >> ~/.zshrc
sudo ln -sf /usr/local/bin/wine64 /usr/local/bin/wine
sudo ln -sf /Applications/Wine\ Stable.app/Contents/Resources/wine/bin/wine64 wine
sudo ln -sf /Applications/Wine\ Stable.app/Contents/Resources/wine/bin/wine64 /opt/homebrew/bin/wine
Run wine64 winecfg and click OK. 

# Check wine is configured correctly: 
wine --version
wine64 --version
wine-8.0.1
Both commands above should yield the same result. 
If an error such as wine: could not exec the wine loader or Bad CPU type in executable: ‘wine', restart the terminal, remove the alias for wine via unalias wine and reapply the symbolic links above and recreate the alias. 
Check wine again (restart the terminal if needed). 

# Install Python through Wine:
Find and download the version of Python that matches your version (run python --version).
Download Python 
Make sure to download the 64 bit version. 
Run wine64 python-3.9.6-amd64.exe

# Install wenv:
Create a .wenv.json file with the following items: 

{
    "arch": "win64",
    "pythonversion": "3.9.6",
    "winearch": "win64"
}

Navigate to the directory where the .wenv.json file is stored and run:
python3 -m pip install wenv
If a warning such as the following appears, run pip uninstall wenv then remove the directory associated to _wenv_python and make sure to remove anything else associated to wenv in the site-packages directory. 
Defaulting to user installation because normal site-packages is not writeable
Collecting wenv
  Using cached wenv-0.5.1-py3-none-any.whl (33 kB)
Installing collected packages: wenv
  WARNING: The scripts _wenv_python and wenv are installed in '/Users/fmartinez/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed wenv-0.5.1

# Create the symbolic links for wenv:
sudo ln -sf /usr/local/bin/wenv wenv
sudo ln -sf /Users/fmartinez/Library/Python/3.9/bin/wenv wenv
sudo ln -sf /Users/fmartinez/Library/Python/3.9/bin/wenv /usr/local/bin/wenv

# Check wenv is configured correctly:
wenv version
0.5.1
Initialize wenv:
Navigate to the directory where your .wenv.json file is stored and run wenv init.
If it appears your terminal is stuck and nothing is happening, hit Enter on your keyboard. Then run wenv pip install pyinstaller. Again, if it appears that the terminal is stuck, hit Enter. If there are any errors retry the step. If an error such as zsh: command not found: wenv or No such file or directory: 'wenv' then go back to restart the setup at the symbolic links for wenv. If an error such as Bad CPU type in executable: 'wine' or wine: could not exec the wine loader, go back to restart the setup at the symbolic links for wine. 

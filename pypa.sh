#!/bin/bash
mod_loc="$(python3 -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')"
filename="build.zip"
cd $mod_loc && zip -r $filename .
cd ${OLDPWD}
mv $mod_loc/$filename .
zip -g $filename get_data.py

#! /bin/bash
# Tip: this file must be executed in it's direct containing folder,

## locations - could modify, modify it before install if need,
bin_dir="/usr/bin"

## locations - can't modify,
pygtrans_config_dir="$HOME/.config/pygtrans"

## command - via "ln -s"
ln -sf "$PWD/main.py" "$bin_dir/pygtrans"
if [ $? -eq 0 ]; then
	echo "Done."
	echo "Use 'pygtrans' as command."
fi

## config file
mkdir -p $pygtrans_config_dir
cp ./template/config.ini.original $pygtrans_config_dir/config.ini

exit 0


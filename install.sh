#! /bin/bash
# Tip: this file must be executed in it's direct containing folder,

bin_dir="/usr/bin"

ln -sf "$PWD/main.py" "$bin_dir/pygtrans"
if [ $? -eq 0 ]; then
	echo "Done. Use 'pygtrans' as command."
fi

exit 0


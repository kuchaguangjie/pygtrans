##README

Simple translator base on google translate, using python.

---
###Warning

This project is not usable any more, due to Google has add dynamic validation mechanism for translation, sorry about that.

refer:	https://github.com/kuchaguangjie/pygtrans/issues/1

---
###Install

see:
	doc/2-1.install.txt

###Configuration

After install could config at:
	~/.config/pygtrans/config.ini

###Usage

command line:

`pygtrans <input_string> [<target_language>] [<source_language>]`

e.g

	# translate "hi" to default language,
	pygtrans hi
	
	# translate "hi" to Japanese,
	pygtrans hi ja
	
	# translate "hi" from English to Japanese,
	pygtrans hi ja en

---
###Bug report

Email: kuchaguangjie@gmail.com

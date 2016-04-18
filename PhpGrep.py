#!/usr/bin/env python
# Author : #aojald
# PHP grep generator for source code audit

extension_file = ['php','php3','php4','ini','include','php.ini','old','bak']

ext = ','.join(extension_file)
 
dangerous_func = open ('dangerous_functions.txt','r')
print " fgrep -Ri --color --include=\*.{php,php3,php4,ini,include,php.ini,old,bak} ' $_GET(' ./"
print " fgrep -Ri --color --include=\*.{php,php3,php4,ini,include,php.ini,old,bak} ' $_GET[' ./"
print " fgrep -Ri --color --include=\*.{php,php3,php4,ini,include,php.ini,old,bak} ' $_POST(' ./"
print " fgrep Ri --color --include=\*.{php,php3,php4,ini,include,php.ini,old,bak} ' $_POST[' ./"
print " fgrep Ri --color --include=\*.{php,php3,php4,ini,include,php.ini,old,bak} ' `' ./"
for i in dangerous_func:
        i=i.replace("\n", "")
        print ' fgrep -Ri --color --include=\*.{'+ext+'} '+'\' '+i+'(\''+' ./'

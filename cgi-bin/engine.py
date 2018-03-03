#!D:/Programs/Python/python.exe
# -*- coding: utf-8 -*-

import os, sys
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout

print('''\
Content-type: text/html\r\n
<html>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Site</title>
	<!-- <link rel="shortcut icon" href="/images/1.png" type="image/png"> -->
	<link rel="stylesheet" href="https://unpkg.com/normalize.css@8.0.0/normalize.css">
	<link rel="stylesheet" href="/css/main.css">
	<link href="https://fonts.googleapis.com/css?family=Lato:900,900i|Oswald:700&amp;subset=cyrillic" rel="stylesheet">
</head>
	<body>
	''')

with open('../src/html/header.html', mode='r') as file_read:
	for line in file_read:
		print(line)

print('''
	<div class='header-wrapper body-wrapper'>
	''')

with open('../src/html/main.html', mode='r') as file_read:
	for line in file_read:
		print(line)

print('''
	</div>
	''')

with open('../src/html/footer.html', mode='r') as file_read:
	for line in file_read:
		print(line)

print('''
</div>
</body>
</html>
''')

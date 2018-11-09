import sublime
import sublime_plugin
import base64
import hashlib
import binascii
import urllib

class Base64decodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view
		try:
			sels = len(list(v.sel()))
			for i in range(0, sels):
				selected = v.substr(v.sel()[i])
				b64_str = base64.b64decode(bytes(selected,'utf-8')).decode('utf-8')
				v.replace(edit, v.sel()[i], b64_str)
		except Exception as err:
			sublime.error_message(str(err))

class Base64encodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view
		sels = len(list(v.sel()))
		for i in range(0, sels):
			selected = v.substr(v.sel()[i])
			b64_str = base64.b64encode(selected.encode('utf-8')).decode("utf-8")
			v.replace(edit, v.sel()[i], b64_str)

class UrlencodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view
		sels = len(list(v.sel()))
		for i in range(0, sels):
			selected = v.substr(v.sel()[i])
			url_str = urllib.parse.quote(selected.encode('utf-8'))
			v.replace(edit, v.sel()[i], url_str)

class UrldecodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view
		try:
			sels = len(list(v.sel()))
			for i in range(0, sels):
				selected = v.substr(v.sel()[i])
				url_str = urllib.parse.unquote(selected)
				v.replace(edit, v.sel()[i], url_str)
		except Exception as err:
			sublime.error_message(str(err))

class HexdecodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view
		sels = len(list(v.sel()))
		try:
			for i in range(0, sels):
				selected = v.substr(v.sel()[i])
				selected = selected.strip(' ')
				selected = selected.replace('\\x','')
				hex_bytes =binascii.unhexlify(selected)
				v.replace(edit, v.sel()[i], str(hex_bytes, 'ascii'))
		except Exception as err:
			sublime.error_message(str(err))

class HexencodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view
		sels = len(list(v.sel()))
		for i in range(0, sels):
			selected = v.substr(v.sel()[i])
			selected = selected.strip(' ')
			hex_bytes = binascii.hexlify(bytes(selected,'utf-8'))
			v.replace(edit, v.sel()[i], str(hex_bytes, 'ascii'))

class Hashmd5Command(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view
		sels = len(list(v.sel()))
		m = hashlib.md5()
		for i in range(0, sels):
			selected = v.substr(v.sel()[i])
			m.update(selected.encode('utf-8'))
			v.replace(edit, v.sel()[i], m.hexdigest())

class Hashsha1Command(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view
		sels = len(list(v.sel()))
		m = hashlib.sha1()
		for i in range(0, sels):
			selected = v.substr(v.sel()[i])
			m.update(selected.encode('utf-8'))
			v.replace(edit, v.sel()[i], m.hexdigest())



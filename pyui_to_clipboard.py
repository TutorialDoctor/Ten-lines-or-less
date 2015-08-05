#Copy pyui to clipboard
import editor
import re
file_path = editor.get_path()
pattern = "\w+\s*\b*\w+\.py"
name = re.findall(pattern,file_path)
filename= ''.join(name)
ui_filename = filename+'ui'
try:
	with open(ui_filename) as in_file:
		clipboard.set(in_file.read())
	print('contents of {} are on the clipboard'.format(ui_filename))
except IOError:
	print 'The file {} has no associated UI file to add to the clipboard.'.format(filename)
	print ui_filename
# The regular expression needs work. doesnt work for single letter names.

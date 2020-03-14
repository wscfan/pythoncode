user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi'
}

for key, value in user_0.items():
	print('\nkey:' + key)
	print('value:' + value)
print('\n')

for key in user_0.keys():
	print(key)
print('\n')

for value in user_0.values():
	print(value)
print('\n')

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}
for language in set(favorite_languages.values()):
	print(language)
 

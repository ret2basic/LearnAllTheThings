def make_album(artist, title, songs=None):
	album = {'artist': artist, 'title': title}
	if songs:
		album['songs'] = songs
	return album

print(make_album('Pink Floyd', 'The Dark Side of the Moon', 10))
print(make_album('The Beatles', 'Abbey Road'))
print(make_album('The Beach Boys', 'Pet Sounds'))

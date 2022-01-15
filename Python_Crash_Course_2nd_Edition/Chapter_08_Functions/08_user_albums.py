def make_album(artist, title, songs=None):
	album = {'artist': artist, 'title': title}
	if songs:
		album['songs'] = songs
	return album

prompt = "Please enter the info of albums: "
prompt += "(Press q at any time to quit)"
print(prompt)

while True:
	artist = input("Please enter the artist of the album: ")
	if artist == 'q':
		print("Bye!")
		break


	title = input("Please enter the title of the album: ")
	if title == 'q':
		print("Bye!")
		break

	print(make_album(artist, title))


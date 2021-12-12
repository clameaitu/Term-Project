from manga import *

mangas = read_manga('data\manga_data.csv')
# print('Mangas read', len(mangas))
# print(mangas[:3])
# print(mangas[3:])

# print(filter_nonpublishing(mangas)[:3])

print(calculate_chapters_per_volume(mangas)[:3])
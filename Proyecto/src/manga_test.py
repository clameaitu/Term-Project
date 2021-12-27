from manga import *

mangas = read_manga('data\manga_data.csv')
print('Mangas read', len(mangas))
print(mangas[:3])
print(mangas[3:])

print(filter_nonpublishing(mangas)[:3])

print(calculate_chapters_per_volume(mangas)[:3])

print(best_scoring_by_more_than_n_people_manga(mangas,500)[:3])

print(obtain_the_n_most_favourited_manga_by_status(mangas, status="Finished", n=3)[:3])
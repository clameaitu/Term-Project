import csv
from collections import namedtuple, Counter, defaultdict
from datetime import date, datetime

manga = namedtuple('manga','title, status, volumes, chapters, publishing, rank, score, scored_by, popularity, members, favourites, synopsis, publish_date, genre')

def read_manga(file):
    with open(file, 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f, delimiter = ";")
        mangas = [manga(title, status, int(volumes), int(chapters), publishing, int(rank), float(score), int(scored_by), int(popularity), int(members), int(favourites), synopsis, publish_date, genre) 
        for title, status, volumes, chapters, publishing, rank, score, scored_by, popularity, members, favourites, synopsis, publish_date, genre in reader]
    return mangas

# def read_manga(file):
#     mangas = []
#     with open(file, encoding='utf-8') as f:
#         for line in f:
#             title, status, volumes, chapters, publishing, rank, score, scored_by, popularity, members, favourites, synopsis, publish_date, genre = line.split(';')
#             volumes = int(volumes)
#             chapters = int(chapters)
#             if publishing == "FALSE":
#                 publishing = False
#             else: publishing = True
#             rank = int(rank)
#             score = float(score)
#             scored_by = int(scored_by)
#             popularity = int(popularity)
#             members = int(members)
#             favourites = int(favourites)
#             publish_date = datetime.strptime(publish_date,'%d/%m/%Y')
#             genre_aux = genre.split(',')
#             manga(title, status, volumes, chapters, publishing, rank, score, scored_by, popularity, members, favourites, synopsis, publish_date, genre_aux)
#             mangas.append(manga)
#     return mangas        

def filter_nonpublishing(mangas):
    nonpublishing = [(e.title, e.status, e.volumes, e.chapters) for e in mangas if e.publishing=="FALSE"]
    return nonpublishing

def calculate_chapters_per_volume(mangas):
    mangas_not_published = filter_nonpublishing(mangas)
    volumes = [e.volumes for e in mangas if e.publishing=="FALSE"]
    chapters = [e.chapters for e in mangas if e.publishing=="FALSE"]
    manga_per = [e2/e1 for e1, e2 in zip(volumes,chapters)]
    mangas_per = mangas_not_published.append(manga_per)
    return mangas_per

def best_scoring_by_more_than_n_people_manga(mangas,n=500):
    pass

def obtain_the_n_most_favourited_manga_by_status(mangas, status="Finished", n=3):
    pass

# Ignora esto como no me sale lo de arriba y no sé cómo funciona la lista de genres estoy perdida
# En el read me he puesto lo que quiero hacer

# def group_genre_by_year(mangas):
#  res = {}
#  for manga in mangas:
#      for genre in genres:
#         key = manga.year
#         if key not in res:
#              res[key] = set(mangas.genre)
#         else:
#             res[key].add(mangas.genre)
#  return res


# Progamming fundamentals 1st term project (Year  \<21\>/\<22\>)
Author: Claudia Meana Iturri   uvus:\ clameaitu

This project's objective is to analyze the top 1000 manga’s ranked by myAnimelist dataset posted on Kaggle which can be downloaded using the following URL (https://www.kaggle.com/astronautelvis/top-1000-ranked-mangas-by-myanimelist?select=top_1000.csv). This dataset originally had 17 columns of which none where of date type. As such, I have chosen 14 out of the 17 (one of them was modified to be type float) and have added another column with the randomly generated dates corresponding to the date when the manga was published.

## Folder structure for the project

* **/src**: Contains the different python modules that make up the project.
  * **\<manga.py\>**: Contains the functions to analyze the manga data.
  * **\<manga_test.py\>**: Contains the test functions for the module manga.py.
  * **\<manga_dataconversion.py\>**: Contains the data conversion functions
  * **\<manga_graph.py\>**:Contains the functions to draw graphs
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<manga_original.csv\>**: The original data file
    * **\<manga_data.csv\>**: Data file with the manga information
    
## *Dataset* Structure

This data set is made out of  \<15\> columns, with the following description:

* **\<title>**: of type \<str\>, the name of the manga
* **\<status>**: of type \<str\>, whether the manga has finished, is still being published or is on hiatus
* **\<volumes>**: of type \<int\>, the number of volumes the manga has
* **\<chapters>**: of type \<int\>,  the number of chapters the manga has
* **\<publishing>**: of type \<boolean\>, whether the manga is still being published or not 
* **\<rank>**: of type \<int\>, the rank according to the scores of the manga
* **\<score>**: of type \<float\>, the mean of the score people have rated the manga out of 10
* **\<scored_by>**: of type \<int\>, the number of people that have participated in scoring the manga
* **\<popularity>**: of type \<int\>, a ramking of the most popular manga based on the number of members and favourites of the manga
* **\<members>**: of type \<int\>, the number of people that are following the manga 
* **\<favourites>**: of type \<int\>, the number of people that have favourited the manga 
* **\<synopsis>**: of type \<str\>, brief summary of the manga
* **\<publish_date>**: of type \<str\>, the date the manga was published
* **\<genre>**: of type \<str\>, a list of genres each manga belongs to


## Implemented types

To work with the data in the dataset the following tupple was made:

manga = namedtuple('manga', 'title, status, volumes, chapters, publishing, rank, score, scored_by, popularity, members, favourites, synopsis, publish_date, genre')

with the following types:

manga(str, str, int, boolean, int, int, int, int, int, int, str, datetime.date, list)

## Implemented Functions
The following functions were implemented in the project:

### \<Module manga\>

* **<read_manga>**: Reads the file and changes the format of the str to the correct one for the project
* **<filter_nonpublishing>**: Given the mangas, give back a list of tupples with the title, status, volumes and chapters of FALSE publishing mangas
* **<calculate_chapters_per_volume>**: Given the mangas, give back a list of tupples with the title, volumes, chapters and how many chapters pero volume (the mangas that are being published don't have a fixed number of chapters and volumes so we filtered those out earlier)
* **<best_scoring_by_more_than_n_people_manga>**: Given the mangas and a value n, give back the the list of tupples ordered by the best score with a minimun number of scored_by
* **<obtain_the_n_most_favourited_manga_by_status>**: Given the mangas, the status and the the number of elements of the list, n. Give back a list of the tupples ordered by favourites within the status chosen and only show the n first elements.
* **<group_genre_by_year>**: Given the mangas, create a dicctionary with the key being the year and for each we will add the genres of the mangas published in that year


### \<Module manga_test\>

* **<test funcion 1>**: Descripción de las pruebas realizadas a la función 1.
* **<test funcion 2>**: Descripción de las pruebas realizadas a la función 2.
* ...
* 
### \<Module graph\>

* **<funcion 1>**: Descripción de la función 1.
* **<funcion 2>**: Descripción de la función 2.
* ...

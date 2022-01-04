# Progamming fundamentals 1st term project (Year  \<21\>/\<22\>)
Author: Claudia Meana Iturri   uvus:\ clameaitu

This project's objective is to analyze the Suicide Rates Overview 1985 to 2016 dataset posted on Kaggle which can be downloaded using the following URL (https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016). This dataset originally had 12 columns, I have chosen 10 out of the 12 (one of them was modified to be type float).

## Folder structure for the project

* **/src**: Contains the different python modules that make up the project.
  * **\<suicide.py\>**: Contains the functions to analyze the manga data.
  * **\<suicide_test.py\>**: Contains the test functions for the module manga.py.
  * **\<suicide_parse.py\>**: Contains the data conversion functions
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<suicide_data.csv\>**: Data file with the manga information
    
## *Dataset* Structure

This data set is made out of  \<10\> columns, with the following description:

* **\<country>**: of type \<str\>, the name of the country where people comitted suicide
* **\<year>**: of type \<datetime\>, the year in which people comitted suicide
* **\<sex>**: of type \<boolean\>, the gender of the people who comitted suicide, if female, it is true, if male, it is false
* **\<age_range>**: of type \<str\>,  the age range of the people who comitted suicide
* **\<suicide_n>**: of type \<int\>, the number of people who comitted suicide
* **\<population>**: of type \<int\>, the number of inhabitants in each country belonging to the age range and sex indicated
* **\<suicide_per_100k>**: of type \<int\>, the number of people who comitted suicide pero 100000 inhabitants 
* **\<gdp_for_year>**: of type \<float\>, gdp of the country in that year in millions of dolars
* **\<gdp_per_capita>**: of type \<int\>, gdp of the country per capita that year in dolars
* **\<generation>**: of type \<str\>, in what generation the people who comitted suicide belonged to (eg Generation X)


## Implemented types

To work with the data in the dataset the following tupple was made:

Data = namedtuple('data','country, year, sex, age_range, suicide_n, population, suicide_per_100k, gdp_for_year, gdp_per_capita, generation')

with the following types:

data(str, datetime.date, boolean, str, int, int, int, float, int, str)

## Implemented Functions
The following functions were implemented in the project:

### \<Module manga\>

* **<read_files>**: Reads the file and changes the format of the str to the correct one for the project.
* **<list_filter_by_country>**: Given the dataset and a parameter country, filters the dataset for only the countries indicated by the parameter country, giving back said list of tupples.
* **<total_num_countries>**: Given the dataset, gives back the number of countries used in the dataset.
* **<tupple_highest_suicide_rate>**: Given the dataset, gives back the tupple with the data of the highest suicide rate per 100k inhabitants.
* **<list_highest_gdp_per_capita>**: Given the dataset and a parameter, gives back the first n elements of a list of tupples with the country, year and the gdp per capita ordered by the gdp per capita.
* **<dicc_generation_in_each_year>**: Given the dataset, gives back a dictionary where the keys are the years and the values are the generation types in each year.
* **<dicc_sum_suicides_per_country>**: Given the dataset, gives back a dictionary where the keys are the countries and the values is the sum of all the suicide numbers.
* **<max_suicides_in_country>**: Given the dataset, gives back the country with the most suicides.
* **<list_suicides_per_year>**: (This is an auxiliary function) Given the dataset, gives back a list of tupples with the year and the number of suicides that year.
* **<list_suicides_per_year_Austria>**:(This is an auxiliary function) Given the dataset, gives back a list of tupples with the year and the number of suicides that year in Austria.
* **<dicc_percentage_suicides_in_Austria>**: Given the dataset, gives back a dictionary where the keys are the years and the values are the percentage of suicides in Austria of the total suicides per year.
* **<list_suicide_increment>**: Given the dataset, gives back a list with the increment (positive or negative) in the number of suicides per year.
* **<num_years>**: (This is an auxiliary function) Given the dataset, gives a list of the years.
* **<dicc_suicides_per_year>**: (This is an auxiliary function) Given the dataset, gives back the dicitionary where the key is the year and the value is the number of suicides.
* **<plt_show_suicides_per_year>**: Given the dataset, shows a graph with the x axis being the years and the y axis being the number of suicides in that year.


### \<Module manga_test\>

* **<test_read_files>**: Testing read_files
* **<test_list_filter_by_country>**: Testing list_filter_by_country
* **<test_total_num_countries>**: Testing total_num_countries
* **<test_tupple_highest_suicide_rate>**: Testing tupple_highest_suicide_rate
* **<test_list_highest_gdp_per_capita>**: Testing list_highest_gdp_per_capita
* **<test_dicc_generation_in_each_year>**: Testing dicc_generation_in_each_year
* **<test_dicc_sum_suicides_per_country>**: Testing dicc_sum_suicides_per_country
* **<test_max_suicides_in_country>**: Testing max_suicides_in_country
* **<test_dicc_percentage_suicides_in_Austria>**: Testing dicc_percentage_suicides_in_Austria
* **<test_list_suicide_increment>**: Testing list_suicide_increment
* **<test_plt_show_suicides_per_year>**: Showing plt_show_suicides_per_year

![graph](https://user-images.githubusercontent.com/93334287/147994301-a6fc4d47-6def-45f8-a4ae-ba54953027bc.png)

### \<Module suicide_parse\>

* **<parse_bool>**: Function to change into boolean
* **<parse_int>**: Function to change into int
* **<parse_date>**: Function to change into date("%Y")
* **<parse_float>**: Function to change into float and replace , with .

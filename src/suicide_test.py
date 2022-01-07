from suicide import *
from datetime import datetime

def test_read_files():
    print("These are the number of data read: ", len(data))
    print("These are the first 3 data: ", data[:3])
    print("These are the last 3 data: ", data[-3:])

def test_list_filter_by_country():
    country = "Albania"
    print("The dataset filtered by the country Albania: ", list_filter_by_country(data,country)[:3])

def test_total_num_countries():
    print("The total number of countries in the dataset: ", total_num_countries(data))

def test_tupple_highest_suicide_rate():
    print("This is the following information on the highest_suicidal_rate: ")
    print(tupple_highest_suicide_rate(data))

def test_list_highest_gdp_per_capita():
    n=3
    print("The 3 year and countriy with the highest gpd per capita is: ")
    print(list_highest_gdp_per_capita(data,n))

def test_dicc_generation_in_each_year():
    print("The generations corresponding to each year are the following: ")
    print(dicc_generation_in_each_year(data))

def test_dicc_sum_suicides_per_country():
    print("The suicides committed in each country: ")
    print(dicc_sum_suicides_per_country(data))

def test_max_suicides_in_country():
    print("The country with the most suicides is: ", max_suicides_in_country(data))

def test_dicc_percentage_suicides_in_Austria():
    print("These are the percentages of how many people committed suicide in Austria per year: ")
    print(dicc_percentage_suicides_in_Austria(data))

def test_list_suicide_increment():
    print("The increment of suicides each year: ")
    print(list_suicide_increment(data))


if __name__ == '__main__':
    data = read_files('data\suicide_data.csv')
    test_read_files()
    test_list_filter_by_country()
    test_total_num_countries()
    test_tupple_highest_suicide_rate()
    test_list_highest_gdp_per_capita()
    test_dicc_generation_in_each_year()
    test_dicc_sum_suicides_per_country()
    test_max_suicides_in_country()
    test_dicc_percentage_suicides_in_Austria()
    test_list_suicide_increment()
    plt_show_suicides_per_year(data)


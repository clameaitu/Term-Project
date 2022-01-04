import csv
from collections import namedtuple
from datetime import date
from suicide_parse import *
from matplotlib import pyplot as plt

Data = namedtuple('data','country, year, sex, age_range, suicide_n, population, suicide_per_100k, gdp_for_year, gdp_per_capita, generation')


def read_files(file):
    '''
    Reads the file and changes the format of the str to the correct one for the project.
    '''
    register = []
    with open(file, 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f, delimiter = ';') #The data is delimited by ;
        next(reader) #The first line are the titles
        for country, year, sex, age_range, suicide_n, population, suicide_per_100k, gdp_for_year, gdp_per_capita, generation in reader: 
            
            year = parse_date(year)
            suicide_n= parse_int(suicide_n)
            population= parse_int(population) 
            suicide_per_100k = parse_int(suicide_per_100k)
            sex = parse_bool(sex) #True is female, False is male
            gdp_for_year = parse_float(gdp_for_year)
            gdp_per_capita = parse_int(gdp_per_capita)
            
            r = Data(country, year, sex, age_range, suicide_n, population, suicide_per_100k, gdp_for_year, gdp_per_capita, generation)
            register.append(r)
    return register 

#1
def list_filter_by_country(data,country):
    '''
    Given the dataset and a parameter country, filters the dataset for only the countries 
    indicated by the parameter country, giving back said list of tupples.
    '''
    return [t for t in data if country in t.country]

#3
def total_num_countries(data):
    '''
    Given the dataset, gives back the number of countries used in the dataset.
    '''
    sets= set(r.country for r in data)
    lists= list(sets)
    return len(lists)

#4
def tupple_highest_suicide_rate(data):
    '''
    Given the dataset, gives back the tupple with the data of the highest suicide rate per 
    100k inhabitants.
    '''
    data.sort(key=lambda x:x[6], reverse=True)
    return data[0]

#6
def list_highest_gdp_per_capita(data,n):
    '''
    Given the dataset and a parameter, gives back the first n elements of a list of tupples
    with the country, year and the gdp per capita ordered by the gdp per capita.
    '''
    gdp_set=set((r.country, r.year.year, r.gdp_per_capita) for r in data)
    gdp_list= list(gdp_set)
    gdp_list.sort(key=lambda x:x[2], reverse=True)
    return gdp_list[:n]

#7
def dicc_generation_in_each_year(data):
    '''
    Given the dataset, gives back a dictionary where the keys are the years and the values
    are the generation types in each year.
    '''
    gen = dict()
    for r in data:
        key = r.year.year
        if key in gen:
            gen[key].add(r.generation)
        else:
            gen[key] = {r.generation}
    return gen

#9
def dicc_sum_suicides_per_country(data):
    '''
    Given the dataset, gives back a dictionary where the keys are the countries and the 
    values is the sum of all the suicide numbers.
    '''
    dicc = dict()
    for r in data:
        key = r.country
        if key in dicc:
            dicc[key]+= r.suicide_n
        else:
            dicc[key] = r.suicide_n
    return dicc

#10
def max_suicides_in_country(data):
    '''
    Given the dataset, gives back the country with the most suicides.
    '''
    dicc=dicc_sum_suicides_per_country(data)
    return max(dicc.items(),key=lambda p:p[1]) [0]


#aux_function
def list_suicides_per_year(data):
    '''
    (This is an auxiliary function) Given the dataset, gives back a 
    list of tupples with the year and the number of suicides that year.
    '''
    dicc = dict()
    for r in data:
        if r.year.year in dicc:
            dicc[r.year.year] += r.suicide_n
        else:
            dicc[r.year.year] = r.suicide_n
    return sorted(dicc.items(), key=lambda x: x[1], reverse=True)

#aux_function
def list_suicides_per_year_Austria(data):
    '''
    (This is an auxiliary function) Given the dataset, gives back a 
    list of tupples with the year and the number of suicides that year 
    in Austria.
    '''
    dicc = dict()
    data_Austria = list_filter_by_country(data,"Austria")
    for r in data_Austria:
        if r.year.year in dicc:
            dicc[r.year.year] += r.suicide_n
        else:
            dicc[r.year.year] = r.suicide_n
    return sorted(dicc.items(), key=lambda x: x[1], reverse=True)


#13
def dicc_percentage_suicides_in_Austria(data):
    '''
    Given the dataset, gives back a dictionary where the keys are the 
    years and the values are the percentage of suicides in Austria of 
    the total suicides per year.
    '''
    dicc = dict()
    global_suicides = dict(list_suicides_per_year(data))
    austria_suicides = dict(list_suicides_per_year_Austria(data))
    for year, value in global_suicides.items():
        percentage = 100 * austria_suicides[year] / value
        if year in dicc:
            dicc[year] += percentage
        else:
            dicc[year] = percentage
    return dict(sorted(dicc.items()))

#15
def list_suicide_increment(data):
    '''
    Given the dataset, gives back a list with the increment (positive 
    or negative) in the number of suicides per year.
    '''
    suicides_globally_now = sorted(list_suicides_per_year(data))
    suicides_globally_following = sorted(list_suicides_per_year(data))[1:]
    dicc = []
    for current_year, next_year in zip(suicides_globally_now, suicides_globally_following):
        percentage = (next_year[1] - current_year[1]) / current_year[1] * 100  # We take away 1 since we're trying to figure out the increment
        dicc.append(percentage)
    return dicc

#aux_function
def list_num_years(data):
    '''
    (This is an auxiliary function) Given the dataset, gives a list of 
    the years.
    '''
    sets= set(r.year.year for r in data)
    lists= list(sets)
    return lists

def dicc_suicides_per_year(data):
    '''
    (This is an auxiliary function) Given the dataset, gives back the 
    dicitionary where the key is the year and the value is the number of suicides.
    '''
    dicc = dict()
    data.sort(key=lambda x:x[1], reverse=False)
    for r in data:
        if r.year.year in dicc:
            dicc[r.year.year] += r.suicide_n
        else:
            dicc[r.year.year] = r.suicide_n
    return dicc


#16
def plt_show_suicides_per_year(data):
    '''
    Given the dataset, shows a graph with the x axis being the years and the y axis 
    being the number of suicides in that year.
    '''
    years = list_num_years(data)
    num_suicides = list(dicc_suicides_per_year(data).values())
    plt.bar(years, num_suicides)
    plt.xlabel('Years')
    plt.ylabel('Number of people who committed suicide')
    plt.title('The total number of suicides every year')
    plt.xticks(years, years, fontsize=7)
    plt.show()


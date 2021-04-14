#!/usr/bin/env python
# coding: utf-8

# # Project Final Submission Template

# ### Step 1a: Planning 
# #### Identify the information in the file your program will read
# 
# The file contains indormation about characters in Marvel cosmics universe. For every characters, it contains:
# - The unique identifier for that characters page within the wikia
# - The name of the character
# - The identity status of the character (Secret Identity, Public identity, [on marvel only: No Dual Identity])
# - If the character is Good, Bad or Neutral
# - Eye color of the character 
# - Hair color of the character 
# - Sex of the character (e.g. Male, Female, etc.)
# - If the character is a gender or sexual minority (e.g. Homosexual characters, bisexual characters)
# - If the character is alive or deceased
# - The number of appareances of the character in comic books (as of Sep. 2, 2014. Number will become increasingly out of date as time goes on.) 
# - The year of the character's first appearance in a comic book, if available

# ### Step 1b: Planning 
# #### Write a description of what your program will produce
# 
# 1. For a specific year range, the percentage of the number of new public identification characters to the total number new character. **Pie chart**
# 2. The number of character with each of the hair color. **bar chart**
# 3. The percentage  living/deceased characters in different aligns (over all/bad/neutral/good). **Pie chart**
# 
# **This program will find the percentage of different alive in different align (3)**

# ### Step 1c: Planning 
# #### Write or draw examples of what your program will produce
# 
# - expect(main('marvel-wikia-data.csv', None), None)
# - expect(main('marvel-wikia-data.csv', Align.bad), None)
# - expect(main('marvel-wikia-data.csv', Align.neutral), None)
# - expect(main('marvel-wikia-data.csv', Align.good), None)
# 
# the four test are shown below in order from left to right than from upper to bottom in the picture provided:
# ![%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20190704112216.jpg](attachment:%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20190704112216.jpg)

# ##### Step 2a: Building
# #### Design data definitions
# Double click this cell to edit.
# 
# I choose to represent the data of Align in the file with enumeration as there are 3 type of align characters stand for one of them. I choose to represent Alive data by using bool as the only one of two state of whether alive or not. I use compound to represent the data of one of the marvel characeter data in one line which contain one align data and one alive data for each Marvel data. A list of Marvel is also created to make the csv into a list.
# 
# For my program I plan to analyse the percentage of living or death for each type of align, these two are two of the imformation I'm going to work with. The character with (one of) these data missing will not be included in analyse. 

# In[15]:


from cs103 import *
from typing import NamedTuple, List, Optional
from enum import Enum
import csv

##################
# Data Definitions

Align = Enum('Align', ['bad', 'neutral', 'good'])
# interp. a align data of a marvel character is either bad, neutral, or good. 
# examples are redundent for Enum

@typecheck
def fn_for_align(a: Align) -> ...:
    # templete based on One of rule (3 cases), atomic distinct (3 times)
    if (a == Align.bad):
        return ...
    elif (a == Align.neutral):
        return ...
    elif (a == Align.good):
        return ...
    
DataRange = Optional[Align]
# interp.  a data range of the analyse (the align of a character), None means the overall range
OVERALL = None
BAD = Align.bad
NEUTRAL = Align.neutral
GOOD = Align.good

@typecheck
#templete based on one of(2 cases), atomic distinct and atomic non-sidtinct, reference rule
def fn_for_data_range(dr: DataRange) -> ...:
    if dr == None:
        return ...
    else:
        return...(fn_for_align(dr))

    
Alive = bool
# interp. a alive data of a marvel character is either True (living) or False (deceased). 
LIVING = True
DECEASED = False

@typecheck
def fn_for_alive(a: Alive) -> ...:
    # templete based on atomic non-s
    return ...(a)
    

Marvel = NamedTuple("Marvel", [("align", Align), 
                               ("alive", Alive)])
#interp. a marvel character data contain its align data (either good, neutral, or bad), and its alive data (either living or deceased)
PETER = Marvel(Align.good, True)
STEVEN = Marvel(Align.good, True)
LOGAN = Marvel(Align.neutral, True)
TONY = Marvel(Align.good, True)
LOKI = Marvel(Align.neutral, True)
TIMOTHY = Marvel(Align.good, False)
CARNAGE = Marvel(Align.bad, True)
VENUS = Marvel(Align.good, True)
MOCK = Marvel(Align.bad, True)

@typecheck
def fn_for_marvel(m: Marvel) -> ...:
    #templete based on componund rule, and reference (two times)
    return ...(fn_for_align(m.align), 
               fn_for_alive(m.alive))



# List[Marvel]
# interp. a list of Marvel

LOM0 = []
LOM1 = [PETER, STEVEN, LOGAN, TONY]
LOM2 = [LOKI, TIMOTHY, CARNAGE, VENUS, MOCK]

@typecheck
def fn_for_lom(lom: List[Marvel]) -> ...:
    # templete based on list rule and reference rule
    # description of the accumulator
    acc = ...      # type: ...
    for m in lom: 
        acc = ...(fn_for_marvel(m), acc)
    return ...(acc)


# ### Step 2b and 2c: Building
# #### Design a function to read the information and store it as data in your program
# #### Design functions to analyze the data
# 

# In[16]:


###########
# main and read Functions

def main(filename: str, data_range: DataRange) -> None: 
    """
    Reads the file from given filename, analyzes the data,
    returns the pie chart of the corresponding given data range
    """
    # templata from HtDAP, based on composition
    return show_pie_chart(read(filename), data_range)

@typecheck
def read(filename: str) -> List[Marvel]:
    """    
    reads information from the specified file and returns a list of Marvel data, 
    only consider the data with valid align data and slive data
    """
    #return []  #stub
    # Template from HtDAP
    # lom contains the result so far
    lom = [] # type: List[Marvel]

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader) # skip header line

        for row in reader:
            if (not row[3] == "") and (not row[8]== ""):
                m = Marvel(convert_align(row[3]), convert_alive(row[8]))
                lom.append(m)
    
    return lom

@typecheck
def convert_align(s: str) -> Align:
    """
    return a Align data of from converting the given str 
    """
    # return Align.bad  # stub
    # templete based on atomic non-distinct
    if (s == "Bad Characters"):
        return Align.bad
    elif (s == "Neutral Characters"):
        return Align.neutral
    elif (s == "Good Characters"):
        return Align.good
    
@typecheck
def convert_alive(s: str) -> Alive:
    """
    return a Alive data from converting the given str
    """
    # return True   # stub
    # template based on atomic non-distinct
    if (s == "Living Characters"):
        return True
    elif (s == "Deceased Characters"):
        return False

# Begin testing
start_testing()

#tests and examples are shown at the very end of this file
# Examples and tests for convert_align
expect(convert_align("Bad Characters"), Align.bad)
expect(convert_align("Neutral Characters"), Align.neutral)
expect(convert_align("Good Characters"), Align.good)
# Examples and tests for convert_alive
expect(convert_alive("Living Characters"), True)
expect(convert_alive("Deceased Characters"), False)

# show testing summary
summary()


# In[17]:


###########
# reusable Functions along the program
@typecheck
def calculate(partial: int, whole: int) -> float:   # in range of [0, 100]
    """
    return the the percentage of the patial to the whole, partial <= whole, both given int are positive
    """
    # return 2.2  # stub
    # templete based on the atomic non-distinct
    assert (partial <= whole) and (partial >= 0) and (whole >= 0)
    if (whole == 0):
        return 0
    else:
        return ((partial/whole) * 100)

@typecheck
def check_align(m: Marvel, demand: Align) -> bool:
    """
    return True if the given demand appear in m.align data
    """
    # return True  # stub
    # template from atomic non-distinct
    return (m.align == demand) 

@typecheck
def check_alive(m: Marvel, demand: Alive) -> bool:
    """
    return True if the given demand appear in m.alive data
    """
    # return True  # stub
    # template from atomic non-distinct
    return (m.alive == demand)


@typecheck
def filter_align(lom: List[Marvel], demand: Align) -> List[Marvel]:
    """
    return a list of marvel character from the given list who has meet the demand
    """
    # return []  # stub
    # templete from List[Marvel] and reference rule
    # acc contain the required marvel character been seen so far
    acc = []      # type: List[Marvel] 
    for m in lom: 
        if check_align(m, demand):
            acc.append(m)
    return acc

@typecheck
def filter_alive(lom: List[Marvel], demand: Alive) -> List[Marvel]:
    """
    return a list of marvel character from the given list who has meet the demand
    """
    # return []  # stub
    # templete from List[Marvel] and reference rule
    # acc contain the required marvel character been seen so far
    acc = []      # type: List[Marvel] 
    for m in lom: 
        if check_alive(m, demand):
            acc.append(m)
    return acc

# Begin testing
start_testing()

# Examples and tests for calculate
expect(calculate(3, 4), 75.0)
expect(calculate(19, 21), 90.47619047619048)
# Examples and tests for check_align
expect(check_align(MOCK, Align.bad), True)
expect(check_align(LOGAN, Align.bad), False)
expect(check_align(MOCK, Align.neutral), False)
expect(check_align(LOGAN, Align.neutral), True)
expect(check_align(LOGAN, Align.good), False)
expect(check_align(TONY, Align.good), True)
# Examples and tests for check_alive
expect(check_alive(PETER, True), True)
expect(check_alive(TIMOTHY, True), False)
expect(check_alive(PETER, False), False)
expect(check_alive(TIMOTHY, False), True)
# Examples and tests for filter_align
expect(filter_align(LOM0, Align.bad), [])
expect(filter_align(LOM1, Align.bad), [])
expect(filter_align(LOM1, Align.good), [PETER, STEVEN, TONY])
expect(filter_align(LOM2, Align.neutral), [LOKI])
# Examples and tests for filter_alive
expect(filter_alive(LOM0, True), [])
expect(filter_alive(LOM2, True), [LOKI, CARNAGE, VENUS, MOCK])
expect(filter_alive(LOM1, False), [])

# show testing summary
summary()


# In[18]:


###########
#  the separate functions for each part of a chart
@typecheck
def living(lom: List[Marvel]) -> float:   #in range [0, 100]
    """
    return the percentage of all the living character in all the character for the given list
    """
    # return 9.9  #stub
    # template based on composition rule
    # 1. get the filtered lists(living),
    # 2. calculate the percentage
    return calculate(len(filter_alive(lom, True)), len(lom))

@typecheck
def deceased(lom: List[Marvel]) -> float:   #in range [0, 100]
    """
    return the percentage of all the deceased character in all the character for the given list
    """
    # return 9.9  #stub
    # template based on composition rule
    # 1. get the filtered lists(deceased),
    # 2. get the len of the filtered lists
    # 3. calculate the percentage
    return calculate(len(filter_alive(lom, False)), len(lom))

@typecheck
def bad_living(lom: List[Marvel]) -> float:   #in range [0, 100]
    """
    return the percentage of all the bad living character in all the bad character for the given list
    """
    # return 9.9  #stub
    # template based on composition rule
    # 1. get the filtered lists(bad and living, bad)
    # 2. get the len of the filtered lists
    # 3. calculate the percentage
    return calculate(len(filter_alive(filter_align(lom, Align.bad), True)), len(filter_align(lom, Align.bad)))

def bad_deceased(lom: List[Marvel]) -> float:   #in range [0, 100]
    """
    return the percentage of all the bad deceased character in all the bad character for the given list
    """
    # return 9.9  #stub
    # template based on composition rule
    # 1. get the filtered lists(bad and deceased, bad)
    # 2. get the len of the filtered lists
    # 3. calculate the percentage
    return calculate(len(filter_alive(filter_align(lom, Align.bad), False)), len(filter_align(lom, Align.bad)))

def neutral_living(lom: List[Marvel]) -> float:   #in range [0, 100]
    """
    return the percentage of all the neutral living character in all the neutral character for the given list
    """
    # return 9.9  #stub
    # template based on composition rule
    # 1. get the filtered lists(neutral and living, neutral)
    # 2. get the len of the filtered lists
    # 3. calculate the percentage
    return calculate(len(filter_alive(filter_align(lom, Align.neutral), True)), len(filter_align(lom, Align.neutral)))

def neutral_deceased(lom: List[Marvel]) -> float:   #in range [0, 100]
    """
    return the percentage of all the neutral deceased character in all the neutral character for the given list
    """
    # return 9.9  #stub
    # template based on composition rule
    # 1. get the filtered lists(neutral and deceased, neutral)
    # 2. get the len of the filtered lists
    # 3. calculate the percentage
    return calculate(len(filter_alive(filter_align(lom, Align.neutral), False)), len(filter_align(lom, Align.neutral)))

def good_living(lom: List[Marvel]) -> float:   #in range [0, 100]
    """
    return the percentage of all the good living character in all the good character for the given list
    """
    # return 9.9  #stub
    # template based on composition rule
    # 1. get the filtered lists(good and living, good)
    # 2. get the len of the filtered lists
    # 3. calculate the percentage
    return calculate(len(filter_alive(filter_align(lom, Align.good), True)), len(filter_align(lom, Align.good)))


def good_deceased(lom: List[Marvel]) -> float:   #in range [0, 100]
    """
    return the percentage of all the good deceased character in all the good character for the given list
    """
    # return 9.9  #stub
    # template based on composition rule
    # 1. get the filtered lists(good and deceased, good)
    # 2. get the len of the filtered lists
    # 3. calculate the percentage
    return calculate(len(filter_alive(filter_align(lom, Align.good), False)), len(filter_align(lom, Align.good)))


# Begin testing
start_testing()

# Examples and tests for living
expect(living(LOM0), 0)
expect(living(LOM1), 100)
expect(living(LOM2), 80)
# Examples and tests for deceased
expect(deceased(LOM0), 0)
expect(deceased(LOM1), 0)
expect(deceased(LOM2), 20)

# Examples and tests for bad_living
expect(bad_living(LOM0), 0)
expect(bad_living(LOM1), 0)
expect(bad_living(LOM2), 100)
# Examples and tests for bad_deceased
expect(bad_deceased(LOM0), 0)
expect(bad_deceased(LOM1), 0)
expect(bad_deceased(LOM2), 0)
# Examples and tests for neutral_living
expect(neutral_living(LOM0), 0)
expect(neutral_living(LOM1), 100)
expect(neutral_living(LOM2), 100)
# Examples and tests for neutral_deceased
expect(neutral_deceased(LOM0), 0)
expect(neutral_deceased(LOM1), 0)
expect(neutral_deceased(LOM2), 0)
# Examples and tests for good_living
expect(good_living(LOM0), 0)
expect(good_living(LOM1), 100)
expect(good_living(LOM2), 50)
# Examples and tests for good_deceased
expect(good_deceased(LOM0), 0)
expect(good_deceased(LOM1), 0)
expect(good_deceased(LOM2), 50.0)

# show testing summary
summary()


# In[19]:


############
# visualization
import matplotlib.pyplot as plt
from cs103 import *
from typing import List

@typecheck
def check_range(lom: List[Marvel], data_range: DataRange) -> List[float]:
    """
    return a list of float according to the given data range
    """
    # return []  # stub
    # template from DataRange
    if (data_range == None):
        return [living(lom), deceased(lom)]
    elif (data_range == Align.bad):
        return [bad_living(lom), bad_deceased(lom)]
    elif (data_range == Align.neutral):
        return [neutral_living(lom), neutral_deceased(lom)]
    elif (data_range == Align.good):
        return [good_living(lom), good_deceased(lom)] 

@typecheck
def title(data_range: DataRange) -> str:
    """
    return a string to represent the title of the pie chart based on the given data range
    """
    # return ""  # stub
    # template based on DataRange
    if (data_range == None):
        return "Overall Alive Percentage of Marvel Characters"
    elif (data_range == Align.bad):
        return "Bad Marvel Character Alive Percentage"
    elif (data_range == Align.neutral):
        return "Neutral Marvel Character Alive Percentage"
    elif (data_range == Align.good):
        return "Good Marvel Character Alive Percentage"
    
    
@typecheck
def show_pie_chart(lom: List[Marvel], data_range: DataRange) -> None:
    """
    show a pie chart of the given data range with the given corresponding fractions of data from list of marvel.
    
    fractions must each be in the range [0,100] and must sum to 100
    (and so must have at least one element).
    
    returns None
    """
    #return None  #stub
    # Template based on visualization and composition rule
    # 1. get fractures based on different data range 
    # 2. draw the pie chart
    
    # specify the percentages, then whether to explode each piece, then the labels, then the formatting
    # for the percentages on the chart, and finally whether you want a shadow or not. If you
    # remove autopct, the percentage will not show on each piece of the pie
    
    plt.pie(check_range(lom, data_range), explode=[0, 0], labels=["Living", "Deceased"], autopct='%.0f%%', shadow=False)
    plt.title(title(data_range))

    plt.show()
    
    return None

# Begin testing
start_testing()

# examples and tests for check_range
expect(check_range([], None), [0, 0])
expect(check_range(LOM1, None), [100.0, 0])
expect(check_range(LOM2, Align.bad), [100.0, 0])
expect(check_range(LOM2, Align.neutral), [100.0, 0])
expect(check_range(LOM2, Align.good), [50.0, 50.0])

# examples and tests for title
expect(title(None), "Overall Alive Percentage of Marvel Characters")
expect(title(Align.bad), "Bad Marvel Character Alive Percentage")
expect(title(Align.neutral), "Neutral Marvel Character Alive Percentage")
expect(title(Align.good), "Good Marvel Character Alive Percentage")

# examples and tests for show_pie_chart
# Should display a pie chart with title of "Overall Alive Percentage of Marvel Characters", 
#                               0% labelled "Living", 0% labelled "Deceased"
expect(show_pie_chart([], None), None)
# Should display a pie chart with title of ""Bad Marvel Character Alive Percentage", 
#                               100% labelled "Living", 0% labelled "Deceased"
expect(show_pie_chart(LOM2, Align.bad), None)
# Should display a pie chart with title of "Neutral Marvel Character Alive Percentage", 
#                               100% labelled "Living", 0% labelled "Deceased"
expect(show_pie_chart(LOM1, Align.neutral), None)
# Should display a pie chart with title of ""Good Marvel Character Alive Percentage", 
#                               50% labelled "Living", 50% labelled "Deceased"
expect(show_pie_chart(LOM2, Align.good), None)

# 
# show testing summary
summary()


# ![%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20190704213543.jpg](attachment:%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20190704213543.jpg)

# In[20]:


##########
# examples and tests for main and read

# Begin testing
start_testing()

# Examples and tests for main

# Should display a pie chart with title of "Neutral Marvel Character Alive Percentage", 
#                               100% labelled "Living", 0% labelled "Deceased"
expect(main('marvel-wikia-data-test1.csv', None), None)
# Should look roughly like the three sketchs except the first one in the markdown cell above.
expect(main('marvel-wikia-data-test2.csv', Align.bad), None)
expect(main('marvel-wikia-data-test1.csv', Align.neutral), None)
expect(main('marvel-wikia-data-test2.csv', Align.good), None)
# Examples and tests for read
expect(read('marvel-wikia-data-test1.csv'), LOM1)
expect(read('marvel-wikia-data-test2.csv'), LOM2)

# show testing summary
summary()


# In[21]:


###########
# Result of the main dataset
main('marvel-wikia-data.csv', None)
main('marvel-wikia-data.csv', Align.bad)
main('marvel-wikia-data.csv', Align.neutral)
main('marvel-wikia-data.csv', Align.good)


# In[ ]:





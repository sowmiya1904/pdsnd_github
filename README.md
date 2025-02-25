### Date created
This project was created on 09/19/22

### Project Title
Data Exploration on U.S. Bikeshare data

### Description
This project focuses on Pandas module in python to explore bikeshare data for three major cities-- Chicago, New York City and Washington. The project computes statistical results and provides an interactive environment for the users to analyze the data. 

### Software Requirements
Python 3, Libraries- Numpy and Pandas
Text Editor like Sublime or Atom
A terminal application like Git Bash

### Files used
chicago.csv, new_york_city.csv, washington.csv -- Dataset containing information for the 3 cities which is used to compute the statistics.

### Data in the above files
All three of the data files contain the same core six (6) columns:

->Start Time (e.g., 2017-01-01 00:07:57)

->End Time (e.g., 2017-01-01 00:20:53)

->Trip Duration (in seconds - e.g., 776)

->Start Station (e.g., Broadway & Barry Ave)

->End Station (e.g., Sedgwick St & North Ave)

->User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
->Gender

->Birth Year

### Statistics computed
#1 Popular times of travel (i.e., occurs most often in the start time)

->most common month

->most common day of week

->most common hour of day

#2 Popular stations and trip

->most common start station

->most common end station

->most common trip from start to end (i.e., most frequent combination of start station and end station)

#3 Trip duration

->total travel time

->average travel time

#4 User info

->counts of each user type

->counts of each gender (only available for NYC and Chicago)

->earliest, most recent, most common year of birth (only available for NYC and Chicago)

### References
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.all.html
https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.weekday.html


import time
import numpy as np 
import pandas as pd 

CITY_DATA = {
	       'chicago' : 'chicago.csv',
	       'new york' : 'new_york_city.csv',
	       'washington' : 'washington.csv'
         }

months = ['january','february','march','april','may','june']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
	"""
	Function to specify city, month and day to analyze

	Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
	print('Hello! Let\'s explore some US bikeshare data!')
	
	while True:
		try:
			#User Input for City
			city = input('Enter the name of the city for which you would like to see the data for? Chicago, New York or Washington\n').lower()
			#If user entered invalid city it raises an exception
			if (city.strip() != 'chicago') and (city.strip()!='new york') and (city.strip()!='washington'):
				raise NameError
			else:
				break
		except NameError:
			print('\nUnfortunately, Data is not provided for the entered city. Please try again...\n')
			continue

	
	while True:
		try:
			#User input to filter the data based on month or day or both 
			choice = input('\nLet us know if you would like to filter the data by month, day, both or None\n').lower()

			if choice == 'month':
				while True:
					try:
						month = input('\nWhich month- January, February, March, April, May, June?\n')
						if month.lower().strip() not in months:
							raise NameError
						day = 'all'
					except NameError:
						print('\nOops..!! Sorry We could not recognize what data you are referring to. Please try again...\n')
						continue
					else: 
						break
			elif choice == 'day':
				while True:
					try:
						day = input('\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday?\n')
						if day.lower().strip() not in days:
							raise NameError
						month = 'all'
					except NameError:
						print('\nOops..!! Sorry We could not recognize what data you are referring to. Please try again...\n')
						continue
					else:
						break
			elif choice == 'both':
				while True:
					try:
						month = input('\nWhich month- January, February, March, April, May, June?\n')
						if month.lower().strip() not in months:
							raise NameError
						else:
							break
					except NameError:
						print('\nOops..!! Sorry We could not recognize what data you are referring to. Please try again...\n')
						continue
				while True:
					try:
						day = input('\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday?\n')
						if day.lower().strip() not in days:
							raise NameError
					except NameError:
						print('\nOops..!! Sorry We could not recognize what data you are referring to. Please try again...\n')
						continue
					else:
						break
			elif choice == 'none':
				month = 'all'
				day = 'all'
			else:
				raise NameError
		except NameError:
			print('\nOops..!! Sorry We could not recognize what data you are referring to. Please try again...\n')
			continue
		else:
			break
	
	print("\nPlease wait while the data is loading...\n")
	print('-'*40)
	return city.strip(), month.lower().strip(), day.lower().strip()


def load_data(city, month, day):
	"""
	Loads data for the specified city and returns DataFrame filtered based on month and day""" 
	print("\nData is getting ready...\n")

	df = pd.read_csv(CITY_DATA[city])
	df['Start Time'] = pd.to_datetime(df['Start Time'])
	df['month'] = df['Start Time'].dt.month
	df['day_of_week'] = df['Start Time'].dt.weekday

	if month != 'all':
		months = ['january','february','march','april','may','june']
		month = months.index(month) + 1
		df = df[df['month'] == month]

	if day != 'all':
		days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
		day = days.index(day) 
		df = df[df['day_of_week'] == day]

	return df

def time_stats(df):
	"""Displays statistics on the most frequent times of travel."""

	print('\nCalculating The Most Frequent Times of Travel...\n')
	start_time = time.time()

	months = ['January','February','March','April','May','June']
	days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

	if ((df['month'].iat[0] == df['month']).all()) and ((df['day_of_week'].iat[0] == df['day_of_week']).all()):
		print("\nFilter Type : Both")

	elif (df['month'].iat[0] == df['month']).all():	 
		print("\nFilter Type Month :",months[df['month'].iat[0]-1])
		popular_day = df['day_of_week'].mode()[0]
		print("\nMost common day:",days[popular_day])

	elif ((df['day_of_week'].iat[0] == df['day_of_week']).all()):
		print("\nFilter Type Day:", days[df['day_of_week'].iat[0]])
		popular_month = df['month'].mode()[0]
		print("\nMost common month:",months[popular_month-1])
	else:
		print("Filter Type : None")
		popular_month = df['month'].mode()[0]
		print("\nMost common month:",months[popular_month-1])
		popular_day = df['day_of_week'].mode()[0]
		print("\nMost common day:",days[popular_day])
		
	df['Start Time'] = pd.to_datetime(df['Start Time'])
	df['hour'] = df['Start Time'].dt.hour
	popular_hour = df['hour'].mode()[0]
	print("\nMost Frequent Start Hour:",popular_hour)

	print("\nThat took %s seconds." % (time.time() - start_time))
	print('-'*40)

def station_stats(df):
	"""Displays statistics on the most popular stations and trip."""

	print('\nCalculating The Most Popular Stations and Trip...\n')
	start_time = time.time()

	popular_start_station = df['Start Station'].mode()[0]
	print("Most Common Start Station : ",popular_start_station)

	popular_end_station = df['End Station'].mode()[0]
	print("\nMost Common End Station :",popular_end_station)

	df['Trip'] = df['Start Station'] + '-' + df['End Station']
	popular_trip = df['Trip'].mode()[0]
	print("\nPopular Trip : FROM ",popular_trip.split('-')[0],"TO",popular_trip.split('-')[1])

	print("\nThat took %s seconds." % (time.time() - start_time))
	print('-'*40)

def trip_duration_stats(df):
	"""Displays statistics on the total and average trip duration."""

	print('\nCalculating Trip Duration...\n')
	start_time = time.time()

	total_travel_time = df['Trip Duration'].sum()
	count = df['Trip Duration'].count()
	avg_travel_time = df['Trip Duration'].mean()
	print("Total Duration in seconds: ",total_travel_time,"\tCount :",count,"\tAverage Duration : ",avg_travel_time)

	print("\nThat took %s seconds." % (time.time() - start_time))
	print('-'*40)

def user_stats(df):

	"""Displays statistics on bikeshare users."""

	print('\nCalculating User Statistics...\n')
	start_time = time.time()

	user_types = df['User Type'].value_counts()
	print(user_types)

	print('\nCalculating Gender Statistics...\n')

	if 'Gender' in df.columns:
		gender_count = df['Gender'].value_counts()
		print(gender_count)
	else:
		print("No gender details to share from this data.")

	print('\nCalculating Birth Statistics...\n')

	if 'Birth Year' in df.columns:
		common_year = df['Birth Year'].mode()[0]
		print("Most common Year of Birth:",int(common_year))
		earliest_year = df['Birth Year'].min()
		print("\nEarliest Year of Birth:",int(earliest_year))
		recent_year = df['Birth Year'].max()
		print("\nRecent Year of Birth:",int(recent_year))
	else:
		print("No Birth details to share from this data.")

	print("\nThat took %s seconds." % (time.time() - start_time))
	print('-'*40)

def display_data(df):
	"""Displays raw data for the selected city."""
	x = 0
	while True:

		raw_data = input('\nWould you like to see the raw data for the entered city? Enter yes or no.\n')
		if raw_data.lower() == 'yes':
			print("Displaying the 5 rows of data!!!")
			x += 1
			print(df.iloc[(x-1)*5:x*5])
			continue
		else:
			break

def main():
	while True:

		city, month, day = get_filters()
		print(city, month, day)
		df = load_data(city, month, day)
		df.to_csv('city.csv')

		
		time_stats(df)
		station_stats(df)
		trip_duration_stats(df)
		user_stats(df)
		display_data(df)

		restart = input('\nWould you like to restart? Enter yes or no.\n')
		if restart.lower() != 'yes':	
			break
	

if __name__ == "__main__":
	main()
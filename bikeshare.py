import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        city = input('For which city would you like to see data?\nChicago, New York City, or Washington \n').lower()
        if city in CITY_DATA:
            break
        else: 
            print('That\'s not a valid entry. Please try again. \n')

    while True:
        month = input('For which month would you like to see data?\nEnter Jan, Feb, Mar, Apr, May, Jun or All. \n').lower()
        if month in months or month == 'all':
            break
        else:
            print('That\'s not a valid entry. Please try again. \n')

    while True:
        day = input('For which day of the week would you like to see data?\nEnter a day of the week or All. \n').lower()
        if day in days or day == 'all':
            break
        else:
            print('That\'s not a valid entry. Please try again. \n')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour
    if month != 'all':
        month = months.index(month)+1
        df = df[df['Month'] == month]
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    common_month = df['Month'].mode()[0]
    common_day = df['Day of Week'].mode()[0]
    common_hour = df['Hour'].mode()[0]

    # TO DO: display the most common month
    # TO DO: display the most common day of week
    # TO DO: display the most common start hour
    print('The most common month to rent in was {}.\nThe most common day to rent on was {}.\nThe most common hour to start at was {}.'.format(common_month, common_day, common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    # TO DO: display most commonly used start station
    # TO DO: display most commonly used end station
    # TO DO: display most frequent combination of start station and end station trip
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    common_start_st = df['Start Station'].mode()[0]
    common_end_st = df['End Station'].mode()[0]

    df['Start and End Stations'] = df['Start Station'] + ' --> ' + df['End Station']
    common_combo = df['Start and End Stations'].mode()[0]

    print('The most common station to start at was {}.\nThe most common station to end at was {}.\nThe most common trip was {}.'.format(common_start_st, common_end_st, common_combo))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    # TO DO: display total travel time
    # TO DO: display mean travel time
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_time = df['Trip Duration'].sum()
    mean_time = df['Trip Duration'].mean()

    print('The total time for all trips returned was {} hours.\nThe average length of each trip was {} minutes.'.format(round(total_time/3600, 2), round(mean_time/60, 2)))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    # TO DO: Display counts of user types
    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_type = df['User Type'].value_counts()
    gender_count = 'is not calculable from this city\'s data.'
    earliest_year = 'not calculable from this city\'s data'
    recent_year = earliest_year
    common_year = earliest_year

    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()

    if 'Birth Year' in df:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])

    print('The gender distibution of riders\n{}\n\nThe earliest birth year is {}.\nThe most recent birth year is {}.\nThe most common birth year is {}.'.format(gender_count, earliest_year, recent_year, common_year))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        count = 0
        lines = 0
        while True:

            view = input('You would like to view the 5 lines of the dataset? Enter yes or no.\n').lower()

            if view == 'yes':
                print(df.iloc[count:lines+5])
                lines += 5
                count += 5

            elif view == 'no':
                break
        restart = input('\nWould you like to restart? Enter Yes or No.\n')
        if restart.lower() != 'Yes':
            break


if __name__ == "__main__":
	main()

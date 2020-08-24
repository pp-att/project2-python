# bikeshare data ver.0.0.2

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ('january', 'february', 'march', 'april', 'may', 'june')

weekdays = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print()
    print('Hello! Let\'s explore some US bikeshare data!')
    print()
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get "priblbly" city
    while True:

        new_city = input("Choose a city (Chicago, New York City or Washington) : ")
        # debug
        #print("Choose a city (Chicago, New York City or Washington) : ")
        #new_city = 'new york city'

        new_city = new_city.lower()
        print()
        if new_city in CITY_DATA :
        #if new_city in CITY_DATA or new_city == 'quit':
            #print('Chosen city: ',new_city)
            city = new_city
            break
        else:
            print("wrong input")

    # get "priblblej" month
    while True:

        month = input("Choose the month (January, February, March, April, May, June) : ")
        # debug
        #print("Choose the month (January, February, March, April, May, June) : ")
        #month = 'January'

        month = month.lower()
        print()
        if month in months:
            #print('Chosen month: ',month)
            break
        else:
            print("wrong input")

    # get a day of the week "nebo co, dela mychra a hajzl ma na chodbe"
    while True:

        day = input("Choose the day of the week (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) : ")
        # debug
        #print("Choose the day of the week (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) : ")
        #day = 'Monday'

        day = day.lower()
        print()
        if day in weekdays:
            #print('Chosen month: ',day)
            break
        else:
            print("wrong input")

    # degub nebo info ?
    # for testing to not enter it all the time


    print()
    print('You selected : ',city, ',', month, ',', day)
    print()

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

    print("\nThe program is loading the data for the filters of your choice.")
    start_time = time.time()

    # debug "nebo co"
    #print()
    #print('You selected : ',city, ',', month, ',', day)
    #print()

    # filter the data according to the selected city filters
    if isinstance(city, list):
        df = pd.concat(map(lambda city: pd.read_csv(CITY_DATA[city]), city),
                       sort=True)
        try:
            df = df.reindex(columns=['Unnamed: 0', 'Start Time', 'End Time',
                                     'Trip Duration', 'Start Station',
                                     'End Station', 'User Type', 'Gender',
                                     'Birth Year'])
        except:
            pass
    else:
        df = pd.read_csv(CITY_DATA[city])

    # which columns from df to display
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.weekday_name
    df['Start Hour'] = df['Start Time'].dt.hour

    # filter the data according to month and weekday into two new DataFrames
    if isinstance(month, list):
        df = pd.concat(map(lambda month: df[df['Month'] ==
                           (months.index(month)+1)], month))
    else:
        df = df[df['Month'] == (months.index(month)+1)]

    if isinstance(day, list):
        df = pd.concat(map(lambda day: df[df['Weekday'] ==
                           (day.title())], day))
    else:
        df = df[df['Weekday'] == day.title()]

    print("\nThis took {} seconds.".format((time.time() - start_time)))

    print('-'*40)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print()
    print('#############################################')
    print('#        Popular times of travel            #')
    print('#############################################')

    start_time = time.time()

    # display month
    most_common_month = df['Month'].mode()[0]
    print('The month with the most travels : ' +
          str(months[most_common_month-1]).title())

    # display day in week
    most_common_day = df['Weekday'].mode()[0]
    print('The most common day of the week : ' +
          str(most_common_day))

    # display the hour
    most_common_hour = df['Start Hour'].mode()[0]
    print('The most common start hour      : ' +
          str(most_common_hour))

    #print('#############################################')

    print("\nThis took {} seconds.".format((time.time() - start_time)))

    #print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print()
    print('#############################################')
    print('#        Popular stations and trip          #')
    print('#############################################')

    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = str(df['Start Station'].mode()[0])
    print("The most common start station:")
    print(" - " +  most_common_start_station)

    # display most commonly used end station
    most_common_end_station = str(df['End Station'].mode()[0])
    print("The most common start end: ")
    print(" - " + most_common_end_station)

    # display most frequent combination of start station and
    # end station trip
    df['Start-End Combination'] = (df['Start Station'] + ' - ' +
                                   df['End Station'])
    most_common_start_end_combination = str(df['Start-End Combination']
                                            .mode()[0])
    print("The most common start-end combination of stations is: ")
    print(" - " + most_common_start_end_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print()
    print('#############################################')
    print('#        Trip duration                      #')
    print('#############################################')

    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = (str(int(total_travel_time//86400)) +
                         'd ' +
                         str(int((total_travel_time % 86400)//3600)) +
                         'h ' +
                         str(int(((total_travel_time % 86400) % 3600)//60)) +
                         'm ' +
                         str(int(((total_travel_time % 86400) % 3600) % 60)) +
                         's')
    print('The total travel time is : ' +
          total_travel_time + '.')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = (str(int(mean_travel_time//60)) + 'm ' +
                        str(int(mean_travel_time % 60)) + 's')
    print("The mean travel time is : " +
          mean_travel_time + ".")

    # TO DO: display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print()
    print('#############################################')
    print('#        Users stats                        #')
    print('#############################################')

    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts().to_string()
    print("Distribution for user types:")
    print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        #print('Gender is OK')
        gender_distribution = df['Gender'].value_counts().to_string()
        print("\nDistribution for each gender:")
        print(gender_distribution)
    else:
        #print('Gender - is missing')
        print("No data of user genders")

    #try:
    #    gender_distribution = df['Gender'].value_counts().to_string()
    #    print("\nDistribution for each gender:")
    #    print(gender_distribution)
    #except KeyError:
    #    print("No data of user genders")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = str(int(df['Birth Year'].min()))
        print("\nThe oldest person on "
              "bike born in    : " + earliest_birth_year)
        most_recent_birth_year = str(int(df['Birth Year'].max()))
        print("The youngest person on "
              "bike born in  : " + most_recent_birth_year)
        most_common_birth_year = str(int(df['Birth Year'].mode()[0]))
        print("The most common birth year of bikers : "
              + most_common_birth_year)
    except:
        print("No data of birth year")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):

    print()
    print('#############################################')
    print('#        RAW data                           #')
    print('#############################################')

    # initial input!
    raw_data = input("\nWould you like to see raw data? Enter 'y' or 'n'\n").strip().lower()
    if raw_data in ("yes", "y"):
        i = 0

        while True:
            if (i + 100 > len(df.index) - 1):
                print(df.iloc[i:len(df.index), :])
                print("No more raw data")
                break

            print(df.iloc[i:i+100, :])
            i += 100

            next_raw_data = input("\nNext 100 rows or quit? Enter 'y' or 'n'\n").strip().lower()
            if next_raw_data not in ("yes", "y"):
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter y (yes) or no.\n')
        if restart.lower() != 'yes' or restart.lower() != 'y':
            break

if __name__ == "__main__":
	main()

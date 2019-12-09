import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ['chicago','new york city', 'washington']
    months = ['all','january','february','march','april','may','june']
    days = ['all','monday','sunday','saturday','tuesday','wednesday','thursday','friday']

    while True:
        city =  input('Please enter a city to get data from Chicago, New York City or Washington: ').lower()
        print('City = ' + city)
        if city not in cities:
            print('Incorrect City, please reinput data')
            continue

        month = input('Please enter a month from January to June or All : ').lower()
        print('Month= '+ month)
        if month not in months:
            print('Incorrect Month, please reinput data')
            continue
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

        day = input('Please choose a day of the week or type \'all\' for everyday: ').lower()
        print('Day= ' + day)
        if day not in days:
            print('Incorrect Day, please reinput data')
            continue
        else:
            break

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid i
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    print('Displaying most common month')
    popular_month = df['month'].mode()[0]
    print('This is the most common month: ',popular_month)

    # TO DO: display the most common day of week
    print('Calculating most common day of week')
    popular_day = df['day_of_week'].mode()[0]
    print('This is the most common day: ', popular_day)

    # TO DO: display the most common start hour
    print('Finding most popular hour')
    popular_hour = df['hour'].mode()[0]
    print('This is the most common hour: ',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Discovering start station')
    most_start = df['Start Station'].mode()[0]
    print('Most used Start Station:',most_start)

    # TO DO: display most commonly used end station
    print('Discovering end station')
    most_end = df['End Station'].mode()[0]
    print('Most used End Station:',most_end)


    # TO DO: display most frequent combination of start station and end station trip
    print('discovering start and end station')
    df['combine_start_end'] = df['Start Station'] + ' and \n ' + df['End Station']
    combined = df['combine_start_end'].mode()[0]
    print('This is the most frequent combination of start and end stations: ', combined)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Calculating total travel time')
    travel_total = df['Trip Duration'].sum()
    print('This is the total travel time in minutes:',travel_total)


    # TO DO: display mean travel time
    print('Calculating mean travel time')
    mean_travel = df['Trip Duration'].mean()
    print('This is the average travel time in minutes:', mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Working on user types')
    user_type = df['User Type'].value_counts()
    print('This is the amount of User Type:',user_type)

    # TO DO: Display counts of gender
    print('Working on gender counts of customers')
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('This is the amount of: ',gender_count)
    else:
        print('No information on gender available for the city')

    # TO DO: Display earliest, most recent, and most common year of birth
    print('Working on Year of Birth of every customer')
    if 'Birth Year' in df:
        recent_birth = df['Birth Year'].max()
        print('Most recent birth year',recent_birth)
        earliest_birth = df['Birth Year'].min()
        print('Earliest birth year',earliest_birth)
    else:
        print('No birth year available for customers in city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    index_1 = 0
    index_2 = 5
    while True:
        the_input = input('Would you like to see 5 lines of raw data? Yes/No: ').lower()
        print('Your choice is:', the_input)
        if the_input == 'yes':
            print(df[df.columns[0:]].iloc[index_1:index_2])
            index_1 += 5
            index_2 += 5
        elif the_input == 'no':
            break
        else:
            print('Please reenter a valid input')



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

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

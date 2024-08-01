def check_season(month):
    month = month.lower()

    seasons = {
        'december': 'Winter', 'january': 'Winter', 'february': 'Winter',
        'march': 'Spring', 'april': 'Spring', 'may': 'Spring',
        'june': 'Summer', 'july': 'Summer', 'august': 'Summer',
        'september': 'Autumn', 'october': 'Autumn', 'november': 'Autumn'
    }

    return seasons.get(month, 'Invalid month')

month = input("Enter a month: ")
print(f"The season is: {check_season(month)}")

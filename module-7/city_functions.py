# Function that accepts city and country as parameters and returns a formatted string
def format_city_country(city, country, population='', language=''):
    """Generate a formatted city and country couple and its info."""
    if population or language:
        city_info = f"{city}, {country} - population {population}, {language}"
    else:
        city_info = f"{city}, {country}"
    return city_info.title()

# Call the function with different city, country values
print(format_city_country("Athens", "Greece"))
print(format_city_country("Beijing", "China", "450000"))
print(format_city_country("Berlin", "Germany", "2300000", "German"))

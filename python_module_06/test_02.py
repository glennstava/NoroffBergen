import pycountry

# Get a list of country objects
print(list(pycountry.countries))

"""
countries = list(pycountry.countries)

for land in countries:
    print(land)


country_codes = {}
country_codes_3 = []

for country in countries:
    country_codes[country.alpha_3] = country.name

for country in countries:
    country_codes_3.append(country.alpha_3)

print(country_codes)
print('\n--\n')
print(country_codes_3)

# Create a dictionary of country names to three-letter codes
country_codes_3 = {country.name: country.alpha_3 for country in countries}

# Example: Get the three-letter country code for a specific country
country = 'United States'
if country in country_codes_3:
    code_3 = country_codes_3[country]
    print(f"The three-letter country code for {country} is {code_3}.")
else:
    print(f"Three-letter country code not found for {country}.")
"""
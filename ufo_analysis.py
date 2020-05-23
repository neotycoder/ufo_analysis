import pandas as pd

# Description: This data set is another practice script to explore the UFO dataset from the data.world.
# If you are curious about the data set, you can download it here: https://data.world/aarranzlopez/ufo-sights-2016-us-and-canada
# In this example, instead of using the read_csv method in pandas, I will be using the read_excel method.

# You will need to install the following modules in order to run this script. 
# Note: As of 1/1/2020, Python 2.7 is no longer used, all of my scripts in all my repos conform to Python 3.

# pip3 install xlrd
# pip3 install wheel

# If you want to run this script, you will need to download the UFOs data set in the link provided above, and put it in the same directory where
# you will run this script.


# load csv file into dataframe

ufos = pd.read_excel("UFOs_coord.xlsx")

# perform analysis

# print out details of the data framne. column names, number of rows
ufos.info()

# print out 
print(ufos)

# print out first 5 entries in the data frame
#print(ufos.head(5))

# Let's perform some queries.

# Let's find out where all these sightings are coming from, so let's do a search on countries.
# In order to do that, let's do a Pandas 'unique' query to just return the countries just once.
# Instead of just printing out the 

# Asign the entries to a list, let's call it country.
country = ufos['Country'].unique().tolist()

# Next let's traverse the country list and print out each item.
x = 0   # initialize count variable. This will represent the entry index for items in the list.

print("Countries where sightings in this data frame are coming from:")
# Traverse the list, and print out the each country in the list.
for n in country:
    print(country[x])
    x = x + 1

# Now let's select rows where the country is not equal to USA.
sightings_outside_usa = ufos.loc[ufos['Country'] != "USA"]
print("Sightings outside of the continental United States: ")
print(sightings_outside_usa)

# If we don't want just the output, but want a count of the rows returned, let's do the following:

# Use the new sightings_outside_usa dataframe we created previously, and perform a row count:
#sightings_outside_usa_count = sightings_outside_usa.shape() # This will return the number of rows in the dataframe.
print("The number of sightings outside the United States: " + str(sightings_outside_usa.shape[0]))

# In context to counting the number of rows, if you want to count the number of columns, you can do this:
print("The number of rows in this data frame: " + str(sightings_outside_usa.shape[1]))

# Let's export the sightings outside of the United States to a csv file.
# We will use the sightings_outside_usa data frame again for this example.

filename = 'sightings_outside_usa.csv'
# Let's export the data frame to a csv file:
print("Exporting just sightings outside of the United States to sightings_outside_usa.csv file. ")
sightings_outside_usa.to_csv(filename, header=True)

# Conclusion: THere are other queries you can perform with this example. I just wanted
# to touch on some highlights I came up with to push something out quickly. I may update this with
# more queries, and maybe turn this into a module that you can import. 
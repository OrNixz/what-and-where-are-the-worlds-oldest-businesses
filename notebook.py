#!/usr/bin/env python
# coding: utf-8

# ## 1. The oldest businesses in the world
# <p>This is Staffelter Hof Winery, Germany's oldest business, which was established in 862 under the Carolingian dynasty. It has continued to serve customers through dramatic changes in Europe such as the Holy Roman Empire, the Ottoman Empire, and both world wars. What characteristics enable a business to stand the test of time? Image credit: <a href="https://commons.wikimedia.org/wiki/File:MKn_Staffelter_Hof.jpg">Martin Kraft</a>
# <img src="https://assets.datacamp.com/production/project_1383/./img/MKn_Staffelter_Hof.jpeg" alt="The entrance to Staffelter Hof Winery, a German winery established in 862." width="400"></p>
# <p>To help answer this question, BusinessFinancing.co.uk <a href="https://businessfinancing.co.uk/the-oldest-company-in-almost-every-country">researched</a> the oldest company that is still in business in almost every country and compiled the results into a dataset. Let's explore this work to to better understand these historic businesses. Our datasets, which are all located in the <code>datasets</code> directory, contain the following information: </p>
# <h3 id="businessesandnew_businesses"><code>businesses</code> and <code>new_businesses</code></h3>
# <table>
# <thead>
# <tr>
# <th style="text-align:left;">column</th>
# <th>type</th>
# <th>meaning</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td style="text-align:left;"><code>business</code></td>
# <td>varchar</td>
# <td>Name of the business.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>year_founded</code></td>
# <td>int</td>
# <td>Year the business was founded.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>category_code</code></td>
# <td>varchar</td>
# <td>Code for the category of the business.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>country_code</code></td>
# <td>char</td>
# <td>ISO 3166-1 3-letter country code.</td>
# </tr>
# </tbody>
# </table>
# <h3 id="countries"><code>countries</code></h3>
# <table>
# <thead>
# <tr>
# <th style="text-align:left;">column</th>
# <th>type</th>
# <th>meaning</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td style="text-align:left;"><code>country_code</code></td>
# <td>varchar</td>
# <td>ISO 3166-1 3-letter country code.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>country</code></td>
# <td>varchar</td>
# <td>Name of the country.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>continent</code></td>
# <td>varchar</td>
# <td>Name of the continent that the country exists in.</td>
# </tr>
# </tbody>
# </table>
# <h3 id="categories"><code>categories</code></h3>
# <table>
# <thead>
# <tr>
# <th style="text-align:left;">column</th>
# <th>type</th>
# <th>meaning</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td style="text-align:left;"><code>category_code</code></td>
# <td>varchar</td>
# <td>Code for the category of the business.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>category</code></td>
# <td>varchar</td>
# <td>Description of the business category.</td>
# </tr>
# </tbody>
# </table>
# <p>Now let's learn about some of the world's oldest businesses still in operation!</p>

# In[2]:


# Import the pandas library under its usual alias
import pandas as pd

# Load the business.csv file as a DataFrame called businesses
businesses = pd.read_csv("datasets/businesses.csv")

# Sort businesses from oldest businesses to youngest
sorted_businesses = businesses.sort_values("year_founded")

# Display the first few lines of sorted_businesses
sorted_businesses.head()


# In[3]:


get_ipython().run_cell_magic('nose', '', '\ndef test_pandas_loaded():\n    assert "pd" in globals(), \\\n    "Did you correctly import the `pandas` library under the alias `pd`?"\n\nimport pandas as pd\ntest_businesses = pd.read_csv("datasets/businesses.csv")\ntest_sorted_businesses = test_businesses.sort_values("year_founded")\n\ndef test_bus():\n    assert isinstance(businesses, pd.DataFrame), \\\n    "Did you create a `businesses` DataFrame using `pd.read_csv()`?"\n    assert test_businesses.reset_index().equals(businesses.reset_index()), \\\n    "Your `businesses` DataFrame is not equal to the expected DataFrame. Did you load your `businesses` DataFrame from `datasets/businesses.csv` using `pd.read_csv()`?"\n    \ndef test_sorted_bus():\n    assert sorted_businesses.iloc[-1:].equals(test_sorted_businesses.iloc[-1:]), \\\n    "Did you create `sorted_businesses` by sorting `year_founded` in _ascending_ order?"\n    assert test_sorted_businesses.reset_index().equals(sorted_businesses.reset_index()), \\\n    "Your `sorted_businesses` DataFrame is not equal to the expected DataFrame. Did you create it by calling `.sort_values()` on `businesses` and sorting by `year_founded`?"')


# ## 2. The oldest businesses in North America
# <p>So far we've learned that Kongō Gumi is the world's oldest continuously operating business, beating out the second oldest business by well over 100 years! It's a little hard to read the country codes, though. Wouldn't it be nice if we had a list of country names to go along with the country codes?</p>
# <p>Enter <code>countries.csv</code>, which is also located in the <code>datasets</code> folder. Having useful information in different files is a common problem: for data storage, it's better to keep different types of data separate, but for analysis, we want all the data in one place. To solve this, we'll have to join the two tables together. </p>
# <h3 id="countries"><code>countries</code></h3>
# <table>
# <thead>
# <tr>
# <th style="text-align:left;">column</th>
# <th>type</th>
# <th>meaning</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td style="text-align:left;"><code>country_code</code></td>
# <td>varchar</td>
# <td>ISO 3166-1 3-letter country code.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>country</code></td>
# <td>varchar</td>
# <td>Name of the country.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>continent</code></td>
# <td>varchar</td>
# <td>Name of the continent that the country exists in.</td>
# </tr>
# </tbody>
# </table>
# <p>Since <code>countries.csv</code> contains a <code>continent</code> column, merging the datasets will also allow us to look at the oldest business on each continent! </p>

# In[4]:


# Load countries.csv to a DataFrame
countries = pd.read_csv("datasets/countries.csv")

# Merge sorted_businesses with countries
businesses_countries = sorted_businesses.merge(countries, on="country_code")

# Filter businesses_countries to include countries in North America only
north_america = businesses_countries[businesses_countries["continent"] == "North America"]
north_america.head()


# In[5]:


get_ipython().run_cell_magic('nose', '', '\nimport pandas as pd\ntest_businesses = pd.read_csv("datasets/businesses.csv")\ntest_sorted_businesses = test_businesses.sort_values("year_founded")\ntest_countries = pd.read_csv("datasets/countries.csv")\ntest_businesses_countries = test_sorted_businesses.merge(test_countries, on= "country_code")\ntest_north_america = test_businesses_countries[test_businesses_countries["continent"]== "North America"]\n\ndef test_cntries():\n    assert isinstance(countries, pd.DataFrame), \\\n    "Did you create a `countries` DataFrame using `pd.read_csv()`?"\n    assert test_countries.reset_index().equals(countries.reset_index()), \\\n    "Your `countries` DataFrame is not equal to the expected DataFrame."\n\ndef test_bus_countries():\n    assert len(businesses_countries.columns) == len(test_businesses_countries.columns), \\\n    "Your `businesses_countries` DataFrame should have six columns: `business`, `year_founded`, `category_code`, `country_code`, `country`, and `continent`."\n    assert test_businesses_countries.reset_index().equals(businesses_countries.reset_index()), \\\n    "Your `businesses_countries` DataFrame is not equal to the expected DataFrame."\n    \ndef test_north_am():\n    assert north_america.shape[0] == test_north_america.shape[0], \\\n    "Did you filter `businesses_countries` to include only countries in North America? It looks like your `north_america` DataFrame has a different number of rows than expected."\n    assert test_north_america.reset_index().equals(north_america.reset_index()), \\\n    "Your `north_america` DataFrame is not equal to the expected DataFrame."')


# ## 3. The oldest business on each continent
# <p>Now we can see that the oldest company in North America is La Casa de Moneda de México, founded in 1534. Why stop there, though, when we could easily find out the oldest business on every continent? </p>

# In[6]:


# Create continent, which lists only the continent and oldest year_founded
continent = businesses_countries.groupby("continent").agg({"year_founded":"min"})

# Merge continent with businesses_countries
merged_continent = continent.merge(businesses_countries, on=["continent", "year_founded"])

# Subset continent so that only the four columns of interest are included
subset_merged_continent = merged_continent[["continent", "country", "business", "year_founded"]]
subset_merged_continent


# In[7]:


get_ipython().run_cell_magic('nose', '', '\nimport pandas as pd\ntest_businesses = pd.read_csv("datasets/businesses.csv")\ntest_countries = pd.read_csv("datasets/countries.csv")\ntest_businesses_countries = test_businesses.merge(test_countries, on="country_code")\ntest_continent = test_businesses_countries.groupby("continent").agg({"year_founded":"min"})\ntest_merged_continent = test_continent.merge(test_businesses_countries, on=["continent", "year_founded"])\ntest_subset_merged_continent = test_merged_continent[["continent", "country", "business", "year_founded"]]\n\ndef test_cont():\n    assert isinstance(continent, pd.DataFrame), \\\n    "Your `continent` DataFrame needs to be a DataFrame and not a Series. The index of the DataFrame will be continent names. You can use the .agg() function to do this."\n    assert len(continent.columns) == len(test_continent.columns), \\\n    "Your `continent` DataFrame should have `continent` as its index and should have a single column called `year_founded`."\n    assert continent.shape[0] == test_continent.shape[0], \\\n    "Did you group `businesses_countries` by `continent`? It looks like your `continent` DataFrame has a different number of rows than expected."\n\ndef test_subset_merged_cont():\n    assert test_subset_merged_continent.columns.all() == subset_merged_continent.columns.all(), \\\n    "Did you correctly subset the `continent` DataFrame by selecting the columns of interest (in order)?"\n    assert subset_merged_continent.shape[0] == test_subset_merged_continent.shape[0], \\\n    "Did you subset the `merged_continent` DataFrame _columns_? The number of rows in `subset_merged_continent` and `merged_continent` should be the same."\n ')


# ## 4. Unknown oldest businesses
# <p>BusinessFinancing.co.uk wasn't able to determine the oldest business for some countries, and those countries are simply left off of <code>businesses.csv</code> and, by extension, <code>businesses</code>. However, the <code>countries</code> that we created <em>does</em> include all countries in the world, regardless of whether the oldest business is known. </p>
# <p>We can compare the two datasets in one DataFrame to find out which countries don't have a known oldest business! </p>

# In[8]:


# Use .merge() to create a DataFrame, all_countries
all_countries = businesses.merge(countries, on="country_code", how="right",  indicator=True)

# Filter to include only countries without oldest businesses
missing_countries = all_countries[all_countries["_merge"] != "both"]

# Create a series of the country names with missing oldest business data
missing_countries_series = missing_countries["country"]

# Display the series
missing_countries_series


# In[9]:


get_ipython().run_cell_magic('nose', '', 'import pandas as pd\noutput = _\ntest_businesses = pd.read_csv("datasets/businesses.csv")\n\ntest_countries = pd.read_csv("datasets/countries.csv")\ntest_all_countries = test_businesses.merge(test_countries, on="country_code", how="right",  indicator = True)\ntest_missing_countries = test_all_countries[test_all_countries["_merge"] != "both"]\ntest_missing_countries_series = test_missing_countries["country"]\n\ndef test_all():\n    assert {\'business\', \'year_founded\', \'category_code\', \'country_code\', \'country\', \'continent\'}.issubset(all_countries.columns), \\\n    "Your `all_countries` DataFrame should include the following columns: `business`, `year_founded`, `category_code`, `country_code`, `country`, `continent`, and `_merge`. Did you create the DataFrame using an outer merge with `indicator = True`?"\n    assert all_countries.shape[0] == test_all_countries.shape[0], \\\n    "Did you use an outer merge to create `all_countries`? It looks like your `all_countries` DataFrame has a different number of rows than expected."\n\ndef test_missing():\n    assert missing_countries.shape[0] == test_missing_countries.shape[0], \\\n    "Did you filter `all_countries` to include only countries that _don\'t_ have a \'both\' value in the `_merge` column? It looks like your `missing_countries` DataFrame has a different number of rows than expected."\n\ndef test_series():\n    assert isinstance(missing_countries_series, pd.Series), \\\n    "Are you sure your `missing_countries_series` is a _Series_ and not a DataFrame?"\n    assert len(missing_countries_series) == len(test_missing_countries), \\\n    "The number of missing countries is different than expected. It should not change between the `missing_countries` DataFrame and `missing_countries_series`."\n    assert test_missing_countries_series.equals(missing_countries_series), \\\n    "Your `missing_countries_series` is not equal to the expected series."\n\ndef test_display_series():\n    assert test_missing_countries_series.equals(_), \\\n    "Did you display `missing_countries_series` as cell output?"')


# ## 5. Adding new oldest business data
# <p>It looks like we've got some holes in our dataset! Fortunately, we've taken it upon ourselves to improve upon BusinessFinancing.co.uk's work and find oldest businesses in a few of the missing countries. We've stored the newfound oldest businesses in <code>new_businesses</code>, located at <code>"datasets/new_businesses.csv"</code>. It has the exact same structure as our <code>businesses</code> dataset. </p>
# <h3 id="new_businesses"><code>new_businesses</code></h3>
# <table>
# <thead>
# <tr>
# <th style="text-align:left;">column</th>
# <th>type</th>
# <th>meaning</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td style="text-align:left;"><code>business</code></td>
# <td>varchar</td>
# <td>Name of the business.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>year_founded</code></td>
# <td>int</td>
# <td>Year the business was founded.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>category_code</code></td>
# <td>varchar</td>
# <td>Code for the category of the business.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>country_code</code></td>
# <td>char</td>
# <td>ISO 3166-1 3-letter country code.</td>
# </tr>
# </tbody>
# </table>
# <p>All we have to do is combine the two so that we've got one more complete list of businesses!</p>

# In[10]:


# Import new_businesses.csv
new_businesses = pd.read_csv("datasets/new_businesses.csv")

# Add the data in new_businesses to the existing businesses
all_businesses = pd.concat([new_businesses, businesses])

# Merge and filter to find countries with missing business data
new_all_countries = all_businesses.merge(countries, on="country_code", how="outer",  indicator=True)
new_missing_countries = new_all_countries[new_all_countries["_merge"] != "both"]

# Group by continent and create a "count_missing" column
count_missing = new_missing_countries.groupby("continent").agg({"country":"count"})
count_missing.columns = ["count_missing"]
count_missing


# In[11]:


get_ipython().run_cell_magic('nose', '', 'import pandas as pd\ntest_businesses = pd.read_csv("datasets/businesses.csv")\ntest_countries = pd.read_csv("datasets/countries.csv")\ntest_new_businesses = pd.read_csv("datasets/new_businesses.csv")\ntest_all_businesses = pd.concat([test_new_businesses, test_businesses])\ntest_new_all_countries = test_all_businesses.merge(test_countries, on="country_code", how="outer",  indicator = True)\ntest_new_missing_countries = test_new_all_countries[test_new_all_countries["_merge"] != "both"]\ntest_count_missing = test_new_missing_countries.groupby("continent").agg({"country":"count"})\ntest_count_missing.columns = ["count_missing"]\n\ndef test_import():\n    assert isinstance(new_businesses, pd.DataFrame), \\\n    "Did you create a `new_businesses` DataFrame using `pd.read_csv()`?"\n\ndef test_all_bus():\n    assert all_businesses.shape[0] == test_all_businesses.shape[0], \\\n    "Did you use `pd.concat()` to create `all_businesses` from `new_businesses` and `businesses`? It looks like your `all_businesses` DataFrame has a different number of rows than expected."\n    assert all_businesses.shape[1] == test_all_businesses.shape[1], \\\n    "Did you create `all_businesses` from `new_businesses` and `businesses` by stacking them _vertically_? It looks like your `all_businesses` DataFrame has a different number of columns than expected."\n    assert test_all_businesses.reset_index().equals(all_businesses.reset_index()), \\\n    "Your `all_businesses` DataFrame is not equal to the expected DataFrame. Did you use `pd.concat()` to stack `new_businesses` and `businesses` vertically?"\n    \ndef test_new_all_cntries():\n    assert {\'business\', \'year_founded\', \'category_code\', \'country_code\', \'country\', \'continent\'}.issubset(new_all_countries.columns), \\\n    "Your `new_all_countries` DataFrame should include the following columns: `business`, `year_founded`, `category_code`, `country_code`, `country`, `continent`, and `_merge`. Did you create the DataFrame using an outer merge with `indicator = True`?"\n    assert new_all_countries.shape[0] == test_new_all_countries.shape[0], \\\n    "Did you use a right or outer merge to create `new_all_countries`? It looks like your `new_all_countries` DataFrame has a different number of rows than expected."\n\ndef test_new_missing_cntries():\n    assert new_missing_countries.shape[0] == test_new_missing_countries.shape[0], \\\n    "Did you filter `new_all_countries` to include only countries that _don\'t_ have a \'both\' value in the `_merge` column? It looks like your `new_missing_countries` DataFrame has a different number of rows than expected."\n\ndef test_count_miss():\n    assert isinstance(count_missing, pd.DataFrame), \\\n    "Your `count_missing` DataFrame needs to be a DataFrame and not a Series. The index will be continent names. You can use the .agg() function to do this."\n    assert count_missing.shape[0] == test_count_missing.shape[0], \\\n    "Did you create `count_missing` by grouping `new_missing_countries` by continent? It looks like your `count_missing` DataFrame has a different number of rows than expected."\n    try:\n        assert count_missing.columns == ["count_missing"]\n    except AssertionError:\n        assert False, "Does `count_missing` have only one column? Did you forget to rename the column to `count_missing`?"\n    assert test_count_missing.equals(count_missing), \\\n    "Your `count_missing` DataFrame is not equal to the expected DataFrame. Did you aggregate the data by _counting_ the number of countries missing from each continent group?"')


# ## 6. The oldest industries
# <p>Remember our oldest business in the world, Kongō Gumi? </p>
# <table>
# <thead>
# <tr>
# <th style="text-align:right;"></th>
# <th style="text-align:left;">business</th>
# <th style="text-align:right;">year_founded</th>
# <th style="text-align:left;">category_code</th>
# <th style="text-align:left;">country_code</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td style="text-align:right;">64</td>
# <td style="text-align:left;">Kongō Gumi</td>
# <td style="text-align:right;">578</td>
# <td style="text-align:left;">CAT6</td>
# <td style="text-align:left;">JPN</td>
# </tr>
# </tbody>
# </table>
# <p>We know Kongō Gumi was founded in the year 578 in Japan, but it's a little hard to decipher which industry it's in. Information about what the <code>category_code</code> column refers to is in <code>"datasets/categories.csv"</code>: </p>
# <h3 id="categories"><code>categories</code></h3>
# <table>
# <thead>
# <tr>
# <th style="text-align:left;">column</th>
# <th>type</th>
# <th>meaning</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td style="text-align:left;"><code>category_code</code></td>
# <td>varchar</td>
# <td>Code for the category of the business.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>category</code></td>
# <td>varchar</td>
# <td>Description of the business category.</td>
# </tr>
# </tbody>
# </table>
# <p>Let's use <code>categories.csv</code> to understand how many oldest businesses are in each category of industry.</p>

# In[12]:


# Import categories.csv and merge to businesses
categories = pd.read_csv("datasets/categories.csv")
businesses_categories = businesses.merge(categories, on="category_code")

# Create a DataFrame which lists the number of oldest businesses in each category
count_business_cats = businesses_categories.groupby("category").agg({"business":"count"})

# Create a DataFrame which lists the cumulative years that businesses from each category have been operating
years_business_cats = businesses_categories.groupby("category").agg({"year_founded":"sum"})

# Rename columns and display the first five rows of both DataFrames
count_business_cats.columns = ["count"]
years_business_cats.columns = ["total_years_in_business"]
display(count_business_cats.head(), years_business_cats.head())


# In[13]:


get_ipython().run_cell_magic('nose', '', '\nimport pandas as pd\ntest_businesses = pd.read_csv("datasets/businesses.csv")\ntest_categories = pd.read_csv("datasets/categories.csv")\ntest_businesses_categories = test_businesses.merge(test_categories, on="category_code")\ntest_count_business_cats = test_businesses_categories.groupby("category").agg({"business":"count"})\ntest_years_business_cats = test_businesses_categories.groupby("category").agg({"year_founded":"sum"})\ntest_count_business_cats.columns = ["count"]\ntest_years_business_cats.columns = ["total_years_in_business"]\n\ndef test_import():\n    assert isinstance(categories, pd.DataFrame), \\\n    "Did you create a `categories` DataFrame using `pd.read_csv()`?"\n\ndef test_count_bus_cats():\n    assert isinstance(count_business_cats, pd.DataFrame), \\\n    "Your `count_business_cats` DataFrame needs to be a DataFrame and not a Series. The index will be category names. You can use the .agg() function to do this."\n    assert count_business_cats.shape[0] == test_count_business_cats.shape[0], \\\n    "Did you group `count_business_cats` by `category`? It looks like your `count_business_cats` DataFrame has a different number of rows than expected."\n    assert test_count_business_cats.index.all() == count_business_cats.index.all(), \\\n    "Did you group `count_business_cats` by `category`? It looks like your `count_business_cats` DataFrame indexes aren\'t the business category names."\n    assert test_count_business_cats.columns.all() == count_business_cats.columns.all(), \\\n    "Did you rename the column in `count_business_cats`?"\n    assert test_count_business_cats.equals(count_business_cats), \\\n    "Did you aggregate the `business` column using `count`?"\n    \ndef test_years_bus_cats():\n    assert isinstance(years_business_cats, pd.DataFrame), \\\n    "Your `years_business_cats` DataFrame needs to be a DataFrame and not a Series. The index will be category names. You can use the .agg() function to do this."\n    assert years_business_cats.shape[0] == test_years_business_cats.shape[0], \\\n    "Did you group `years_business_cats` by `category`? It looks like your `years_business_cats` DataFrame has a different number of rows than expected."\n    assert test_count_business_cats.index.all() == count_business_cats.index.all(), \\\n    "Did you group `years_business_cats` by `category`? It looks like your `years_business_cats` DataFrame indexes aren\'t the business category names."\n    assert test_years_business_cats.columns.all() == years_business_cats.columns.all(), \\\n    "Did you rename the column in `years_business_cats`?"\n    assert test_years_business_cats.equals(years_business_cats), \\\n    "Did you aggregate the `year_founded` column using `sum` when creating `years_business_cats`?"')


# ## 7. Restaurant representation
# <p>No matter how we measure it, looks like Banking and Finance is an excellent industry to be in if longevity is our goal! Let's zoom in on another industry: cafés, restaurants, and bars. Which restaurants in our dataset have been around since before the year 1800?</p>

# In[14]:


# Filter using .query() for CAT4 businesses founded before 1800; sort results
old_restaurants = businesses_categories.query('year_founded < 1800 and category_code == "CAT4"')

# Sort the DataFrame
old_restaurants = old_restaurants.sort_values("year_founded")
old_restaurants


# In[15]:


get_ipython().run_cell_magic('nose', '', '\nimport pandas as pd\ntest_businesses = pd.read_csv("datasets/businesses.csv")\ntest_categories = pd.read_csv("datasets/categories.csv")\ntest_businesses_categories = test_businesses.merge(test_categories, on="category_code")\ntest_old_restaurants = test_businesses_categories.query(\'year_founded < 1800 and category_code == "CAT4"\').sort_values("year_founded")\n\ndef test_old_rests():\n    assert old_restaurants.shape[0] == test_old_restaurants.shape[0], \\\n    "Did you filter using `.query()` where `year_founded` is less than 1800 and `category_code` is \'CAT4\'? It looks like your `old_restaurants` DataFrame has a different number of rows than expected."\n    assert old_restaurants.iloc[-1:].equals(test_old_restaurants.iloc[-1:]), \\\n    "Did you sort `old_restaurants` by `year_founded` in _ascending_ order?"\n    assert test_old_restaurants.reset_index().equals(old_restaurants.reset_index()), \\\n    "Your `old_restaurants` DataFrame is not equal to the expected DataFrame. Did you filter using `.query()` where `year_founded` is less than 1800 and `category_code` is \'CAT4\'? Did you sort from oldest to newest?"')


# ## 8. Categories and continents
# <p>St. Peter Stifts Kulinarium is old enough that the restaurant is believed to have served Mozart - and it would have been over 900 years old even when he was a patron! Let's finish by looking at the oldest business in each category of commerce for each continent. </p>

# In[16]:


# Merge all businesses, countries, and categories together
businesses_categories_countries = businesses_categories.merge(countries, on="country_code")

# Sort businesses_categories_countries from oldest to most recent
businesses_categories_countries = businesses_categories_countries.sort_values("year_founded")

# Create the oldest by continent and category DataFrame
oldest_by_continent_category = businesses_categories_countries.groupby(["continent", "category"]).agg({"year_founded":"min"})
oldest_by_continent_category.head()


# In[17]:


get_ipython().run_cell_magic('nose', '', 'import pandas as pd\ntest_businesses = pd.read_csv("datasets/businesses.csv")\ntest_categories = pd.read_csv("datasets/categories.csv")\ntest_countries = pd.read_csv("datasets/countries.csv")\ntest_businesses_categories = test_businesses.merge(test_categories, on="category_code")\ntest_businesses_categories_countries = test_businesses_categories.merge(test_countries, on="country_code").sort_values("year_founded")\ntest_oldest_by_continent_category = test_businesses_categories_countries.groupby(["continent", "category"]).agg({"year_founded":"min"})\n\ndef test_bus_cat_countries():\n    assert len(businesses_categories_countries.columns) == len(businesses_categories_countries.columns), \\\n    "Your `businesses_categories_countries` DataFrame should have seven columns: `business`, `year_founded`, `category_code`, `country_code`, `category`, `country`, and `continent`."\n    assert businesses_categories_countries.shape[0] == test_businesses_categories_countries.shape[0], \\\n    "It looks like your `businesses_categories_countries` DataFrame has a different number of rows than expected."\n    assert test_businesses_categories_countries.iloc[-1:].equals(businesses_categories_countries.iloc[-1:]),\\\n    "Did you sort `businesses_categories_countries` by `year_founded`?"\n        \ndef test_grouped():\n    assert isinstance(oldest_by_continent_category, pd.DataFrame), \\\n    "Your `oldest_by_continent_category` DataFrame needs to be a DataFrame and not a Series. The index will be continent and category names since it is grouped by both. You can use the .agg() function to do this."\n    assert test_oldest_by_continent_category.index.get_level_values("category").all() == oldest_by_continent_category.sort_index().index.get_level_values("category").all(),\\\n    "Did you group `oldest_by_continent_category` by `continent` and `category`?"\n        \ndef test_values():\n    assert test_oldest_by_continent_category.equals(oldest_by_continent_category),\\\n    "Your `old_restaurants` DataFrame is not equal to the expected DataFrame. Did you aggregate the `year_founded` column by finding its minimum?"\n    ')


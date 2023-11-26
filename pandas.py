import pandas as pd

data = {
    "country": ["china", "japan", "korea", "usa"],
    "gdp": [1409250000, 516700000, 169320000, 2041280000],
    "population": [141500, 12718, 5180, 32676],
}

country = pd.DataFrame(data)
country = country.set_index("country")

print(country.shape)  # (4, 2)
print(country.size)  # 8
print(country.ndim)  # 2
print(country.values)

country.index.name = "Country"
country.columns.name = "Info"

print(country.index)
# Index(['china', 'japan', 'korea', 'usa'], dtype='onject', name='Country')
print(country.columns)
# Index(['gdp', 'population'], dtype='object', name='Info')

import pandas

words = pandas.read_csv('data/test.csv')
dataframe = words.to_dict()

print(dataframe)

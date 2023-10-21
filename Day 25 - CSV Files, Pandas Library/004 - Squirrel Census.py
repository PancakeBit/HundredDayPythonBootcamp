import pandas

census = pandas.read_csv('004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
colors = ['Gray', 'Cinnamon', 'Black']
counts = []
for color in colors:
    all = census[census['Primary Fur Color'] == color]
    counts.append(len(all['Primary Fur Color']))

finalcount = pandas.DataFrame({'Colors': colors, 'Count': counts})
finalcount.to_csv('CountOfColors.csv')


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read data
path = 'Files/train.csv'
data = pd.read_csv(path, sep = ',', index_col = 0)  # index_col for using our own indexing

def abs_val(prcnt, all_values):
	val = np.sum(all_values) * prcnt / 100
	return '{p:.2f}%\n({v:.0f})'.format(p=prcnt,v=val)

# set figure's background
plt.figure(1).set_facecolor('lightgrey')


#####################################################
# women/men number	
# values = data.Sex.value_counts()

# plt.figure(1).canvas.set_window_title('Men\\Women')
# plt.title('# of male\\female on the ship:')
# plt.pie(values,
# 		labels=['Men', 'Women'],
# 		autopct=lambda prcnt : abs_val(prcnt, values),
# 		colors=[(0.3, 0.2, 0.8), (0.8, 0.1, 0.4)],
# 		wedgeprops=dict(width=0.5, alpha=0.5),
# 		rotatelabels=True,
# 		startangle=64,
# 		pctdistance=0.75)
# plt.show()
#####################################################


#####################################################
# passengers in each class
# values = data.Pclass.value_counts()

# plt.figure(1).canvas.set_window_title('Passenger per class')
# plt.title('# of passengers per class')
# plt.pie(values,
# 		labels=['Third','First','Second'],
# 		wedgeprops=dict(alpha=0.5),
#  		colors=[(0.3, 0.4, 0.9), (0.3, 0.2, 0.4), (0.05, 0.2, 0.7) ],
# 		autopct=lambda prcnt : abs_val(prcnt, values),
# 		explode=[0,.05,0])
# plt.show()
#####################################################


#####################################################
# average age by class
# age_by_class = data.groupby(['Sex','Pclass'])
# age_by_class.Age.mean().plot(kind='bar', grid=True, rot=15)
# plt.show()
#####################################################


#####################################################
# fraction of survived
# survived = data.Survived.value_counts()/len(data)
# plt.pie(data.Survived.value_counts(),
# 	labels=['Not Survived','Survived'],
# 	wedgeprops=dict(alpha=0.6),
# 	autopct=lambda prcnt : abs_val(prcnt, data.Survived.value_counts()),
# 	colors=[(0.9,0.1,0.1),(0.2,0.5,0.1)])
# plt.show()
#####################################################


#####################################################
# child survivorship
# child_survived = data[data.Age < 14].Survived.value_counts()
# elder_survived = data[data.Age >= 14].Survived.value_counts()

# plt.pie(child_survived,
# 		labeldistance=0.35,
# 		wedgeprops=dict(width=0.3, alpha=0.6, edgecolor='w'),
# 	 	colors=[(0,0.4,0),(0.9,0,0)],
# 		autopct = '%.1f%%',
# 		pctdistance=0.75,
# 	 	radius=1-0.3)

# plt.pie(elder_survived,
# 		wedgeprops=dict(width = 0.3, alpha=0.7, edgecolor='w'),
# 		autopct = '%.1f%%',
# 		pctdistance=0.85,
# 	 	colors=[(0.9,0,0),(0,0.4,0)],
# 	 	startangle=138.5)

# plt.annotate('Adults', xy=(-0.9,0.4), xytext=(-1.4,0.6),
# 			bbox=dict(boxstyle="round", fc="w"),
# 			arrowprops=dict(facecolor='black', width=0.3, headwidth=6))

# plt.annotate('Childs', xy=(0.58, 0.37), xytext=(0.9,0.7),
# 			bbox=dict(boxstyle="round", fc="w"),
# 			arrowprops=dict(facecolor='black', width=0.3, headwidth=6))
# plt.show()
#####################################################


#####################################################
# women survivorship
# men_survived = data[data.Sex == 'male'].Survived.value_counts()
# women_survived = data[data.Sex == 'female'].Survived.value_counts()

# plt.pie(men_survived,
# 		labeldistance=0.35,
# 		wedgeprops=dict(width=0.3, alpha=0.6, edgecolor='w'),
# 	 	colors=[(0.9,0,0), (0,0.4,0)],
# 		autopct = '%.1f%%',
# 		pctdistance=0.75,
# 		startangle=68,
# 	 	radius=1-0.3)

# plt.pie(women_survived,
# 		wedgeprops=dict(width = 0.3, alpha=0.7, edgecolor='w'),
# 		autopct = '%.1f%%',
# 		pctdistance=0.85,
# 	 	colors=[(0,0.4,0),(0.9,0,0)])

# plt.annotate('Women', xy=(-0.9,0.4), xytext=(-1.4,0.6),
# 			bbox=dict(boxstyle="round", fc="w"),
# 			arrowprops=dict(facecolor='black', width=0.3, headwidth=6))

# plt.annotate('Men', xy=(0.58, 0.37), xytext=(0.9,0.7),
# 			bbox=dict(boxstyle="round", fc="w"),
# 			arrowprops=dict(facecolor='black', width=0.3, headwidth=6))
# plt.show()
#####################################################


#####################################################
# ticket mean and std
# print('Average ticket price is ${:.2f}'.format(data.Fare.mean()))
# print('Mean absolute deviation is ${:.2f}'.format(data.Fare.mad()))
# print('And standard deviation is ${:.2f}'.format(data.Fare.std()))
#####################################################


#####################################################
# rich guys survivorship
# rich_guys = data[data.Fare > data.Fare.mean()].Survived.value_counts(normalize=True) * 100
# poor_guys = data[data.Fare < data.Fare.mean()].Survived.value_counts(normalize=True) * 100

# survived = (rich_guys[0], poor_guys[1])
# not_survived = (rich_guys[1], poor_guys[0])

# # positioning of bars
# bar_pos = (0,1)
# plt.bar(bar_pos, survived, width=0.5, color=(0, .6, .1), alpha=0.85)
# plt.bar(bar_pos, not_survived, width=0.5, color=(.7, 0, 0), alpha=0.85, bottom=survived)

# # labels
# plt.figure(1).canvas.set_window_title('Pic')
# plt.title('Survivorship by fare')
# plt.ylabel('Survivorship, %')
# plt.xticks(bar_pos, ('Rich','Poor'))
# plt.show()
#####################################################


#####################################################
# most popular male name
Names = [s.split('.', 1)[-1] for s in data[data.Sex == 'female'].Name]		# get all after point
Names = [s.split(' ',2)[1] for s in Names]				# extract name
Names = [s.translate({ord(i) : None for i in '()/'}) for s in Names]
Names = pd.Series(Names)

print(Names)

most_popular_names = Names.value_counts()[:5]
bar_pos = range(len(most_popular_names))

plt.bar(bar_pos, most_popular_names.values, width = 0.8, color=(0,0.3,0.3), alpha=0.6)

plt.title('Most popular male names')
plt.xticks(bar_pos, most_popular_names.keys(), rotation=0)

for i, height in enumerate(most_popular_names.values):
	plt.text(i-0.2, height + 0.15, most_popular_names.values[i])

plt.show()
#####################################################


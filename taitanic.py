import pandas as pd

# train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
# train = pd.read_csv(train_url)
# test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
# test = pd.read_csv(test_url)
train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")
print("train.describe()", end=" : ")
print(train.describe())
print("train.shape", end=" : ")
print(train.shape)

# 2
print(train["Survived"].value_counts())
print(train["Survived"].value_counts(normalize=True))
print(train["Sex"] == 'male')
print(train['Survived'][train['Sex'] == 'male'].value_counts(normalize=True))
print(train['Survived'][train['Sex'] == 'female'].value_counts(normalize=True))

# 3

train["Child"] = float('NaN')

pd.options.mode.chained_assignment = None  # default='warn'

train["Child"][train['Age'] < 18] = 1 #이거 이상한거 떠도 되긴 되네 너무 신기 위에꺼 하면 안뜨네
train["Child"][train['Age'] >= 18] = 0

print(train["Survived"][train["Child"] == 1].value_counts(normalize=True))

print(train["Survived"][train["Child"] == 0].value_counts(normalize=True))

# 출처 : https://smlee729.wordpress.com/category/data-analysis/

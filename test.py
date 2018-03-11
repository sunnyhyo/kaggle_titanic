from IPython.display import Image

Image(
    url="https://static1.squarespace.com/static/5006453fe4b09ef2252ba068/5095eabce4b06cb305058603/5095eabce4b02d37bef4c24c/1352002236895/100_anniversary_titanic_sinking_by_esai8mellows-d4xbme8.jpg")

import pandas as pd

train = pd.read_csv('input/train.csv')
test = pd.read_csv('input/test.csv')
train.head(80)
test.head()
train.shape
test.shape
train.info()
test.info()
train.isnull().sum()
test.isnull().sum()

import matplotlib.pyplot as plt
# % matplotlib inline
import seaborn as sns

sns.set()  # setting seaborn default for plots


def bar_chart(feature):
    survived = train[train['Survived'] == 1][feature].value_counts()
    dead = train[train['Survived'] == 0][feature].value_counts()
    df = pd.DataFrame([survived, dead])
    df.index = ['Survived', 'Dead']
    df.plot(kind='bar', stacked=True, figsize=(10, 5))
    


bar_chart('Sex')
print("ohoh")

#!/usr/bin/env python
# coding: utf-8

# # 0. Data Processing

# In[1]:


import pandas as pd


# In[2]:


wines = pd.read_csv("wine_dataset.csv")
pd.options.display.max_columns = None
wines.head()


# In[3]:


wines.shape


# ### 0-1. Handling Imbalanced Dataset

# In[4]:


from sklearn.utils import resample


# In[5]:


wines["style"].value_counts()


# In[6]:


wines_w = wines[wines["style"] == "white"]
wines_r = wines[wines["style"] == "red"]


# In[7]:


wines_w_d = resample(wines_w, n_samples=1599, replace=False, random_state=0)


# In[8]:


wines_d = pd.concat([wines_w_d, wines_r], axis=0)


# In[9]:


wines_d["style"].value_counts()


# ### 0-2. Define Y and X

# In[10]:


wines_d.columns.get_loc("style")


# In[11]:


y = wines_d.iloc[:,12]


# In[12]:


col = list(range(0, 13))
del col[12]


# In[13]:


x = wines_d.iloc[:, col]


# In[14]:


from sklearn.model_selection import train_test_split


# In[15]:


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=15)


# # 1. Prediction Models

# ## 1-1. Decision Trees

# In[16]:


from sklearn.tree import DecisionTreeClassifier


# ### 1) Criterion = entropy

# In[17]:


from sklearn import metrics
from sklearn.model_selection import cross_val_score
import numpy as np


# In[18]:


nums_d = range(1, 20)


# In[19]:


for n in nums_d: 
    dtc = DecisionTreeClassifier(criterion="entropy", max_depth= n, random_state= 0)
    scores = cross_val_score(dtc, x, y, cv=5)
    print(n, ":", np.mean(scores))


# In[20]:


# visualization

d = dict()

for n in nums_d: 
    dtc = DecisionTreeClassifier(criterion="entropy", max_depth= n, random_state= 0)
    dtc.result = dtc.fit(x_train, y_train)
    y_pred = dtc.predict(x_test)
    scores = cross_val_score(dtc, x, y, cv=5)
    cv_m = np.mean(scores)
    d[n]=cv_m
    
from matplotlib import pyplot as plt

pos = np.arange(len(d.keys()))
width = 1.0

ax = plt.axes()
ax.set_xticks(pos + (width/2))
ax.set_xticklabels(d.keys())

plt.bar(d.keys(), d.values(), color = 'g')


# ### 2) Criterion = gini

# In[21]:


for n in nums_d: 
    dtc = DecisionTreeClassifier(criterion="gini", max_depth= n, random_state= 0)
    scores = cross_val_score(dtc, x, y, cv=5)
    print(n, ":", np.mean(scores))


# #### - Evaluation of Decision Tree at max_depth = 14 with entropy

# + Precision, recall, f1-score 

# In[22]:


dtc = DecisionTreeClassifier(criterion = "entropy", max_depth = 5, random_state= 0)
dtc.result = dtc.fit(x_train, y_train)
y_pred_d = dtc.predict(x_test)


# In[23]:


print(metrics.classification_report(y_test, y_pred_d))


# + Accuracy score

# In[24]:


metrics.accuracy_score(y_test, y_pred_d)


# + Confusion matrix 

# In[25]:


metrics.confusion_matrix(y_test, y_pred_d)


# In[26]:


cfm = pd.DataFrame(metrics.confusion_matrix(y_test, y_pred_d))
cfm.index.name = "True"
cfm.columns.name = "Predicted"
cfm


# In[27]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.heatmap(cfm, annot=True, cmap="Blues")
plt.show()


# In[28]:


from sklearn.tree import plot_tree

dtc = DecisionTreeClassifier(criterion = "entropy", max_depth = 3, random_state = 0)
dtc.result = dtc.fit(x_train, y_train)

class_names = wines_d["style"].value_counts().keys().tolist()
plt.figure(figsize=(50, 20))
plot_tree(dtc.result, feature_names = x.columns, class_names = class_names, filled=True)

plt.show()


# ## 1-2. Random Forest

# ### 1) Criterion = entropy

# In[29]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import numpy as np


# In[30]:


nums_r = range(2, 35)


# In[31]:


for n in nums_r:
    rfc = RandomForestClassifier(criterion="entropy", n_estimators=n, random_state=0)
    scores = cross_val_score(rfc, x, y, cv=5)
    print(n,":",np.mean(scores))


# ### 2) Criterion = gini

# In[32]:


for n in nums_r:
    rfc = RandomForestClassifier(criterion="gini", n_estimators=n, random_state=0)
    scores = cross_val_score(rfc, x, y, cv=5)
    print(n,":",np.mean(scores))


# #### - Evaluation

# In[33]:


rfc = RandomForestClassifier(criterion="gini", n_estimators = 29, random_state=0)
rfc.fit(x_train, y_train)
y_pred_r = rfc.predict(x_test)


# + Accuracy score

# In[34]:


metrics.accuracy_score(y_test, y_pred_r)


# #### - Feature Importance

# In[35]:


fi = rfc.feature_importances_


# In[36]:


pd.DataFrame(fi,index = x.columns, columns=["Feature Importance"])


# In[37]:


from sklearn.preprocessing import StandardScaler


# In[38]:


scaler = StandardScaler()


# In[39]:


scaler.fit(x)


# ## 1-3. Neural Network

# ### Scaling

# In[40]:


scaled_x = scaler.transform(x)
scaled_x_train = scaler.transform(x_train)
scaled_x_test = scaler.transform(x_test)


# - Relu Function

# In[41]:


from sklearn.neural_network import MLPClassifier
from sklearn import metrics
from sklearn.model_selection import cross_val_score
import numpy as np


# In[42]:


for n in range(2, 25):
    model = MLPClassifier(activation = "relu", hidden_layer_sizes = (n), max_iter = 1500, random_state = 0)
    scores = cross_val_score(model, scaled_x, y, cv = 5)
    print(n, ":", np.mean(scores))


# In[43]:


import itertools
a = b = (5, 10, 15)
abs = list(itertools.product(a, b))
for ab in abs:
    model = MLPClassifier(activation = "relu", hidden_layer_sizes = ab, max_iter = 1500, random_state = 0)
    scores = cross_val_score(model, scaled_x, y, cv = 5)
    print(ab, ":", np.mean(scores))


# ## 1-4. Support 

# ### 1) SVM models without parameter tuning

# In[44]:


from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
import numpy as np


# #### - Linear SVM

# In[45]:


model = SVC(kernel = "linear", random_state = 0)
score = cross_val_score(model, scaled_x, y, cv = 5)
print("linear", ":", np.mean(score))


# #### - Nonlinear SVM

# In[46]:


ks = ["poly", "rbf", "sigmoid"]


# In[47]:


for k in ks:
    model = SVC(kernel = k, random_state = 0)
    score = cross_val_score(model, scaled_x, y, cv = 5)
    print(k, ":", np.mean(score))


# ### 2) SVM models with parameter tuning

# In[48]:


from sklearn.model_selection import GridSearchCV


# In[49]:


C_range = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1]
gamma_range = ['auto', 'scale']


# In[50]:


param = dict(gamma = gamma_range, C = C_range)
param


# #### - Linear SVM

# In[51]:


for c in C_range:
    model = SVC(kernel = "linear", C = c, random_state = 0)
    score = cross_val_score(model, scaled_x, y, cv = 5)
    print(c, ":", np.mean(score))


# #### - Nonlinear SVM

# In[52]:


for k in ks:
    grid = GridSearchCV(SVC(kernel = k, random_state = 0), param_grid = param, cv = 5)
    grid.fit(scaled_x, y)
    print(k, ":", grid.best_params_, grid.best_score_)


# ## 1-5. Naive

# In[53]:


from sklearn.naive_bayes import GaussianNB


# In[54]:


nb = GaussianNB()


# In[55]:


nb.fit(scaled_x_train, y_train)


# In[56]:


y_pred = nb.predict(scaled_x_test)


# In[57]:


from sklearn import metrics


# In[58]:


metrics.accuracy_score(y_test, y_pred)


# #### - Cross Validation

# In[59]:


np.mean(cross_val_score(nb, scaled_x, y, cv=5))


# ## 1-6. KNN

# #### - Decide the most optimal number of n_neighbors with Cross Validation

# In[60]:


from sklearn.neighbors import KNeighborsClassifier


# In[61]:


nums = (1, 3, 5, 7, 9)


# In[62]:


for n in nums:
    knn = KNeighborsClassifier(n_neighbors = n)
    scores = cross_val_score(knn, scaled_x, y, cv=5)
    print(n,":",np.mean(scores))


# #### - Evaluation

# In[63]:


knn = KNeighborsClassifier(n_neighbors = 9)


# In[64]:


knn.fit(scaled_x_train, y_train)


# In[65]:


y_pred=knn.predict(scaled_x_test)


# + Accuracy score

# In[66]:


metrics.accuracy_score(y_test, y_pred)


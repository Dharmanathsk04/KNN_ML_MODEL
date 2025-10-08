from sklearn.neighbors import KNeighborsClassifier


x = [[1,8],[2,7],[3,6],[4,5],[5,4]]

y = [0,0,1,1,1]

model = KNeighborsClassifier(n_neighbors=3)


model.fit(x, y)

print(model.predict([[3,5]]))

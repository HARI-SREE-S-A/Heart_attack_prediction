data = ()
data_list = np.asarray(data)
reshaped = data_list.reshape(1,-1)
prediction = model.predict(reshaped)

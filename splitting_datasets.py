features = heartdata.drop(columns = 'Heart Disease',axis = 1)
target = heartdata['Heart Disease']
features_train,features_test,target_train,target_test = train_test_split(features,target,test_size = 0.20,stratify = target,random_state = 2) 

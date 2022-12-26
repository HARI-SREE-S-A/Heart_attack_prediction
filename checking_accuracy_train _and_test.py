//training accuracy
train_pred = model.predict(features_train)
train_accuracy = accuracy_score(train_pred,target_train)

//test accuracy

test_pred = module.predict(features_test)
test_accuracy = accuracy_score(test_pred,target_test)

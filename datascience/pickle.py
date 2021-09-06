import pickle

#assuming the variable model to be our trained classifier
model = "trained_classifier"

#we open a file which will use to save our trained model
with open('classifier.pickle', 'wb') as f:
	pickle.dump(model, f)

#to load the trained model from file without doing the time consuming training
pickle_in = open('classifier.picle', 'rb')
model = pickle.load(pickle_in)
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import LinearSVC
import joblib

def startLearning(lang, data):
    texts = data['text'].astype(str)
    y = data['is_offensive']

    # Vectorize the text
    vectorizer = CountVectorizer(stop_words='english', min_df=0.0001)
    X = vectorizer.fit_transform(texts)

    # Train the model
    model = LinearSVC(class_weight="balanced", dual=False, tol=1e-2, max_iter=1e5)
    cclf = CalibratedClassifierCV(base_estimator=model)
    cclf.fit(X, y)

    # Save the model
    joblib.dump(vectorizer, lang + '/vectorizer.joblib')
    joblib.dump(cclf, lang + '/model.joblib')


# Read in data
#data_en = pd.read_csv('./corpus/offensive-language.csv')
data_am = pd.read_csv('./corpus/profanity_am.csv')

#print("English")
#startLearning('en', data_en)
print("Amharic")
startLearning('am', data_am)
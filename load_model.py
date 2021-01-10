import numpy as np
import joblib

def _get_profane_prob(prob):
  return prob[1]

def predict(lang, texts):
  vectorizer = joblib.load(lang + '/vectorizer.joblib')
  model = joblib.load(lang + '/model.joblib')
  return model.predict(vectorizer.transform(texts))

def predict_prob(lang, texts):
  vectorizer = joblib.load(lang + '/vectorizer.joblib')
  model = joblib.load(lang + '/model.joblib')
  return np.apply_along_axis(_get_profane_prob, 1, model.predict_proba(vectorizer.transform(texts)))
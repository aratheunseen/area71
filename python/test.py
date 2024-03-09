import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
english_stopwords = stopwords.words("english")
english_stopwords[:5]
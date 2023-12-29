Machine Learning Model to classify real vs fake voices

Sounds initialy preprocessed using librosa library:
  - Audio processing.ipynb: code used to process the original audio database from kaggle : https://www.kaggle.com/datasets/birdy654/   deep-voice-deepfake-voice-recognition
  - First_model.ipynb : Started with an XGboost model. After optimizing the parameter we tested it on voices the model wasnt trained on.
  - Extract_train_features_ASVS (1).ipynb : We explored expanding the model Database by adding the audio from ASVS 2019 : https://www.asvspoof.org/index2019.html. This notebook was the code used to extract the features from the folder and add the labels.
  -XGboost - Teapot and tpot.ipynb: We added extra real voice sounds from youtube and retrained the XGboost model. We trained a new model after adding the ASVS database. We dropped that last database because it added too much noise (the sound clips had too much gaps without sounds). We did the same process using Teapot. The XGboost model had higher precision score.


api folder:
The API is hosted on GCP.
I used uvicorn and FastAPI.

interface folder:
website hosted with Streamlit :

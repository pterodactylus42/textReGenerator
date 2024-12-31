FROM tensorflow/tensorflow 

RUN pip install nltk && pip install flask==2.1.3 && pip install werkzeug==2.3.7 && pip install flask-cors

ADD predict.py /predict.py
ADD etah-murr.txt /etah-murr.txt
ADD word_to_int.etah.pickle /word_to_int.etah.pickle
ADD int_to_word.etah.pickle /int_to_word.etah.pickle
ADD etah.keras /etah.keras

CMD ["python","/predict.py"]

#todo move adds to single ADD archive

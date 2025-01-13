# textReGenerator

Originally this was intended to transcribe podcasts in order to be able to feed neural networks to regenerate similar content.

Due to missing quality of the obtained text sources from the transcriptions, this has turned into a text generation Project that relies on written text sources.

The provided notebooks create a model from a content source which can be used for text predictions.

The project includes a simple website which visualizes predictions. The site can be deployed on a docker host. You need to choose the basic text and train the model yourself.

The nginx container runs as server for the site.
The predictor container contains the model.

![Bild](https://github.com/user-attachments/assets/78be84e4-45b6-47bb-a371-7598aac6c591)

For documentation take a look into the readme files in the shared/container subdirs.

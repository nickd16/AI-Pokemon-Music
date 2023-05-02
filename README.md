This project uses transformer encoder blocks to predict next notes in a sequence. This model was trained on pokemon music from generations I and IV and was able to recreate pokemon music as well as create originals. 

Music sequences were in the form of MIDI files and were parsed using the "pretty midi" library. The parsing of the notes using this library was inspired by Tensorflow's documentation on LSTM music. 

To make the model successful, I created a vocabulary that was an arrangement of 128 notes, 8 different durations, and 8 different note steps. The total size of the vocabulary was 8192 and then the sequences of notes were tokenized based on this metric so the network could learn embeddings for the 8192 different tokens. 

The actual transformer model used just a single encoder block with the feed forwward network size being 1024/2048. This was just because it was too computationally expensive for my computer to train a larger network. The transformer also uses the noam learning rate scheduler from the "Attention is all you need" paper with warmpup_steps = 4000. 

The largest limitation of the network was that most of the pokemon music especially the later generation music featured many different instruments and the model only used an acoustic grand piano. It would have been better to have the network learn which notes are being played on which instruments but that would have exponentially raised the time it would take to train. 

RESULTS:

Gen 1 original made by the transformer:


https://user-images.githubusercontent.com/108239710/235576536-e93337b4-07a7-4353-aa5b-4fc24f0187e0.mp4


https://soundcloud.com/nick-disalvo-979346533/transformer-gen-i-original?si=9195ac6bfbeb4340b25e09e168d753ec&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing


Gen IV original made by the transformer:


https://user-images.githubusercontent.com/108239710/235576556-2eac1122-1430-4bd3-96f3-d4ce4c7b76c8.mp4


https://soundcloud.com/nick-disalvo-979346533/transformer-gen-iv-original?si=7119ab7ab970450aa475851281da07e8&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing


Additionally, here are some noteable songs the model learned well you may recognize if you have played pokemon before:

Gen I - S.S. Anne
https://soundcloud.com/nick-disalvo-979346533/s-s-anne?si=d6dbed5a16c54d7abdceee9dd4421bca&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

Gen IV - Route 201
https://soundcloud.com/nick-disalvo-979346533/route-201?si=8f950f5fe3da4bcd84041d28f42210d4&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

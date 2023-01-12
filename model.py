import tensorflow as tf
from tensorflow import keras
from keras import layers

class EncoderBlock(layers.Layer):
    def __init__(self, key_dim, dense_dim, num_heads, name):
        super(EncoderBlock, self).__init__()
        self.attention = layers.MultiHeadAttention(num_heads=num_heads, key_dim=key_dim, dropout=0.1, name = name)
        self.Ln1 = layers.LayerNormalization()
        self.drop1 = layers.Dropout(0.1)
        self.dense = keras.Sequential( [layers.Dense(dense_dim, activation='relu', name = name + '1'), layers.Dense(key_dim, name = name + '2')] )
        self.drop2 = layers.Dropout(0.1)
        self.Ln2 = layers.LayerNormalization()
        self.drop3 = layers.Dropout(0.1)
        
    def call(self, inputs):
        x = self.attention(query=inputs,value=inputs,key=inputs,use_causal_mask=True) 
        res1 = self.Ln1(x + inputs)
        x = self.drop1(res1)
        x = self.dense(x)
        x = self.drop2(x)
        x = self.Ln2(x + res1)
        x = self.drop3(x)
        return x

class InputEmbedding(layers.Layer):
    def __init__(self, seq_length, vocab_size, embed_dim, name):
        super(InputEmbedding, self).__init__()
        self.token_embeddings = layers.Embedding(input_dim=vocab_size, output_dim=embed_dim, name = name)
        self.position_embeddings = layers.Embedding(input_dim=seq_length, output_dim=embed_dim, name = name)
        self.seq_length = seq_length
        self.vocab_size = vocab_size
        self.embed_dim = embed_dim
    
    def call(self, inputs):
        positions = tf.range(start=0, limit=self.seq_length, delta=1)
        tok_embeddings = self.token_embeddings(inputs)
        pos_embeddings = self.position_embeddings(positions)
        return tok_embeddings + pos_embeddings
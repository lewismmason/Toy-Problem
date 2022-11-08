# Testing for the network stuff

def main():
    length = 122

    input = keras.Input(shape=(length,))
    x = layers.Dense(30, activation='relu')(input)
    output = layers.Dense(3,activation='relu')(x)

    model = keras.Model(input, output, name='test')
    model.compile(optimizer = keras.optimizers.Adam(learning_rate = 1e-3),
            loss = keras.losses.BinaryCrossentropy())
    model.summary()

    num_samples = 20

    data_in = np.random.random(size=[num_samples,length])
    data_val = keras.utils.to_categorical(np.random.randint(3,size=num_samples))

    history = model.fit(data_in, data_val, validation_split=0.2,
                epochs = 1000, batch_size = 64)

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.legend(['training loss','val loss'])
    plt.show()


if __name__ == "__main__":
    import numpy as np
    import tensorflow as tf
    import keras
    from keras import layers
    import matplotlib.pyplot as plt
    main()
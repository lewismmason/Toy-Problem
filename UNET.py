# Testing for the network stuff

def main():
    length = 122
    width = 29
    depth = 14

    input = keras.Input(shape=(length,width,depth,1))
    x = layers.Conv3D(16, 3, activation='relu')(input)
    
    x = layers.Reshape(((length-2)*(width-2)*(depth-2)*16,))(x)
    x = layers.Dense(30, activation='relu')(x)
    output = layers.Dense(3,activation='relu')(x)

    model = keras.Model(input, output, name='test')
    model.compile(optimizer = keras.optimizers.Adam(learning_rate = 1e-5),
            loss = keras.losses.BinaryCrossentropy())
    model.summary()

    num_samples = 200

    data_in = np.random.randint(10, size=[num_samples,length,width,depth])/10
    data_val = keras.utils.to_categorical(np.random.randint(3,size=num_samples))

    history = model.fit(data_in, data_val, validation_split=0.2,
                epochs = 10, batch_size = 32)

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
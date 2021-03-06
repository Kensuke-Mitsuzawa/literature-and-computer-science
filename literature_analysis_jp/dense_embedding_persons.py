#! -*- coding: utf-8 -*-
# keras
from keras.models import Sequential
from keras.layers.convolutional import Conv1D
from keras.layers.pooling import MaxPool1D
from keras.optimizers import Adam
from keras.layers.core import Dense, Activation, Dropout, Flatten
from keras.utils import np_utils

import logging
logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)

"""

"""


def cnn_auto_encoder():
    """"""
    pass





def test_function_cifar10():
    """Kerasの実行テストのためにcifar10で分類タスクを実行する"""
    from keras.datasets import cifar10
    from keras.utils import plot_model
    from keras.layers.convolutional import Conv2D
    from keras.layers.pooling import MaxPool2D

    nb_classes = 10

    (X_train, y_train), (X_test, y_test) = cifar10.load_data()

    # floatに型変換
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    # 各画素値を正規化
    X_train /= 255.0
    X_test /= 255.0

    Y_train = np_utils.to_categorical(y_train, nb_classes)
    Y_test = np_utils.to_categorical(y_test, nb_classes)

    # モデルの定義
    model = Sequential()

    model.add(Conv2D(32, 3, input_shape=(32, 32, 3)))
    model.add(Activation('relu'))
    model.add(Conv2D(32, 3))
    model.add(Activation('relu'))
    model.add(MaxPool2D(pool_size=(2, 2)))

    model.add(Conv2D(64, 3))
    model.add(Activation('relu'))
    model.add(MaxPool2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(1024))
    model.add(Activation('relu'))
    model.add(Dropout(1.0))

    model.add(Dense(nb_classes, activation='softmax'))
    adam = Adam(lr=1e-4)
    model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=["accuracy"])
    history = model.fit(X_train, Y_train, batch_size=3, nb_epoch=100, verbose=1, validation_split=0.1)

    # モデルをプロット
    plot_model(model, to_file='./model2.png')


if __name__ == '__main__':
    test_function_cifar10()
from ann_util import make_matrix  # Make an N rows by M columns Matrix
from ann_util import between  # Return a real random value between min and max


use_bias = 1


class ANN:
    # representing Artifical Neural Network
    # will have couple of layers
    def __init__(self):
        pass

    def train(self):
        pass

    def predict(self):
        pass

    def update_weights(self):
        pass




class Layer:
    # representing a single layer of Neurons
    # collection of Neurons
    def __init__(self, id, layer_size, prev_layer_size):

        self.id = id  # for debugging purposes
        self.n_neurons = layer_size # number of neurons that will be given as parameter
        self.bias_val = 1  # is bias value the number we add or subtract by 1?

        self.input = [0] * self.n_neurons # as big as number of neurons is has

        self.output = [0] * (self.n_neurons + use_bias) # use_bias is defined on top as 1
        self.output[0]  = self.bias_val

        self.error = [0] * self.n_neurons

       # layer will connect to layer infront of it using weight matrix
    # synapsis between previous layer and new layer
        self.weight = make_matrix(prev_layer_size + use_bias, self.n_neurons)
        for i in range(len(self.weight)):  # initializing to weight to small values
            for j in range(len(self.weight[i])):
                self.weight[i][j] = between (- 0.2, 0.2)




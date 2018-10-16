import numpy as np
import sklearn.datasets
import sklearn.linear_model

def sigmoid(x_dot_weight):
    #return predict value
    predict_output = 1.0/(1 + np.exp(-x_dot_weight))

    return predict_output, x_dot_weight

def activation():


def forward_propagation(layer_input):
    cache = []

    prev_layer_output = layer_input

    #layer start from 0
    for l in range(1, 3):
        current_layer_input = prev_layer_output

        current_layer_output = activation(current_layer_input)


def nn_train(layer_input):
    for i in range(0, 30000):
        layer_output, cache = forward_propagation(layer_input)

class NeutralNetwork:
    def __init__(self, layers_structure):
        self.layers_structure = layers_structure
        self.layer_num        = len(layers_structure)
        self.learning_rate    = 0.0618
        self.num_iterations   = 2000 
        self.x                = None
        self.y                = None
        self.w                = dict()
        self.b                = dict()
        self.costs            = []
        self.init_w_b()

    def set_learning_rate(self, learning_rate):
        self.learning_rate = learning_rate
    
    def set_num_iterations(self, num_iterations)
        self.num_iterations = num_iterations
    
    def set_xy(self, input, expected_value):
        self.x = input
        self.y = expected_value

    def init_w_b(self):
        for layer in range(1, self.layer_num):
            self.w[] = np.random.radn()
            self.b[]




if __name__ == '__main__':
    
    xy, colors = sklearn.datasets.make_moons(60, noise=1.0)

    expect_output = []

    for c in colors:
        if c == 1:
            expect_output.append([0,1])
        else:
            expect_output.append([1,0])
    
    expect_output = np.array(expect_output).T

    print(expect_output)
  

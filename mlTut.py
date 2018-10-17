import numpy as np
import sklearn.datasets
import sklearn.linear_model

def sigmoid(x_dot_weight):
    #return predict value
    predict_output = 1.0/(1 + np.exp(-x_dot_weight))

    return predict_output, x_dot_weight

class NeutralNetwork:
    def __init__(self, layers_structure):
        self.layers_structure = layers_structure
        self.layer_num        = len(layers_structure)
        self.param_layer_num  = self.layer_num - 1
        self.learning_rate    = 0.0618
        self.num_iterations   = 2000 
        self.x                = None
        self.y                = None
        self.w                = dict()
        self.b                = dict()
        self.costs            = []
        self.init_w_b()

        print("Netrual Network layer = %d" % self.layer_num)

    def set_learning_rate(self, learning_rate):
        self.learning_rate = learning_rate

        print("set learning rate @ %d" % learning_rate)
    
    def set_num_iterations(self, num_iterations):
        self.num_iterations = num_iterations

        print("set training iteration = %d" %num_iterations)
    
    def set_xy(self, input, expected_value):
        self.x = input
        self.y = expected_value

    def init_w_b(self):
        np.random.seed(3)

        for layer in range(1, self.layer_num):
            self.w["w" + str(layer)] = np.random.randn(self.layers_structure[layer], self.layers_structure[layer - 1])/np.sqrt(self.layers_structure[layer-1])
            self.b["b" + str(layer)] = np.zeros((self.layers_structure[layer], 1))      
    
    def layer_activation_forward(self, x, w, b):

        input_sum = np.dot(w, x) + b
        output    = sigmoid(input_sum)

        return output, (x, w, b, input_sum)
    
    def compute_error(self, output):
        
        m = self.y.shape[1]

        error = -np.sum(np.multiply(np.log(output), self.y) + np.multiply(np.log(1 - output), 1 - self.y))/m

        print(error)

        return total_error

    def forward_propagation(self, x):
        caches            = []
        output_prev_layer = x

        num_of_param_layer = self.param_layer_num

        #caculate prediction
        for layer_index in range(1, num_of_param_layer):
            input_current_layer = output_prev_layer
            output_prev_layer, cache = self.layer_activation_forward(input_current_layer, self.w["w" + str(layer_index)], self.b["b" + str(layer_index)])
            caches.append(cache)

        output, cache = self.layer_activation_forward(output_prev_layer,  self.w["w" + str(num_of_param_layer)], self.b["b" + str(num_of_param_layer)])
        caches.append(cache)

        return output, caches

    def training_model(self):
        np.random.seed(5)

        for i in range(0, self.num_iterations):
            output, caches = self.forward_propagation(self.x)

            cost           = self.compute_error(output)
           


if __name__ == '__main__':
    
    xy, colors = sklearn.datasets.make_moons(60, noise=1.0)

    expect_output = []

    hidden_layer_neuron_num_list = [1, 2, 4, 10, 20, 50]

    for c in colors:
        if c == 1:
            expect_output.append([0,1])
        else:
            expect_output.append([1,0])
    # [2, 4, 2]
    expect_output = np.array(expect_output).T

    nn = NeutralNetwork([2, hidden_layer_neuron_num_list[2], 2])

    nn.set_xy(xy.T, expect_output)
    nn.set_learning_rate(0.1)
    nn.set_num_iterations(100000)

    nn.training_model()
  

   

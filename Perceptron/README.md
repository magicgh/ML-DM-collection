# Perceptron
## Task
>Consider the following prototype patterns.  
><img src="https://i.loli.net/2020/04/06/43UdKOtx5aFuXVl.png">  <br>
>Find weights and bias which will produce the decision boundary you
>found in part i, and sketch the network diagram.

<div align=right>(NNDesign 2nd Edition : E3.2 ii.)</div>

## Test Questions
* Q1: The evolution of neuron from biology to mathematics?  
  &emsp;&emsp;From a neuronal synaptic model to a nonlinear function whose output is the input superimposed with multiple incoming pulses.  
  <center>

  |Biological Neuron|Artificial Neuron|
  |:----:|:----:|
  |Cell Nucleus|Node|
  |Dendrites|Input|
  |Synapse|Weights or interconnections|
  |Axon|Output|
  </center>
  </br>
* Q2: The key concepts of Perceptron and its limitations.   
  &emsp;&emsp;1. Key concepts: Decision boundary, Activate function, Learning rate.   
  &emsp;&emsp;2. Limitations: Unable to solve the problem if the learning set is not linearly separable, such as XOR problem.
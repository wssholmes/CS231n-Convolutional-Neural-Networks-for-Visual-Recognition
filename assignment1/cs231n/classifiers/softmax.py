import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  for i in range(X.shape[0]):
    scores = X[i].dot(W)
    scores = scores.reshape(1,W.shape[1])
    scores -= np.max(scores)

    scores = np.exp(scores)
    scores /= np.sum(scores)
    # print(scores)
    loss -= np.log(scores[0,y[i]])

    label = np.zeros((1,W.shape[1]))
    label[0,y[i]] = 1
    x = X[i].reshape(1,X.shape[1])
    dW += x.T.dot(scores - label)
  
  loss /= X.shape[0]
  dW /= X.shape[0]

  loss += reg*np.sum(W*W)
  dW += 2*reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores = X.dot(W)
  scores -= np.max(scores, axis=1, keepdims=True)
  scores = np.exp(scores)
  scores /= np.sum(scores, axis=1, keepdims=True)

  loss = np.sum(-np.log(scores[range(X.shape[0]), y]))/X.shape[0]
  loss += reg*np.sum(W*W)

  labels = np.zeros(scores.shape)
  labels[range(X.shape[0]), y] = 1

  dW = X.T.dot(scores - labels)/X.shape[0]
  dW += 2*reg*W


  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


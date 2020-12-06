#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#
#   Find the state feedback control gain
#
def LQRGain():
    from lraClass import LRA2_HELPER
    lra = LRA2_HELPER()

    # Solve Algebric Riccati Equation
    S = lra.solveRiccati(A,B,Q,R)

    # find the gain K
    K = np.dot(np.dot(np.linalg.inv(R),np.transpose(B)),S)
    return K


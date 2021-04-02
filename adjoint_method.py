import numpy as np

n = 10
p = np.ones(n).reshape(n,1)
alpha = 0.01 #Gradient descent
delta = 0.0001 #To find partial derivatives
h = [np.array(x).reshape(n,1) for x in np.eye(n)*delta]
norm = 1
cutoff = 10**(-6)
maxIters = 10000

def A(p):
    return p @ p.T + np.eye(n)

def f(x_p):
    x_p.reshape(n,1)
    return np.sqrt(x_p.T @ x_p) # np.sqrt ?

b = np.ones(n).reshape(n,1) # Normally a function
for i in range(maxIters):
    if norm > cutoff:
        Ainv = np.linalg.inv(A(p))
        
        # Del_x f:
        x_p = Ainv @ b
        
        gradfx = np.array([(f(x_p+a)-f(x_p))/delta for a in h]).reshape(n,1)
        #gradb =  (b(p+h)-b(p))/delta
        gradb = np.zeros((n,n,1))
        gradA = np.array([(A(p+a)-A(p))/delta for a in h])
        
        
        q = gradfx.T @ Ainv
        gradg = (q @ (-gradA @ x_p + gradb)).reshape(n,1)
        p = p + alpha*gradg #Since gradient is negative
        norm = np.linalg.norm(gradg) #Complete and check with others
    
        if i % 50 == 0 :
            print(norm)
    else:
        psol = p
        break
print(psol)
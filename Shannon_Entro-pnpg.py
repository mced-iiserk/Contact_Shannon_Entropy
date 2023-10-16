import numpy as np

def countbinstr(Arr,binstr):
    # count frequency of the binary string 'binstr' in array 'Arr'
    #proddiff = np.prod(Arr==binstr,axis=0)
    #count = np.sum(proddiff)
    proddiff = len(binstr)-np.sum(Arr==binstr,axis=0)<=0
    count = np.sum(proddiff)
    idxnon0 = proddiff==0
    newArr = Arr[:,idxnon0]
    return count,newArr

def ubc(Arr):
    COM = Arr
    Ubs = np.empty((COM.shape[0],0))
    COUNT = []
    while COM.shape[1]>=1:
        bs = COM[:,0].reshape(-1,1)
        count,COM = countbinstr(COM,bs)
        COUNT.append(count)
        Ubs=np.hstack((Ubs,bs))
    return Ubs,np.array(COUNT)

comFILE = np.load('contact_matrix-pnpg-.npz')
com300K = comFILE['T300K']
com315K = comFILE['T315K']

Ubs300K, Count300K = ubc(com300K)
Ubs315K, Count315K = ubc(com315K)
Freq300K = Count300K/np.sum(Count300K)
Freq315K = Count315K/np.sum(Count315K)

SE300K = -np.sum(Freq300K*np.log(Freq300K))
SE315K = -np.sum(Freq315K*np.log(Freq315K))

sys1 = """

300K
--------------------
Unique H-bond arrangements: %d
System Entropy: %.3f
"""%(Ubs300K.shape[1],SE300K)

sys2 = """

315K
--------------------
Unique H-bond arrangements: %d
System Entropy: %.3f
"""%(Ubs315K.shape[1],SE315K)

print(sys1)
print(sys2)

#!/usr/bin/env python
# coding: utf-8

# In[8]:


def solution(A, K):
    q=len(A)
    if K<q:
        l=A[0:K-1]
        A[0:K]=A[K-1:q]
        A[K:q]=l
    if K>=q:
        K=K+1
        l=A[0:K-1]
        A[0:K]=A[K-1:q]
        A[K:q]=l
    return (A)


# In[ ]:





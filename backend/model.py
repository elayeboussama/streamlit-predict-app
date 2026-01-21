import streamlit as st
from sklearn.linear_model import LogisticRegression
import numpy as np

@st.cache_resource
def load_model():
    # Dummy trained model (for demo)
    model = LogisticRegression()
    X = np.array([[0], [1], [2], [3]])
    y = np.array([0, 0, 1, 1])
    model.fit(X, y)
    return model

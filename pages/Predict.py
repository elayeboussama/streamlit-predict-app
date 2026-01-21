import streamlit as st
import pandas as pd

from backend.model import load_model
from backend.preprocessing import preprocess
from backend.inference import predict

st.title("🔮 Prediction")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Uploaded Data")
    st.dataframe(df)

    if st.button("Run Prediction"):
        with st.spinner("Processing..."):
            X = preprocess(df)
            model = load_model()
            preds = predict(model, X)

            df["prediction"] = preds

        st.success("Prediction completed ✅")
        st.subheader("📊 Results")
        st.dataframe(df)

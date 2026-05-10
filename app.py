import streamlit as st
import pickle
import numpy as np
# Load Model
model=pickle.load(open('fraud_model.pkl','rb'))
#App title
st.title("UPI Transaction Risk Analyzer")
#Inputs
amount=st.number_input("Transcation Amount")
hour=st.slider('Transcation Hour',0,23)
status=st.selectbox(
      "Transcation Status",
      [0,1]
)
sender_bank=st.number_input(
      "Sender Bank Code"
)
receiver_bank=st.number_input(
      "Receiver Bank code"
)
#Add Day
day = st.slider(
    "Day",
    1,
    31
)
#Add Month
month = st.slider(
    "Month",
    1,
    12
)
#Add is_night
is_night = st.selectbox(
    "Night Transaction",
    [0,1]
)
#prediction
if st.button('Analyze'):
      features=np.array([
             [
            amount,
            status,
            hour,
            sender_bank,
            receiver_bank,
            day,
            month,
            is_night
        ]
      ])
      prediction=model.predict(features)
      probability=model.predict_proba(features)
      risk_score=probability[0][1]*100
      st.subheader(
            f"Risk score: {risk_score:.2f}%"
      )
      if prediction[0]==1:
            st.error("High Risk Transcation")
      else:
            st.success("Low Risk Transcation")
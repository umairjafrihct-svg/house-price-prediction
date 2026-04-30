import streamlit as st
import pickle

reg=pickle.load(open("house_pred.pkl","rb"))

st.title("House Price Prediction App!")

area=st.number_input("Input Area (in sqft)",min_value=100)
bed=st.slider("Input Bed Rooms",1,6)
location_score=st.number_input("Input Location Score",min_value=1.0)
bath_room=st.slider("Input Bath Rooms",1,4)
age=st.slider("Input age",0,50)

if st.button("Prediction Price"):
    input_data=[[area,bed,location_score,bath_room,age]]
    predicted_price=reg.predict(input_data)
    st.success(f"Estimated Selling Price:{predicted_price[0]}")



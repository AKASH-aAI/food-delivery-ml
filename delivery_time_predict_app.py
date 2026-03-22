import streamlit as st 
import joblib 
import pandas as pd 

# load model + columns 
model = joblib.load('model.pkl')
columns = joblib.load('columns.pkl')



# Title
st.title("🚚 Food Delivery Time Predictor")


# user inputs 
distance = st.number_input('Enter distance in KM',min_value=0.0,step=0.5)
traffic = st.selectbox('Enter Traffic Level ',['Low','Medium','High'])
weather = st.selectbox('Enter Weather',["Clear", "Rainy", "Foggy", "Windy", "Snowy"])
vehicle = st.selectbox('Enter Vehicle' , ['Bike','Car','Scooter'])
daytime = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])

# predict button 
if st.button("🚀 Predict Now"):
    if (distance<=0):
        st.success('Estimated Delivery Time : 0 minutes ')

    # create input dataframe 
    else : 
        input_data = pd.DataFrame({
            'Distance_km':[distance],
            'Traffic_Level':[traffic],
            'Weather':[weather],
            'Vehicle_Type':[vehicle],
            'Time_of_Day':[daytime]
            })

        # encoding 
        input_data = pd.get_dummies(input_data)
        # match training columns 
        input_data = input_data.reindex(columns=columns, fill_value=0)
        # prediction 
        prediction = model.predict(input_data)
        # output 
        st.success(f'Estimated Delivery Time : {prediction[0]:.2f} minutes ')

st.markdown("---")
st.write("Enter details and get estimated delivery time instantly!")

import pandas as pd
df = pd.read_csv("cleaned_food_delivery_times.csv")
df = df.sort_values(by='Distance_km')
st.line_chart(df.set_index('Distance_km')['Delivery_Time_min'])
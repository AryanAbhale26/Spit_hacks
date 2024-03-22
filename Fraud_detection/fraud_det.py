import streamlit as st
import joblib
import pandas as pd

# Load the saved models
logreg_model = joblib.load('logistic_regression_model.pkl')
dt_model = joblib.load('decision_tree_model.pkl')
rf_model = joblib.load('random_forest_model.pkl')
gb_model = joblib.load('gradient_boosting_model.pkl')

# Define a function to make predictions
def predict(model, data):
    return model.predict(data)

# Create the Streamlit app
def main():
    # Inject custom CSS to set background image
   with open('llm.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.title('Online Payments Fraud Detection')

    st.sidebar.title('Predictions')
    st.sidebar.write('### Input Features:')
    # Get input features from user
    amount = st.sidebar.number_input('Amount')
    oldbalanceOrg = st.sidebar.number_input('Old Balance of Origin')
    newbalanceOrig = st.sidebar.number_input('New Balance of Origin')
    oldbalanceDest = st.sidebar.number_input('Old Balance of Destination')
    newbalanceDest = st.sidebar.number_input('New Balance of Destination')

    # Create a dataframe with the input features
    input_data = pd.DataFrame({
        'step': [1],  # Fixed step as 1
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest],
        'type_CASH_OUT': [0],
        'type_DEBIT': [0],
        'type_PAYMENT': [0],
        'type_TRANSFER': [1]  # Fixed type as TRANSFER
    })

    # Make predictions
    if st.sidebar.button('Predict'):
        st.write('### Predictions:')
        st.write('Logistic Regression Model:')
        logreg_prediction = predict(logreg_model, input_data)
        st.write("Fraud Detected" if logreg_prediction[0] == 1 else "No Fraud Detected")

        st.write('Decision Tree Classifier Model:')
        dt_prediction = predict(dt_model, input_data)
        st.write("Fraud Detected" if dt_prediction[0] == 1 else "No Fraud Detected")

        st.write('Random Forest Classifier Model:')
        rf_prediction = predict(rf_model, input_data)
        st.write("Fraud Detected" if rf_prediction[0] == 1 else "No Fraud Detected")

        st.write('Gradient Boosting Classifier Model:')
        gb_prediction = predict(gb_model, input_data)
        st.write("Fraud Detected" if gb_prediction[0] == 1 else "No Fraud Detected")

if __name__ == '__main__':
    main()

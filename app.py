import streamlit as st
import pandas as pd
import joblib as jb
import numpy as np

df = pd.read_csv('1662574418893344.csv')
recommender = jb.load('result_recommender.joblib')
rating_matrix = pd.read_csv('rating_matrix.csv')

# The main recommender code!
def Get_Recommendations(title):
    user= df[df['Name']==title]
    user_index = np.where(rating_matrix.index==int(user['Food_ID']))[0][0]
    user_ratings = rating_matrix.iloc[user_index]

    reshaped = user_ratings.values.reshape(1,-1)
    reshaped = reshaped[0][1:]
    reshaped = np.array([reshaped])
    distances, indices = recommender.kneighbors(reshaped,n_neighbors=16)
    
    nearest_neighbors_indices = rating_matrix.iloc[indices[0]].index[1:]
    nearest_neighbors = pd.DataFrame({'Food_ID': nearest_neighbors_indices})
    
    result = pd.merge(nearest_neighbors,df,on='Food_ID',how='left')
    
    return result.head()


st.title('Sistem Rekomendasi 🍴')
st.header('Menggunakan algoritma TF-IDF dan Cosine Similarities', divider='grey')

user_input = st.text_input('Nama Makanan', placeholder='Masukan Nama Makanan yang diinginkan')

user_input = user_input.lower()

if 'output' not in st.session_state:
    st.session_state.output = ''

def btn_action():
    try:
        st.session_state.output = Get_Recommendations(user_input)
    except:
        st.session_state.output = 'Makanan tidak tidak ditemukan'

st.button('submit', on_click=btn_action)
st.write(st.session_state.output)
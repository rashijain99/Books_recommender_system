import streamlit as st
import pickle
import numpy as np
import sklearn
from sklearn.neighbors import NearestNeighbors

booksname = pickle.load(open('booksname.pkl','rb'))
bookpivot = pickle.load(open('bookpivot.pkl','rb'))
model = pickle.load(open('final_model.pkl','rb'))
booksinfo = pickle.load(open('booksinfo.pkl','rb'))


def recommendation(name):
    book_id = np.where(bookpivot.index == name)[0][0]
    distances, suggestions = model.kneighbors(bookpivot.iloc[book_id, :].values.reshape(1,-1), n_neighbors=7)
    
    for i in range(len(suggestions)):
        # if i == 0:
        #     print("The suggestions are:")
        if not i:
            var = bookpivot.index[suggestions[i]]
            recommended_books = var.to_list()

    return recommended_books        


st.title('Books Recommender System')
selected_book_name = st.selectbox(
     'Select book name',
     booksname)

st.write('You selected:', selected_book_name)

if st.button('Recommend Books'):
    name = recommendation(selected_book_name)

    col1 , col2 = st.columns(2)
    with col1:
        st.subheader(name[0])
        imgcol1 = booksinfo[booksinfo['Book-Title']==name[0]].values[0][1]
        st.image(imgcol1)

    with col2:
        st.subheader(name[1])
        imgcol2 = booksinfo[booksinfo['Book-Title']==name[1]].values[0][1]
        st.image(imgcol2)


    col3, col4 = st.columns(2)
    with col3:
        st.subheader(name[2])
        imgcol3 = booksinfo[booksinfo['Book-Title']==name[2]].values[0][1]
        st.image(imgcol3)

    with col4:
        st.subheader(name[3])
        imgcol4 = booksinfo[booksinfo['Book-Title']==name[3]].values[0][1]
        st.image(imgcol4)


    col5 ,col6 = st.columns(2)
    with col5:
        st.subheader(name[4])
        imgcol5 = booksinfo[booksinfo['Book-Title']==name[4]].values[0][1]
        st.image(imgcol5)

    with col6:
        st.subheader(name[5])    
        imgcol6 = booksinfo[booksinfo['Book-Title']==name[5]].values[0][1]
        st.image(imgcol6)
       



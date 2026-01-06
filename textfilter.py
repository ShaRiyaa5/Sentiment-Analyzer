import streamlit as st #for designing - pip install streamlit (use this command in terminal to install python packages), st short form
from textblob import TextBlob #for texting - pip install textblob (TextBlob is a part of textblob the whole thing)

#textblob - corrects the incorrect text to a correct one
#tailwind CSS, Bootstrap - instead of using CSS we can use this to design faster

st.title("Sentiment Analyzer")
st.subheader("Customer Review Intelligence")
user_text = st.text_area("Enter your feedback", height=150) #getting input from the user
if st.button("Check result"):
    if user_text:
        blob = TextBlob(user_text)
        score = blob.sentiment.polarity #polarity - is to get the score that'll range from -1 to 1
        if(score>0):
            st.success(f"Positive feedback... Score = {score:.2f}") #:.2f - float identifier, to have 2 decimal values
            st.balloons()
        elif(score<0):
            st.error(f"Negative feedback... Score = {score:.2f}")
        elif(score == 0):
            st.warning(f"Neutral feedback... Score = {score:.2f}")
        else:
            st.error("Error")
    else:
        st.warning("Enter your review to check result")
else:
    st.write("Type something")
st.sidebar.title("About")
st.sidebar.info("This app use NLP to analyze text emotions")

# streamlit run filename.py - type this command in your terminal to run this project
# if this doesn't work then we can use, python -m streamlit run filename.py
# These are to run the file in your browser using Local URL and Network URL.
# If you wish to deploy this code, then we have to create another text file named requirements.txt
# We have to add the library names that are used in this code
# eg: here we used streamlit and textblob, so we need to write these two libraries in that txt file
# make sure of its spelling CAPS small and especially the file name requirements.txt
# even if you name it as requirement.txt you'll get an error
# now create a new repository in Github and upload these two files in that repository i.e., code file and requirements
# then google share.streamlit, you'll be taken to share.streamlit.io
# login to that website using your github account
# now you'll have create app option at the top right corner
# you'll have 3 options to deploy. select Deploy a public app from GitHub
# make sure to fill all the required fields and click deploy
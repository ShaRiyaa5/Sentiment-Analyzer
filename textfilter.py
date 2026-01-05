import streamlit as st #for designing
from textblob import TextBlob #for texting

#textblob - corrects the incorrect text to a correct one
#tailwind CSS, Bootstrap - instead of using CSS we can use this to design faster

st.title("Sentiment Analyzer")
st.subheader("Customer Review Intelligence")
user_text = st.text_area("Enter your review", height = 150)
if st.button("Check result"):
    if user_text:
        blob=TextBlob(user_text)
        score=blob.sentiment.polarity
        st.write("------------------")
        if score>0:
            st.success(f"Positive Review... Score {score}")
            st.balloons()
        elif score<0:
            st.error(f"Negative Review... Score {score}")
        else:
            st.warning(f"Neutral Review... Score {score}")
else:
    st.write("Type something")
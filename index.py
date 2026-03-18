
import streamlit as st 
import requests as req 

txt=st.text_input("enter the text")

btn=st.button("submit")


if btn:
    data={
    "contents": [
      {
        "parts": [
          {
            "text": f"{txt}"
          }
        ]
      }
    ]
    }
    headers= {"x-goog-api-key":"AIzaSyD7e4Ev2dhtvaDFl3LGyG0vf9jHglGcw5Q" ,
  "Content-Type": "application/json" }
    with st.spinner("....loading"):
      res=req.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent",json=data,headers=headers)
    data=res.json()
    # st.markdown(data["candidates"][0]["content"]["parts"]["text"])
    st.markdown(data["candidates"][0]["content"]["parts"][0]["text"])
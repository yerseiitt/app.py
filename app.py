import streamlit as st
import google.generativeai as genai

# Сайттың тақырыбы мен дизайны
st.set_page_config(page_title="Физика Виртуалды Көмекшісі", page_icon="⚛️")
st.title("⚛️ Физика пәнінен виртуалды көмекші")
st.write("Сәлем! Мен физика есептерін шығаруға және заңдылықтарды түсіндіруге көмектесемін.")

# API кілтті орнату (Мұнда өз кілтіңізді қоясыз немесе Streamlit-ке жасырасыз)
API_KEY = "AIzaSyD2ny1Pk_H4Jg4dVpHxbR4LZahAEyQNoFU" 
genai.configure(api_key=API_KEY)

# Модель баптаулары (Физика мұғалімі рөлін беру)
model = genai.GenerativeModel('gemini-1.5-flash', 
                              system_instruction="Сен физика пәнінің тәжірибелі мұғалімісің. Оқушыларға есептерді түсінікті тілмен түсіндір, формулаларды көрсет және қазақ тілінде жауап бер.")

# Чат тарихын сақтау
if "messages" not in st.session_state:
    st.session_state.messages = []

# Ескі хабарламаларды көрсету
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Оқушының сұрағын қабылдау
if prompt := st.chat_input("Сұрағыңды жаз (мысалы: Ньютонның 2-заңы деген не?)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI жауабы
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
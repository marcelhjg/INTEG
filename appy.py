import streamlit as st

# 1. PAGE CONFIG
st.set_page_config(page_title="TikTok Recipe Vault", layout="wide")

# 2. CUSTOM CSS
st.markdown("""
    <style>
    .stApp { background-color: #F3E5F5; }
    .stButton>button { background-color: #CE93D8; color: white; border-radius: 10px; border: none; }
    .stSidebar { background-color: #E1BEE7; }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
st.sidebar.title("💜 Recipe Vault")
nav = st.sidebar.radio("Navigation", ["Home Page", "About App"])

# 4. HOME PAGE (MANO-MANO DISPLAY)
if nav == "Home Page":
    st.title("🍔 Trending TikTok Recipes")
    
    # Layout gamit ang columns para maganda tignan
    col1, col2, col3 = st.columns(3)

    # Dito natin ilalagay nang manual ang bawat picture
    with col1:
        st.image("image/1.png", caption="Ilocos Empanada", use_container_width=True)
        if st.button("View Empanada"): st.session_state.page = "Empanada"
        st.write("Rating: 4.8 ⭐")
        
        st.image("image/4.png", caption="Samyang Omelette", use_container_width=True)
        if st.button("View Omelette"): st.session_state.page = "Omelette"
        st.write("Rating: 4.7 ⭐")

    with col2:
        st.image("image/2.png", caption="Dubai Chewy Cookie", use_container_width=True)
        if st.button("View Cookie"): st.session_state.page = "Cookie"
        st.write("Rating: 4.9 ⭐")
        
        st.image("image/5.png", caption="Cheesy Corn", use_container_width=True)
        if st.button("View Corn"): st.session_state.page = "Corn"
        st.write("Rating: 4.6 ⭐")

    with col3:
        st.image("image/3.png", caption="Tofu Squares", use_container_width=True)
        if st.button("View Tofu"): st.session_state.page = "Tofu"
        st.write("Rating: 4.2 ⭐")
        
        st.image("image/6.png", caption="Spud", use_container_width=True)
        if st.button("View Spud"): st.session_state.page = "Spud"
        st.write("Rating: 4.4 ⭐")

    # Pang-pito na recipe
    st.image("image/7.png", caption="Tiramisu", use_container_width=True)
    if st.button("View Tiramisu"): st.session_state.page = "Tiramisu"
    st.write("Rating: 5.0 ⭐")

# 5. ABOUT PAGE
elif nav == "About App":
    st.title("ℹ️ About App")
    st.write("Isang digital recipe book para sa mga trending TikTok recipes.")
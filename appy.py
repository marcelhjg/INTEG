import streamlit as st
import os

# ==========================================
# 1. PAGE CONFIG & LIGHT PURPLE THEME
# ==========================================
st.set_page_config(page_title="TikTok Recipe Vault", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F3E5F5; }
    .stButton>button { background-color: #CE93D8; color: white; border-radius: 10px; border: none; }
    .stDownloadButton>button { background-color: #AB47BC; color: white; border-radius: 10px; width: 100%; }
    .stSidebar { background-color: #E1BEE7; }
    h1, h2, h3, h4 { color: #6A1B9A; }
    </style>
    """, unsafe_allow_html=True)

# Path setup para sa WSL/Ubuntu
current_dir = os.path.dirname(os.path.abspath(__file__))
# Siguraduhin na ang folder name mo ay "integ images" sa explorer
img_dir = os.path.join(current_dir, "integ images")

# ==========================================
# 2. DATABASE NG MGA PAGKAIN
# ==========================================
recipes = {
    "Ilocos Empanada": {
        "img": "1.png", "rating": "4.8", "emoji": "🥟",
        "link": "https://www.panlasangpinoy.com",
        "ing": ["Rice flour", "Longganisa", "Egg", "Papaya"],
        "inst": "Flatten dough, add fillings, and deep fry until crispy."
    },
    "Dubai Chewy Cookie": {
        "img": "2.png", "rating": "4.9", "emoji": "🍪",
        "link": "https://www.tiktok.com",
        "ing": ["Butter", "Flour", "Pistachio cream", "Kunafa"],
        "inst": "Mix ingredients, stuff with kunafa, and bake at 180°C."
    },
    "Tofu Squares": {
        "img": "3.png", "rating": "4.2", "emoji": "🍲",
        "link": "https://www.yummy.ph",
        "ing": ["Firm Tofu", "Cornstarch", "Soy Sauce", "Honey"],
        "inst": ["Cube tofu.", "Coat in starch.", "Air fry until golden."]
    },
    "Samyang Omelette": {
        "img": "4.png", "rating": "4.7", "emoji": "🍳",
        "link": "https://www.google.com",
        "ing": ["Samyang Noodles", "Eggs", "Cheese"],
        "inst": "Boil noodles, mix sauce, and fold into an omelette."
    },
    "Cheesy Corn": {
        "img": "5.png", "rating": "4.6", "emoji": "🌽",
        "link": "https://www.allrecipes.com",
        "ing": ["Sweet Corn", "Mozzarella", "Mayo", "Butter"],
        "inst": "Sauté corn in butter, add mayo and cheese, then melt."
    },
    "Spud": {
        "img": "6.png", "rating": "4.4", "emoji": "🥔",
        "link": "https://www.foodnetwork.com",
        "ing": ["Potato", "Cheese", "Bacon", "Sour Cream"],
        "inst": "Bake potato, mash the inside, and add toppings."
    },
    "Tiramisu": {
        "img": "7.png", "rating": "5.0", "emoji": "🍰",
        "link": "https://www.delish.com",
        "ing": ["Ladyfingers", "Espresso", "Mascarpone"],
        "inst": "Layer coffee-dipped biscuits with mascarpone cream."
    }
}

# State Management
if 'page_view' not in st.session_state:
    st.session_state.page_view = "Home"
if 'selected_food' not in st.session_state:
    st.session_state.selected_food = None

# ==========================================
# 3. SIDEBAR NAVIGATION
# ==========================================
st.sidebar.title("💜 Recipe Vault")
nav = st.sidebar.radio("Navigation", ["Home Page", "About App"])

if nav == "About App":
    st.title("ℹ️ About This App")
    st.write("**Use-Case:** Digital Recipe Book for Viral TikTok Foods.")
    st.write("**Target User:** Home cooks and students.")
    st.write("**Inputs:** Selection buttons, ratings, and feedback.")
    if st.sidebar.button("Back to Home"):
        st.session_state.page_view = "Home"
        st.rerun()

# ==========================================
# 4. MAIN INTERFACE
# ==========================================
if nav == "Home Page":
    if st.session_state.selected_food is None:
        st.title("🍔 TikTok Trending Recipes")
        
        # Grid View (3 Columns)
        cols = st.columns(3)
        for idx, (name, info) in enumerate(recipes.items()):
            with cols[idx % 3]:
                img_path = os.path.join(img_dir, info['img'])
                if os.path.exists(img_path):
                    st.image(img_path, use_container_width=True)
                else:
                    st.error(f"Image {info['img']} not found")
                
                if st.button(f"View {name}", key=name, use_container_width=True):
                    st.session_state.selected_food = name
                    st.rerun()
                st.write(f"Rating: {info['rating']} ⭐")
                st.divider()

    else:
        # RECIPE DETAIL VIEW (Katulad ng format sa screenshot 2)
        food = st.session_state.selected_food
        item = recipes[food]
        
        if st.button("⬅️ Back to Menu"):
            st.session_state.selected_food = None
            st.rerun()
            
        st.header(f"{food} {item['emoji']}")
        st.divider()
        
        # Layout with Image and Details
        col_img, col_details = st.columns([1, 2])
        
        with col_img:
            img_path = os.path.join(img_dir, item['img'])
            st.image(img_path, caption=f"Finished {food}", use_container_width=True)
            if st.button("⭐ Save to Favorites"):
                st.toast(f"{food} added to favorites!")
        
        with col_details:
            st.subheader("🛒 Ingredients")
            for ing in item['ing']:
                st.write(f"• {ing}")
                
            st.subheader("📝 Instructions")
            st.write(item['inst'])
            
            st.divider()
            # Link to Original Recipe
            st.link_button(f"🔗 View Original {food} Recipe", item['link'])
            
            # Additional UI Components (Merit Points)
            st.slider("How hard is this to cook?", 1, 5, 3)
            st.checkbox("I have all ingredients")
            if st.button("🚀 Share Success"):
                st.balloons()
import streamlit as st
import os

# ==========================================
# 1. SETUP PATHS
# ==========================================
# Kukunin nito ang location ng appy.py para mahanap ang images folder
base_path = os.path.dirname(__file__)

# ==========================================
# 2. PAGE CONFIG & THEME (Light Purple)
# ==========================================
st.set_page_config(page_title="TikTok Recipe Vault", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F3E5F5; }
    .stButton>button { background-color: #CE93D8; color: white; border-radius: 10px; border: none; }
    .stSidebar { background-color: #E1BEE7; }
    h1, h2, h3 { color: #6A1B9A; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. DATABASE NG MGA PAGKAIN (7 Recipes)
# ==========================================
# Ginamit ang "image" na folder name base sa iyong explorer
recipes = {
    "Ilocos Empanada": {
        "img": os.path.join(base_path, "image", "1.png"), 
        "emoji": "🥟", "rating": "4.8",
        "link": "https://www.panlasangpinoy.com",
        "ing": ["Rice flour", "Longganisa", "Egg", "Papaya"],
        "inst": "Flatten dough, add fillings, and deep fry until crispy."
    },
    "Dubai Chewy Cookie": {
        "img": os.path.join(base_path, "image", "2.png"), 
        "emoji": "🍪", "rating": "4.9",
        "link": "https://www.tiktok.com",
        "ing": ["Butter", "Flour", "Pistachio cream", "Kunafa"],
        "inst": "Mix ingredients, stuff with kunafa, and bake at 180°C."
    },
    "Tofu Squares": {
        "img": os.path.join(base_path, "image", "3.png"), 
        "emoji": "🍲", "rating": "4.2",
        "link": "https://www.yummy.ph",
        "ing": ["Firm Tofu", "Cornstarch", "Soy Sauce", "Honey"],
        "inst": "Cube tofu, coat in starch, and air fry hanggang mag-golden brown."
    },
    "Samyang Omelette": {
        "img": os.path.join(base_path, "image", "4.png"), 
        "emoji": "🍳", "rating": "4.7",
        "link": "https://www.google.com",
        "ing": ["Samyang Noodles", "Eggs", "Cheese"],
        "inst": "Lutuin ang noodles, i-mix ang sauce, at ibalot sa omelette."
    },
    "Cheesy Corn": {
        "img": os.path.join(base_path, "image", "5.png"), 
        "emoji": "🌽", "rating": "4.6",
        "link": "https://www.allrecipes.com",
        "ing": ["Sweet Corn", "Mozzarella", "Mayo", "Butter"],
        "inst": "Sauté corn in butter, add mayo and cheese, then melt."
    },
    "Spud": {
        "img": os.path.join(base_path, "image", "6.png"), 
        "emoji": "🥔", "rating": "4.4",
        "link": "https://www.foodnetwork.com",
        "ing": ["Potato", "Cheese", "Bacon", "Sour Cream"],
        "inst": "Bake potato, mash the inside, and add toppings."
    },
    "Tiramisu": {
        "img": os.path.join(base_path, "image", "7.png"), 
        "emoji": "🍰", "rating": "5.0",
        "link": "https://www.delish.com",
        "ing": ["Ladyfingers", "Espresso", "Mascarpone"],
        "inst": "Layer coffee-dipped biscuits with mascarpone cream."
    }
}

if 'selected_food' not in st.session_state:
    st.session_state.selected_food = None

# Sidebar
st.sidebar.title("💜 Recipe Vault")
nav = st.sidebar.radio("Navigation", ["Home Page", "About App"])

# ==========================================
# 4. INTERFACE LOGIC
# ==========================================
if nav == "About App":
    st.title("ℹ️ About App")
    st.write("Digital Recipe Book para sa mga trending foods.")
    if st.button("Back to Home"):
        st.session_state.selected_food = None
        st.rerun()

else:
    if st.session_state.selected_food is None:
        st.title("🍔 Trending TikTok Recipes")
        
        # Grid layout (3 Columns)
        cols = st.columns(3)
        for idx, (name, info) in enumerate(recipes.items()):
            with cols[idx % 3]:
                # SAFETY CHECK: I-check kung exist ang pic bago i-display
                if os.path.exists(info['img']):
                    st.image(info['img'], caption=name, use_container_width=True)
                else:
                    st.error(f"Missing: {name} pic")
                
                if st.button(f"View Recipe", key=name, use_container_width=True):
                    st.session_state.selected_food = name
                    st.rerun()
                st.write(f"Rating: {info['rating']} ⭐")
                st.divider()

    else:
        # DETAIL VIEW
        food = st.session_state.selected_food
        item = recipes[food]
        
        if st.button("⬅️ Back to Menu"):
            st.session_state.selected_food = None
            st.rerun()
            
        col_img, col_details = st.columns([1, 2])
        with col_img:
            if os.path.exists(item['img']):
                st.image(item['img'], caption=f"Finished {food}", use_container_width=True)
            else:
                st.warning("Image not found.")
        
        with col_details:
            st.header(f"{food} {item['emoji']}")
            st.subheader("🛒 Ingredients")
            for ing in item['ing']:
                st.write(f"• {ing}")
            st.subheader("📝 Instructions")
            st.write(item['inst'])
            st.link_button("🔗 Original Source", item['link'])
            if st.button("🚀 Share Success"):
                st.balloons()
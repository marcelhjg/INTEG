import streamlit as st
import os

# ==========================================
# 1. SETUP PATHS (Importante para sa Cloud)
# ==========================================
# Kukunin nito ang folder location kung nasaan ang appy.py mo
base_path = os.path.dirname(__file__)

# ==========================================
# 2. PAGE CONFIG & THEME
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
# 3. DATABASE (7 Recipes)
# ==========================================
# Siguraduhin na "integ images" ang nakalagay para tumugma sa VS Code mo
recipes = {
    "Ilocos Empanada": {
        "img": os.path.join(base_path, "integ images", "1.png"), 
        "emoji": "🥟", "rating": "4.8",
        "link": "https://www.panlasangpinoy.com",
        "ing": ["Rice flour", "Longganisa", "Egg", "Papaya"],
        "inst": "Flatten dough, add fillings, and deep fry until crispy."
    },
    "Dubai Chewy Cookie": {
        "img": os.path.join(base_path, "integ images", "2.png"), 
        "emoji": "🍪", "rating": "4.9",
        "link": "https://www.tiktok.com",
        "ing": ["Butter", "Flour", "Pistachio cream", "Kunafa"],
        "inst": "Mix ingredients, stuff with kunafa, and bake at 180°C."
    },
    "Tofu Squares": {
        "img": os.path.join(base_path, "integ images", "3.png"), 
        "emoji": "🍲", "rating": "4.2",
        "link": "https://www.yummy.ph",
        "ing": ["Firm Tofu", "Cornstarch", "Soy Sauce", "Honey"],
        "inst": "Cube tofu, coat in starch, and air fry until golden."
    },
    "Samyang Omelette": {
        "img": os.path.join(base_path, "integ images", "4.png"), 
        "emoji": "🍳", "rating": "4.7",
        "link": "https://www.google.com",
        "ing": ["Samyang Noodles", "Eggs", "Cheese"],
        "inst": "Boil noodles, mix sauce, and fold into an omelette."
    },
    "Cheesy Corn": {
        "img": os.path.join(base_path, "integ images", "5.png"), 
        "emoji": "🌽", "rating": "4.6",
        "link": "https://www.allrecipes.com",
        "ing": ["Sweet Corn", "Mozzarella", "Mayo", "Butter"],
        "inst": "Sauté corn in butter, add mayo and cheese, then melt."
    },
    "Spud": {
        "img": os.path.join(base_path, "integ images", "6.png"), 
        "emoji": "🥔", "rating": "4.4",
        "link": "https://www.foodnetwork.com",
        "ing": ["Potato", "Cheese", "Bacon", "Sour Cream"],
        "inst": "Bake potato, mash the inside, and add toppings."
    },
    "Tiramisu": {
        "img": os.path.join(base_path, "integ images", "7.png"), 
        "emoji": "🍰", "rating": "5.0",
        "link": "https://www.delish.com",
        "ing": ["Ladyfingers", "Espresso", "Mascarpone"],
        "inst": "Layer coffee-dipped biscuits with mascarpone cream."
    }
}

if 'selected_food' not in st.session_state:
    st.session_state.selected_food = None

# Sidebar Navigation
st.sidebar.title("💜 Recipe Vault")
nav = st.sidebar.radio("Navigation", ["Home Page", "About App"])

# ==========================================
# 4. HOME PAGE / GALLERY
# ==========================================
if nav == "Home Page":
    if st.session_state.selected_food is None:
        st.title("🍔 Trending TikTok Recipes")
        
        cols = st.columns(3)
        for idx, (name, info) in enumerate(recipes.items()):
            with cols[idx % 3]:
                # SAFETY CHECK: I-check muna kung exist ang picture para hindi mag-error
                if os.path.exists(info['img']):
                    st.image(info['img'], caption=name, use_container_width=True)
                else:
                    st.error(f"Missing: {name} pic")
                
                if st.button(f"View Recipe", key=name, use_container_width=True):
                    st.session_state.selected_food = name
                    st.rerun()
                st.write(f"Rating: {info['rating']} ⭐")
                st.divider()

# ==========================================
# 5. RECIPE DETAIL VIEW
# ==========================================
    else:
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
            
            if st.button("❤️ Favorite"):
                st.toast("Added to favorites!")
        
        with col_details:
            st.header(f"{food} {item['emoji']}")
            st.subheader("🛒 Ingredients")
            for ing in item['ing']:
                st.write(f"• {ing}")
            st.subheader("📝 Instructions")
            st.write(item['inst'])
            st.link_button(f"🔗 Source Link", item['link'])
            if st.button("🚀 Share"):
                st.balloons()
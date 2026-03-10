import streamlit as st
import os

# ==========================================
# 1. PAGE CONFIG & THEME (Light Purple)
# ==========================================
st.set_page_config(page_title="TikTok Recipe Lab", layout="wide")

# Custom CSS para sa Light Purple Theme
st.markdown("""
    <style>
    .stApp { background-color: #F3E5F5; }
    .stButton>button { 
        background-color: #CE93D8; 
        color: white; 
        border-radius: 12px; 
    }
    .stSidebar { background-color: #E1BEE7; }
    h1, h2, h3 { color: #6A1B9A; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. DYNAMIC PATH SETTING (Para sa WSL/Ubuntu)
# ==========================================
# Ito ang kukuha ng folder kung nasaan ang appy.py mo ngayon
current_dir = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(current_dir, "integ images")

# function para makuha ang tamang path ng bawat pic
def get_img(filename):
    return os.path.join(image_folder, filename)

# ==========================================
# 3. DATABASE (7 Recipes Only)
# ==========================================
recipes = {
    "Ilocos Empanada": {
        "emoji": "🥟", "img": get_img("1.png"), "rating": "4.8",
        "link": "https://www.panlasangpinoy.com",
        "ing": ["2 cups rice flour", "1/2 cup water", "Grated green papaya", "Longganisa", "1 egg"],
        "inst": ["Mix flour & water.", "Flatten on plastic.", "Add filling.", "Deep fry until crispy."]
    },
    "Dubai Chewy Cookie": {
        "emoji": "🍪", "img": get_img("2.png"), "rating": "4.9",
        "link": "https://www.tiktok.com",
        "ing": ["1 cup butter", "1 cup sugar", "2 cups flour", "Pistachio cream", "Kunafa pastry"],
        "inst": ["Cream butter.", "Fold in flour.", "Stuff with pistachio.", "Bake at 180°C."]
    },
    "Tofu Squares": {
        "emoji": "🍲", "img": get_img("3.png"), "rating": "4.2",
        "link": "https://www.yummy.ph",
        "ing": ["Firm tofu", "Cornstarch", "Soy sauce", "Honey"],
        "inst": ["Cube tofu.", "Coat in starch.", "Air fry.", "Toss in sauce."]
    },
    "Samyang Omelette": {
        "emoji": "🍳", "img": get_img("4.png"), "rating": "4.7",
        "link": "https://www.google.com",
        "ing": ["Samyang noodles", "2 Eggs", "Cheese slice"],
        "inst": ["Boil noodles.", "Mix with sauce.", "Fold into omelette."]
    },
    "Cheesy Corn": {
        "emoji": "🌽", "img": get_img("5.png"), "rating": "4.6",
        "link": "https://www.allrecipes.com",
        "ing": ["Sweet corn", "Mayonnaise", "Mozzarella", "Butter"],
        "inst": ["Sauté corn.", "Mix mayo/cheese.", "Melt until gooey."]
    },
    "Spud": {
        "emoji": "🥔", "img": get_img("6.png"), "rating": "4.4",
        "link": "https://www.foodnetwork.com",
        "ing": ["Large potato", "Butter", "Cheese", "Bacon"],
        "inst": ["Bake potato.", "Mash inside.", "Add toppings."]
    },
    "Tiramisu": {
        "emoji": "🍰", "img": get_img("7.png"), "rating": "5.0",
        "link": "https://www.delish.com",
        "ing": ["Ladyfingers", "Espresso", "Mascarpone"],
        "inst": ["Dip biscuits.", "Layer with cheese.", "Chill 4 hours."]
    }
}

# Session State
if 'selected_food' not in st.session_state:
    st.session_state.selected_food = None
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

# ==========================================
# 4. SIDEBAR & ABOUT
# ==========================================
st.sidebar.title("💜 TikTok Food Vault")
nav = st.sidebar.radio("Navigation", ["Home Page", "About App"])

if st.session_state.favorites:
    st.sidebar.divider()
    st.sidebar.subheader("⭐ My Favorites")
    for fav in st.session_state.favorites:
        st.sidebar.write(f"• {fav}")

if nav == "About App":
    st.title("ℹ️ Project Information")
    st.markdown("""
    - **What it does:** Digital recipe book for TikTok trends.
    - **Target User:** Home cooks and students.
    - **Inputs:** Buttons, sliders, file uploaders.
    - **Outputs:** Recipes, images, and links.
    """)
    if st.button("Back to Home"):
        st.session_state.selected_food = None
        st.rerun()

# ============= HOME PAGE =============
else:
    if st.session_state.selected_food is None:
        st.title("🍔 Trending TikTok Recipes 2026")
        
        cols = st.columns(3)
        food_items = list(recipes.keys())

        for idx, food in enumerate(food_items):
            with cols[idx % 3]:
                # Display Image
                if os.path.exists(recipes[food]['img']):
                    st.image(recipes[food]['img'], use_container_width=True)
                else:
                    st.error(f"Pic not found at: {recipes[food]['img']}")
                
                if st.button(f"View {food}", key=f"btn_{food}", use_container_width=True):
                    st.session_state.selected_food = food
                    st.rerun()
                st.write(f"Rating: {recipes[food]['rating']} ⭐")
                st.divider()

    # ============= RECIPE DETAIL =============
    else:
        food = st.session_state.selected_food
        data = recipes[food]

        if st.button("⬅️ Back to Gallery"):
            st.session_state.selected_food = None
            st.rerun()

        col1, col2 = st.columns([1, 1.2])
        with col1:
            st.image(data['img'], use_container_width=True)
            if food not in st.session_state.favorites:
                if st.button("⭐ Add to Favorites"):
                    st.session_state.favorites.append(food)
                    st.rerun()
            else:
                if st.button("💔 Remove Favorite"):
                    st.session_state.favorites.remove(food)
                    st.rerun()

        with col2:
            st.header(f"{food} {data['emoji']}")
            st.link_button("🔗 Recipe Source", data['link'])
            st.subheader("🛒 Ingredients")
            for item in data['ing']:
                st.write(f"• {item}")
            st.subheader("📝 Instructions")
            for i, step in enumerate(data['inst'], 1):
                st.write(f"{i}. {step}")
        
        st.divider()
        st.progress(100, text="Recipe Loaded!")
        st.balloons() if st.button("Cooked this!") else None
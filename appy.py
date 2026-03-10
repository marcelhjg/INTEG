import streamlit as st
import time

# ==========================================
# 1. PAGE CONFIG & THEME (Light Purple)
# ==========================================
st.set_page_config(page_title="TikTok Recipe Lab", layout="wide")

# Custom CSS para sa Light Purple Theme
st.markdown("""
    <style>
    .stApp {
        background-color: #F3E5F5;
    }
    .stButton>button {
        background-color: #CE93D8;
        color: white;
        border-radius: 10px;
    }
    .stSidebar {
        background-color: #E1BEE7;
    }
    h1, h2, h3 {
        color: #6A1B9A;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. DATABASE (Updated List & Paths)
# ==========================================
# Paalala: Siguraduhin na ang folder name ay "integ images" sa VS Code mo.
recipes = {
    "Ilocos Empanada": {
        "emoji": "🥟", "img": "images/1.png", "rating": "4.8",
        "link": "https://example.com/ilocos-empanada-recipe", # PALITAN MO ITO NG TUNAY NA LINK
        "ing": ["2 cups rice flour", "1/2 cup water", "Grated green papaya", "Longganisa", "1 egg"],
        "inst": ["Mix flour & water.", "Flatten on plastic.", "Add filling.", "Deep fry."]
    },
    "Dubai Chewy Cookie": {
        "emoji": "🍪", "img": "images/2.png", "rating": "4.9",
        "link": "https://example.com/dubai-cookie-recipe",
        "ing": ["1 cup butter", "1 cup sugar", "2 cups flour", "Pistachio cream", "Kunafa pastry"],
        "inst": ["Cream butter.", "Fold in flour.", "Stuff with pistachio.", "Bake 180°C."]
    },
    "Tofu Squares": {
        "emoji": "🍲", "img": "images/3.png", "rating": "4.2",
        "link": "https://example.com/tofu-squares-recipe",
        "ing": ["Firm tofu", "Cornstarch", "Soy sauce", "Honey"],
        "inst": ["Cube tofu.", "Coat in starch.", "Air fry.", "Toss in sauce."]
    },
    "Samyang Omelette": {
        "emoji": "🍳", "img": "images/4.png", "rating": "4.7",
        "link": "https://example.com/samyang-omelette-recipe",
        "ing": ["Samyang noodles", "2 Eggs", "Cheese slice"],
        "inst": ["Boil noodles.", "Mix with sauce.", "Fold into omelette."]
    },
    "Cheesy Corn": {
        "emoji": "🌽", "img": "images/5.png", "rating": "4.6",
        "link": "https://example.com/cheesy-corn-recipe",
        "ing": ["Sweet corn", "Mayonnaise", "Mozzarella", "Butter"],
        "inst": ["Sauté corn.", "Mix mayo/cheese.", "Melt until gooey."]
    },
    "Spud": {
        "emoji": "🥔", "img": "images/6.png", "rating": "4.4",
        "link": "https://example.com/spud-recipe",
        "ing": ["Large potato", "Butter", "Cheese", "Bacon"],
        "inst": ["Bake potato.", "Mash inside.", "Add toppings."]
    },
    "Tiramisu": {
        "emoji": "🍰", "img": "images/7.png", "rating": "5.0",
        "link": "https://example.com/tiramisu-recipe",
        "ing": ["Ladyfingers", "Espresso", "Mascarpone"],
        "inst": ["Dip biscuits.", "Layer with cheese.", "Chill 4 hours."]
    }
}

# Session State para sa Favorites at Selection
if 'selected_food' not in st.session_state:
    st.session_state.selected_food = None
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

# ==========================================
# 3. SIDEBAR
# ==========================================
st.sidebar.title("💜 TikTok Food Vault")
page = st.sidebar.radio("Navigation", ["Home Page", "About App"])

if st.session_state.favorites:
    st.sidebar.divider()
    st.sidebar.subheader("⭐ My Favorites")
    for fav in st.session_state.favorites:
        st.sidebar.write(f"- {fav}")

# ==========================================
# 4. ABOUT PAGE
# ==========================================
if page == "About App":
    st.title("ℹ️ Project Info")
    st.markdown("""
    - **Use-Case:** Digital Recipe Book for Viral TikTok Foods.
    - **Target User:** Home cooks and students.
    - **Inputs:** Clicks, ratings, favorite toggles, and photo uploads.
    - **Outputs:** Step-by-step guides, images, and external recipe links.
    """)
    if st.button("Back to Home"):
        st.session_state.selected_food = None
        st.rerun()

# ==========================================
# 5. HOME PAGE (Gallery with Images)
# ==========================================
else:
    if st.session_state.selected_food is None:
        st.title("🍔 Trending TikTok Recipes 2026")
        st.write("Click a card to see the full recipe:")
        
        # Grid System
        cols = st.columns(3)
        food_list = list(recipes.keys())

        for i, food in enumerate(food_list):
            with cols[i % 3]:
                # Ipakita ang Picture sa Home
                try:
                    st.image(recipes[food]['img'], use_container_width=True)
                except:
                    st.caption(f"(Image for {food} not found)")
                
                if st.button(f"View {food}", key=food, use_container_width=True):
                    st.session_state.selected_food = food
                    st.rerun()
                st.write(f"Rating: {recipes[food]['rating']} ⭐")
                st.divider()

    # ==========================================
    # 6. RECIPE DETAIL VIEW
    # ==========================================
    else:
        food = st.session_state.selected_food
        data = recipes[food]

        if st.button("⬅️ Back to Gallery"):
            st.session_state.selected_food = None
            st.rerun()

        st.divider()
        col_left, col_right = st.columns([1, 1.2])

        with col_left:
            st.image(data['img'], use_container_width=True)
            
            # Favorite Button
            if food not in st.session_state.favorites:
                if st.button("⭐ Add to Favorites"):
                    st.session_state.favorites.append(food)
                    st.toast(f"Added {food} to favorites!")
                    st.rerun()
            else:
                if st.button("💔 Remove from Favorites"):
                    st.session_state.favorites.remove(food)
                    st.rerun()

        with col_right:
            st.header(f"{food} {data['emoji']}")
            
            # Link to Full Recipe
            st.link_button("🔗 Original Recipe Link", data['link'])
            
            st.subheader("🛒 Ingredients")
            for ing in data['ing']:
                st.write(f"- {ing}")
            
            st.subheader("📝 Instructions")
            for i, step in enumerate(data['inst'], 1):
                st.write(f"{i}. {step}")

        # Components for Merit Points
        st.divider()
        t1, t2 = st.tabs(["User Review", "Kitchen Tools"])
        with t1:
            st.slider("Rate the difficulty:", 1, 5, 3)
            st.text_input("Any substitutions used?")
            st.file_uploader("Upload your cook photo")
        with t2:
            st.checkbox("Oven used")
            st.checkbox("Air Fryer used")
            st.color_picker("Customize app highlight color:", "#CE93D8")
            st.progress(100, text="Recipe Loaded!")
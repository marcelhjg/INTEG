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
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #AB47BC; border: none; }
    .stSidebar { background-color: #E1BEE7; }
    h1, h2, h3 { color: #6A1B9A; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. DATABASE (7 Recipes Only)
# ==========================================
# Path format: "folder_name/file_name.extension"
recipes = {
    "Ilocos Empanada": {
        "emoji": "🥟", "img": "integ images/1.png", "rating": "4.8",
        "link": "https://www.panlasangpinoy.com", # Palitan mo ang link dito
        "ing": ["2 cups rice flour", "1/2 cup water", "Grated green papaya", "Longganisa", "1 egg"],
        "inst": ["Mix flour & water.", "Flatten on plastic.", "Add filling.", "Deep fry until crispy."]
    },
    "Dubai Chewy Cookie": {
        "emoji": "🍪", "img": "integ images/2.png", "rating": "4.9",
        "link": "https://www.tiktok.com",
        "ing": ["1 cup butter", "1 cup sugar", "2 cups flour", "Pistachio cream", "Kunafa pastry"],
        "inst": ["Cream butter and sugar.", "Fold in flour.", "Stuff with pistachio/kunafa.", "Bake at 180°C."]
    },
    "Tofu Squares": {
        "emoji": "🍲", "img": "integ images/3.png", "rating": "4.2",
        "link": "https://www.yummy.ph",
        "ing": ["Firm tofu", "Cornstarch", "Soy sauce", "Honey", "Garlic"],
        "inst": ["Cube tofu.", "Coat in starch.", "Air fry until golden.", "Toss in honey-soy sauce."]
    },
    "Samyang Omelette": {
        "emoji": "🍳", "img": "integ images/4.png", "rating": "4.7",
        "link": "https://www.google.com",
        "ing": ["Samyang Buldak noodles", "2 Eggs", "Cheese slice", "Green onions"],
        "inst": ["Boil noodles.", "Mix with spicy sauce.", "Fold into a cheesy omelette."]
    },
    "Cheesy Corn": {
        "emoji": "🌽", "img": "integ images/5.png", "rating": "4.6",
        "link": "https://www.allrecipes.com",
        "ing": ["Sweet corn", "Mayonnaise", "Mozzarella", "Butter", "Chili powder"],
        "inst": ["Sauté corn in butter.", "Mix mayo and cheese.", "Melt until gooey and charred."]
    },
    "Spud": {
        "emoji": "🥔", "img": "integ images/6.png", "rating": "4.4",
        "link": "https://www.foodnetwork.com",
        "ing": ["Large potato", "Butter", "Cheese", "Sour cream", "Bacon bits"],
        "inst": ["Bake or boil potato.", "Mash the inside.", "Top with cheese and bacon."]
    },
    "Tiramisu": {
        "emoji": "🍰", "img": "integ images/7.png", "rating": "5.0",
        "link": "https://www.delish.com",
        "ing": ["Ladyfingers", "Espresso", "Mascarpone", "Cocoa powder"],
        "inst": ["Dip biscuits in coffee.", "Layer with mascarpone.", "Chill for 4 hours.", "Dust with cocoa."]
    }
}

# State management
if 'selected_food' not in st.session_state:
    st.session_state.selected_food = None
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

# ==========================================
# 3. SIDEBAR & ABOUT
# ==========================================
st.sidebar.title("💜 TikTok Food Vault")
nav = st.sidebar.radio("Navigation", ["Home Page", "About App"])

if st.session_state.favorites:
    st.sidebar.divider()
    st.sidebar.subheader("⭐ My Favorites")
    for fav in st.session_state.favorites:
        st.sidebar.write(f"• {fav}")

# ==========================================
# 4. ABOUT PAGE
# ==========================================
if nav == "About App":
    st.title("ℹ️ Project Information")
    st.info("Course: Streamlit UI Design | Final Output")
    st.markdown("""
    - **What it does:** Isang interactive gallery para sa viral foods sa TikTok.
    - **Target User:** Food enthusiasts at students.
    - **Inputs:** Buttons, sliders, text inputs, file uploaders.
    - **Outputs:** Detailed recipes, images, links, at metrics.
    """)
    if st.button("Back to Home"):
        st.session_state.selected_food = None
        st.rerun()

# ============= HOME PAGE / GALLERY =============
else:
    if st.session_state.selected_food is None:
        st.title("🍔 Trending TikTok Recipes 2026")
        st.write("Click a recipe card below to explore:")
        
        # GRID SYSTEM (3 Columns)
        cols = st.columns(3)
        food_items = list(recipes.keys())

        for idx, food in enumerate(food_items):
            with cols[idx % 3]:
                # Error checking for images
                if os.path.exists(recipes[food]['img']):
                    st.image(recipes[food]['img'], use_container_width=True)
                else:
                    st.warning(f"⚠️ {food} image not found.")
                
                # Command to Select Recipe
                if st.button(f"View {food}", key=f"btn_{food}", use_container_width=True):
                    st.session_state.selected_food = food
                    st.rerun()
                st.write(f"Rating: {recipes[food]['rating']} ⭐")
                st.divider()

    # ============= RECIPE DETAIL VIEW =============
    else:
        food = st.session_state.selected_food
        data = recipes[food]

        if st.button("⬅️ Back to Gallery"):
            st.session_state.selected_food = None
            st.rerun()

        st.divider()
        col1, col2 = st.columns([1, 1.2])

        with col1:
            st.image(data['img'], use_container_width=True)
            
            # Favorite Toggle
            if food not in st.session_state.favorites:
                if st.button("⭐ Add to Favorites"):
                    st.session_state.favorites.append(food)
                    st.toast(f"{food} added!", icon="✅")
                    st.rerun()
            else:
                if st.button("💔 Remove Favorite"):
                    st.session_state.favorites.remove(food)
                    st.rerun()

        with col2:
            st.header(f"{food} {data['emoji']}")
            
            # Link Button
            st.link_button("🔗 Open Original Recipe Source", data['link'])
            
            st.subheader("🛒 Ingredients")
            for item in data['ing']:
                st.write(f"• {item}")
            
            st.subheader("📝 Instructions")
            for i, step in enumerate(data['inst'], 1):
                st.write(f"{i}. {step}")

        # Components for Merit Points
        st.divider()
        t1, t2 = st.tabs(["Feedback", "Cooking Status"])
        with t1:
            st.slider("Recipe Difficulty:", 1, 5, 3)
            st.text_input("Comment your thoughts:")
            st.file_uploader("Show us your creation!", type=['png', 'jpg'])
        with t2:
            st.progress(100, text="Recipe Fully Loaded")
            st.color_picker("Pick a highlight color for your kitchen:")
            if st.button("🚀 Share to Community"):
                st.balloons()
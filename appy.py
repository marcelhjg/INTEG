import streamlit as st
import time

# ==========================================
# 1. DATABASE NG MGA PAGKAIN
# ==========================================
recipes = {
    "Ilocos Empanada": {
        "emoji": "🥟", "img": "image/1.png", "rating": "4.8",
        "ing": ["2 cups rice flour", "1/2 cup water", "Grated green papaya", "Longganisa", "1 egg"],
        "inst": ["Mix flour & water.", "Flatten on plastic.", "Add filling.", "Deep fry."]
    },
    "Dubai Chewy Cookie": {
        "emoji": "🍪", "img": "image/2.png", "rating": "4.9",
        "ing": ["1 cup butter", "1 cup sugar", "2 cups flour", "Pistachio cream", "Kunafa pastry"],
        "inst": ["Cream butter.", "Fold in flour.", "Stuff with pistachio.", "Bake 180°C."]
    },
    "Tofu Squares": {
        "emoji": "🍲", "img": "image/3.png", "rating": "4.2",
        "ing": ["Firm tofu", "Cornstarch", "Soy sauce", "Honey"],
        "inst": ["Cube tofu.", "Coat in starch.", "Air fry.", "Toss in sauce."]
    },
    "Samyang Omelette": {
        "emoji": "🍳", "img": "image/4.png", "rating": "4.7",
        "ing": ["Samyang noodles", "2 Eggs", "Cheese slice"],
        "inst": ["Boil noodles.", "Mix with sauce.", "Fold into omelette."]
    },
    "Cheesy Corn": {
        "emoji": "🌽", "img": "image/5.png", "rating": "4.6",
        "ing": ["Sweet corn", "Mayonnaise", "Mozzarella", "Butter"],
        "inst": ["Sauté corn.", "Mix mayo/cheese.", "Melt until gooey."]
    },
    "Spud": {
        "emoji": "🥔", "img": "image/6.png", "rating": "4.4",
        "ing": ["Large potato", "Butter", "Cheese", "Bacon"],
        "inst": ["Bake potato.", "Mash inside.", "Add toppings."]
    },
    "Tiramisu": {
        "emoji": "🍰", "img": "image/7.png", "rating": "5.0", # Inayos ang key na "img: "
        "ing": ["Ladyfingers", "Espresso", "Mascarpone"],
        "inst": ["Dip biscuits.", "Layer with cheese.", "Chill 4 hours."]
    } # Inayos ang pag-close ng dictionary
}

# Session State para maalala kung anong pagkain ang pinindot
if 'selected_food' not in st.session_state:
    st.session_state.selected_food = None

# ==========================================
# 2. SIDEBAR NAVIGATION
# ==========================================
st.sidebar.title("📱 TikTok Food Lab")
page = st.sidebar.radio("Go to", ["Home Page", "About App"])

# ==========================================
# 3. ABOUT PAGE
# ==========================================
if page == "About App":
    st.title("ℹ️ Project Information")
    st.info("Created for Streamlit UI Assignment")
    st.markdown("""
    - **What it does:** Isang digital recipe book para sa viral TikTok foods.
    - **Target User:** Home cooks at foodies.
    - **Inputs:** Button clicks, ratings, comments, and file uploads.
    - **Outputs:** Recipe details, images, and cooking status.
    """)
    if st.button("Back to Home"):
        st.session_state.selected_food = None
        st.rerun()

# ==========================================
# 4. HOME PAGE (Gallery View)
# ==========================================
else:
    if st.session_state.selected_food is None:
        st.title("🍔 Trending TikTok Recipes 2026")
        st.write("Pumili ng pagkain para makita ang recipe:")
        
        # Grid layout (3 columns)
        cols = st.columns(3)
        food_list = list(recipes.keys())

        for i, food in enumerate(food_list):
            with cols[i % 3]:
                st.write(f"### {recipes[food]['emoji']}")
                if st.button(food, key=food, use_container_width=True):
                    st.session_state.selected_food = food
                    st.rerun()
                st.caption(f"Rating: {recipes[food]['rating']} ⭐")

    # ==========================================
    # 5. RECIPE DETAIL VIEW
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
            try:
                st.image(data['img'], caption=f"Viral {food}", use_container_width=True)
            except:
                st.warning(f"Ilagay ang '{data['img']}' sa folder mo.")
            
            st.metric("Popularity", data['rating'])

        with col_right:
            st.header(f"{food} {data['emoji']}")
            st.subheader("🛒 Ingredients")
            for ing in data['ing']:
                st.write(f"- {ing}")
            
            st.subheader("📝 Instructions")
            for i, step in enumerate(data['inst'], 1):
                st.write(f"{i}. {step}")

        # Extra Interactivity
        st.divider()
        tab1, tab2 = st.tabs(["Rate & Review", "Cook Mode"])
        with tab1:
            st.slider("Rate this:", 1, 10, 8)
            st.text_area("Anong masasabi mo?")
            st.file_uploader("Upload your version", type=['jpg', 'png'])
            if st.button("Submit Review"):
                st.balloons()
                st.toast("Review Posted!", icon="✅")
        with tab2:
            st.progress(40, text="Cooking Progress...")
            st.color_picker("Pick a plate color:")
            st.status("Kitchen is heating up...")
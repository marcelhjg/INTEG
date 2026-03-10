import streamlit as st

# 1. PAGE CONFIG
st.set_page_config(page_title="TikTok Recipe Vault", layout="wide")

# 2. CUSTOM CSS
st.markdown("""
    <style>
    .stApp { background-color: #F3E5F5; }
    </style>
    """, unsafe_allow_html=True)

# 3. DATABASE - Direct path gamit ang "image/"
recipes = {
    "Ilocos Empanada": {
        "img": "image/1.png",
        "emoji": "🥟", "rating": "4.8",
        "link": "https://www.panlasangpinoy.com",
        "ing": ["Rice flour", "Longganisa", "Egg", "Papaya"],
        "inst": "Flatten dough, add fillings, and deep fry until crispy."
    },
    "Dubai Chewy Cookie": {
        "img": "image/2.png",
        "emoji": "🍪", "rating": "4.9",
        "link": "https://www.tiktok.com",
        "ing": ["Butter", "Flour", "Pistachio cream", "Kunafa"],
        "inst": "Mix ingredients, stuff with kunafa, and bake at 180°C."
    },
    "Tofu Squares": {
        "img": "image/3.png",
        "emoji": "🍲", "rating": "4.2",
        "link": "https://www.yummy.ph",
        "ing": ["Firm Tofu", "Cornstarch", "Soy Sauce", "Honey"],
        "inst": "Cube tofu, coat in starch, and air fry until golden."
    },
    "Samyang Omelette": {
        "img": "image/4.png",
        "emoji": "🍳", "rating": "4.7",
        "link": "https://www.google.com",
        "ing": ["Samyang Noodles", "Eggs", "Cheese"],
        "inst": "Boil noodles, mix sauce, and fold into an omelette."
    },
    "Cheesy Corn": {
        "img": "image/5.png",
        "emoji": "🌽", "rating": "4.6",
        "link": "https://www.allrecipes.com",
        "ing": ["Sweet Corn", "Mozzarella", "Mayo", "Butter"],
        "inst": "Sauté corn in butter, add mayo and cheese, then melt."
    },
    "Spud": {
        "img": "image/6.png",
        "emoji": "🥔", "rating": "4.4",
        "link": "https://www.foodnetwork.com",
        "ing": ["Potato", "Cheese", "Bacon", "Sour Cream"],
        "inst": "Bake potato, mash the inside, and add toppings."
    },
    "Tiramisu": {
        "img": "image/7.png",
        "emoji": "🍰", "rating": "5.0",
        "link": "https://www.delish.com",
        "ing": ["Ladyfingers", "Espresso", "Mascarpone"],
        "inst": "Layer coffee-dipped biscuits with mascarpone cream."
    }
}

# 4. SESSION STATE
if 'selected' not in st.session_state:
    st.session_state.selected = None

# 5. UI LOGIC
st.sidebar.title("💜 Recipe Vault")
nav = st.sidebar.radio("Navigation", ["Home", "About"])

if nav == "Home":
    if st.session_state.selected is None:
        st.title("🍔 Trending TikTok Recipes")
        cols = st.columns(3)
        for i, (name, info) in enumerate(recipes.items()):
            with cols[i % 3]:
                # DITO AY ST.IMAGE LANG ANG GAMIT
                st.image(info['img'], caption=name, use_container_width=True)
                if st.button(f"View {name}", key=name):
                    st.session_state.selected = name
                    st.rerun()
    else:
        # DETAIL VIEW
        item = recipes[st.session_state.selected]
        if st.button("⬅️ Back"):
            st.session_state.selected = None
            st.rerun()
        st.header(f"{st.session_state.selected} {item['emoji']}")
        # DITO RIN ST.IMAGE LANG
        st.image(item['img'], use_container_width=True)
        st.write("### Ingredients")
        for ing in item['ing']: st.write(f"- {ing}")
        st.write("### Instructions", item['inst'])

elif nav == "About":
    st.title("ℹ️ About")
    st.write("Digital Recipe Book.")
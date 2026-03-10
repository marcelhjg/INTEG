import streamlit as st
import os

# 1. PAGE CONFIG
st.set_page_config(page_title="TikTok Recipe Vault", layout="wide")

# 2. DATABASE - Gamit ang format na "images/filename.png"
# Siguraduhin na ang folder sa VS Code ay "images" at nandoon ang files
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

# 3. INTERFACE
if 'selected_food' not in st.session_state:
    st.session_state.selected_food = None

st.sidebar.title("💜 Recipe Vault")
nav = st.sidebar.radio("Navigation", ["Home Page", "About App"])

if nav == "Home Page":
    if st.session_state.selected_food is None:
        st.title("🍔 Trending TikTok Recipes")
        cols = st.columns(3)
        for i, (name, info) in enumerate(recipes.items()):
            with cols[i % 3]:
                # DITO GINAYA NATIN YUNG FORMAT SA SCREENSHOT NA GUMAGANA
                st.image(info['img'], caption=name, use_container_width=True)
                
                if st.button(f"View Recipe", key=name):
                    st.session_state.selected_food = name
                    st.rerun()
                st.write(f"Rating: {info['rating']} ⭐")
    else:
        # DETAIL VIEW
        item = recipes[st.session_state.selected_food]
        if st.button("⬅️ Back"):
            st.session_state.selected_food = None
            st.rerun()
        st.header(f"{st.session_state.selected_food} {item['emoji']}")
        # GINAYA RIN DITO YUNG FORMAT
        st.image(item['img'], use_container_width=True)
        st.write("### Ingredients")
        for ing in item['ing']: st.write(f"- {ing}")
import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="TikTok Recipe Vault", layout="wide", page_icon="🍔")

# Database
recipes = {
    "Ilocos Empanada": {"emoji": "🥟", "img": "image/1.png", "rating": 5, "diff": "Hard", "ing": ["rice flour", "water", "green papaya", "longganisa", "egg"], "inst": ["Start by mixing the rice flour with water.", "Flatten the dough thinly on a piece of plastic.", "Add the grated papaya, longganisa, and egg filling.", "Seal the edges tightly and deep fry until perfectly crispy."]},
    "Dubai Chewy Cookie": {"emoji": "🍪", "img": "image/2.png", "rating": 5, "diff": "Medium", "ing": ["butter", "sugar", "flour", "pistachio cream", "kunafa pastry"], "inst": ["Cream the butter and sugar until light and fluffy.", "Fold in the flour to create a soft dough.", "Stuff the center generously with pistachio cream and crunchy kunafa.", "Bake at 180°C until the edges are golden and chewy."]},
    "Tofu Squares": {"emoji": "🍲", "img": "image/3.png", "rating": 4, "diff": "Easy", "ing": ["firm tofu", "cornstarch", "soy sauce", "honey"], "inst": ["Cube your tofu into bite-sized pieces.", "Coat each piece thoroughly in cornstarch.", "Air fry until golden and crispy.", "Toss immediately in a mixture of soy sauce and honey."]},
    "Samyang Omelette": {"emoji": "🍳", "img": "image/4.png", "rating": 4, "diff": "Easy", "ing": ["Samyang noodles", "2 eggs", "cheese slice"], "inst": ["Boil your noodles according to the package.", "Mix the spicy sauce thoroughly into the noodles.", "Fold the mixture into a beaten egg omelette and top with cheese."]},
    "Cheesy Corn": {"emoji": "🌽", "img": "image/5.png", "rating": 4, "diff": "Easy", "ing": ["sweet corn", "mayonnaise", "mozzarella", "butter"], "inst": ["Sauté the sweet corn in melted butter.", "Stir in mayonnaise for a creamy texture.", "Top with a mountain of mozzarella and melt until gooey."]},
    "Spud": {"emoji": "🥔", "img": "image/6.png", "rating": 4, "diff": "Medium", "ing": ["large potato", "butter", "cheese", "bacon"], "inst": ["Bake the potato until tender throughout.", "Mash the inside with creamy butter.", "Layer with crispy bacon and shredded cheese."]},
    "Tiramisu": {"emoji": "🍰", "img": "image/7.png", "rating": 5, "diff": "Medium", "ing": ["ladyfingers", "espresso", "mascarpone"], "inst": ["Quickly dip the ladyfingers into strong espresso.", "Create alternating layers of biscuits and mascarpone cream.", "Chill for at least four hours to let the flavors meld."]}
}

favorites = ["Ilocos Empanada", "Tofu Squares"]

if 'selected_food' not in st.session_state: st.session_state.selected_food = None

# Sidebar
with st.sidebar:
    st.title("📱 TikTok Food Lab")
    page = st.radio("Navigation", ["Home", "About"])
    st.markdown("---")
    st.subheader("⭐ Creator's Favorites")
    for fav in favorites:
        if st.button(f"❤️ {fav}", key=f"fav_{fav}"): st.session_state.selected_food = fav; st.rerun()

# Logic
if page == "About":
    st.title("ℹ️ Project Information")
    st.info("Created for Streamlit UI Assignment")
    st.write("- **What it does:** Digital recipe book for viral TikTok trends.")
    st.write("- **Target User:** Aspiring home cooks and food enthusiasts.")
    st.write("- **Inputs:** Star ratings, file uploads, text areas, and sliders.")
    st.write("- **Outputs:** Detailed recipe cards, progress status, and success celebrations.")
else:
    if st.session_state.selected_food is None:
        st.title("🍔 Trending TikTok Recipes 2026")
        
        cols = st.columns(3)
        for i, (name, data) in enumerate(recipes.items()):
            with cols[i % 3]:
                st.image(data['img'], use_container_width=True)
                if st.button(f"{data['emoji']} {name}", key=name, use_container_width=True):
                    st.session_state.selected_food = name; st.rerun()
                st.write(f"Rating: {'⭐' * data['rating']}")
    else:
        food = st.session_state.selected_food
        data = recipes[food]
        if st.button("⬅️ Back to Gallery"): st.session_state.selected_food = None; st.rerun()
        
        c1, c2 = st.columns([1, 1.5])
        with c1:
            st.image(data['img'], use_container_width=True)
            st.metric("Difficulty", data['diff'])
        with c2:
            st.header(f"{food} {data['emoji']}")
            st.write(f"**Rating:** {'⭐' * data['rating']}")
            st.subheader("🛒 What You Need")
            st.write(f"To make this delicious {food}, you'll need {', '.join(data['ing'])}.")
            st.subheader("👨‍🍳 How to Prepare")
            st.write(" ".join(data['inst']))
            
            st.divider()
            if st.button("⏱️ Start Cooking Timer"):
                with st.empty():
                    for s in range(5, 0, -1): st.write(f"Cooking... {s}s"); time.sleep(1)
                    st.success("Your dish is ready!")
            
            st.slider("Review this recipe", 1, 5, 3)
            st.text_area("Your thoughts:")
            st.file_uploader("Upload your dish", type=['jpg'])
            if st.button("Submit Review"): st.balloons()
            st.progress(70)
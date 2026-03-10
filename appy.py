import streamlit as st
import time

# Page Config
st.set_page_config(page_title="Snackverse", layout="wide", page_icon="🍔")

# Purple Theme
st.markdown("""
<style>
.stApp { background-color: #f6f0ff; }
h1, h2, h3 { color: #6a0dad; }
.stButton>button { background-color: #9b59ff; color: white; border-radius: 10px; }
.stButton>button:hover { background-color: #7a3cff; color: white; }
</style>
""", unsafe_allow_html=True)

# Recipe Database
recipes = {
    "Ilocos Empanada": {"emoji": "🥟", "img": "image/1.png", "rating": 5, "diff": "Hard", "ing": ["rice flour", "water", "green papaya", "longganisa", "egg"], "inst": ["Start by mixing the rice flour with water.", "Flatten the dough thinly on plastic.", "Add papaya, longganisa, and egg filling.", "Seal edges and deep fry until crispy."]},
    "Dubai Chewy Cookie": {"emoji": "🍪", "img": "image/2.png", "rating": 5, "diff": "Medium", "ing": ["butter", "sugar", "flour", "pistachio cream", "kunafa pastry"], "inst": ["Cream butter and sugar.", "Fold in flour.", "Stuff with pistachio cream and kunafa.", "Bake at 180°C until chewy."]},
    "Tofu Squares": {"emoji": "🍲", "img": "image/3.png", "rating": 4, "diff": "Easy", "ing": ["firm tofu", "cornstarch", "soy sauce", "honey"], "inst": ["Cube tofu.", "Coat in cornstarch.", "Air fry until crispy.", "Toss in soy sauce and honey."]},
    "Samyang Omelette": {"emoji": "🍳", "img": "image/4.png", "rating": 4, "diff": "Easy", "ing": ["Samyang noodles", "2 eggs", "cheese slice"], "inst": ["Cook noodles.", "Mix spicy sauce.", "Fold noodles inside omelette and add cheese."]},
    "Cheesy Corn": {"emoji": "🌽", "img": "image/5.png", "rating": 4, "diff": "Easy", "ing": ["sweet corn", "mayonnaise", "mozzarella", "butter"], "inst": ["Sauté corn in butter.", "Add mayonnaise.", "Top with mozzarella and melt."]},
    "Spud": {"emoji": "🥔", "img": "image/6.png", "rating": 4, "diff": "Medium", "ing": ["large potato", "butter", "cheese", "bacon"], "inst": ["Bake potato.", "Mash with butter.", "Top with bacon and cheese."]},
    "Tiramisu": {"emoji": "🍰", "img": "image/7.png", "rating": 5, "diff": "Medium", "ing": ["ladyfingers", "espresso", "mascarpone"], "inst": ["Dip ladyfingers in espresso.", "Layer with mascarpone cream.", "Chill for 4 hours."]},
    "Grilled Scallops": {"emoji": "🐚", "img": "image/8.png", "rating": 5, "diff": "Medium", "ing": ["scallops", "butter", "garlic", "lemon"], "inst": ["Clean scallops.", "Sauté garlic in butter.", "Grill scallops until opaque.", "Add lemon juice."]},
    "Chocolate Xiao Long Bao": {"emoji": "🥟", "img": "image/9.png", "rating": 5, "diff": "Hard", "ing": ["dumpling wrapper", "dark chocolate", "heavy cream"], "inst": ["Make chocolate ganache.", "Chill mixture.", "Wrap inside dumpling wrapper.", "Steam for 5 minutes."]},
    "Buko Sherbet": {"emoji": "🥥", "img": "image/10.png", "rating": 5, "diff": "Easy", "ing": ["young coconut meat", "coconut water", "condensed milk", "crushed ice"], "inst": ["Blend coconut meat and water until smooth.", "Stir in condensed milk.", "Freeze for an hour.", "Serve over crushed ice."]}
}

favorites = ["Ilocos Empanada", "Tofu Squares", "Buko Sherbet"]

if "selected_food" not in st.session_state: st.session_state.selected_food = None

# Sidebar
with st.sidebar:
    st.title("📱 FYP Trends")
    page = st.radio("Navigation", ["Home", "About"])
    st.markdown("---")
    st.subheader("⭐ Creator's Favorites")
    for fav in favorites:
        if st.button(f"❤️ {fav}", key=f"fav_{fav}"): st.session_state.selected_food = fav; st.rerun()

# Logic
if page == "About":
    st.title("ℹ️ Project Information")
    st.write("- **What it does:** Digital recipe book for viral TikTok trends.")
    st.write("- **Target User:** Aspiring home cooks and food lovers.")
    st.write("- **Inputs:** Ratings, reviews, sliders, and file uploads.")
    st.write("- **Outputs:** Recipe cards, interactive timers, and animations.")
else:
    if st.session_state.selected_food is None:
        st.title("🍔 Snackverse 2026")
        cols = st.columns(3)
        for i, (name, data) in enumerate(recipes.items()):
            with cols[i % 3]:
                try:
                    st.image(data["img"], use_container_width=True)
                except:
                    st.warning("Image missing")
                if st.button(f"{data['emoji']} {name}", key=name, use_container_width=True):
                    st.session_state.selected_food = name; st.rerun()
                st.write(f"Rating: {'⭐' * data['rating']}")
    else:
        food = st.session_state.selected_food
        data = recipes[food]
        if st.button("⬅️ Back to Gallery"): st.session_state.selected_food = None; st.rerun()
        
        c1, c2 = st.columns([1, 1.5])
        with c1:
            try: st.image(data["img"], use_container_width=True)
            except: st.error("Image not found.")
            st.metric("Difficulty", data["diff"])
        with c2:
            st.header(f"{food} {data['emoji']}")
            st.write(f"**Rating:** {'⭐' * data['rating']}")
            st.subheader("🛒 What You Need")
            st.write(f"To make this delicious {food}, you'll need {', '.join(data['ing'])}.")
            st.subheader("👨‍🍳 How to Prepare")
            st.write(" ".join(data["inst"]))
            st.divider()
            if st.button("⏱️ Start Cooking Timer"):
                with st.empty():
                    for s in range(5, 0, -1): st.write(f"Cooking... {s}s"); time.sleep(1)
                    st.success("Your dish is ready!")
            st.slider("Review this recipe", 1, 5, 3)
            st.text_area("Your thoughts:")
            st.file_uploader("Upload your dish", type=["jpg"])
            if st.button("Submit Review"): st.balloons()
            st.progress(70)
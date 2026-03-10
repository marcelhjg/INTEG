import streamlit as st
import time

# Page Config
st.set_page_config(page_title="Snackverse", layout="wide", page_icon="🍔")

# Purple Theme
st.markdown("""
<style>
.stApp { background-color: #E6E6FA; }
h1, h2, h3 { color: #CF9FFF; }
.stButton>button { background-color: #9b59ff; color: white; border-radius: 10px; }
.stButton>button:hover { background-color: #7a3cff; color: white; }
</style>
""", unsafe_allow_html=True)

# Recipe Database
recipes = {
    "Ilocos Empanada": {
        "emoji": "🥟", "img": "image/1.png", "rating": 5, "diff": "Hard", 
        "ing": ["rice flour", "atsuete-infused water", "grated green papaya", "skinless longganisa", "fresh egg"], 
        "inst": ["Start by mixing the rice flour with atsuete-infused water until you get that signature orange dough. Flatten small portions of the dough thinly on a plastic sheet, then generously layer the grated green papaya, savory longganisa, and a fresh egg right in the center. Carefully fold the dough over to seal the edges tight and deep-fry in hot oil until the crust becomes perfectly golden brown and crispy."]
    },
    "Dubai Chewy Cookie": {
        "emoji": "🍪", "img": "image/2.png", "rating": 5, "diff": "Medium", 
        "ing": ["creamed butter", "granulated sugar", "all-purpose flour", "pistachio cream", "kunafa pastry"], 
        "inst": ["Cream the butter and sugar until the mixture is light and fluffy before gradually folding in the flour to form a soft dough. Stuff the center of each dough ball with a generous amount of rich pistachio cream and crunchy kunafa pastry bits. Bake in a preheated oven at 180°C until the edges are nicely golden and the center remains delightfully chewy."]
    },
    "Tofu Squares": {
        "emoji": "🍲", "img": "image/3.png", "rating": 4, "diff": "Easy", 
        "ing": ["firm tofu cubes", "cornstarch", "soy sauce", "honey"], 
        "inst": ["Cube the tofu into bite-sized pieces and coat them evenly in cornstarch for that extra crunch. Air fry the tofu squares until they are crispy on the outside, then toss them immediately in a sweet and savory glaze made from soy sauce and honey until well-coated."]
    },
    "Samyang Omelette": {
        "emoji": "🍳", "img": "image/4.png", "rating": 4, "diff": "Easy", 
        "ing": ["Samyang spicy noodles", "two fresh eggs", "cheese slice"], 
        "inst": ["Cook the noodles until al dente and toss them well in the spicy sauce provided. Whisk the eggs thoroughly and pour them into a hot pan to make an omelette, then fold the spicy noodles into the center and top with a cheese slice until it perfectly melts."]
    },
    "Cheesy Corn": {
        "emoji": "🌽", "img": "image/5.png", "rating": 4, "diff": "Easy", 
        "ing": ["sweet corn kernels", "mayonnaise", "mozzarella cheese", "butter"], 
        "inst": ["Sauté the sweet corn in a pan with butter until it's fragrant and slightly toasted. Stir in the mayonnaise to add that creamy richness, then top it all off with a generous heap of mozzarella cheese and let it melt until it’s perfectly gooey and stretchy."]
    },
    "Spud": {
        "emoji": "🥔", "img": "image/6.png", "rating": 4, "diff": "Medium", 
        "ing": ["large potato", "salted butter", "grated cheese", "crispy bacon bits"], 
        "inst": ["Bake the potato in the oven until the inside is tender and soft. Slice it open to mash the fluffy interior with a generous knob of butter, then finish the dish by loading it up with plenty of grated cheese and crispy bacon bits."]
    },
    "Tiramisu": {
        "emoji": "🍰", "img": "image/7.png", "rating": 5, "diff": "Medium", 
        "ing": ["ladyfingers", "strong brewed espresso", "whipped mascarpone cream"], 
        "inst": ["Briefly dip the ladyfingers into the strong espresso, making sure they soak up just enough coffee without getting too soft. Create alternating layers of the coffee-soaked biscuits and the rich mascarpone cream in a dish, then chill in the refrigerator for at least four hours to let the flavors fuse perfectly."]
    },
    "Grilled Scallops": {
        "emoji": "🐚", "img": "image/8.png", "rating": 5, "diff": "Medium", 
        "ing": ["fresh scallops", "melted butter", "minced garlic", "fresh lemon juice"], 
        "inst": ["Clean the scallops and pat them dry to ensure a beautiful sear. Sauté the minced garlic in melted butter, then brush this savory mixture over the scallops before tossing them on a hot grill until they turn opaque. Serve immediately with a fresh squeeze of lemon to highlight their natural sweetness."]
    },
    "Chocolate Xiao Long Bao": {
        "emoji": "🥟", "img": "image/9.png", "rating": 5, "diff": "Hard", 
        "ing": ["dumpling wrappers", "dark chocolate ganache", "heavy cream"], 
        "inst": ["Prepare a rich ganache by melting dark chocolate with warm heavy cream and chilling it in the fridge until firm. Place a small, chilled scoop of the ganache in the center of each dumpling wrapper, then pleat the edges tightly to seal the chocolate inside. Steam the parcels for five minutes until the wrapper is soft and the center is molten."]
    },
    "Buko Sherbet": {
        "emoji": "🥥", "img": "image/10.png", "rating": 5, "diff": "Easy", 
        "ing": ["fresh young coconut meat", "chilled coconut water", "condensed milk", "finely crushed ice"], 
        "inst": ["Blend the young coconut meat and chilled coconut water until the mixture is perfectly smooth. Stir in the condensed milk to add that creamy sweetness, freeze the base for at least an hour to set, and serve it over a refreshing bed of finely crushed ice."]
    }
}

# State initialization
if "selected_food" not in st.session_state: 
    st.session_state.selected_food = None

# Sidebar
with st.sidebar:
    st.title("📱 FYP Trends")
    page = st.radio("Navigation", ["Home", "About"])
    st.markdown("---")
    st.subheader("⭐ Creator's Favorites")
    favorites = ["Ilocos Empanada", "Tofu Squares", "Buko Sherbet"]
    for fav in favorites:
        if st.button(f"❤️ {fav}", key=f"fav_{fav}"): 
            st.session_state.selected_food = fav
            st.rerun()

# Logic
if page == "About":
    st.title("ℹ️ Project Information")
    st.info("Created for Streamlit UI Assignment")
    st.write("- **What it does:** Digital recipe book for TikTok trends.")
    st.write("- **Target User:** Aspiring home cooks and food enthusiasts.")
    st.write("- **Inputs:** Ratings, notes, sliders, and photo uploads.")
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
                    st.session_state.selected_food = name
                    st.rerun()
                st.write(f"Rating: {'⭐' * data['rating']}")
    else:
        food = st.session_state.selected_food
        data = recipes[food]
        if st.button("⬅️ Back to Gallery"): 
            st.session_state.selected_food = None
            st.rerun()
        
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
                    for s in range(5, 0, -1): 
                        st.write(f"Cooking... {s}s")
                        time.sleep(1)
                    st.success("Your dish is ready!")
            st.slider("Review this recipe", 1, 5, 3)
            st.text_area("Your thoughts:")
            st.file_uploader("Upload your dish", type=["jpg"])
            if st.button("Submit Review"): st.balloons()
            st.progress(70)
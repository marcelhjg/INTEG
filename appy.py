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
    "Ilocos Empanada": {
        "emoji": "🥟", "img": "image/1.png", "rating": 5, "diff": "Hard", 
        "ing": ["rice flour", "atsuete water", "grated green papaya", "skinless longganisa", "fresh egg"], 
        "inst": ["Begin by kneading the rice flour mixed with atsuete water to achieve that vibrant orange dough. Flatten small portions thinly on a plastic sheet, then generously layer the grated green papaya, savory longganisa, and a fresh egg in the center. Carefully fold the dough over to seal the edges, ensuring the filling is snug. Deep-fry in hot oil until the crust turns perfectly golden and crunchy."]
    },
    "Buko Sherbet": {
        "emoji": "🥥", "img": "image/6.png", "rating": 5, "diff": "Easy", 
        "ing": ["young coconut meat", "fresh coconut water", "condensed milk", "crushed ice"], 
        "inst": ["Scoop out the soft meat from the young coconut and blend it with fresh coconut water until you reach a silky consistency. Gently stir in the condensed milk to balance the sweetness of the coconut. Pour this mixture into a container and freeze for at least an hour to let it firm up. Finally, serve it over a heap of crushed ice for that ultimate tropical refreshment."]
    },
    "Tofu Sisig": {
        "emoji": "🍲", "img": "image/3.png", "rating": 4, "diff": "Medium", 
        "ing": ["firm tofu", "calamansi", "soy sauce", "red onions", "chili peppers"], 
        "inst": ["Start by frying the cubed tofu until it becomes crispy and golden brown on all sides. In a separate bowl, toss the fried tofu with freshly squeezed calamansi, savory soy sauce, chopped red onions, and a kick of spicy chili peppers. Serve it hot on a sizzling plate to capture that authentic street-food aroma."]
    },
    "Adobo Flakes": {
        "emoji": "🍗", "img": "image/4.png", "rating": 5, "diff": "Medium", 
        "ing": ["cooked chicken adobo", "garlic", "vegetable oil"], 
        "inst": ["Take your leftover chicken adobo and carefully shred the meat into thin, bite-sized strips. Heat a generous amount of oil in a pan and fry the shredded chicken along with plenty of minced garlic until the edges turn dark and extra crispy. This crunchy, savory treat is best paired with a mound of steaming garlic rice."]
    },
    "Pinoy-Style Spaghetti": {
        "emoji": "🍝", "img": "image/5.png", "rating": 5, "diff": "Easy", 
        "ing": ["spaghetti noodles", "sweet-style tomato sauce", "hotdogs", "ground pork", "cheddar cheese"], 
        "inst": ["Boil your spaghetti noodles until al dente. In a pan, sauté the ground pork and sliced hotdogs, then pour in the signature sweet-style tomato sauce, letting it simmer until the flavors meld. Toss the cooked noodles into the sauce until every strand is coated, and top it off with a generous amount of grated cheddar cheese."]
    },
    "Mango Graham Float": {
        "emoji": "🥭", "img": "image/10.png", "rating": 5, "diff": "Easy", 
        "ing": ["ripe mangoes", "graham crackers", "all-purpose cream", "condensed milk"], 
        "inst": ["Whisk together the all-purpose cream and condensed milk until the mixture is thick and smooth. Create a foundation by laying graham crackers at the bottom of a container, followed by a layer of the cream mixture and a generous amount of sliced ripe mangoes. Repeat these layers until the container is full, then chill until the float is perfectly set and creamy."]
    },
    "Tiramisu": {
        "emoji": "🍰", "img": "image/7.png", "rating": 5, "diff": "Medium", 
        "ing": ["ladyfingers", "strong espresso", "mascarpone cheese"], 
        "inst": ["Quickly dip each ladyfinger into the strong espresso, making sure not to soak them too long. Create alternating layers of the coffee-soaked biscuits and a rich, whipped mascarpone cream mixture. Allow the dessert to rest in the refrigerator for at least four hours, letting the coffee and cream fuse into a heavenly, melt-in-your-mouth experience."]
    },
    "Grilled Scallops": {
        "emoji": "🐚", "img": "image/8.png", "rating": 5, "diff": "Medium", 
        "ing": ["fresh scallops", "salted butter", "minced garlic", "lemon wedges"], 
        "inst": ["Thoroughly clean the scallops and pat them dry. Sauté a generous amount of minced garlic in melted butter, then pour this mixture over the scallops before placing them on a hot grill. Cook them briefly until they turn opaque, and serve with a fresh squeeze of lemon to highlight the natural sweetness of the seafood."]
    },
    "Chocolate Xiao Long Bao": {
        "emoji": "🥟", "img": "image/9.png", "rating": 5, "diff": "Hard", 
        "ing": ["dumpling wrappers", "dark chocolate", "heavy cream"], 
        "inst": ["Create a rich ganache by melting dark chocolate with warm heavy cream, then set it in the fridge until it becomes firm. Carefully place a small spoonful of the ganache in the center of a dumpling wrapper, pleating the edges tightly to seal the chocolate inside. Steam these delicate parcels for just five minutes until the wrapper is soft and the center is molten."]
    },
    "Dubai Chewy Cookie": {
        "emoji": "🍪", "img": "image/2.png", "rating": 5, "diff": "Medium", 
        "ing": ["butter", "sugar", "all-purpose flour", "pistachio cream", "kunafa pastry"], 
        "inst": ["Cream the butter and sugar until the texture is light and fluffy. Slowly fold in the flour to create a soft, manageable dough. Stuff the center of each ball with a rich mixture of pistachio cream and crunchy kunafa pastry, then bake at 180°C until the edges are golden and the center remains delightfully chewy."]
    }
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
   if page == "About":
    st.title("ℹ️ Project Information")
    st.info("Created for Streamlit UI Assignment")
    st.write("- **What it does:** This app works as a digital recipe book that collects popular and trending foods seen on TikTok. Users can browse different viral dishes, view their ingredients, and follow step-by-step cooking instructions to recreate them at home.")
    st.write("- **Target User:** The app is designed for aspiring home cooks, students, food enthusiasts, and anyone who enjoys trying viral food trends from social media.")
    st.write("- **Inputs:** The app collects user interactions such as star ratings for recipes, text inputs for personal cooking notes, sliders for preferences, and optional file uploads where users can share photos of the dishes they cooked.")
    st.write("- **Outputs:** The app displays detailed recipe cards that include images, ingredients, and instructions. It also shows feedback such as recipe ratings, progress indicators, and visual confirmations to enhance the user experience.")
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
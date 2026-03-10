import streamlit as st
import time

# ==========================================
# 1. RECIPE DATABASE
# ==========================================
# Ginamit natin ito para madaling i-manage ang data
recipes = {
    "Ilocos Empanada": {
        "emoji": "🥟", "img": "ilocos_empanada.jpg", "rating": 4.8, "level": "Medium",
        "ing": ["2 cups rice flour", "1/2 cup water", "Green papaya", "Longganisa", "1 egg"],
        "inst": ["Mix rice flour and water.", "Flatten batter on plastic.", "Add filling.", "Deep fry until orange."]
    },
    "Dubai Chewy Cookie": {
        "emoji": "🍪", "img": "dubai_cookie.jpg", "rating": 4.9, "level": "Hard",
        "ing": ["1 cup butter", "1 cup sugar", "2 cups flour", "Pistachio cream", "Kunafa pastry"],
        "inst": ["Cream butter and sugar.", "Fold in flour.", "Stuff with pistachio and kunafa.", "Bake at 180°C."]
    },
    "Bell Pepper Cream Cheese w/ Cheetos": {
        "emoji": "🌶️", "img": "bell_pepper.jpg", "rating": 4.5, "level": "Easy",
        "ing": ["Mini bell peppers", "Cream cheese", "Flamin' Hot Cheetos", "Bagel seasoning"],
        "inst": ["Slice peppers.", "Fill with cream cheese.", "Top with crushed Cheetos."]
    },
    "Tofu Squares": {
        "emoji": "🍲", "img": "tofu.jpg", "rating": 4.2, "level": "Easy",
        "ing": ["Firm tofu", "Cornstarch", "Soy sauce", "Honey", "Garlic"],
        "inst": ["Cube tofu.", "Coat in starch.", "Air fry until crispy.", "Toss in sauce."]
    },
    "Samyang Omelette": {
        "emoji": "🍳", "img": "samyang.jpg", "rating": 4.7, "level": "Easy",
        "ing": ["Samyang Buldak noodles", "2 Eggs", "Cheese slice", "Seaweed"],
        "inst": ["Boil noodles.", "Mix with sauce.", "Fold into a beaten egg omelette base."]
    },
    "Cheesy Corn": {
        "emoji": "🌽", "img": "corn.jpg", "rating": 4.6, "level": "Easy",
        "ing": ["Sweet corn", "Mayonnaise", "Mozzarella", "Butter"],
        "inst": ["Sauté corn in butter.", "Mix mayo and cheese.", "Torch or bake until melted."]
    },
    "Spud": {
        "emoji": "🥔", "img": "spud.jpg", "rating": 4.4, "level": "Medium",
        "ing": ["Large potato", "Butter", "Cheese", "Sour cream", "Bacon bits"],
        "inst": ["Bake or boil potato.", "Mash the inside with butter.", "Add toppings."]
    },
    "Tiramisu": {
        "emoji": "🍰", "img": "tiramisu.jpg", "rating": 5.0, "level": "Medium",
        "ing": ["Ladyfingers", "Espresso", "Mascarpone", "Cocoa powder"],
        "inst": ["Dip biscuits in coffee.", "Layer with mascarpone.", "Dust cocoa.", "Chill for 4 hours."]
    },
    "Panipuri": {
        "emoji": "🥣", "img": "panipuri.jpg", "rating": 4.3, "level": "Medium",
        "ing": ["Puri shells", "Spiced potatoes", "Tamarind water", "Chutney"],
        "inst": ["Poke hole in puri.", "Fill with potato mixture.", "Dip in flavored water."]
    }
}

# ==========================================
# 2. SIDEBAR NAVIGATION & CONFIG
# ==========================================
st.set_page_config(page_title="TikTok Recipe Lab", layout="wide") # Extra: Page Config

st.sidebar.title("👨‍🍳 Viral Recipe Lab")
# Component 1: st.sidebar.radio
page = st.sidebar.radio("Main Menu", ["Home / Discover", "About the App"])

# Component 2: st.sidebar.toggle (Extra Merit: Toggle component)
show_details = st.sidebar.toggle("Show Extra Stats", value=True)

# ==========================================
# 3. ABOUT PAGE
# ==========================================
if page == "About the App":
    # Component 3: st.title
    st.title("ℹ️ About This Project")
    
    # Component 4: st.info
    st.info("Course Requirement: Streamlit UI Flow Demonstration (No API)")

    # Component 5: st.markdown
    st.markdown("""
    ### 🎯 Use-Case
    Ang **TikTok Recipe Lab** ay isang interactive digital cookbook. Ginawa ito para matulungan ang mga users na mahanap ang pinakasikat na pagkain sa TikTok (Batch 2026) nang hindi na kailangang mag-scroll nang matagal sa social media.

    ### 👥 Target User
    - **Home Cooks:** Mga gustong sumubok ng viral food trends.
    - **Content Creators:** Mga naghahanap ng inspiration para sa kanilang susunod na video.
    
    ### 📥 Inputs & 📤 Outputs
    - **Inputs:** Recipe selection (selectbox), servings (number input), user reviews (text area), rating (slider), profile color (color picker), at file uploads.
    - **Outputs:** Ingredients list, step-by-step instructions, popularity metrics, at dynamic cooking status.
    """)
    
    # Component 6: st.divider
    st.divider()
    # Component 7: st.link_button (Extra Merit: Link Button)
    st.link_button("View Developer Portfolio", "https://github.com")

# ==========================================
# 4. HOME PAGE / DISCOVER
# ==========================================
else:
    # Component 8: st.header
    st.header("🍔 Discover TikTok's Best Recipes")
    
    # Component 9: st.tabs
    tab_recipe, tab_community = st.tabs(["📖 Recipe Book", "💬 Community Hub"])

    with tab_recipe:
        # Component 10: st.selectbox
        food_choice = st.selectbox("Pumili ng pagkaing lulutuin:", list(recipes.keys()))
        selected = recipes[food_choice]

        # Component 11: st.columns
        col1, col2 = st.columns([1, 1])

        with col1:
            # Component 12: st.image (Placeholder handling)
            try:
                st.image(selected['img'], use_container_width=True)
            except:
                st.warning(f"Image file '{selected['img']}' not found. Please add it to your folder.")
        
        with col2:
            # Component 13: st.subheader
            st.subheader(f"{food_choice} {selected['emoji']}")
            
            # Component 14: st.metric
            st.metric("Popularity", f"{selected['rating']} / 5.0", delta="Trending Now")
            
            # Component 15: st.select_slider (Extra Merit: Select Slider)
            servings = st.select_slider("Adjust Servings:", options=[1, 2, 4, 6, 8], value=2)

            if show_details:
                # Component 16: st.code (Extra Merit: Code display for difficulty)
                st.code(f"Difficulty Level: {selected['level']}", language='python')

        st.divider()

        # Component 17: st.columns for lists
        c1, c2 = st.columns(2)
        with c1:
            st.write("### 🛒 Ingredients")
            for item in selected['ing']:
                # Component 18: st.write
                st.write(f"- {item}")
        
        with c2:
            st.write("### 📝 Cooking Steps")
            for i, step in enumerate(selected['inst'], 1):
                st.write(f"{i}. {step}")

        # Component 19: st.checkbox
        if st.checkbox("Mark as 'Ready to Cook'"):
            # Component 20: st.success
            st.success("Ingredients prepared! Let's start.")

    with tab_community:
        st.write("### Tell us what you think!")
        # Component 21: st.slider
        user_rating = st.slider("Rate this recipe:", 0, 10, 8)
        # Component 22: st.text_area
        user_note = st.text_area("Add your personal cooking tips:")
        # Component 23: st.color_picker
        st.color_picker("Pick a theme for your review card:")
        # Component 24: st.file_uploader
        st.file_uploader("Upload your result photo", type=['png', 'jpg'])

    # ==========================================
    # 5. ACTION & FEEDBACK (Advanced UI)
    # ==========================================
    st.divider()
    # Component 25: st.button
    if st.button("🚀 Post to TikTok Community"):
        # Component 26: st.status (Extra Merit: Status updates)
        with st.status("Processing your review...", expanded=True) as status:
            time.sleep(1)
            st.write("Scanning for quality...")
            time.sleep(1)
            st.write("Syncing with Community Feed...")
            status.update(label="Review Posted!", state="complete", expanded=False)
        
        # Component 27: st.balloons
        st.balloons()
        # Component 28: st.toast (Extra Merit: Toast notification)
        st.toast(f"Successfully shared {food_choice} review!", icon='✅')

    # Component 29: st.expander
    with st.expander("❓ Common FAQs"):
        st.write("Can I use an air fryer? - Yes, for most fried recipes here!")

    # Component 30: st.progress
    st.write("Your Cooking Profile Level")
    st.progress(65)
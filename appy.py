import streamlit as st

# =======================
# Sidebar / Navigation
# =======================
st.sidebar.title("🍴 Trending Recipes")
page = st.sidebar.radio("Go to", ["Home", "About"])

# =======================
# About Page
# =======================
if page == "About":
    st.title("About TikTok Trending Recipes App")
    st.markdown("""
    **What the app does:**  
    This app showcases trending recipes from TikTok. Click on a food name to view its recipe and instructions.  

    **Target user:**  
    Food enthusiasts, home cooks, and anyone looking to try viral TikTok recipes.  

    **Inputs collected:**  
    - Food selection  
    - Optional: customizations (servings, spice level, notes, photo upload)  

    **Outputs shown:**  
    - Recipe ingredients  
    - Step-by-step cooking instructions  
    - Optional pictures/videos of the dish
    """)
    st.image("about_placeholder.jpg", caption="Sample trending dishes")  # Replace with your image

# =======================
# Home / Recipe Page
# =======================
else:
    st.title("🍔 TikTok Trending Recipes 2026")

    # Trending recipe list
    trending_foods = [
        "Ilocos Empanada",
        "Dubai Chewy Cookie",
        "Bell Pepper Cream Cheese with Cheetos",
        "Tofu Squares",
        "Samyang Omelette",
        "Cheesy Corn",
        "Spud",
        "Tiramisu",
        "Panipuri"
    ]

    # Select a recipe
    food_choice = st.selectbox("Select a trending food:", trending_foods)

    # =======================
    # Recipe Sections
    # =======================
    if food_choice == "Ilocos Empanada":
        st.header("Ilocos Empanada 🥟")
        st.image("ilocos_empanada.jpg", caption="Ilocos Empanada")  
        st.subheader("Ingredients")
        st.write("""
        - 2 cups rice flour  
        - 1/2 cup water  
        - 1/2 cup grated green papaya  
        - 1/2 cup longganisa (Filipino sausage)  
        - 1 egg  
        - Oil for frying
        """)
        st.subheader("Instructions")
        st.write("""
        1. Mix rice flour and water to make a thin batter.  
        2. Heat a thin layer of oil in a pan, pour batter to make thin pancake-like base.  
        3. Add grated papaya, longganisa, and egg on top.  
        4. Fold and seal edges, fry until golden brown.  
        5. Serve hot!
        """)
        st.checkbox("I tried this recipe!")

    elif food_choice == "Dubai Chewy Cookie":
        st.header("Dubai Chewy Cookie 🍪")
        st.image("dubai_cookie.jpg", caption="Dubai Chewy Cookie")  
        st.subheader("Ingredients")
        st.write("""
        - 1 cup butter, softened  
        - 1 cup sugar  
        - 2 cups all-purpose flour  
        - 1 tsp baking powder  
        - 1 tsp vanilla extract  
        - Chocolate chips (optional)
        """)
        st.subheader("Instructions")
        st.write("""
        1. Preheat oven to 180°C (350°F).  
        2. Cream butter and sugar together.  
        3. Add flour, baking powder, and vanilla extract. Mix well.  
        4. Fold in chocolate chips.  
        5. Scoop onto baking tray, bake for 12-15 minutes.  
        6. Cool and enjoy!
        """)
        st.checkbox("I tried this recipe!")

    elif food_choice == "Bell Pepper Cream Cheese with Cheetos":
        st.header("Bell Pepper Cream Cheese w/ Cheetos 🌶️🧀")
        st.image("bell_pepper_cheese.jpg", caption="Bell Pepper Cream Cheese with Cheetos")  
        st.subheader("Ingredients")
        st.write("""
        - 2 bell peppers, sliced  
        - 100g cream cheese  
        - 1 cup crushed Cheetos  
        - 1 tbsp olive oil  
        - Salt and pepper
        """)
        st.subheader("Instructions")
        st.write("""
        1. Sauté bell peppers in olive oil until tender.  
        2. Mix cream cheese and crushed Cheetos in a bowl.  
        3. Stuff bell peppers with cream cheese mixture.  
        4. Sprinkle extra crushed Cheetos on top.  
        5. Bake at 180°C (350°F) for 10 minutes.  
        6. Serve warm.
        """)
        st.checkbox("I tried this recipe!")

    elif food_choice == "Tofu Squares":
        st.header("Tofu Squares 🍲")
        st.image("tofu_squares.jpg", caption="Tofu Squares")  
        st.subheader("Ingredients")
        st.write("""
        - 1 block firm tofu, cubed  
        - 2 tbsp soy sauce  
        - 1 tbsp cornstarch  
        - Oil for frying  
        - Optional: green onions
        """)
        st.subheader("Instructions")
        st.write("""
        1. Marinate tofu cubes in soy sauce for 10 minutes.  
        2. Coat tofu lightly with cornstarch.  
        3. Fry until golden and crispy.  
        4. Garnish with chopped green onions.  
        5. Serve with dipping sauce.
        """)
        st.checkbox("I tried this recipe!")

    elif food_choice == "Samyang Omelette":
        st.header("Samyang Omelette 🍳🌶️")
        st.image("samyang_omelette.jpg", caption="Samyang Omelette")  
        st.subheader("Ingredients")
        st.write("""
        - 2 packs Samyang noodles  
        - 2 eggs  
        - 1 tbsp oil  
        - Optional: cheese, green onions
        """)
        st.subheader("Instructions")
        st.write("""
        1. Cook Samyang noodles according to package instructions.  
        2. Heat oil in pan, pour beaten eggs to make omelette base.  
        3. Add cooked noodles on top, fold omelette.  
        4. Top with cheese and green onions.  
        5. Serve hot.
        """)
        st.checkbox("I tried this recipe!")

    elif food_choice == "Cheesy Corn":
        st.header("Cheesy Corn 🌽🧀")
        st.image("cheesy_corn.jpg", caption="Cheesy Corn")  
        st.subheader("Ingredients")
        st.write("""
        - 2 cups corn kernels  
        - 1/2 cup mayonnaise  
        - 1/2 cup grated cheese  
        - 1 tbsp butter  
        - Optional: chili flakes
        """)
        st.subheader("Instructions")
        st.write("""
        1. Sauté corn in butter until soft.  
        2. Mix in mayonnaise and cheese.  
        3. Cook for 2-3 minutes until cheese melts.  
        4. Sprinkle chili flakes if desired.  
        5. Serve warm.
        """)
        st.checkbox("I tried this recipe!")

    elif food_choice == "Spud":
        st.header("Spud 🥔")
        st.image("spud.jpg", caption="Spud")  
        st.subheader("Ingredients")
        st.write("""
        - 3 large potatoes  
        - 2 tbsp butter  
        - 1/2 cup grated cheese  
        - Salt and pepper  
        - Optional: herbs
        """)
        st.subheader("Instructions")
        st.write("""
        1. Boil potatoes until tender, then slice or cube.  
        2. Sauté with butter, add cheese, salt, pepper, and herbs.  
        3. Cook until cheese melts.  
        4. Serve hot.
        """)
        st.checkbox("I tried this recipe!")

    elif food_choice == "Tiramisu":
        st.header("Tiramisu 🍰")
        st.image("tiramisu.jpg", caption="Tiramisu")  
        st.subheader("Ingredients")
        st.write("""
        - 1 pack ladyfinger biscuits  
        - 1 cup mascarpone cheese  
        - 1/2 cup sugar  
        - 1/2 cup coffee, cooled  
        - Cocoa powder for topping
        """)
        st.subheader("Instructions")
        st.write("""
        1. Dip ladyfingers in coffee and layer in dish.  
        2. Mix mascarpone and sugar, spread over biscuits.  
        3. Repeat layers.  
        4. Dust cocoa powder on top.  
        5. Chill for 2-3 hours before serving.
        """)
        st.checkbox("I tried this recipe!")

    elif food_choice == "Panipuri":
        st.header("Panipuri 🥣")
        st.image("panipuri.jpg", caption="Panipuri")  
        st.subheader("Ingredients")
        st.write("""
        - 20-25 puris (hollow crisp shells)  
        - 1 cup boiled chickpeas  
        - 1 cup boiled potatoes, cubed  
        - 1/2 cup tamarind chutney  
        - 1/2 cup mint chutney  
        - Optional: onion, spices
        """)
        st.subheader("Instructions")
        st.write("""
        1. Mix chickpeas and potatoes with spices.  
        2. Fill puris with mixture.  
        3. Add chutneys to taste.  
        4. Serve immediately and enjoy!
        """)
        st.checkbox("I tried this recipe!")

    # Optional UI components for interactivity
    st.expander("💡 Cooking Tips"):
        st.write("Adjust seasoning to taste. Try different toppings for variety!")

    st.text_input("Add your own recipe note:")
    st.slider("How much did you like this recipe? 🍴", 0, 10, 5)
    st.number_input("Number of servings you want to cook:", min_value=1, max_value=10, value=2)
    st.color_picker("Pick a color for your dish presentation:", "#ff0000")
    st.file_uploader("Upload your photo after cooking:", type=["jpg","png"])
    st.button("Save my experience")

    st.progress(70)
    st.metric("Recipe Popularity", "🔥 4.5/5 stars", "⬆️ 0.2")
from src.domain.recipe.models import Recipe, Owner, RecipeAdditionalInformation, NutritionValue, ScaleOption, \
    Ingredient, SimpleStep, NewRecipe
from src.domain.recipe.repository import AbstractRecipeRepository


class LocalRecipe(AbstractRecipeRepository):
    def __init__(self):
        self.recipe = dict(
            title="Homemade Individual Pizza",
            description="The Best Michelin pizza",
            pictures_url=[
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ36kjyynbamjmpKJo5Jq-38Uw9NpF31G4EaA&usqp=CAU",
                "https://www.recipetineats.com/wp-content/uploads/2020/05/Pepperoni-Pizza_5-SQjpg.jpg",
                "https://www.foodandwine.com/thmb/CGXpgjWOgHWv9TsqyMoLyl5cYrs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/soppressata-pizza-with-calabrian-chile-hot-honey-FT-RECIPE0422-827abb3537834dbcb6ab0bbd6efece39.jpg",
                "https://realfood.tesco.com/media/images/1400x919-MargaritaPizza-555a4065-2573-4b41-bcf3-7193cd095d8f-0-1400x919.jpg",
                "https://www.chuckecheese.com/wp-content/uploads/2022/04/CEC-22-0063-Website-Menu-Page-Update_stuffed-crust.jpg",
                "https://www.history.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTYyMTgyOTYzMDk2NzkwODQ5/pizza-gettyimages-638790274.jpg",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ36kjyynbamjmpKJo5Jq-38Uw9NpF31G4EaA&usqp=CAU",
                "https://www.recipetineats.com/wp-content/uploads/2020/05/Pepperoni-Pizza_5-SQjpg.jpg",
                "https://www.foodandwine.com/thmb/CGXpgjWOgHWv9TsqyMoLyl5cYrs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/soppressata-pizza-with-calabrian-chile-hot-honey-FT-RECIPE0422-827abb3537834dbcb6ab0bbd6efece39.jpg",
                "https://realfood.tesco.com/media/images/1400x919-MargaritaPizza-555a4065-2573-4b41-bcf3-7193cd095d8f-0-1400x919.jpg",
                "https://www.chuckecheese.com/wp-content/uploads/2022/04/CEC-22-0063-Website-Menu-Page-Update_stuffed-crust.jpg",
                "https://www.history.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTYyMTgyOTYzMDk2NzkwODQ5/pizza-gettyimages-638790274.jpg",
            ],
            owner=Owner(
                id=31622,
                profile_picture="https://lh3.googleusercontent.com/a/AEdFTp5RFyK4Y_6lcNuJgw617FQe4h3yTfQhkzFjNvppzFA=s96-c",
                name='michael tugy',
                recipes=[],
                description=(
                    "John Smith, a skilled and experienced chef with a passion for creating delicious and visually"
                    " stunning dishes. With years of training and experience in some of the finest kitchens,"
                    " Chef Smith has honed his craft to perfection. From classic French cuisine to modern fusion"
                    " dishes, he is able to impress palates with his unique and inventive creations."
                    " He is dedicated to using only the freshest and highest-quality ingredients to ensure that"
                    " every dish is not just delicious but also healthy. Chef Smith's commitment to excellence is "
                    "evident in every plate he serves, making him a respected and sought-after chef in the culinary"
                    " world.")
            ),
            rating=[],
            tags=["Italian", "Street"],
            additional_info=RecipeAdditionalInformation(
                prep_time=30,
                work_time=45,
                servings=10,
            ),
            nutrition=[
                NutritionValue(
                    name='Calories',
                    value=500,
                ),
                NutritionValue(
                    name='Protain',
                    value=6.6,
                    scale=ScaleOption.gram
                ),
                NutritionValue(
                    name='Fat Saturated',
                    value=39.5,
                    scale=ScaleOption.gram
                ),
                NutritionValue(
                    name='Cholesterol',
                    value=6.6,
                    scale=ScaleOption.gram
                ),
                NutritionValue(
                    name='Energy',
                    value=39.5,
                    scale=ScaleOption.gram
                ),
            ],
            ingredients=[
                Ingredient(
                    name='pizza dough, divided',
                    value=24,
                    scale=ScaleOption.aunce
                ),
                Ingredient(
                    name='all-purpose flour, for dusting',
                    value=0.5,
                    scale=ScaleOption.cup
                ),
                Ingredient(
                    name='pesto',
                    value=1,
                    scale=ScaleOption.cup
                ),
                Ingredient(
                    name='grated mozzarella/provolone cheese',
                    value=3,
                    scale=ScaleOption.cup
                ),
                Ingredient(
                    name='roasted or confit garlic cloves',
                    value=1,
                    scale=ScaleOption.cup
                ),
                Ingredient(
                    name='red skinned potatoes, very thinly sliced',
                    value=4,
                ),
                Ingredient(
                    name='Italian seasoning',
                    value=0.5,
                    scale=ScaleOption.teaspoon
                ),
                Ingredient(
                    name='Olive oil',
                ),
            ],
            sections=[
                SimpleStep(
                    title='How to roll out pizza dough',
                    description='Start out with about 12-16 ounces of dough. I worked really hard to perfect my Pizza Dough'
                                ' recipe and highly recommend it! But any pizza dough, homemade or store bought, will work '
                                'for this recipe. Prepare your work surface. I know most people dust the counter with flour'
                                ', but I find that you risk ending up with a tougher dough this way. Too much flour = '
                                'tough crust. (If your dough is very sticky, using flour is going to be just fine). '
                                'Instead, of flour, I usually drizzle some olive oil right onto my counter. Use your '
                                'hands to rub it around. Place your ball of dough in the center of your work surface and '
                                'use your hands to press it down, starting from the center. Keep gently patting out the '
                                'dough, moving the dough outward from the center. I like to leave a pretty healthy crust '
                                'on the edges of my dough.',
                    pictures_url=[
                        "https://thefoodcharlatan.com/wp-content/uploads/2021/08/Homemade-Pizza-Recipe-1-Hour-or-Overnight-5-650x434.jpg"
                    ]
                ),
                SimpleStep(
                    title='How to par bake pizza crust',
                    description='Once the oven is up to temperature, we are going to do a 1 to 2 minute par bake. This step'
                                ' is technically not necessary, but I never skip it. It guarantees a thoroughly cooked '
                                'crust. Nobody wants a doughy pizza, yuck.Use your pizza peel or a flat baking sheet to '
                                'transfer the pizza dough and the parchment paper onto your pizza stone, pizza pan, or '
                                'baking sheet. (I always just pull on the paper to move it onto the stone). Transfer to '
                                'your stone or pan, shut the oven door and bake for 1-2 minutes, until it is slightly '
                                'puffed.',
                    pictures_url=[
                        "https://thefoodcharlatan.com/wp-content/uploads/2021/08/Homemade-Pizza-Recipe-1-Hour-or-Overnight-9-650x434.jpg"
                    ]
                ),
                SimpleStep(
                    title='Prepare your toppings',
                    description='Use your pizza peel or flat baking sheet to remove the pizza (still on the parchment '
                                'paper) from the oven. Poke down any bubbles. Leave the crust on the peel while you add '
                                'the toppings.',
                    pictures_url=[
                        "https://thefoodcharlatan.com/wp-content/uploads/2021/08/Homemade-Pizza-Recipe-1-Hour-or-Overnight-10-650x434.jpg"
                    ]
                ),
                SimpleStep(
                    title='What cheese is best for homemade pizza?',
                    description="Mozzarella, mozzarella!! It’s hardly even pizza if there is no mozzarella, right? You "
                                "need parmesan too. You can use pre-shredded regular (low moisture) mozzarella from the "
                                "store. It’s what I use most of the time. Mozzarella that you shred yourself is going to "
                                "melt better though. The shredded stuff has anti-caking agents added to it that inhibits "
                                "melting. If you are feeling fancy, you can also try out fresh mozzarella. (all the final "
                                "photos in this post actually show regular low-moisture mozzarella fyi) You can find fresh"
                                " in the deli section of your grocery store. While you are there, pick up a block of "
                                "parmesan so you can add a couple tablespoons over the toppings of your pizza. Parmesan "
                                "adds that little umph, don’t skip it.",
                    pictures_url=[
                        "https://thefoodcharlatan.com/wp-content/uploads/2021/08/Homemade-Pizza-Recipe-1-Hour-or-Overnight-12-650x434.jpg"
                    ]
                ),
                SimpleStep(
                    title='Homemade Pizza Ideas for Toppings – What can I put on a homemade pizza?',
                    description="The sky is the limit here! Some of my favorite pizza toppings. Just Cheese: don’t "
                                "underestimate the power of cheese. You need variety: Mozzarella, Fontina, Parmesan, "
                                "and Gorgonzola would be amazing. Pepperoni: Have you tried the new Hormel Cup n’ Crisp "
                                "Pepperoni? It’s what I’ve been searching for forever!! I love the pepperoni that shrinks"
                                " up and turns into ultra crispy cups. This gives you exactly that! I’ve never been able "
                                "to find it at the store, only in restaurants. So excited! (The photos on this post show "
                                "regular pepperoni, but there is a lil baby Cup n’ Crisp in this photo, can you see it?)"
                                "Supreme: pepperoni, mushroom, red/green bell pepper, red onion, black olives, fresh basil"
                                " Meat Lovers: Pepperoni, salami, Italian sausage, ham, bacon Hawaiian: Canadian bacon, "
                                "pineapple Margherita: fresh mozzarella, fresh basil, tomatoes BBQ: Use barbecue sauce "
                                "instead of tomato sauce, then rotisserie chicken, red onions, bacon Veggie pizza: spinach,"
                                " tomato, corn, peppers, red onion, mushrooms Buffalo: Use Frank’s sauce instead of tomato"
                                " sauce, then add rotisserie chicken, garlic, blue cheese, red onions",
                    pictures_url=[
                        "https://thefoodcharlatan.com/wp-content/uploads/2021/08/Homemade-Pizza-Recipe-1-Hour-or-Overnight-15-650x434.jpg"
                    ]
                ),
                SimpleStep(
                    title='How long to cook Homemade Pizza',
                    description="Once your pizza is in the oven, you need to cook it for about 8-12 minutes. This is of "
                                "course going to depend on how hot your oven is, and how thick your pizza is. The crust "
                                "should be golden brown, and the cheese should be bubbly and also starting to brown. If "
                                "you don’t have a pizza stone, use a spatula to lift the edge of your pizza to make sure "
                                "that it is browning all across the center on bottom. If the bottom is still white, you are"
                                " looking at a doughy pizza. No thanks. Leave it in longer.Try to minimize the time you "
                                "have your oven door open; every second that the oven is open, you are losing temperature."
                                " So keep checks to a minimum. If the top of your pizza is browning too quickly but the "
                                "bottom crust isn’t done (I’m telling you, this will never happen with a pizza stone) then"
                                " tent the top of the pizza with foil to slow browning. Do",
                    pictures_url=[
                        "https://thefoodcharlatan.com/wp-content/uploads/2021/08/Homemade-Pizza-Recipe-1-Hour-or-Overnight-17-650x975.jpg"
                    ]
                ),
                SimpleStep(
                    title='Do you need a pizza stone to make Homemade Pizza?',
                    description="Yes. And no. Here’s the thing, your oven kind of sucks at making pizza. I don’t care how "
                                "nice your oven is, unless it’s a specialty item, it only goes up to 550 degrees, max. "
                                "Pizza needs 700-1000 degrees to be cooked properly. The solution? A pizza stone. It turns"
                                " your wimpy oven into a mini brick oven! (Pretend that I remembered to remove the "
                                "parchment paper for this photo. The pizza should be directly on the stone. It’s not the "
                                "end of the world if you forget, I did it this way for years before I learned more about"
                                " stones.) Pizza stones are slabs of ceramic or stone that sit in a preheating oven,"
                                " absorbing tons of heat (thermal mass. Yep, we’re going there. Stay with me!) A pizza "
                                "stone mimics a brick oven, which is how pizza is traditionally made. The stone is a poor"
                                " conductor of heat, meaning your food is less likely to burn on the edges (as it would "
                                "with a metal pan at such a high temperature.) But it also has thermal mass, which stores"
                                " heat in the stone and provides inertia against temperature changes. In other words,"
                                " it heats the pizza more evenly. A pizza stone is going to actually regulate the "
                                "temperature of your oven.",
                    pictures_url=[
                        "https://thefoodcharlatan.com/wp-content/uploads/2021/08/Homemade-Pizza-Recipe-1-Hour-or-Overnight-16-650x434.jpg"
                    ]
                ),
                SimpleStep(
                    title='Baking pizza on an inverted baking sheet is a stupid idea',
                    description="I read about this method and tried it out. It was a bit of a disaster, truth be told. "
                                "You are supposed to turn a large baking sheet upside down in your oven, let it preheat "
                                "for about a half hour, then slide your pizza onto it. It did cook my pizza, in the end. "
                                "But it also made a huge mess when grease trickled off the edge of the pan onto the floor "
                                "of the oven (yes, my smoke alarms definitely went off!) The center of the pan bows up at"
                                " such a high temperature, making all your pizza toppings and grease slide to the edges. "
                                "I wouldn’t do this again. Instead, preheat your rimmed baking sheet (right side up), "
                                "sprinkle with cornmeal, and slide your pizza onto the center. This method is not going "
                                "to give you as crispy of a crust. The pizza I tested using this method had a texture like"
                                " a Papa Murphy’s Take and Bake Pizza. Kinda soggy on the bottom. But, it’ll do in a pinch",
                    pictures_url=[
                        "https://thefoodcharlatan.com/wp-content/uploads/2021/08/Homemade-Pizza-Recipe-1-Hour-or-Overnight-21-650x975.jpg"
                    ]
                ),
                SimpleStep(
                    title='Baking pizza on a pizza pan',
                    description="I have not personally tested making pizza on a pizza pan. It’s going to have the same "
                                "problem that a baking sheet does: the higher the temperature goes, the more likely it is "
                                "to burn (because metal conducts heat so well.) Tips for choosing a pizza pan: get one with"
                                " holes in the bottom (to help evaporation and achieve a crispier crust), and get one that"
                                " has NO non-stick coating. This Cuisinart pizza pan looks like a decent and affordable "
                                "option. Be sure to put another pan beneath it when baking, to catch any drips.",
                    pictures_url=[
                        "https://thefoodcharlatan.com/wp-content/uploads/2021/08/Homemade-Pizza-Recipe-1-Hour-or-Overnight-18-650x975.jpg"
                    ]
                ),
            ],
        )

    def get_recipe(self, recipe_id) -> Recipe:
        return Recipe(
            id=recipe_id,
            **self.recipe
        )

    def set_recipe(self, recipe_id: int, new_recipe: NewRecipe) -> Recipe:
        new_recipe = new_recipe.dict()
        owner = self.recipe['owner']
        owner.id = new_recipe.pop('owner_id')
        self.recipe = dict(
            owner=owner,
            **new_recipe,
        )
        return self.get_recipe(recipe_id)

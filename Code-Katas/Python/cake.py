# Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. 
# Can you help him to find out, how many cakes he could bake considering his recipes?

def cakes(recipe, available):

    lowest_batch_count = None

    for ingredient in recipe.keys():

        if ( ingredient in available ):

            batch_count = available[ ingredient ] // recipe[ingredient]

            if lowest_batch_count == None: 
                lowest_batch_count = batch_count
                
            if batch_count <= lowest_batch_count:
                lowest_batch_count = batch_count

        else:

            print( 'Missing ingredient from recipe: 0' )
            return 0

    print( lowest_batch_count )
    return lowest_batch_count

# TESTS 

recipe = {"flour": 500, "sugar": 200, "eggs": 1 };
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200};
# 2


# recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100};
# available = {"sugar": 500, "flour": 2000, "milk": 2000};
# # 0

# recipe = {"chocolate":69,"cocoa":16,"nuts":80}
# available = {"apples":2000,"sugar":6400,"pears":7200,"milk":800,"cocoa":0,"butter":9000,"flour":600,"eggs":4400,"nuts":1100,"chocolate":4500,"oil":900,"crumbles":4900,"cream":2500}
# # 0

# recipe = {"chocolate":0,"nuts":2,"pears":37}
# available = {"pears":5200,"apples":6800,"eggs":1000,"nuts":9900,"chocolate":500,"milk":7800,"cream":2600,"oil":2700,"butter":6100,"cocoa":800,"flour":4400,"crumbles":7600,"sugar":6400}

cakes(recipe, available)
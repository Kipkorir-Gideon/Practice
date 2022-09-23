var animals = {
    Zebra : {
        classification : "Mammal",
        appearance : ["White with black stripes", "4 legs", "looks like a doney"],
        habitat : "GRasslands",
        lifespan : 25,
        diet : "Herbivore",
        friendly : true
    },

    Crocodile : {
        classification : "Reptile",
        appearance : ["Long, wide mouth with many teeth", "Close relatives to dinossaurs", "Looks like a big lizard"],
        habitat : "Grasslands",
        lifespan : 100,
        diet : "Carnivore",
        friendly : false
    },
};

var ostrich = {
    classification : "Bird",
    appearance : ["Big, tall bird", "Has a long neck"],
    habitat : "Grasslands",
    lifespan : 45,
    diet : "Herbivore",
    friendly : true
};

animals.Ostrich = ostrich;

var shark =  {
    classification : "Fish",
    appearance : ["Sharp teeth", "Has fins", "Has gills"],
    habitat : "Water",
    lifespan : 30,
    diet : "Carnivore",
    friendly : true
};

animals.Shark = shark;

console.log(animals);
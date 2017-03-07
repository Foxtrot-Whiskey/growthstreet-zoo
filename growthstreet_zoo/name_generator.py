import random
import math


adjs = ['Autumn', 'Hidden', 'Bitter', 'Misty', 'Silent', 'Empty', 'Dry', 'Dark', 'Summer', 'Icy', 'Delicate', 'Quiet',
        'White', 'Cool', 'Spring', 'Winter', 'Patient', 'Twilight', 'Dawn', 'Crimson', 'Wispy', 'Weathered',
        'Blue', 'Billowing', 'Broken', 'Cold', 'Damp', 'Falling', 'Frosty', 'Green', 'Long', 'Late', 'Lingering',
        'Bold', 'Little', 'Morning', 'Muddy', 'Old', 'Red', 'Rough', 'Still', 'Small', 'Sparkling', 'Throbbing',
        'Shy', 'Wandering', 'Withered', 'Wild', 'Black', 'Young', 'Holy', 'Solitary', 'Fragrant', 'Aged',
        'Snowy', 'Proud', 'Floral', 'Restless', 'Divine', 'Polished', 'Ancient', 'Purple', 'Lively', 'Nameless']

nouns = ["waterfall", "river", "breeze", "moon", "rain", "wind", "sea", "morning", "snow", "lake", "sunset", "pine",
         "shadow", "leaf", "dawn", "glitter", "forest", "hill", "cloud", "meadow", "sun", "glade", "bird", "brook",
         "butterfly", "bush", "dew", "dust", "field", "fire", "flower", "firefly", "feather", "grass", "haze",
         "mountain", "night", "pond", "darkness", "snowflake", "silence", "sound", "sky", "shape", "surf", "thunder",
         "violet", "water", "wildflower", "wave", "water", "resonance", "sun", "wood", "dream", "cherry", "tree",
         "fog", "frost", "voice", "paper", "frog", "smoke", "star"]

def generate_name(separator='-'):
    adj = random.choice(adjs)
    noun = random.choice(nouns)
    return '{adj}{separator}{noun}'.format(adj=adj,
                                           noun=noun,
                                           separator=separator)

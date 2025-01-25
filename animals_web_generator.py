import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

def serialize_animal(animal):
    animal_name = animal['name']
    animal_diet = animal['taxonomy']['order']
    animal_location = ', '.join(animal['locations'])
    animal_type = animal['characteristics'].get('type', 'Unknown')

    # Create the HTML list item with the animal data
    return f'''
<li class="cards__item">
    <div class="card__title">{animal_name}</div><br/>
    <p class="card__text">
        <strong>Diet:</strong> {animal_diet}<br/>
        <strong>Location:</strong> {animal_location}<br/>
        <strong>Type:</strong> {animal_type}<br/>
    </p>
</li>
'''

for animal in animals_data:
    print(serialize_animal(animal))
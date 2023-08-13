import json

recommendation_data = []

def load_data():
    global recommendation_data
    try:
        with open('recommendation_data.json', 'r') as f:
            recommendation_data = json.load(f)
    except FileNotFoundError:
        recommendation_data = []

def get_recommendation_data():
    load_data()
    return recommendation_data

def update_recommendation_data(new_data):
    global recommendation_data
    recommendation_data = new_data
    with open('recommendation_data.json', 'w') as f:
        json.dump(recommendation_data, f)

def delete_recommendation_data():
    global recommendation_data
    recommendation_data = []
    with open('recommendation_data.json', 'w') as f:
        json.dump(recommendation_data, f)
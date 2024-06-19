import json

def load_rankings(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def format_rankings(rankings):
    formatted_rankings = {}
    for region in rankings:
        for country, rank in rankings[region].items():
            if rank.isdigit():  # Ensure the rank is a digit before adding
                formatted_rankings[country] = int(rank)
    return formatted_rankings

def print_rankings_dict(rankings_dict):
    print("D = {")
    for country, rank in sorted(rankings_dict.items(), key=lambda item: item[1]):  # Sort by rank
        print(f"    '{country}': {rank},")
    print("}")

if __name__ == "__main__":
    filename = "fifa_rankings.json"
    rankings = load_rankings(filename)
    formatted_rankings = format_rankings(rankings)
    print_rankings_dict(formatted_rankings)

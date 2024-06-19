import tkinter as tk
from tkinter import messagebox
import json

# Dictionaries to hold rankings for each region
rankings = {
    "EuroLib": {country: "" for country in ['Albania', 'Austria', 'Belgium', 'Bosnia & Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'England', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Montenegro', 'Netherlands', 'North Macedonia', 'Northern Ireland', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Scotland', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'Wales']},
    "AfroLib": {country: "" for country in ['Algeria', 'Angola', 'Benin', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'Comoros', 'Congo Rep.', 'DRC', 'Egypt', 'Equatorial Guinea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Morocco', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']},
    "SALib": {country: "" for country in ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']},
    "NALib": {country: "" for country in ['Bahamas', 'Barbados', 'Belize', 'Bermuda', 'Canada', 'Costa Rica', 'Cuba', 'Curaçao', 'Dominica', 'Dominican Republic', 'El Salvador', 'French Guiana', 'Grenada', 'Guadeloupe', 'Guatemala', 'Guyana', 'Haiti', 'Haiti', 'Honduras', 'Jamaica', 'Martinique', 'Mexico', 'Nicaragua', 'Panama', 'Saint Lucia', 'Snt Vincent & Gren.', 'Suriname', 'Trinidad and Tobago', 'USA']},
    "AsiaLib": {country: "" for country in ['Australia', 'Bahrain', 'Brunei', 'Cambodia', 'China', 'India', 'Indonesia', 'Iran', 'Iraq', 'Japan', 'Jordan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar (Burma)', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkmenistan', 'UAE', 'Uzbekistan', 'Vietnam', 'Yemen']},
    "OceaniaLib": {country: "" for country in ['Fiji', 'New Zealand', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Vanuatu']}
}

class FifaRankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FIFA Rankings Input")

        # Create a canvas and a scrollbar
        self.canvas = tk.Canvas(root)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame inside the canvas
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.frames = {}
        for region in rankings:
            frame = tk.Frame(self.frame)
            frame.pack(side="top", fill="both", expand=True)
            self.frames[region] = frame

            label = tk.Label(frame, text=region, font=("Helvetica", 16))
            label.pack(pady=10)

            for country in rankings[region]:
                self.create_country_input(frame, region, country)

        button_frame = tk.Frame(self.frame)
        button_frame.pack(side="bottom", fill="x", pady=10)

        self.save_button = tk.Button(button_frame, text="Save Rankings", command=self.save_rankings)
        self.save_button.pack()

        # Configure the scroll region
        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def create_country_input(self, frame, region, country):
        country_frame = tk.Frame(frame)
        country_frame.pack(fill="x", padx=10, pady=2)

        label = tk.Label(country_frame, text=country, width=25, anchor="w")
        label.pack(side="left")

        entry = tk.Entry(country_frame)
        entry.pack(side="right", fill="x", expand=True)
        entry.bind("<FocusOut>", lambda event, r=region, c=country, e=entry: self.update_ranking(r, c, e))

    def update_ranking(self, region, country, entry):
        rankings[region][country] = entry.get()

    def save_rankings(self):
        with open("fifa_rankings.json", "w") as f:
            json.dump(rankings, f, indent=4)
        messagebox.showinfo("Save Rankings", "Rankings saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FifaRankingApp(root)
    root.mainloop()

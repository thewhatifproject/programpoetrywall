
# Title: The Little Prince.py
# Powered by The 'What If' Project

# 🌟 Once upon an asteroid...

class LittlePrince:
    def __init__(self):
        self.planet = "B-612"
        self.rose = "😙"
        self.volcanoes = 3
        self.heart = "curious"
        self.journey = []

    def leave_planet(self):
        self.journey = ["King", "Vain Man", "Drunkard", "Businessman", "Lamplighter", "Geographer"]
        print("Farewell,", self.rose)
        return "Onward to Earth 🌌"

    def tame(self, creature):
        if creature == "Fox":
            print("You become responsible, forever, for what you have tamed.")
            self.heart = "wise"
            return "�� Friendship planted"
        return "🐝 Encounter passed"

    def question_adults(self):
        for figure in self.journey:
            print(f "Asking {figure}: What truly matters?")
        return "Answers weighed in stars ✪"

    def meet_pilot(self):
        return {
            "crash_site": "Sahara",
            "draw_sheep()": "😑",
            "lesson": "What is essential is invisible to the eye."
        }

 if __name__ == "__main__":
    prince = LittlePrince()
    print(prince.leave_planet())
    print(prince.tame("Fox"))
    print(prince.question_adults())
    print(prince.meet_pilot())
class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        print(f"Hi, I’m {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}.")
        print(f"Fun fact: {self.fun_fact}\n")

    def show_stack(self):
        print("My Tech Stack:")
        for tool in self.tech_stack:
            print(f"   • {tool}")
        print()

    def github_link(self):
        return f"https://github.com/{self.github_username}"


# -------- Example Usage -------- #
if __name__ == "__main__":
    # My profile here
    my_profile = Profile(
        name="Marvin Tumusiime",
        favorite_language="Python",
        hobby="Forex Trading",
        tech_stack=["Python", "Django", "Git", "MySQL"],
        github_username="T4marvin",
        fun_fact="I can debug code faster with coffee"
    )

    # Call methods
    my_profile.introduce()
    my_profile.show_stack()
    print("My GitHub:", my_profile.github_link())

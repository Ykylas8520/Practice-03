def create_user(name, **details):
    print("Name:", name)
    for k, v in details.items():
        print(k, ":", v)

create_user("Madi", age=20, city="Astana")

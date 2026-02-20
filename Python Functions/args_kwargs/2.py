def print_info(**kwargs):
    for k, v in kwargs.items():
        print(k, ":", v)

print_info(name="Ali", age=21, city="Almaty")

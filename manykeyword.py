def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def print_dict(**kwargs):
    print(
        (list(kwargs))[1]
    )  # -> It's will print as a dictionary {'name': 'Geeta', 'field': 'Computing', 'award': 'Gold Medal'}


print_profile(name="Geeta", field="Computing", award="Gold Medal")
# If i want to extract a specify key
print_dict(name="Geeta", field="Computing", award="Gold Medal")

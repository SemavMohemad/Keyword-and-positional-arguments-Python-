# 1- Clarity and Self-Documentation
def create_user(name, age, role, is_active):
    pass


# Compare these:
create_user("Alex", 30, "editor", True)  # confusing
create_user(name="Alex", age=30, role="editor", is_active=True)  # clear


# 2-  Safe Reordering and Partial Use
def send_email(to, subject, body="No content"):
    print(f"To: {to}\nSubject: {subject}\nBody: {body}")


send_email(subject="Meeting Reminder", to="team@example.com")


# 3-  Fewer Bugs with Similar-Type Parameters
# using keyword arguments ensures you don’t accidentally assign the wrong value to the wrong parameter.
def resize_image(width, height, keep_aspect):
    pass


resize_image(1080, 720, True)  # Could be wrong order!
resize_image(width=1080, height=720, keep_aspect=True)  # precise


# 4-Better Compatibility with Defaults
def connect(host, port=8080, use_ssl=True):
    pass


connect(host="localhost", use_ssl=False)

class Credentials:

    def __init__(self, name, password):
        self.name = name
        self.password = password

credentials = {
    'role': Credentials('name', 'password')
}
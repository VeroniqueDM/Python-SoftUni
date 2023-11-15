class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.is_on = False
        self.apps = []

    def power(self):
        # if self.is_on == False:
        #     self.is_on = True
        # else:
        #     self.is_on = False
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if self.is_on and self.memory> app_memory:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"
        elif not self.is_on:
            return f"Turn on your phone to install {app}"
        elif app_memory > self.memory:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"

smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())

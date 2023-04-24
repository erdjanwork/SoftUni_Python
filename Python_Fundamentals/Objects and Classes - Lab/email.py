class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
line = input()
while line != "Stop":
    tokens = line.split(" ")
    sender, receiver, content = line.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    line = input()

indexes = [int(el) for el in input().split(", ")]

for index, email in enumerate(emails):
    if index in indexes:
        emails[index].send()
    print(f"{email.sender} says to {email.receiver}: {email.content}. Sent: {email.is_sent}")
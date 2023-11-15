class Email:
    def __init__(self, sender, receiver, content,):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

command = input()
list_of_mails = []
while command != "Stop":

    email_list = command.split()
    name_sender = email_list[0]
    name_receiver = email_list[1]
    mail_content = email_list[2]
    email = Email(name_sender, name_receiver, mail_content)
    list_of_mails.append(email)
    command = input()

# sent_mails = input().split(", ")
# sent_mails_indices = [int(x) for x in sent_mails]
indices = list(map(int, input().split(", ")))
for i in range(len(list_of_mails)):
    curr_mail = list_of_mails[i]
    if i in indices:
        curr_mail.send()
    current_email_info = curr_mail.get_info()
    print(current_email_info)
import smtplib
from email.utils import formataddr
import imghdr
from email.message import EmailMessage

sender_email = 'banlienlac12a0912@gmail.com'
password = 'mpaohkghbfdpacts'

receiver_email = 'khachoang.info@gmail.com'

msg = EmailMessage()
msg['Subject'] = "Mail send by Python 2"
msg['From'] = formataddr(("Ban liên lạc", sender_email))
msg['To'] = receiver_email
# msg['Cc'] = 'khachoang.mi@gmail.com'
# msg['Bcc'] = 'tinhoccong@gmail.com'

msg.set_content('Image attached...')

# send nội dung HTML
msg.add_alternative(f"""\
<!DOCTYPE html>
<html>
<body>

<h1>The Window Object</h1>
<p> Xin chào {receiver_email}
<h2>The alert() Method</h2>

<p>Click the button to see line-breaks in an alert box.</p>

<button onclick="myFunction()">Try it</button>

</body>
</html>

""", subtype='html')

# files = ['hoang.jpg']

# for file in files:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         file_type = imghdr.what(f.name)
#         file_name = f.name

# msg.add_attachment(file_data, maintype='image',
#                    subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, password)

    smtp.send_message(msg)

print('Done')

from trycourier import Courier

TOKEN = 'pk_prod_296G2Q1HXTM629JN5V7HAFJESS3G'
client = Courier(auth_token=TOKEN)

def requestMadeEmail(email_address, sender_name, recipient_name):
    client.send_message(
    message={
        "to": {
        "email": email_address,
        },
        "template": "7028KDW66K4SQKMFD0187YK610H0",
        "data": {
        "recipient_name": recipient_name,
        "sender_name": sender_name
        },
    }
    )

def requestSentEmail(email_address, sender_name, recipient_name, status):
    client.send_message(
  message={
    "to": {
      "email": email_address,
    },
    "template": "NVD5QP12P744A4PRC1YA312GSM2B",
    "data": {
      "sender_name": sender_name,
      "recipient_name": recipient_name,
        "status": status
    },
  }
)

requestMadeEmail("jerry.volcy@gmail.com", "Danae Troupe", "Jerry Volcy")
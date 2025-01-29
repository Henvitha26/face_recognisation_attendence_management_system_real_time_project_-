from twilio.rest import Client
import keys

# Initialize the Twilio client
client = Client(keys.account_sid, keys.auth_token)

# Create and send the message
message = client.messages.create(
    body="Today u r attended to company",
    from_=keys.twilio_number,  # Note the underscore after 'from'
    to=keys.my_phone_number
)

# Print the message body to confirm
print(message.body)

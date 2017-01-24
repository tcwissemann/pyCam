from twilio.rest import TwilioRestClient

client = TwilioRestClient("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

client.messages.create(to="+1xxxxxxxxxx", from_="+1xxxxxxxxxx", body="Hello World!", media_url=["https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQ6eclMOzgr8WmjwRMQnGFLJdSKg7oM0gMRXaOppFkVQkL22ytM"])

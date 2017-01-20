from twilio.rest import TwilioRestClient

client = TwilioRestClient("AC47b13b617c5806614265237ce06fa110", "e4e74dbdf6719d769422a90225dd8814")

client.messages.create(to="+15122997254", from_="+15125807197", body="Hello World!", media_url=["https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQ6eclMOzgr8WmjwRMQnGFLJdSKg7oM0gMRXaOppFkVQkL22ytM"])
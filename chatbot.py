import google.generativeai as ai


API_KEY='AIzaSyAKiXfI0jwzuHx1Qq3X-5hHXyigjBU10Mg'


ai.configure(api_key=API_KEY)


model=ai.GenerativeModel('gemini-pro')


chat= model.start_chat()

while True:
	message= input("Your Message: ")
	if message=='choco':
		print("Hero")
		continue
	if message.lower()=='bye':

		print("Good Bye")
		break

	response=chat.send_message(message)
	print("Chat: ",response.text)
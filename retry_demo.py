import time

MAX_RETRIES = 3

for attempt in range(MAX_RETRIES):
	print("Attempt:" ,attempt + 1)

	try:
		if attempt < 2:
			raise ConnectionError("simlated temporery API error")
		print ("success")
		break
	except ConnectionError as error:
		print ("Error:", error)

		if attempt == 	MAX_RETRIES - 1:
			print("max retries reached")
			break

		wait_time= 2 **attempt
		print (f"waiting {wait_time} seconds before retry...")
		time.sleep(wait_time)


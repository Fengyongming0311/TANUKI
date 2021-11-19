def get_fake_mobile_phone():
	import random
	initial = random.choice(["130", "131", "132", "133", "134", "135",
							 "136", "137", "138", "139", "177", "181",
							 "186"])
	return "%s%08d" % (initial, random.randint(0, 99999999))



phone = get_fake_mobile_phone()

print (phone)
for i in range(78,112):
	with open("del.txt","a") as f:
		f.write(f"elif rule_id == \"ucp_ae_sd_165_{i}\": \n	pass\n ")

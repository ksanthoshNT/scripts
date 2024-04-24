def extraction_results(data: dict,keys_to_filter: list) -> dict:

"""
convert keys values into str by extracting value key
data = {"main":{"keys_extraction":{"value":["abc","def"],"coordinate":[]}}}
"""
	result: dict = {}

	for k,v in data.items():
		if k not in keys_to_filter:
			result[k] = v['value'][0]
		else:
			v['value'] = v['value'][0]
			result[k] = v

	return result


keys_to_filter: list = ["acceptance_instructions"]
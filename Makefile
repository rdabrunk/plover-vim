.PHONY: test all

test:
	python3 test.py

all:
	# python3 plover_dict.py
	# python3 templates/command_letter/customised.py
	python3 templates/easy_motion/customised.py > templates/easy_motion/customised.json

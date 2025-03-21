.PHONY: list run copy

list:
	@mpremote connect list

run:
	@sudo mpremote connect /dev/ttyACM0 run main.py

copy:
	@sudo mpremote connect  fs cp your_script.py :main.py

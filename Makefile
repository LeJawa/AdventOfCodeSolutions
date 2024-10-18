all: bu run

run_main:
	PYTHONPATH=$(shell pwd) python3 main.py

run_bu_data:
	PYTHONPATH=$(shell pwd) python3 tools/bu_data.py

run_bu_data_force:
	PYTHONPATH=$(shell pwd) python3 tools/bu_data.py --force

bu: run_bu_data
buf: run_bu_data_force
run: run_main

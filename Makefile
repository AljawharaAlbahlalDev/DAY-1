.PHONY: doctor test serve

doctor:
	python scripts/doctor.py

test:
	pytest -q

serve:
	uvicorn src.bayan.serving.app:app --host 0.0.0.0 --port 8000 --reload

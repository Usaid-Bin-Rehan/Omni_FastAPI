# 1. Create/Activate venv
python -m venv venv
venv\Scripts\activate.bat

# 2. Install a list of packages
pip install -r requirements.txt
pip freeze > requirements.txt

# 3. Run the FastAPI app
uvicorn main:app --reload

# Mole Analyzer Backend

Instructions:

# 1. Create virtual environment:
python -m venv tfenv

# 2. Activate virtual environment:
# On Windows:
tfenv\Scripts\activate
# On Linux/Mac:
source tfenv/bin/activate

# 3. Install required packages:
pip install -r requirements.txt

# 4. Run the FastAPI backend:
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 5. Use ngrok(optional):
link to set up ngrok: https://ngrok.com/
ngrok http 8000 (Paste the link to mobile app baseUrl)

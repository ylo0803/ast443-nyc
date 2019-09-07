source ../pyenv/bin/activate
python exocands-prepconvert.py
python mjd-utc-convert.py
python exocands-postconvert.py >> exocands-transit-candidates.txt
deactivate

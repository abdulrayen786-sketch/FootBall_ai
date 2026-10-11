AI-Based Football Player Tracking and Performance Analysis Using Computer Vision
=====================================================================

PROJECT
-------
This project uses computer vision and YOLO to analyze football match videos.

Main features:
- Player detection and tracking
- Ball detection
- Player speed estimation
- Distance covered estimation
- Team-level statistics
- AI-generated performance summary
- Analyzed match video
- PDF report generation
- Excel report generation

REQUIREMENTS
------------
- Python 3.12 or compatible Python 3 version
- Windows recommended
- Internet connection for installing Python packages

INSTALLATION
------------
1. Install Python 3.12.
2. Open Command Prompt.
3. Go to the project folder:

   cd C:\Users\abdul\Desktop\football_ai_project

   Change the path if the project is stored somewhere else.

4. Create a virtual environment:

   python -m venv venv

5. Activate it:

   venv\Scripts\activate

6. Install the required packages:

   python -m pip install -r requirements.txt

RUN THE PROJECT
---------------
After activating the virtual environment, run:

   python -m streamlit run app.py

The Streamlit dashboard will open in a web browser.

USING THE DASHBOARD
-------------------
1. Open the dashboard.
2. Upload/select a football match video.
3. Set the calibration value if required.
4. Start the analysis.
5. Wait for the analysis to finish.
6. View player, ball, speed, distance and team statistics.
7. Download the PDF or Excel report if required.

IMPORTANT NOTES
---------------
- Keep yolo11n.pt in the same folder as app.py.
- Do not rename or delete required project files.
- The venv folder does not need to be submitted. It can be recreated using the steps above.
- Player distance and speed are estimates based on pixel-to-meter calibration.
- Tracking IDs may not always correspond perfectly to individual real-world players.
- Results depend on video quality, camera angle, lighting and player/ball visibility.

TROUBLESHOOTING
---------------
If "python was not found" appears:
- Make sure Python is installed.
- Activate the virtual environment before running the project.

If a package is missing:

   python -m pip install -r requirements.txt

If Streamlit does not start:

   python -m streamlit run app.py

PROJECT TITLE
-------------
AI-Based Football Player Tracking and Performance Analysis Using Computer Vision

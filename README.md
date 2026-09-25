# RepSense AI Gym Coach

> Real-time movement tracking, rep counting, and proactive coaching for focused home workouts.

RepSense AI Gym Coach is a Streamlit-powered fitness companion that uses your camera and MediaPipe pose landmarks to analyze exercise form while you train. It counts repetitions, tracks workout sets, gives live form metrics, stores workout history, and can provide AI voice coaching.

## What It Does

- Real-time pose detection through the browser camera
- Automatic repetition and set tracking
- Exercise-specific form metrics
- AI coaching feedback through Groq
- Optional voice feedback with text-to-speech
- Workout history backed by SQLite
- Responsive light and dark dashboard themes
- Collapsible sidebar for a focused workout view

## Supported Exercises

- Squats
- Push-ups
- Biceps Curls (Dumbbell)
- Shoulder Press
- Lunges

## Tech Stack

| Layer | Technology |
| --- | --- |
| App UI | Streamlit |
| Pose tracking | MediaPipe Tasks |
| Video processing | OpenCV + streamlit-webrtc |
| AI coaching | Groq |
| Voice output | gTTS |
| Persistence | SQLite |
| Styling | Custom CSS |

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Aman05cody/RepSense---AI-Gym-Coach.git
cd RepSense---AI-Gym-Coach
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure AI coaching

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

The app can still run without the key, but AI voice coaching will be unavailable.

### 5. Start the app

```bash
streamlit run main.py
```

Open the local URL shown by Streamlit, usually `http://localhost:8501`.

## How To Use It

1. Enter a unique username to create or open a training profile.
2. Choose an exercise, target sets, and reps in the sidebar.
3. Select **Start Workout** and allow camera access.
4. Follow the live metrics and coach feedback while exercising.
5. End the session to save completed sets to workout history.

## Project Structure

```text
.
├── main.py                         # Streamlit application entry point
├── core/                           # Shared exercise abstractions
├── detectors/                      # Exercise-specific pose detectors
├── ml_models/                      # MediaPipe pose landmarker model
├── services/
│   ├── auth/                       # Username profile flow
│   ├── coaching/                   # LLM, TTS, and voice pipeline
│   ├── config/                     # Exercise and metric definitions
│   ├── persistence/                # SQLite repository functions
│   ├── state/                      # Streamlit session defaults
│   ├── tracking/                   # Rep, set, and history synchronization
│   ├── ui/                         # CSS and component styling
│   └── vision/                     # WebRTC video processing
├── static/                         # Custom stylesheet and font
├── requirements.txt
└── .streamlit/config.toml          # Streamlit theme configuration
```

## Configuration Notes

- Camera access is required for live pose tracking.
- The MediaPipe model is included in `ml_models/pose_landmarker_full.task`.
- Workout history is stored locally in `data.db` and is ignored by Git.
- Secrets and local environment files are excluded through `.gitignore`.
- The dashboard defaults to light mode and supports dark mode from the sidebar.

## Deployment

For Streamlit Community Cloud:

1. Push this repository to GitHub.
2. Create a new app from the repository.
3. Set the main file to `main.py`.
4. Add `GROQ_API_KEY` under the app's Secrets settings.
5. Deploy.

Camera permissions and WebRTC availability depend on the browser and hosting environment.

## Development

Compile-check the main Python modules with:

```powershell
.\.venv\Scripts\python.exe -m py_compile main.py services\auth\login_wall.py services\vision\exercise_video_processor.py
```

Keep generated files, local databases, virtual environments, and API keys out of commits.

## License

No license has been specified for this project yet.

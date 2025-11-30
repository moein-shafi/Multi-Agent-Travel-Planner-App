# Multi-Agent Travel Planner App

A small multi-agent travel planning web app (Flask + client-side JS) that generates day-by-day itineraries based on user input. The app demonstrates a simple front-end form, client-side itinerary generation logic, and a backend Flask scaffold for handling requests.

This README describes how to install, run, and extend the app, and where to find the main code components.

## Key features
- Form-based travel planner UI (city, number of days, attractions per day)
- Client-side itinerary generation and rendering (dynamic per-day content)
- Conditional rendering of optional fields (addresses, meal suggestions, overall tips)
- Simple Flask backend scaffold for API or server-side expansion
- Clear project layout for further multi-agent / LLM integration

## Prerequisites
- Windows machine (instructions use PowerShell / cmd)
- Python 3.8+
- Node/npm (optional if you add front-end build tooling)
- git (optional)

## Quick start (development)

1. Clone the repo (if not already local)
   ```
   git clone <repo-url>
   cd Multi-Agent-Travel-Planner-App
   ```

2. Create and activate a Python virtual environment (PowerShell)
   ```
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   or (cmd)
   ```
   .\.venv\Scripts\activate.bat
   ```

3. Install Python dependencies
   ```
   pip install -r requirements.txt
   ```
   If `requirements.txt` is missing, install Flask:
   ```
   pip install Flask
   ```

4. Run the Flask app (example)
   - If the app is structured under `3-cewAI-App-Flask`:
     ```
     cd 3-cewAI-App-Flask
     set FLASK_APP=app.py
     set FLASK_ENV=development
     flask run
     ```
     or (PowerShell)
     ```
     $env:FLASK_APP = "app.py"
     $env:FLASK_ENV = "development"
     flask run
     ```

5. Open the UI in your browser
   - By default: http://127.0.0.1:5000

## How the UI works (important files)
- Template / static files:
  - `3-cewAI-App-Flask/templates/` — Jinja2 HTML templates (form, results container).
  - `3-cewAI-App-Flask/static/js/travel-planner.js` — client-side logic for:
    - capturing form submit,
    - creating `FormData` and extracting values,
    - simulating / calling API and generating itinerary data,
    - building HTML output with conditional rendering (address, meals, overall tips).
  - `3-cewAI-App-Flask/static/css/` — styles for layout (if present).

- Backend:
  - `3-cewAI-App-Flask/app.py` (or similar) — Flask app routes and server logic.

## Form field names and client-side expectations
The client JS extracts values via `FormData`. Ensure your HTML form input `name` attributes match the keys the script expects. Typical keys used in client code:
- `city` — city name (string)
- `days` or `numDays` — number of days (integer)
- `attractions_per_day`, `attractionsPerDay`, or `attractions` — attractions per day (integer)

Example form snippet:
```html
<form id="tripForm">
  <input name="city" type="text" value="New York" />
  <input name="days" type="number" value="3" />
  <input name="attractions_per_day" type="number" value="3" />
  <button type="submit">Plan trip</button>
</form>
```

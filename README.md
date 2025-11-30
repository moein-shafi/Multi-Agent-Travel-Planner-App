# Multi-Agent Travel Planner App

A demo multi-agent travel planner web app (Flask backend + client-side JavaScript). The app shows how to collect user inputs, generate per-day itineraries, and render them with conditional fields (addresses, meal suggestions, overall tips). It is intended as a starting point for integrating real multi-agent or LLM-backed planning logic.

This README covers project layout, setup, how the front-end and back-end communicate, configuration, and extension points.

---

## Contents

- Project overview
- Features
- Requirements
- Quick install & run (Windows)
- Project structure
- Key files and where to modify behavior
- Form and API contract (input / output shape)
- Conditional rendering rules
- Extending with a real backend or agents
- Troubleshooting
- Contributing & license

---

## Overview

The app accepts a city name, number of days, and attractions-per-day from a form, then generates daily plans and renders them. Client-side code currently simulates generation but is organized to call a backend API. Optional fields (attraction address, meal suggestions, overall tips) are conditionally displayed only when present.

---

## Features

- UI form to capture trip parameters (city, days, attractions per day)
- Client-side itinerary generation (demo) and dynamic rendering of:
  - Day-by-day attractions
  - Meal suggestions (if available)
  - Overall tips (if available)
- Conditional rendering to avoid empty sections
- Simple Flask scaffold for server-side expansion

---

## Requirements

- Python 3.8+
- pip
- (Optional) Node/npm if adding JS build tooling
- Windows command line / PowerShell instructions included below

---

## Quick start (Windows)

1. Open PowerShell or CMD and change to project root:
   ```
   cd "c:\Users\Arash RES 1\Documents\certificate\multi-agent-travel-planner-app\Multi-Agent-Travel-Planner-App"
   ```

2. Create and activate virtual environment (PowerShell):
   ```
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   CMD:
   ```
   .\.venv\Scripts\activate.bat
   ```

3. Install dependencies (if `requirements.txt` exists):
   ```
   pip install -r requirements.txt
   ```
   If missing, install Flask:
   ```
   pip install Flask
   ```

4. Run the Flask app (example for the included Flask scaffold):
   ```
   cd app
   set FLASK_APP=app.py
   set FLASK_ENV=development
   flask run
   ```
   PowerShell:
   ```
   $env:FLASK_APP = "app.py"
   $env:FLASK_ENV = "development"
   flask run
   ```

5. Open the UI in a browser:
   - http://127.0.0.1:5000

---

## Project structure (typical)

- app/
  - app.py (Flask routes / API)
  - templates/
    - index.html (form + results container)
  - static/
    - js/
      - travel-planner.js (form handling, FormData extraction, itinerary rendering)
    - css/
      - styles.css
- README.md (this file)
- requirements.txt (optional)
- LICENSE (optional)

Adjust structure to your repository if different.

---

## Key files & what they do

- static/js/travel-planner.js
  - Captures form submit, builds a FormData object, extracts:
    - city (string)
    - days (integer)
    - attractions_per_day (integer)
  - Simulates or fetches itinerary data and builds HTML
  - Uses conditional rendering:
    - Only show attraction address if present
    - Only show meal suggestions if provided
    - Only show overall tips if present
- templates/index.html
  - Form markup: ensure `name` attributes match keys used by JS
- app.py
  - Example Flask app and API endpoint placeholder (POST /api/plan)

---

## Form field names (must match JS FormData extraction)

Default keys expected by the client script:
- `city` — city name (string)
- `days` — number of days (integer)
- `attractions_per_day` — attractions per day (integer)

Example form snippet:
```html
<form id="tripForm">
  <input name="city" type="text" value="New York" />
  <input name="days" type="number" value="3" />
  <input name="attractions_per_day" type="number" value="3" />
  <button type="submit">Plan trip</button>
</form>
```
If you change these names, update `travel-planner.js` accordingly.

---

## API contract (recommended JSON response)

If moving generation server-side, return JSON shaped like:

{
  "city": "City Name",
  "days": 3,
  "daily_plans": [
    {
      "day_number": 1,
      "attractions": [
        {
          "name": "Attraction 1",
          "category": "Tourist Spot",
          "estimated_duration": "2 hours",
          "address": "Optional address string",
          "description": "Short description"
        }
      ],
      "meal_suggestions": ["Breakfast ...", "Lunch ..."] // optional
    }
  ],
  "overall_tips": "Optional overall tips string" // optional
}

Client-side usage example (replace simulated delay):
```javascript
const response = await fetch('/api/plan', {
  method: 'POST',
  body: formData
});
const data = await response.json();
```

---

## Conditional rendering rules implemented in client

- Attraction address: rendered only if attraction.address exists and is non-empty.
- Meal suggestions: section shown only if meal_suggestions is an array with length > 0.
- Overall tips: shown only if overall_tips is present and non-empty.

This prevents empty blocks from appearing in the UI.

---

## Extending the app

- Replace simulated generation with a real planner:
  - Implement `/api/plan` in Flask to accept form fields and return the JSON contract above.
  - Integrate multi-agent or LLM systems to generate richer itinerary data.
- Improve UI:
  - Add maps, images, links, or time scheduling.
  - Add client-side caching and editing of generated plans.
- Add tests:
  - Unit tests for server endpoints and response shapes.
  - Front-end tests for rendering logic.

---

## Troubleshooting

- Blank page or errors: open browser DevTools console to inspect errors from `travel-planner.js`.
- Wrong values posted: verify form `name` attributes match the JS extraction keys.
- Flask won't start: ensure virtualenv activated and FLASK_APP set correctly.

---

## Contributing

- Fork the repository, create a branch with a focused change, run locally, and open a PR.
- Keep changes small and include tests for new backend logic.


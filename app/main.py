from flask import Flask, request, jsonify, render_template
from travel_planner.travel_planner_crew import TravelPlannerCrew

# Initialize Flask application
app = Flask(__name__)


# Route for the home page
@app.route('/')
def index():
    # Render the HTML template
    return render_template('index.html')


@app.route('/api/plan', methods=['POST'])
def plan_trip():
    try:
        # Get form data
        city = request.form.get('city')
        days = int(request.form.get('days'))
        attractions_per_day = int(request.form.get('attractions_per_day'))

        # Calculate total attractions needed
        total_attractions = days * attractions_per_day

        try:
            # Initialize the TravelPlannerCrew instance
            travel_planner = TravelPlannerCrew()
            
            # Run the crew
            result = travel_planner.travel_crew().kickoff(inputs={
                "city": city,
                "days": days,
                "attractions_per_day": attractions_per_day,
                "total_attractions": total_attractions
            })

            if result.pydantic:
                # Return the pydantic output in JSON format
                return jsonify(result.pydantic.model_dump())
            
            # Return an error message if no itinerary is generated
            return jsonify({"error": "No travel itinerary generated"}), 404

        except Exception as e:
            # Return an error message if there is an exception during crew execution
            return jsonify({"error": f"Error generating travel plan: {str(e)}"}), 500

        # Further processing will be done here...

    except Exception as e:
        return jsonify({"error": str(e)}), 400        
    except Exception as e:
        # Return an error message if there is an exception in the request processing
        return jsonify({"error": str(e)}), 400
    

if __name__ == '__main__':
    # Only run the app when this file is executed directly
    app.run(
        host='0.0.0.0',  # Listen on all network interfaces
        port=3000,       # Run on port 3000
        debug=True       # Enable debug mode for development
    )
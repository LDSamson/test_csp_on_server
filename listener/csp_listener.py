# listener/csp_listener.py

from flask import Flask, request, jsonify
import json # Import the json module

# Create a Flask application instance
app = Flask(__name__)

# Define the endpoint to receive CSP violation reports
# This endpoint will listen for POST requests to the '/csp-reports' path
@app.route('/csp-reports', methods=['POST'])
def receive_csp_report():
    """
    Receives CSP violation reports sent via POST requests.
    Attempts to parse the body as JSON and prints it to the console.
    Returns a 200 OK response.
    """
    # Check if the request has a body
    if request.data:
        try:
            # Decode the raw request data (expected to be UTF-8 JSON)
            decoded_data = request.data.decode('utf-8', errors='ignore')

            # Attempt to parse the decoded data as JSON
            report_data = json.loads(decoded_data)

            # If parsing was successful, print the formatted report
            print("\n--- Received and Parsed CSP Violation Report ---")
            # Use json.dumps for pretty printing with indent and ensure_ascii=False
            print(json.dumps(report_data, indent=4, ensure_ascii=False))
            print("----------------------------------------------")

        except json.JSONDecodeError as e:
            # Handle cases where the body is not valid JSON
            print(f"\n--- Received Data but JSON Parsing Failed ---")
            print(decoded_data) # Print raw decoded data
            print(f"JSON Decode Error: {e}")
            print("---------------------------------------------")
        except Exception as e:
            # Catch any other unexpected errors during processing
            print(f"\n--- An Unexpected Error Occurred ---")
            print(decoded_data) # Print raw decoded data
            print(f"Error: {e}")
            print("------------------------------------")

    else:
        # Handle requests with no body (shouldn't happen for CSP reports, but good practice)
        print("\n--- Received POST request with no body ---")
        print("------------------------------------------")

    # Always return a 200 OK response to acknowledge receipt
    # The browser expects a 2xx response for the report to be considered delivered
    return jsonify({"status": "Report received"}), 200

# Run the Flask application
# It will listen on all available interfaces (0.0.0.0) on port 5000
# debug=True enables debug mode, which is useful for development
if __name__ == '__main__':
    print("Starting CSP listener within Docker on http://0.0.0.0:5000/csp-reports")
    # Use threaded=True to handle multiple incoming reports concurrently
    # Set use_reloader=False to prevent the app from starting twice in debug mode
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True, use_reloader=False)

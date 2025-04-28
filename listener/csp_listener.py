# listener/csp_listener.py

from flask import Flask, request, jsonify
import json # Import the json module for manual parsing if needed later

# Create a Flask application instance
app = Flask(__name__)

# Define the endpoint to receive CSP violation reports
# This endpoint will listen for POST requests to the '/csp-reports' path
@app.route('/csp-reports', methods=['POST'])
def receive_csp_report():
    """
    Receives CSP violation reports sent via POST requests.
    Prints the report body to the console and returns a 200 OK response.
    """
    # Check if the request has a body
    if request.data:
        # *** MODIFIED: Accept 'application/csp-report' mimetype for JSON parsing ***
        # Browsers send CSP reports with Content-Type: application/csp-report
        # We tell Flask's get_json to accept this mimetype.
        report_data = request.get_json(force=True, silent=True, cache=False, mimetype='application/csp-report')

        if report_data is not None:
            # If parsing was successful (either application/json or application/csp-report)
            print("\n--- Received CSP Violation Report ---")
            # Use ensure_ascii=False to handle non-ASCII characters correctly
            # Use indent for pretty printing
            print(json.dumps(report_data, indent=4, ensure_ascii=False))
            print("-------------------------------------")
        else:
            # If get_json failed, it might be a non-JSON body or another issue
            print(f"\n--- Received Non-JSON or Unparsable CSP Report Body ---")
            try:
                # Attempt to decode and print the raw body
                print(request.data.decode('utf-8', errors='ignore'))
            except Exception as e:
                print(f"Could not decode request data: {e}")
            print("-----------------------------------------------------")

    else:
        # Handle requests with no body
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

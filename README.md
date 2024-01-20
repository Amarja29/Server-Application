Fizz-Buzz Server

Overview
This is a Fizz-Buzz REST Server implemented in Python using Streamlit. The server exposes a simple web interface for generating Fizz-Buzz sequences based on user-defined parameters.

Third Party Library
Streamlit:
Used for building the web interface and creating an interactive application.

Dependencies
Streamlit: For building the web application.
Getting Started
1. Install dependencies:
   pip install streamlit

2. Run the application:
   streamlit run main.py

Open your web browser and navigate to http://localhost:8501.

Usage
Enter the desired values for int1, int2, limit, str1, and str2 in the web interface.
Click the "Generate Fizz-Buzz" button.
View the Fizz-Buzz sequence generated based on the provided parameters.
Project Structure

fizzbuzz_rest_server/
|-- fizzbuzz/
|   |-- controller.py
|   |-- service.py
|-- tests/
|   |-- test_controller.py
|   |-- test_service.py
|-- main.py
|-- README.md

Files:-
main.py: Main application file. Run this to start the Streamlit server.
fizzbuzz/controller.py: Controller module containing the Fizz-Buzz generation logic.
fizzbuzz/service.py: Service module containing the core Fizz-Buzz algorithm.
tests/test_controller.py: Unit tests for the controller module.
tests/test_service.py: Unit tests for the service module.
# Brute force

In this project, we use python3.11 or higher to test a brute force algorithm with a flask basic project.

## Setup
1. Create and activate python virtual environnement
<pre>
    $python -m venv en
    $source env/bin/activate
</pre>

2. Install dependencies
<pre>
    $pip install -r requirements.txt
</pre>

## Run the application
To run this project, use the following command:

<pre>
    $python -m flask run -p 3000
</pre>

The app will run on http://localhost:3000.

## Test the brute force algorithm

To test the brute force algorithm, follow these steps:
1. Create a directory for storing the available routes:
<pre>
    $mkdir routes_availables
</pre>
2. Run the brute force algorithm:
<pre>
    $python brut_force.py
</pre>

The available routes will be stored in files in the `routes_availables` directory. The number of files created depends on your `CPU count`.

Note: If you change the specified port when running the app, you must also set the `TARGET_URL` in the `brute_force.py` file.
import subprocess
import webbrowser
import time

def start_flask_server():
    # Start the Flask server using waitress as a WSGI server
    flask_process = subprocess.Popen(['python', '-m', 'waitress', '--port=8000', 'app:app'])
    return flask_process

def open_html_file():
    # Open the HTML file in the default web browser
    webbrowser.open('modified.html')

if __name__ == "__main__":
    flask_process = start_flask_server()
    
    # Wait for a few seconds to ensure the server is up
    time.sleep(3)
    
    open_html_file()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        flask_process.terminate()

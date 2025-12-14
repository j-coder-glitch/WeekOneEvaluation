import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    # 1. READ CONFIGURATION FROM AZURE (NOT HARDCODED)
    app_name = os.environ.get('APP_NAME', 'Error: App Name Missing')
    environment = os.environ.get('APP_ENV', 'Error: Environment Missing')
    
    # 2. SIMPLE LOGIC TO DISPLAY STATUS
    return f"""
    <html>
        <head><title>{app_name}</title></head>
        <body style="font-family: sans-serif; text-align: center; padding: 50px;">
            <h1 style="color: #0078D4;">{app_name}</h1>
            <h3>Current Environment: <span style="color: red;">{environment}</span></h3>
            <p>If you see 'Error' above, you need to configure App Settings in Azure!</p>
            <hr>
            <p>Visit <a href='/admin/files/policy.txt'>/admin/files/policy.txt</a> to view company policy.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run()
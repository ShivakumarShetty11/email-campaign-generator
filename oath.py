from google_auth_oauthlib.flow import InstalledAppFlow

# 👇 SCOPES includes both read and send access
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send'
]

def main():
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret_843679773716-d437bs72cspk6qe2qg224fn3ciaqfap0.apps.googleusercontent.com.json', SCOPES)

    creds = flow.run_local_server(port=0)

    with open('token.json', 'w') as token:
        token.write(creds.to_json())

if __name__ == '__main__':
    main()

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
from colorama import Fore, Style
from oauth2 import Request

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


class AuthAPI:
    def __init__(self, credentials_file, token_file):
        self.credentials_file = credentials_file
        self.token_file = token_file

    def get_credentials(self):
        creds = None
        """
        The file token.json stores the user's access and refresh tokens, and is
        created automatically when the authorization flow completes for the first
        time.
        """

        if os.path.exists(self.token_file):
            creds = Credentials.from_authorized_user_file(self.token_file, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())
        return creds

    def get_service(self):
        # Call the Gmail API
        return build('gmail', 'v1', credentials=self.get_credentials())

    def get_messages(self, service, query):
        try:
            msgs_list = []
            next_page_token = None
            # Call the Gmail API
            messages = service.users().messages().list(userId='me', q=query).execute()
            print(f"Messages >> {messages}\n")
            if 'nextPageToken' in messages:
                next_page_token = messages['nextPageToken']

            for message in messages['messages']:
                msgs = service.users().messages().get(userId='me', id=message['id']).execute()
                msgs_list.append(msgs['snippet'])

            while next_page_token:
                messages = service.users().messages().list(userId='me', q=query, pageToken=next_page_token).execute()
                if 'nextPageToken' in messages:
                    next_page_token = messages['nextPageToken']
                else:
                    next_page_token = None
                for message in messages['messages']:
                    msgs = service.users().messages().get(userId='me', id=message['id']).execute()
                    msgs_list.append(msgs['snippet'])

            return msgs_list
        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f'An error occurred: {error}')


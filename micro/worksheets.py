# -*- coding: utf-8 -*

from micro import config

import logging
import gspread
import os

##
#

class WorkSheet:

    def __init__(self, gs):
        self.pages = []

        for x in gs.worksheets():
            title = x.title.lower()
            self.pages.append({
                "title": title,
                "ws": x
            })
            logging.debug("sheet %s found", title)
        
        self.pagesCount = len(self.pages)

    def __str__(self):
        return ",".join([x['title'] for x in self.pages])

    def __getitem__(self, index):

        if type(index) is int:
            if index < 0 or index >= self.pagesCount:
                raise Exception(f"{index} doen't exist")
            return self.pages[index]['ws']

        elif type(index) is str:
            title = index.lower()
            page = [x for x in self.pages if x['title'] == title]
            if not page:
                raise Exception(f"{title} doen't exist")
            return page[0]['ws']

        raise Exception(f"Index cannot support: {index}")

##
#

CREDENTIALS = os.getenv("CREDENTIALS") or 'credentials.json'

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets'
]

__instances__ = {'account': None}

def open(sheetId):

    logging.debug("Connecting to Google Sheet")

    client = __instances__['account']

    if client is None:

        if not os.path.exists(CREDENTIALS):
            raise Exception(f"{CREDENTIALS} not found")

        client = gspread.service_account(filename=CREDENTIALS)

        __instances__['account'] = client

    logging.debug("sheet connected")

    return WorkSheet(client.open_by_key(sheetId))

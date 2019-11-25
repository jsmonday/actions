from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'secrets/client_secrets.json'
VIEW_ID = '199681216'

def initialize_reporting():
  credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
  analytics = build('analyticsreporting', 'v4', credentials=credentials)
  return analytics


def get_report(analytics):
  return analytics.reports().batchGet(
    body = {
      'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '2019-01-01', 'endDate': 'today'}],
          'metrics': [
            {'expression': 'ga:uniquePageViews'},
            {'expression': 'ga:pageviews'},
            {'expression': 'ga:timeOnPage'},
            {'expression': 'ga:avgTimeOnPage'},
          ],
          'dimensions': [{'name': 'ga:pagePath'}]
        }
      ]
    }
  ).execute()

def print_response(response):
  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

    for row in report.get('data', {}).get('rows', []):
      dimensions = row.get('dimensions', [])
      dateRangeValues = row.get('metrics', [])

      for header, dimension in zip(dimensionHeaders, dimensions):
        print(header + ': ' + dimension)

      for i, values in enumerate(dateRangeValues):
        print('Date range: ' + str(i))
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          print(metricHeader.get('name') + ': ' + value)


def main():
  analytics = initialize_reporting()
  response = get_report(analytics)
  print_response(response)

if __name__ == '__main__':
  main()

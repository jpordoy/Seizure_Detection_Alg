# Function to format data into individual rows for event 5580
def format_data_into_rows(json_data):
    formatted_rows = []
    for event in json_data:
        if event['id'] == 5580:
            event_id = event['id']
            for datapoint in event['datapoints']:
                if datapoint['eventId'] == 5580:
                    hr = datapoint['hr']
                    raw_data = datapoint['rawData']
                    row = f"{event_id}, {hr}, {raw_data}"
                    formatted_rows.append(row)
    return formatted_rows




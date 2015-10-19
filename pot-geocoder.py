import geocoder
import csv

rows = []
fieldnames = ['Licensee Name', 'DBA', 'License #', 'Street Address', 'City', 'Zip', 'Operation', 'lat', 'lng']

# Change file name to be geocoded
with open('pot-cultivation-no-dups.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for line in reader:
        g = geocoder.mapquest(line['location'])

        # Add the CSV line data into the Geocoder JSON result
        result = g.json
        result.update(line)

        # Store Geocoder results in a list to save it later
        rows.append(result)

with open('pot-cultivation-geocoded.csv', 'a') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(rows)
    #time.sleep(2)

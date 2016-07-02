## Running Train Status - CLI ##

### Usage: ###
./script.py [-h] [--day {today,tomorrow,yesterday}] train_num

positional arguments:<br />
  train_num             Enter the train number<br />
optional arguments:<br />
  -h, --help            show this help message and exit<br />
  --day {today,tomorrow,yesterday}<br />
                        Enter the day<br />
----
### Example: ###

```sh
./script.py --day today 12952)
{
   "url": "http://spoturtrain.com/status.php?tno=12952&date=0",
   "status": [
      "12952 MUMBAI RAJDHANI EXPRESS 23:13, 02 Jul 16 Left THURIA at 23:03 Train Running on Time Last Updated at 23:04 02 Jul 94 KM to reach RATLAM JN"
   ],
   "timetable": {
      "STATIONS": "ETA",
      "RATLAM JN": "00:02",
      "VADODARA JN": "03:24",
      "SURAT": "04:58",
      "BORIVALI": "07:29",
      "MUMBAI CENTRAL": "08:15"
   }
}
```
----
Scraped from [spotyourtrain.com](http://spoturtrain.com/)

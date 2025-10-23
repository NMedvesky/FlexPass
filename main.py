from ics import Calendar
import requests
url = "https://providencecatholic.myschoolapp.com/podium/feed/iCal.aspx?z=QkgRCgwN981Q0EgglEn%2bkPikCgRySC4Z2loStcQH36F6FTLrmYr0jPBDCuzbLyf%2bxkIdpJO0iNssXQzBZEhl4w%3d%3d"
def main():
    print("Welcome to FlexPass!")
    cal = Calendar(requests.get(url).text)
    print(cal.events)

if __name__ == "__main__":
    main()
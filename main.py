from ics import Calendar

def main():
    with open("CalExport.ics", "r") as f:
        file = f.read() 
        c = Calendar(file)
        print(c.events)

if __name__ == "__main__":
    main()
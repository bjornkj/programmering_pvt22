import requests
import datetime

URL = "https://proagile.se/api/publicEvents"


# Kurser ser ut att bestå av ett eller flera kurstillfällen
# vilkas utsträckning i tid hittas under nyckeln 'segments'
# vi plockar ut det första kurstillfället och från det starttiden
# och konverterar till en datetime. Detta låtsas vi är kursens start
def get_start_date(event_dict: dict) -> datetime.datetime:
    segments = event_dict['segments']
    first_segment = segments[0]
    return datetime.datetime.fromtimestamp(first_segment['start'])


# Räknar ut hur lång en kurs är i timmar
def get_course_len(event_dict: dict) -> float:
    segments = event_dict['segments']
    total_seconds = 0
    for segment in segments:
        total_seconds += segment['stop'] - segment['start']
    return total_seconds / 60 / 60


def print_courses():
    results = requests.get(URL)
    public_events = results.json()

    for event in public_events:
        start_date = get_start_date(event)
        course_len = get_course_len(event)
        print(f"{start_date} {event['courseName']} pågår under {course_len:.1f} timmar")


if __name__ == '__main__':
    print_courses()

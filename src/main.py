import turtle as t
import datetime
import requests

import graph
import youtube
import settings


class FixedQueue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def __str__(self):
        return f"FixedQueue({self.queue})"

    def __repr__(self):
        return f"FixedQueue({self.queue})"

    def enqueue(self, element):
        if len(self.queue) == self.size:
            self.dequeue()

        self.queue.append(element)

    def dequeue(self):
        return self.queue.pop(0)


def create_fullscreen_window():
    window = t.Screen()
    window.screensize()
    window.setup(height=1.0, width=1.0)

    height = window.window_height()
    width = window.window_width()

    window.setworldcoordinates(0, height, width, 0)

    return window


def get_api_key(filepath):
    f = open(filepath, "r")
    return f.readline()


def get_rewind_dislikes(api_key):
    try:
        return youtube.get_dislikes(api_key, settings.YOUTUBE_REWIND_ID)
    except requests.exceptions.ConnectionError:
        return None


def main():
    window = create_fullscreen_window()
    window.title("Youtube rewind graph")
    turtle = t.Turtle()
    turtle.speed(0)

    data = {
        "data_points": FixedQueue(settings.GRAPH_DATA_LIMIT),
        "time_points": FixedQueue(settings.GRAPH_DATA_LIMIT),
    }

    api_key = get_api_key(settings.API_KEY_LOCATION)

    def update_graph():
        new_data_point = get_rewind_dislikes(api_key)
        if new_data_point is not None:
            window.clear()
            current_datetime = datetime.datetime.now()

            data["data_points"].enqueue(new_data_point)
            data["time_points"].enqueue(current_datetime.strftime("%I:%M %p"))

            graph.create_graph(
                window, turtle,
                data["data_points"].queue, axes=data["time_points"].queue)

        window.ontimer(update_graph, settings.UPDATE_DELAY_SECONDS * 1000)

    update_graph()
    window.mainloop()


if __name__ == "__main__":
    main()

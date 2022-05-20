class CinemaHall:

    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name, customers, cleaning_staff):
        print(f"{movie_name} started in hall {self.number}.")
        for customer in customers:
            self.watch_movie(movie_name)
        print(f"{movie_name} ended.")
        self.clean_hall(cleaning_staff)

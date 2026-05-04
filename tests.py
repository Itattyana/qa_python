from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_valid_length(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in collector.books_genre
        assert collector.books_genre['Гарри Поттер'] == ''

    def test_add_new_book_too_long(self):
        collector = BooksCollector()
        long_name = 'A' * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.books_genre

    def test_add_new_book_empty(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.books_genre) == 0

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        name = 'Гарри Поттер'
        collector.add_new_book(name)
        collector.add_new_book(name)
        assert len(collector.books_genre) == 1

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.books_genre['Гарри Поттер'] == 'Фантастика'

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер']

    def test_get_books_for_children_fantasy(self):
        """Фантастика — подходит для детей"""
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert 'Гарри Поттер' in collector.get_books_for_children()

    def test_get_books_for_children_animation(self):
        """Мультфильмы — подходят для детей"""
        collector = BooksCollector()
        collector.add_new_book('Мулан')
        collector.set_book_genre('Мулан', 'Мультфильмы')
        assert 'Мулан' in collector.get_books_for_children()

    def test_get_books_for_children_detective_excluded(self):
        """Детективы — НЕ подходят для детей"""
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert 'Шерлок Холмс' not in collector.get_books_for_children()

    def test_add_book_in_favorites(self):
        """Добавление книги в избранное"""
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    def test_add_book_in_favorites_no_duplicate(self):
        """Запрет дублирования в избранном"""
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')  # повтор
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        """Удаление из избранного"""
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == []
from django.db import models


class Genre(models.Model):
    """Modelo que representa um genero de livro."""
    name = models.CharField(max_length=200, help_text="Digite um gênero (ex. Ficção Científica)")

    def __str__(self):
        return self.name


class Book(models.Model):
    """Modelo que representa um livro (mas não uma cópia específica)"""
    title = models.CharField(max_length=200)

    # Foreign Key porque um livro pode ter so um autor mas um autor pode ter varios livros
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Uma breve descrição do livro')
    isbn = models.CharField('ISBN', max_length=13, help_text='<a href="https://www.isbn-international.org/content/what-isbn">Número ISBN</a> de 13 carcateres')


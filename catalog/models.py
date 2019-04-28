from django.db import models
from django.urls import reverse
import uuid  # Required for unique book instances


class Genre(models.Model):
    """Modelo que representa um genero de livro."""
    name = models.CharField(max_length=200, help_text="Digite um gênero (ex. Ficção Científica)")

    def __str__(self):
        return self.name


"""OBS.: In both field types (ManyToManyField and ForeignKey) the related model class is declared as the first unnamed parameter using either the model class or a string containing the name of the related model. You must use the name of the model as a string if the associated class has not yet been defined in this file before it is referenced!"""


class Book(models.Model):
    """Modelo que representa um livro (mas não uma cópia específica)"""
    title = models.CharField(max_length=200)

    # Foreign Key porque um livro pode ter so um autor mas um autor pode ter varios livros
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Uma breve descrição do livro')
    isbn = models.CharField('ISBN', max_length=13, help_text='<a href="https://www.isbn-international.org/content/what-isbn">Número ISBN</a> de 13 carcateres')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Escolha um gênero para este livro')
    Language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, help_text='Escolha uma língua para este título')

    def __str__(self):
        """string para representar o obejto Model"""
        return self.title

    def get_absolute_url(self):
        """Retorna a url para acessar o registro detalhado do livro"""
        """we have to define a URL mapping that has the name book-detail, and define an associated view and template"""
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """Cria uma string para o genero, necessário para mostrá-lo na página Admin"""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'


class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico para este livro em particular")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
                   ('m', 'Manutenção'),
                   ('e', 'Emprestado'),
                   ('d', 'Disponível'),
                   ('r', 'Reservado')
                   )

    status = models.CharField(
                              max_length=1,
                              choices=LOAN_STATUS,
                              blank=True,
                              default='m',
                              help_text='Disponibilidade do livro'
                              )

    # ordena os registros retornados numa query
    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String que representa o obejto Model"""
        return f'{self.id} ({self.book.title})'
        # equivale a '{0} ({1})'.format(self.id,self.book.title)


class Author(models.Model):
    """Modelo que representa o autor"""
    first_name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)
    date_of_birth = models.DateField('Data de nascimento', null=True, blank=True)
    date_of_death = models.DateField('Morte', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia de um autor em particular"""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Language(models.Model):
    name = models.CharField(
                            max_length=200,
                            help_text='Digite a língua nativa do livro',
                            )

    def __str__(self):
        """String para representar o objeto no site Admin"""
        return self.name

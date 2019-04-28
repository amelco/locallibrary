from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance, Language

# Forma básica de registrar modelos
# Eles aparecerão na página Admin em sua forma padrão
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)


class AuthorAdmin(admin.ModelAdmin):
    """Forma 'customizada' de registrar modelos
    Cada classe define como eles irão ser mostrados na página Admin"""
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


# Registra a classe admin com seu modelo associado
admin.site.register(Author, AuthorAdmin)

# Registra a classe Admin para Book utiliando o decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    # O genero do livro é de relação ManytoMany no modelo. Assim, o genero
    # será listado através de uma função display_genre()

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

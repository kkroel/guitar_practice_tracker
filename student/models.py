from django.db import models

# Create your models here.


class Level(models.Model):
    LEVEL_CHOICES = (
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced')
    )
    level = models.CharField(max_length=32,
                             choices=LEVEL_CHOICES,
                             default='BEGINNER',
                             unique=True)
    description = models.CharField(max_length=256,
                                   blank=True)

    def __str__(self):
        return self.level


class Style(models.Model):
    STYLE_CHOICES = (
        ('FINGERSTYLE', 'FingerStyle'),
        ('FLATPICK', 'Flatpick'),
        ('HYBRID_PICKING', 'Hybrid_Picking'),
        ('STRUMMING', 'Strumming')
    )
    style = models.CharField(max_length=32,
                             choices=STYLE_CHOICES,
                             default='FINGERSTYLE',
                             unique=True)
    description = models.CharField(max_length=256,
                                   blank=True)

    def __str__(self):
        return self.style


class Genre(models.Model):
    GENRE_CHOICES = (
        ('ROCK', 'Rock'),
        ('BLUEGRASS', 'Bluegrass'),
        ('CLASSICAL', 'Classical'),
        ('FOLK', 'Folk'),
        ('POP', 'Pop'),
        ('COUNTRY', 'Country'),
        ('JAZZ', 'Jazz'),
        ('OTHER', 'Other')
    )
    genre = models.CharField(max_length=32,
                             choices=GENRE_CHOICES,
                             default='ROCK',
                             unique=True)
    description = models.CharField(max_length=256,
                                   blank=True)

    def __str__(self):
        return self.genre


class Song(models.Model):
    title = models.CharField(max_length=256)
    composer = models.CharField(max_length=64)
    description = models.TextField()
    level = models.ForeignKey(Level,
                              to_field='level',
                              on_delete=models.PROTECT)
    style = models.ForeignKey(Style,
                              to_field='style',
                              on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre,
                              to_field='genre',
                              on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Student(models.Model):
    user_name = models.CharField(max_length=32,
                                 unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12,
                                    blank=True)
    # picture = models.ImageField() # set W x H for good thumbnail size
    songs = models.ManyToManyField(
        to='Song',
        through='StudentSong',
        related_name='student_songs',
        blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Purpose(models.Model):
    PURPOSE_CHOICES = (
        ('PERSONAL_ENJOYMENT', 'Personal_Enjoyment'),
        ('EXERCISE', 'Exercise'),
        ('REPETOIRE', 'Repetoire'),
        ('RECITAL', 'Recital')
    )
    purpose = models.CharField(max_length=32,
                               choices=PURPOSE_CHOICES,
                               default='PERSONAL_ENJOYMENT',
                               unique=True)
    description = models.CharField(max_length=256,
                                   blank=True)

    def __str__(self):
        return self.purpose


class Status(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In_Progress'),
        ('GOAL_ACHIEVED', 'Goal_Achieved'),
        ('MAINTENANCE', 'Maintenance'),
        ('ON_HOLD', 'On_Hold'),
        ('INACTIVE', 'Inactive')
    )
    status = models.CharField(max_length=32,
                              choices=STATUS_CHOICES,
                              default='IN_PROGRESS',
                              unique=True)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.status


class StudentSong(models.Model):
    student = models.ForeignKey(Student,
                                on_delete=models.PROTECT)  # auto-generated
    song = models.ForeignKey(Song,
                             on_delete=models.PROTECT)        # auto-generated
    tempo = models.IntegerField(default=50,
                                help_text='Current tempo in BPM')
    tempo_goal = models.IntegerField()
    purpose = models.ForeignKey(Purpose,
                                to_field='purpose',
                                on_delete=models.PROTECT)
    status = models.ForeignKey(Status,
                               to_field='status',
                               on_delete=models.PROTECT)

    def __str__(self):
        return '{}: {}'.format(self.student, self.song)

    class Meta:
        unique_together = ('student', 'song')


class Update(models.Model):
    student = models.ForeignKey(Student,
                                on_delete=models.PROTECT)
    song = models.ForeignKey(StudentSong,
                             on_delete=models.PROTECT)
    entered = models.DateTimeField('Entered')
    update = models.TextField(blank=True)
    tempo = models.IntegerField(blank=True)
    # how to make this the first 64 chars of update?? or just put new tempo if no update notes
    display_update = models.CharField(max_length=64)

    def __str__(self):
        return self.display_update


class Link(models.Model):
    LINK_CHOICES = (
        ('TAB', 'Tab'),
        ('NOTATION', 'Notation'),
        ('PERFORMANCE', 'Performance'),
        ('BOOK', 'Book'),
        ('LESSON', 'Lesson'),
        ('NOTES', 'Notes')
    )
    student = models.ForeignKey(Student,
                                on_delete=models.PROTECT)
    song = models.ForeignKey(StudentSong,
                             on_delete=models.PROTECT)
    type = models.CharField(max_length=32,
                            choices=LINK_CHOICES,
                            default='TAB')
    link = models.URLField  # may have to change to allow for local files

    def __str__(self):
        return self.link

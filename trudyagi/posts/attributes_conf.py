from django import forms

MATERIAL_CHOICES = (
    ('Кожа', 'Кожа'),
    ('Ткань', 'Ткань'),
)

COLOR_CHOISE = (
    ('Красный', 'Красный'),
    ('Синий', 'Синий'),
    ('Белый', 'Белый'),
    ('Коричневый', 'Кориченевый'),
    ('Розовый', 'Розовый'),
)

CPU_CHOICES = (
    ('Intel-I5', 'Intel-I5'),
    ('Intel-I3', 'Intel-I3'),
)

RAM_CHOICES = (
    ('2', '2GB'),
    ('4', '4GB'),
    ('8', '8GB'),
    ('16', '16GB'),
    ('32', '32GB'),
)

attributes_config={
    'Обувь':{
        'Материал': forms.MultipleChoiceField(label='Материал',required=False, choices=MATERIAL_CHOICES,
                                              widget=forms.CheckboxSelectMultiple),
        'Размер': forms.IntegerField(label='Размер',required=False),
        'Цвет': forms.MultipleChoiceField(label='Цвет',required=False, choices=COLOR_CHOISE,
                                              widget=forms.CheckboxSelectMultiple),
    },
    'Компьютеры':{
        'CPU': forms.MultipleChoiceField(label='CPU',required=False, choices=CPU_CHOICES,
                                              widget=forms.CheckboxSelectMultiple),
        'RAM': forms.MultipleChoiceField(label='RAM',required=False, choices=RAM_CHOICES,
                                              widget=forms.CheckboxSelectMultiple),
    }

}
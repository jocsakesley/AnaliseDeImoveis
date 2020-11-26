from django import forms

class CoreForm(forms.Form):
    ESTADOS = (
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
        ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
        ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
    )
    TIPO_BUSCA = (
        ('venda','Comprar'),
        ('aluguel', 'Alugar'),
    )
    TIPO = (
        ('casas', 'Casa'),
        ('apartamentos', 'Apartamento'),
    )
    estado = forms.CharField(label='Estado', widget=forms.Select(choices=ESTADOS))
    tipo_busca = forms.CharField(widget=forms.Select(choices=TIPO_BUSCA))
    tipo = forms.CharField(widget=forms.Select(choices=TIPO))
from django.db import models


class DiaProgramacao(models.Model):
    nome = models.CharField(max_length=100)  # Nome do evento
    data = models.DateField()  # Data no formato dd/mm/yyyy

    def __str__(self):
        return f"{self.nome} - {self.data.strftime('%d/%m/%Y')}"


class OrdemProgramacao(models.Model):
    ACOES_CHOICES = [
        ('Louvor', 'Louvor'),
        ('Mensagem', 'Mensagem'),
        ('Sermao', 'Sermao'),
    ]

    hora = models.TimeField()  # Seleção de hora
    acao = models.CharField(max_length=50, choices=ACOES_CHOICES, blank=True)
    descricao = models.CharField(max_length=100, blank=True)  # Descrição adicional
    programacao = models.ForeignKey(DiaProgramacao, on_delete=models.CASCADE,
                                    related_name="ordens")  # Associação com "DiaProgramacao"

    def __str__(self):
        return f"{self.hora} {self.acao} ( {self.descricao} ) - Dia: {self.programacao.nome}"

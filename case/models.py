from django.db import models
from django.core.validators import MinValueValidator


class Company(models.Model):
    name = models.CharField(
        verbose_name='案件元企業',
        blank=False,
        null=False,
        max_length=50,
        default='',
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        verbose_name='カテゴリー名',
        blank=False,
        null=False,
        max_length=20,
        default='',
    )

    def __str__(self):
        return self.name


class Nationality(models.Model):
    restriction = models.CharField(
        verbose_name='国籍制限',
        blank=False,
        null=False,
        max_length=20,
        default='',
    )

    def __str__(self):
        return self.restriction


class Status(models.Model):
    status = models.CharField(
        verbose_name='ステータス',
        blank=True,
        null=True,
        max_length=20,
        default='',
    )

    def __str__(self):
        return self.status


class LowSkill(models.Model):
    low_flag = models.CharField(
        verbose_name='ロースキル案件',
        blank=True,
        null=True,
        max_length=20,
        default='',
    )

    def __str__(self):
        return self.low_flag


class Case(models.Model):
    title = models.CharField(
        verbose_name='案件名',
        blank=False,
        null=False,
        max_length=200,
        default='',
    )
    text = models.TextField(
        verbose_name='概要',
        blank=True,
        null=True,
        max_length=1000,
        default='',
    )
    created_date = models.DateField(
        verbose_name='紹介日',
        blank=False,
        null=False,
        default='',
    )
    updated_date = models.DateField(
        verbose_name='更新日',
        blank=True,
        null=True,
        default='',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    number = models.IntegerField(
        verbose_name='組合案件番号',
        blank=True,
        null=True,
        default='',
        validators=[MinValueValidator(0)],
    )
    start_at = models.DateField(
        verbose_name='開始日',
        blank=True,
        null=True,
        default='',
    )
    end_at = models.DateField(
        verbose_name='終了日',
        blank=True,
        null=True,
        default='',
    )
    place = models.CharField(
        verbose_name='場所',
        blank=False,
        null=False,
        max_length=50,
        default='',
    )
    member = models.IntegerField(
        verbose_name='人数',
        blank=True,
        null=True,
        default='',
        validators=[MinValueValidator(0)],
    )
    first_skill = models.TextField(
        verbose_name='必須スキル',
        blank=True,
        null=True,
        max_length=100,
        default='',
    )
    second_skill = models.TextField(
        verbose_name='尚可スキル',
        blank=True,
        null=True,
        max_length=100,
        default='',
    )
    personal_skill = models.TextField(
        verbose_name='求める人物像',
        blank=True,
        null=True,
        max_length=100,
        default='',
    )
    lower_cost = models.IntegerField(
        verbose_name='下限単金',
        blank=True,
        null=True,
        default='',
        validators=[MinValueValidator(0)],
    )
    upper_cost = models.IntegerField(
        verbose_name='上限単金',
        blank=True,
        null=True,
        default='9999',  # スキル見合いは9999で定義する
        validators=[MinValueValidator(0)],
    )
    nationality = models.ForeignKey(
        Nationality,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    low_skill = models.ForeignKey(
        LowSkill,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    comment = models.TextField(
        verbose_name='備考',
        blank=True,
        null=True,
        max_length=1000,
        default='',
    )

    def __str__(self):
        return self.title

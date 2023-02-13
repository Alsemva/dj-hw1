import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            print(phones)

        for phone in phones:
            # TODO: Добавьте сохранение модели
            new_phone = Phone(
                id=int(phone['id']),
                name=phone['name'],
                image=phone['image'],
                price=phone['price'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=slugify(phone['name']))
            new_phone.save()
        return print('True!!!!!!!!!!!!!!!!!!')
    # def handle(self, *args, **options):
    #     with open('phones.csv', 'r') as csvfile:
    #
    #         phone_reader = csv.reader(csvfile, delimiter=';')
    #         # пропускаем заголовок
    #         next(phone_reader)
    #
    #         for line in phone_reader:
    #             new_phone = Phone.objects.create(
    #                 id=int(line[0]),
    #                 name=line[1],
    #                 image=line[2],
    #                 price=int(line[3]),
    #                 release_date=line[4],
    #                 lte_exists=line[5],
    #                 slug=slugify(line[1]),)
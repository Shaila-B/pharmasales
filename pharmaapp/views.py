import csv
import json
from datetime import datetime

import pandas as pd
from django.core import serializers
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from pharmaapp.models import DrugReview, PharmaSales

def read_csv(request):
    data = pd.read_csv('PharmaSales.csv')

    header = ['id', 'datum', 'm01ab', 'm01ae', 'n02ba', 'n02be', 'n05b', 'n05c', 'r03', 'r06', 'year']
    df = pd.DataFrame(data, columns=header)
    m01ab = pd.DataFrame(df[['id', 'datum', 'm01ab', 'year']])
    m01ab['ATC Classification'] = 'Acetic acid derivatives and related substances'
    m01ab['Drug Classification'] = 'Musculo-Skeletal System Drugs'

    # m01ab.drop(m01ab.columns[1], axis=0, inplace=True)

    m01ab.to_csv('m01ab.csv')

    with open('m01ab.csv') as pharma_sales_csv:
        header = ['id', 'datum', 'm01ab', 'year', 'ATC Classification', 'Drug Classification']
        reader = csv.reader(pharma_sales_csv)
        for row in reader:
            doc = {}
            for n in range(0, len(header)):
                if header[n] == row[n]:
                    pass
                else:
                    doc[header[n]] = row[n + 1]
            print('Saved')
            print(type(doc['datum']))
            if doc['id'].isdigit() and doc['year'].isdigit() and isinstance(doc['m01ab'], str):
                doc['id'] = int(doc['id'])
                doc['m01ab'] = float(doc['m01ab'])
                doc['year'] = int(doc['year'])
                doc['datum'] = datetime.strptime(doc['datum'],
                                                 '%Y-%m-%d')
                print(doc['datum'])
                print(type(doc['datum']))
                print(doc['m01ab'])
                print(type(doc['m01ab']))
                print(doc['year'])
                print(type(doc['year']))
                print(doc['ATC Classification'])
                print(doc['Drug Classification'])
                pharmasale = PharmaSales(pharmasale_id=doc['id'], date=doc['datum'], year=doc['year'],
                                         atc_code=doc['m01ab'], atc_classification=doc['ATC Classification'],
                                         drug_classification=doc['Drug Classification'])

                pharmasale.save()

    m01ae = pd.DataFrame(df[['id', 'datum', 'm01ae', 'year']])
    m01ae['ATC Classification'] = 'Propionic acid derivatives, antiinflammatory and antirheumatic products'
    m01ae['Drug Classification'] = 'Musculo-Skeletal System Drugs'
    m01ae.to_csv('m01ae.csv')
    with open('m01ae.csv') as pharma_sales_csv:
        header = ['id', 'datum', 'm01ae', 'year', 'ATC Classification', 'Drug Classification']
        reader = csv.reader(pharma_sales_csv)
        for row in reader:
            doc = {}
            for n in range(0, len(header)):
                if header[n] == row[n]:
                    pass
                else:
                    doc[header[n]] = row[n + 1]

            if doc['id'].isdigit() and doc['year'].isdigit() and isinstance(doc['m01ae'], str):
                doc['id'] = int(doc['id'])
                doc['m01ae'] = float(doc['m01ae'])
                doc['year'] = int(doc['year'])
                doc['datum'] = datetime.strptime(doc['datum'],
                                                 '%Y-%m-%d')

                pharmasale = PharmaSales(pharmasale_id=doc['id'], date=doc['datum'], year=doc['year'],
                                         atc_code=doc['m01ae'], atc_classification=doc['ATC Classification'],
                                         drug_classification=doc['Drug Classification'])
                pharmasale.save()

    #
    n02ba = pd.DataFrame(df[['id', 'datum', 'n02ba', 'year']])
    n02ba['ATC Classification'] = 'Salicylic acid and derivatives, analgesics and antipyretics'
    n02ba['Drug Classification'] = 'Nervous System Drugs'
    n02ba.to_csv('n02ba.csv')

    with open('n02ba.csv') as pharma_sales_csv:
        header = ['id', 'datum', 'n02ba', 'year', 'ATC Classification', 'Drug Classification']
        reader = csv.reader(pharma_sales_csv)
        for row in reader:
            doc = {}
            for n in range(0, len(header)):
                if header[n] == row[n]:
                    pass
                else:
                    doc[header[n]] = row[n + 1]

            if doc['id'].isdigit() and doc['year'].isdigit() and isinstance(doc['n02ba'], str):
                doc['id'] = int(doc['id'])
                doc['n02ba'] = float(doc['n02ba'])
                doc['year'] = int(doc['year'])
                doc['datum'] = datetime.strptime(doc['datum'],
                                                 '%Y-%m-%d')

                pharmasale = PharmaSales(pharmasale_id=doc['id'], date=doc['datum'], year=doc['year'],
                                         atc_code=doc['n02ba'], atc_classification=doc['ATC Classification'],
                                         drug_classification=doc['Drug Classification'])
                pharmasale.save()

    n02be = pd.DataFrame(df[['id', 'datum', 'n02be', 'year']])
    n02be['ATC Classification'] = 'Anilide analgesics and antipyretics'
    n02be['Drug Classification'] = 'Nervous System Drugs'
    n02be.to_csv('n02be.csv')
    with open('n02be.csv') as pharma_sales_csv:
        header = ['id', 'datum', 'n02be', 'year', 'ATC Classification', 'Drug Classification']
        reader = csv.reader(pharma_sales_csv)
        for row in reader:
            doc = {}
            for n in range(0, len(header)):
                if header[n] == row[n]:
                    pass
                else:
                    doc[header[n]] = row[n + 1]

            if doc['id'].isdigit() and doc['year'].isdigit() and isinstance(doc['n02be'], str):
                doc['id'] = int(doc['id'])
                doc['n02be'] = float(doc['n02be'])
                doc['year'] = int(doc['year'])
                doc['datum'] = datetime.strptime(doc['datum'],
                                                 '%Y-%m-%d')

                pharmasale = PharmaSales(pharmasale_id=doc['id'], date=doc['datum'], year=doc['year'],
                                         atc_code=doc['n02be'], atc_classification=doc['ATC Classification'],
                                         drug_classification=doc['Drug Classification'])
                pharmasale.save()

    n05b = pd.DataFrame(df[['id', 'datum', 'n05b', 'year']])
    n05b['ATC Classification'] = 'ANXIOLYTICS'
    n05b['Drug Classification'] = 'Nervous System Drugs'
    n05b.to_csv('n05b.csv')
    with open('n05b.csv') as pharma_sales_csv:
        header = ['id', 'datum', 'n05b', 'year', 'ATC Classification', 'Drug Classification']
        reader = csv.reader(pharma_sales_csv)
        for row in reader:
            doc = {}
            for n in range(0, len(header)):
                if header[n] == row[n]:
                    pass
                else:
                    doc[header[n]] = row[n + 1]

            if doc['id'].isdigit() and doc['year'].isdigit() and isinstance(doc['n05b'], str):
                doc['id'] = int(doc['id'])
                doc['n05b'] = float(doc['n05b'])
                doc['year'] = int(doc['year'])
                doc['datum'] = datetime.strptime(doc['datum'],
                                                 '%Y-%m-%d')

                pharmasale = PharmaSales(pharmasale_id=doc['id'], date=doc['datum'], year=doc['year'],
                                         atc_code=doc['n05b'], atc_classification=doc['ATC Classification'],
                                         drug_classification=doc['Drug Classification'])
                pharmasale.save()

    n05c = pd.DataFrame(df[['id', 'datum', 'n05c', 'year']])
    n05c['ATC Classification'] = 'HYPNOTICS AND SEDATIVES'
    n05c['Drug Classification'] = 'Nervous System Drugs'
    n05c.to_csv('n05c.csv')
    with open('n05c.csv') as pharma_sales_csv:
        header = ['id', 'datum', 'n05c', 'year', 'ATC Classification', 'Drug Classification']
        reader = csv.reader(pharma_sales_csv)
        for row in reader:
            doc = {}
            for n in range(0, len(header)):
                if header[n] == row[n]:
                    pass
                else:
                    doc[header[n]] = row[n + 1]

            if doc['id'].isdigit() and doc['year'].isdigit() and isinstance(doc['n05c'], str):
                doc['id'] = int(doc['id'])
                doc['n05c'] = float(doc['n05c'])
                doc['year'] = int(doc['year'])
                doc['datum'] = datetime.strptime(doc['datum'],
                                                 '%Y-%m-%d')

                pharmasale = PharmaSales(pharmasale_id=doc['id'], date=doc['datum'], year=doc['year'],
                                         atc_code=doc['n05c'], atc_classification=doc['ATC Classification'],
                                         drug_classification=doc['Drug Classification'])
                pharmasale.save()

    r03 = pd.DataFrame(df[['id', 'datum', 'r03', 'year']])
    r03['ATC Classification'] = 'DRUGS FOR OBSTRUCTIVE AIRWAY DISEASES'
    r03['Drug Classification'] = 'Respiratory System Drugs'
    r03.to_csv('r03.csv')
    with open('r03.csv') as pharma_sales_csv:
        header = ['id', 'datum', 'r03', 'year', 'ATC Classification', 'Drug Classification']
        reader = csv.reader(pharma_sales_csv)
        for row in reader:
            doc = {}
            for n in range(0, len(header)):
                if header[n] == row[n]:
                    pass
                else:
                    doc[header[n]] = row[n + 1]

            if doc['id'].isdigit() and doc['year'].isdigit() and isinstance(doc['r03'], str):
                doc['id'] = int(doc['id'])
                doc['r03'] = float(doc['r03'])
                doc['year'] = int(doc['year'])
                doc['datum'] = datetime.strptime(doc['datum'],
                                                 '%Y-%m-%d')

                pharmasale = PharmaSales(pharmasale_id=doc['id'], date=doc['datum'], year=doc['year'],
                                         atc_code=doc['r03'], atc_classification=doc['ATC Classification'],
                                         drug_classification=doc['Drug Classification'])
                pharmasale.save()

    r06 = pd.DataFrame(df[['id', 'datum', 'r06', 'year']])
    r06['ATC Classification'] = 'ANTIHISTAMINES FOR SYSTEMIC USE'
    r06['Drug Classification'] = 'Respiratory System Drugs'
    r06.to_csv('r06.csv')
    with open('r06.csv') as pharma_sales_csv:
        header = ['id', 'datum', 'r06', 'year', 'ATC Classification', 'Drug Classification']
        reader = csv.reader(pharma_sales_csv)
        for row in reader:
            doc = {}
            for n in range(0, len(header)):
                if header[n] == row[n]:
                    pass
                else:
                    doc[header[n]] = row[n + 1]

            if doc['id'].isdigit() and doc['year'].isdigit() and isinstance(doc['r06'], str):
                doc['id'] = int(doc['id'])
                doc['r06'] = float(doc['r06'])
                doc['year'] = int(doc['year'])
                doc['datum'] = datetime.strptime(doc['datum'],
                                                 '%Y-%m-%d')

                pharmasale = PharmaSales(pharmasale_id=doc['id'], date=doc['datum'], year=doc['year'],
                                         atc_code=doc['r06'], atc_classification=doc['ATC Classification'],
                                         drug_classification=doc['Drug Classification'])
                pharmasale.save()

    with open('DrugReview.csv') as drug_review_csv:
        header = ['id', 'condition', 'date', 'drugName', 'rating', 'review', 'uniqueID', 'usefulCount']
        reader = csv.reader(drug_review_csv)
        print(type(reader))
        for row in reader:
            doc = {}
            for n in range(0, len(header)):
                doc[header[n]] = row[n]
            print(doc)
            if doc['id'].isdigit() and doc['rating'].isdigit() and doc['uniqueID'].isdigit() and doc[
                'usefulCount'].isdigit():
                doc['id'] = int(doc['id'])
                doc['rating'] = int(doc['rating'])
                doc['uniqueID'] = int(doc['uniqueID'])
                doc['usefulCount'] = int(doc['usefulCount'])

                drug = DrugReview(drug_id=doc['id'], condition=doc['condition'], date=doc['date'],
                                  drug_name=doc['drugName'], rating=doc['rating'], review=doc['review'],
                                  unique_id=doc['uniqueID'], useful_count=doc['usefulCount'])
                drug.save()
    return HttpResponse('CSV Read successful')


class GetPharmaSalesViewSet(APIView):
    def get(self, request, *args, **kwargs):
        drug_classification = request.data.get('drug_classification', False)
        year = request.data.get('year', False)
        print(drug_classification)
        print(year)
        if year.isdigit():
            year = int(year)
            pharmsale_reviews = PharmaSales.objects.filter(drug_classification=drug_classification, year=year)
            tmpJson = serializers.serialize("json", pharmsale_reviews)
            tmpObj = json.loads(tmpJson)

            res = []
            for item in tmpObj:
                dict = {}

                dict['drug_classification'] = item['fields']['drug_classification']
                dict['atc_classification'] = item['fields']['atc_classification']
                dict['year'] = item['fields']['year']
                dict['prev_year'] = dict['year'] - 1
                print(dict)
                res.append(dict)
            context = {
                "data": res
            }
            return Response(context)


class GetDrugReviewViewSet(APIView):
    def get(self, request, *args, **kwargs):
        year = request.data.get('year', False)
        drug_name = request.data.get('drug_name', False)
        print(year)
        print(type(year))
        print(drug_name)
        if year.isdigit():
            year = int(year)

            drug_reviews = DrugReview.objects.filter(drug_name=drug_name, date__year=year)

            tmpJson = serializers.serialize("json", drug_reviews)
            tmpObj = json.loads(tmpJson)
            res = []
            for item in tmpObj:
                dict = {}
                dict['drug_name'] = item['fields']['drug_name']
                dict['condition'] = item['fields']['condition']
                dict['review'] = item['fields']['review']
                dict['date'] = item['fields']['date']
                print(dict)
                res.append(dict)
            context = {
                "data": res
            }
            return Response(context)

import csv

def write_csv(data):
    with open ('Name.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow((data['Name'],data['SurName'],data['Age']))

def write_csv2(data):
    with open('Name.csv','a') as file:
        order = ['Name','SurName','Age']
        writer = csv.DictWriter(file,fieldnames= order)

        writer.writerow(data)






def main():
    d = {'Name':'Petr','SurName':'Ivanov','Age':21}
    d1 = {'Name':'Ivan','SurName':'Ivanov','Age':18}
    d2 = {'Name':'Ksu','SurName':'Petrova','Age':32}

    lis = [d,d1,d2]

    with open ('name.csv') as file:
        fieldname = ['name','surname','age']
        reader = csv.DictReader(file,fieldnames=fieldname)

        for row in reader:
            print(row)

if __name__ == '__main__':
    main()
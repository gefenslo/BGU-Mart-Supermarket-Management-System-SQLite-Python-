from persistence import *
import sys

def main(args: list[str]):
    inputfilename = args[1]
    
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline = line.strip().split(",")  
            if len(splittedline) < 4:  
                continue

            try:
                product_id = int(splittedline[0])
                num_units = int(splittedline[1])
                activator_id = int(splittedline[2])
                activity_date = splittedline[3].strip()  

                product = repo.products.find(id=product_id)
                if product:
                    if isinstance(product, list):
                        product = product[0]

                    if num_units > 0:
                        product.quantity += num_units
                    elif num_units < 0:
                        if product.quantity >= abs(num_units):
                            product.quantity += num_units
                        else:
                            continue

                    activity = Activitie(product_id, num_units, activator_id, activity_date)
                    repo.activities.insert(activity)
                    repo.products.update(product)

            except Exception as e:
                continue

if __name__ == '__main__':
    main(sys.argv)
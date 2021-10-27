import datetime

def verify_response(question, response):
    """ verify response before save it in the dictionnary """
    if question[2]:
        condition = question[2]
        if condition == int:
            try:
                int(response)
            except ValueError:
                print("vous devez indiquer un nombre")
                return False
            else:
                return True
        elif type(condition) == list:
            if response in condition:
                return True
            else:
                print("vous devez choisir votre réponse dans la liste proposée")
                return False
        elif condition == "date":
            date = response.split("-")
            try:
                date_test = datetime.date(int(date[2]), int(date[1]), int(date[1]))
            except ValueError:
                print("vérifier que le nombre de mois est entre 1 et 12 et que le nombre de jours " \
                       "est entre 1 et 31")
                return False
            except TypeError:
                print("les éléments de la date doivent etre des chiffres séparés par un tiret")
                return False
            except IndexError:
                print("Vous devez indiquez un jour(jj), un mois(mm) et une année(aaaa)")
                return False
            else:
                if datetime.date(1900,1,1) < date_test:
                    return True
                else:
                    print("L'année doit être composée de 4 chiffres")
                    return False
        elif condition == "required":
            if response:
                return True
            else:
                print("Vous devez entrer une réponse")
                return False
        else:
            pass
    else:
        return True

def check_float(number_to_test):
    try:
        float(number_to_test)
    except ValueError:
        return f"Vous devez entrer un nombre"
    else:
        return True

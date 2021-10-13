import datetime

def verify_response(question, response):
    """ verify response before save it in the dictionnary """
    if question[2]:
        condition = question[2]
        if condition == int:
            try:
                int(response)
            except ValueError:
                return f"vous devez indiquer un nombre"
            else:
                return True
        elif type(condition) == list:
            if response in condition:
                return True
            else:
                return "vous devez choisir votre réponse dans la liste proposée"
        elif condition == "date":
            date = response.split("-")
            try:
                date_test = datetime.date(int(date[2]), int(date[1]), int(date[1]))
            except ValueError:
                return "vérifier que le nombre de mois est entre 1 et 12 et que le nombre de jours " \
                       "est entre 1 et 31"
            except TypeError:
                return "les éléments de la date doivent etre des chiffres séparés par un tiret"
            except IndexError:
                return "Vous devez indiquez un jour(jj), un mois(mm) et une année(aaaa)"
            else:
                if datetime.date(1900,1,1) < date_test:
                    return True
                else:
                    return f"L'année doit être composée de 4 chiffres"
        elif condition == "required":
            if response:
                return True
            else:
                return f"Vous devez entrer une réponse"
        else:
            pass
    else:
        return True

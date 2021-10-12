import datetime

def verify_response(question, response):
    """ verify response before save it in the dictionnary """
    if question[2]:
        condition = question[2]
        if condition == int:
            try:
                response = int(response)
                if type(response) == condition:
                    return True
            except ValueError:
                return f"vous devez indiquer un nombre"
        elif type(condition) == list:
            if response in condition:
                return True
            else:
                return "vous devez choisir votre réponse dans la liste proposée"
        elif condition == "date":
            date = response.split("-")
            try:
                datetime.date(int(date[2]), int(date[1]), int(date[1]))
                return True
            except ValueError:
                return "vérifier que le nombre de mois est entre 1 et 12 et que le nombre de jours " \
                       "est entre 1 et 31"
            except TypeError:
                return "les éléments de la date doivent etre des chiffres séparés par un tiret"
            except IndexError:
                return "Vous devez indiquez un jour(jj), un mois(mm) et une année(aaaa)"
        elif condition == "required":
            if response:
                return True
            else:
                return f"Vous devez entrer une réponse"
        else:
            pass
    else:
        return True

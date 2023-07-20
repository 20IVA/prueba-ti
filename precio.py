def numerosdenentreda(mensaje):

    while True:
        try:
          numero_ingreso = input(input("mensaje"))
        except ValueError:
         print("te equivocaste de esto")
        else:

          break
    return numero_ingreso
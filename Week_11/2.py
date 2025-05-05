class Model:
    services = {
        'email': {'number': 1000, 'price': 2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }
class View:
    def list_services(self, services):
        for svc in services:
            print(svc,'')
    def list_pricing(self, services):
        for svc in services:
            print("For", Model.services[svc]['number'],
                svc, "message you pay $",
                Model.services[svc]['price'])

class View2:
    def list_services(self, services):
        for svc in services:
            print(svc,'')
    def list_pricing(self, services):
        for svc in services:
            print("Untuk setiap", Model.services[svc]['number'],
                svc, "anda membayar $",
                Model.services[svc]['price'])

class Controller:
    def __init__(self,bahasa):
        self.model = Model()
        if bahasa==1:
            self.view = View()
        else:
            self.view = View2()
    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))
    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))
#Instansiasi objek
def english():
    controller = Controller(1)
    print("Services Provided:")
    controller.get_services()
    print("Pricing for Services:")
    controller.get_pricing()

def indo():
    controller = Controller(2)
    print("Layanan yang disediakan: ")
    controller.get_services()
    print("Tarif tiap layanan: ")
    controller.get_pricing()

pilihan=input("What language do you choose? [1]English [2]Indonesia: ")
if pilihan == "1":
    english()
elif pilihan =="2":
    indo()
else:
    print("error, choose the language number!")




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

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))
    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))
    def bid_price(self):
        print("price according to your bid:")
        tawar=input("What service do you want to bid? email, sms, or voice :")
        harga=input("enter the price you want (in $): ")
        self.model.services[tawar]["price"]=harga


#Instansiasi objek
controller = Controller()
print("Services Provided:")
controller.get_services()
print("Pricing for Services:")
controller.get_pricing()
controller.bid_price()
controller.get_pricing()

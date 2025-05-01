class MakeOverGame :
    
   def __init__ (self):
        self.dresses ={
            "1" : "a red wedding dress"
            "2 ": " a blue and white denim jacket"
            "3 " : "an orange sparkly gown"
        }
        self.hairstyle = {
            "1" : "silky long hair"
            "2": "curly hair"
            "3":"a braided bun"
        }
        self.acessorries ={
            "1":"a gold  neckalce"
            "2":"a bracelet and ring"
            "3": "a hat and sunglasses"
        }
        self.dress = None
        self.hairstle = None
        self.acessorries = None

        def welcome(self):
            print("WELCOME TO MAKEOVER FOR A PARTY,WEDDING & PICNIC")
            print("LETS GET YOU READY FOR THE BIG EVENT")

            def choose_option(self, options: dict,category: str) -> str:
                print(f"\n Choose a {category}:")
                for key,value in options.items():
                    print(f"{key} . {value}")
                    choice = input("enyer thhe number of your choice:")
                    return options.get(choice,f"stylish{category}")

                    def play(self):
                        self.welcome()
                        self.dress= self.choose_options(self.dresses, "dress")
                        self.hairstyle = self.choose_options(self.hairstyles, "hairstyle")
                        self.acessorries = self.choose_options(self.acessorries, "acessorries")
                        self.reveal_look()

                        def reveal_look (self):
                            print("here is your final look")
                            print("you are wearng {self.dresses},with {self.hairstyle},with{self.acessorries}")
                            print("you are looking absolutely fabulous! Have a magical time at the party,wedding & picnic")

                            #run the game
                            if __name__ =="__main__" :
                                game = DressUpGame()
                                game.play()
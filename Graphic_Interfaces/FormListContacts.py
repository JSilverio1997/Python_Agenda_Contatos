import tkinter.messagebox
from tkinter import *
from Funtionalities.ContactFuntionalities import ContactFuntionalities
from Graphic_Interfaces.FormMainMenu import FormMenu


class FormListContacts(FormMenu):

    def __init__(self, master, id_login):
        self.master = master
        self.master.title("Lista de Histórico de Contatos")
        self.id_login = id_login
        self.create_comp_contacts_all_contac(master)

    def create_comp_contacts_all_contac(self, window):
        self.create_menu_component(window)

        lbl_title = Label(text="Lista de Contatos", font="arial, 25", bg="light gray")
        lbl_title.grid(row=2, column=2, columnspan=3200, pady=5)

        self.create_grid_view(window)

    def create_grid_view(self, window):

        lbl_name_contact = Label(text="Nome", bg="#B0E0E6",
                                 pady=5, width=30, font="arial, 12", relief="ridge")
        lbl_name_contact.grid(row=5, column=2)

        lbl_main_number = Label(text="Número Principal",
                                bg="#B0E0E6", pady=5, width=30, font="arial, 12"
                                , relief="ridge")
        lbl_main_number.grid(row=5, column=3)

        lbl_secundary_number = Label(text=f"Número Secundário", bg="#B0E0E6", pady=5, width=40, font="arial, 12",
                                     relief="ridge")
        lbl_secundary_number.grid(row=5, column=4)

        if self.id_login is not None:
            contacts = ContactFuntionalities()
            datas_contacts = contacts.show_all_contacts(self.id_login)

            line = 6
            color = "white"
            if datas_contacts is not None:
                for columns in datas_contacts:
                    name_contact = columns[0]
                    main_number = columns[1]
                    secundary_number = columns[2]

                    if line % 2 == 0:
                        color = "white"
                    else:
                        color = "light blue"

                    lbl_name = Label(text=f"{name_contact}", bg=color,
                                     pady=5, width=30, font="arial, 12", relief="ridge")
                    lbl_name.grid(row=line + 1, column=2)

                    lbl_main_number = Label(text=f"{main_number}", bg=color, pady=5, width=30, font="arial, 12",
                                            relief="ridge")
                    lbl_main_number.grid(row=line + 1, column=3)

                    lbl_secundary_number = Label(text=f"{secundary_number}", bg=color, pady=5, width=40
                                                 , font="arial, 12", relief="ridge")
                    lbl_secundary_number.grid(row=line + 1, column=4)

                    line += 1

                    print("-" * 70)
                    print("\t \t \t Histórico de Contatos")
                    print(f"Nome do Contato: {name_contact.title()}")
                    print(f"Número Principal: {main_number}")
                    print(f"Número Secundário: {secundary_number}")

            print(f"Quantidades de Contatos em sua Agenda: {len(datas_contacts)}. ")

            btn_return_menu = Button(text="Voltar", font="arial, 12", width=25, command=self.return_form_menu)
            btn_return_menu.grid(row=line + 1, column=2, padx=2, pady=5, columnspan=2500)

        else:
            tkinter.messagebox.showinfo("Contatos", "Você não possuí nenhum  contato adicionado.")


def instance_form_show_contacts(id_login):
    form_show_contacts = Tk()

    FormListContacts(form_show_contacts, id_login)
    form_show_contacts.iconbitmap(r"Images/IconeAgenda.ico")
    form_show_contacts.geometry("930x500+270+30")
    form_show_contacts.resizable(0, 0)
    form_show_contacts.configure(relief="ridge", border="4", bg="light gray")

    form_show_contacts.mainloop()
    exit()


# instance_form_show_contacts(3)

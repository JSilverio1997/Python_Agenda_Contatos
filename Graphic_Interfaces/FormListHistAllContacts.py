import tkinter.messagebox
from tkinter import *
from Funtionalities.HistoryContactFuntionalities import HistoryContact
from Graphic_Interfaces.FormMainMenu import FormMenu


class FormHistAllContacts(FormMenu):

    def __init__(self, master, id_login):
        self.master = master
        self.master.title("Lista de Histórico de Contatos")
        self.id_login = id_login
        self.create_comp_hist_all_contac(master)

    def create_comp_hist_all_contac(self, window):
        self.create_menu_component(window)

        lbl_title = Label(text="Lista de Histórico de Contatos", font="arial, 18", bg="light gray")
        lbl_title.grid(row=2, column=4, columnspan=2, pady=5)

        self.create_grid_view(window)

    def create_grid_view(self, window):

        lbl_name_contact_hist = Label(text="Nome", bg="#B0E0E6",
                                      pady=5, width=30, font="arial, 9", relief="ridge")
        lbl_name_contact_hist.grid(row=5, column=2)

        lbl_main_number_contact_hist = Label(text="Número Principal",
                                             bg="#B0E0E6", pady=5, width=25, font="arial, 9"
                                             , relief="ridge")
        lbl_main_number_contact_hist.grid(row=5, column=3)

        lbl_secundary_number_contact_hist = Label(text=f"Número Secundário",
                                                  bg="#B0E0E6", pady=5, width=25, font="arial, 9"
                                                  , relief="ridge")
        lbl_secundary_number_contact_hist.grid(row=5, column=4)

        lbl_status_contact_hist = Label(text="Status",
                                        bg="#B0E0E6", pady=5, width=20, font="arial, 9"
                                        , relief="ridge")
        lbl_status_contact_hist.grid(row=5, column=5)

        lbl_created_date_contact_hist = Label(text="Data de Criação",
                                              bg="#B0E0E6", pady=5, width=20, font="arial, 9"
                                              , relief="ridge")
        lbl_created_date_contact_hist.grid(row=5, column=6)

        lbl_updated_date_contact_hist = Label(text="Data de Alteração",
                                              bg="#B0E0E6", pady=5, width=20, font="arial, 9"
                                              , relief="ridge")
        lbl_updated_date_contact_hist.grid(row=5, column=7)

        if self.id_login is not None:
            all_contacts_historic = HistoryContact()
            contacts_hist = all_contacts_historic.show_all_contact_hist(self.id_login)

            line = 6
            color = "white"
            if contacts_hist is not None:
                for columns in contacts_hist:
                    name_contact_hist = columns[0]
                    main_number = columns[1]
                    secundary_number = columns[2]
                    status_contact = columns[3]
                    created_date = columns[4]
                    updated_date = columns[5]

                    if line % 2 == 0:
                        color = "white"
                    else:
                        color = "light blue"

                    lbl_name_contact_hist = Label(text=f"{name_contact_hist}", bg=color,
                                                  pady=5, width=30, font="arial, 9", relief="ridge")
                    lbl_name_contact_hist.grid(row=line + 1, column=2)

                    lbl_main_number_contact_hist = Label(text=f"{main_number}",
                                                         bg=color, pady=5, width=25, font="arial, 9"
                                                         , relief="ridge")
                    lbl_main_number_contact_hist.grid(row=line + 1, column=3)

                    lbl_secundary_number_contact_hist = Label(text=f"{secundary_number}",
                                                              bg=color, pady=5, width=25, font="arial, 9"
                                                              , relief="ridge")
                    lbl_secundary_number_contact_hist.grid(row=line + 1, column=4)

                    lbl_status_contact_hist = Label(text=f"{status_contact}",
                                                    bg=color, pady=5, width=20, font="arial, 9"
                                                    , relief="ridge")
                    lbl_status_contact_hist.grid(row=line + 1, column=5)

                    lbl_created_date_contact_hist = Label(text=f"{created_date}",
                                                          bg=color, pady=5, width=20, font="arial, 9"
                                                          , relief="ridge")
                    lbl_created_date_contact_hist.grid(row=line + 1, column=6)

                    lbl_updated_date_contact_hist = Label(text=f"{updated_date}",
                                                          bg=color, pady=5, width=20, font="arial, 9"
                                                          , relief="ridge")
                    lbl_updated_date_contact_hist.grid(row=line + 1, column=7)

                    line += 1

                    print("-" * 70)
                    print("\t \t \t Histórico de Contatos")
                    print(f"Nome do Contato: {name_contact_hist.title()}")
                    print(f"Número Principal: {main_number}")
                    print(f"Número Secundário: {secundary_number}")
                    print(f"Status do Contato: {status_contact}")
                    print(f"Data de Criação: {created_date}")
                    print(f"Data de Alteração: {updated_date}")

            btn_return_menu = Button(text="Voltar", font="arial, 12", width=20, command=self.return_form_menu)
            btn_return_menu.grid(row=line + 1, column=4, padx=2, pady=5, columnspan=2)

        else:
            tkinter.messagebox.showwarning("Atenção", "Não Existe Histórico dos seus Contatos.")


def instance_form_hist_all_contacts(id_login):
    form_hist_all_contacts = Tk()

    FormHistAllContacts(form_hist_all_contacts, id_login)
    form_hist_all_contacts.iconbitmap(r"Images/IconeAgenda.ico")
    form_hist_all_contacts.geometry("1025x450+200+120")
    form_hist_all_contacts.resizable(0, 0)
    form_hist_all_contacts.configure(relief="ridge", border="4", bg="light gray")

    form_hist_all_contacts.mainloop()
    exit()


# instance_form_hist_all_contacts(3)

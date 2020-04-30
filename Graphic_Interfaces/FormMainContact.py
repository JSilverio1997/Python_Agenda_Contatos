import tkinter.messagebox
from tkinter import *
from Graphic_Interfaces.FormMainMenu import FormMenu
from Funtionalities.ContactFuntionalities import ContactFuntionalities


class FormMainContact(FormMenu):

    def __init__(self, master, id_login):
        self.master = master
        self.master.title("Contatos")
        self.create_comp_form_contacts(master)
        self.id_login = id_login

    def create_comp_form_contacts(self, window):
        self.create_menu_component(window)

        lbl_title = Label(text="Contatos", font="arial, 18", bg="light gray")
        lbl_title.grid(row=1, column=3, columnspan=1, pady=5)

        canvas_image = Canvas(window, width=225, height=225)
        bg_image = tkinter.PhotoImage(file=r"Images/ImageMainContact.png")
        canvas_image.create_image((0, 0), image=bg_image, anchor=NW)
        canvas_image.image = bg_image
        canvas_image.grid(row=2, column=3, columnspan=1, pady=5)

        lbl_name_contact_searched = Label(text="  Nome do Contato:", font="arial,14", bg="light gray")
        lbl_name_contact_searched.grid(row=3, column=2, columnspan=1, pady=25)

        txt_name_contact_searched = Entry(width="25", font="arial")
        txt_name_contact_searched.grid(row=3, column=3, pady=2)
        txt_name_contact_searched.focus()
        self.txt_name_contact_searched = txt_name_contact_searched

        btn_search = Button(text="Pesquisar", width=8, font="arial, 12", command=self.search_contact)
        btn_search.grid(row=3, column=4, columnspan=2, padx=5, pady=5)

        lbl_name_contact = Label(text="\t    Nome:", font="arial,14", bg="light gray")
        lbl_name_contact.grid(row=5, column=2, columnspan=1, pady=5)

        txt_name_recorvered = Entry(width="25", font="arial")
        # txt_name_recorvered.grid(row=4, column=3, pady=2)
        self.txt_name_recorvered = txt_name_recorvered

        txt_name_contact = Entry(width="25", font="arial")
        txt_name_contact.grid(row=5, column=3, pady=2)
        self.txt_name_contact = txt_name_contact

        lbl_main_number = Label(text="  Número Principal:", font="arial,14", bg="light gray")
        lbl_main_number.grid(row=6, column=2, columnspan=1, pady=5)

        txt_main_number = Entry(width="25", font="arial")
        txt_main_number.grid(row=6, column=3, pady=5)
        self.txt_main_number = txt_main_number

        lbl_secundary_number = Label(text="Número Secudário:", font="arial,14", bg="light gray")
        lbl_secundary_number.grid(row=7, column=2, columnspan=1, pady=5)

        txt_secundary_number = Entry(width="25", font="arial")
        txt_secundary_number.grid(row=7, column=3, pady=5)
        self.txt_secundary_number = txt_secundary_number

        btn_insert = Button(text="Cadastrar", width=10, font="arial, 12", command=self.insert_contact)
        btn_insert.grid(row=11, column=2, columnspan=2, padx=105, pady=5)
        self.btn_insert = btn_insert

        btn_update = Button(text="Alterar", width=10, font="arial, 12", command=self.update_datas_contact)
        btn_update.configure(state="disabled")
        btn_update.grid(row=12, column=2, columnspan=2, padx=105, pady=5)
        self.btn_update = btn_update

        btn_clear = Button(text="Limpar", width=10, font="arial, 12", command=self.clear_all_components)
        btn_clear.grid(row=11, column=3, columnspan=2, padx=105, pady=5)
        self.btn_clear = btn_clear

        btn_delete = Button(text="Excluir", width=10, font="arial, 12", command=self.delete_contact)
        btn_delete.configure(state="disabled")
        btn_delete.grid(row=12, column=3, columnspan=2, padx=105, pady=5)
        self.btn_delete = btn_delete

        btn_return_menu = Button(text="Voltar", width=10, font="arial, 12", command=self.return_form_menu)
        btn_return_menu.grid(row=13, column=2, columnspan=200, padx=35, pady=5)

    def activate_buttons(self, activate):
        if activate:
            self.btn_insert.configure(state="disabled")
            self.btn_update.configure(state="normal")
            self.btn_delete.configure(state="normal")
        else:
            self.btn_insert.configure(state="normal")
            self.btn_update.configure(state="disabled")
            self.btn_delete.configure(state="disabled")

    def search_contact(self):

        if self.txt_name_contact_searched.get() == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite um nome.")
            self.txt_name_contact_searched.focus_force()

        else:
            id_login = self.id_login
            name_contact = self.txt_name_contact_searched.get()

            if id_login is not None and name_contact != "":
                search_contact_hist = ContactFuntionalities()
                contact = search_contact_hist.search_contact(id_login, name_contact)
                if contact is not None:
                    self.activate_buttons(activate=True)
                    self.clear_datas_components()

                    self.txt_name_recorvered.insert(0, contact[0])
                    self.txt_name_contact.insert(0, contact[0])
                    self.txt_main_number.insert(1, contact[1])
                    self.txt_secundary_number.insert(2, contact[2])

                else:
                    tkinter.messagebox.showwarning("Atenção", "Não existe nenhum usuário contato com este Nome.")
                    self.clear_all_components()

    def insert_contact(self):
        error_secundary_number = False
        id_login = self.id_login
        name_contact = self.txt_name_contact.get()
        main_number = self.txt_main_number.get()
        secundary_number = self.txt_secundary_number.get()

        main_number = main_number.replace("-", "").replace(".", "")

        if id_login is None:
            tkinter.messagebox.showwarning("Atenção", "Por favor cheque se o ID_login foi adicionado.")
        elif name_contact == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite o Nome do Contato.")
            self.txt_name_contact.focus()

        elif main_number == "" or main_number.isdigit() is False:
            tkinter.messagebox.showwarning("Atenção", "Por favor digite o Número Principal do Contato "
                                                      "corretamente.")
            self.txt_main_number.focus()

        elif secundary_number != "":
            secundary_number = secundary_number.replace("-", "").replace(".", "")
            if secundary_number.isdigit() is False:
                try:
                    check_secundary_number = int(secundary_number)
                except ValueError:
                    error_secundary_number = True
                    tkinter.messagebox.showwarning("Atenção", "Por favor digite o Número Secundário do Contato "
                                                              "corretamente.")
                    self.txt_secundary_number.focus()

        if error_secundary_number is False:
            if id_login is not None and name_contact != "" and main_number.isdigit():
                if secundary_number == "":
                    secundary_number = None

                datas_new_contact = [id_login, name_contact, main_number, secundary_number]

                contact = ContactFuntionalities()
                contact.insert_contact(datas_new_contact)
                self.clear_all_components()

    def update_datas_contact(self):
        if tkinter.messagebox.askyesnocancel("Alterar", "Você Deseja Alterar os Dados deste Contato ?" ):
            error_secundary_number = False
            id_login = self.id_login
            name_contact_recovered = self.txt_name_recorvered.get()
            name_contact = self.txt_name_contact.get()
            main_number = self.txt_main_number.get()
            secundary_number = self.txt_secundary_number.get()

            main_number = main_number.replace("-", "").replace(".", "")

            if id_login is None:
                tkinter.messagebox.showwarning("Atenção", "Por favor cheque se o ID_login foi adicionado.")

            elif name_contact_recovered == "":
                tkinter.messagebox.showwarning("Atenção", "Por favor digite um Nome para Pesquisar.")

            elif name_contact == "":
                tkinter.messagebox.showwarning("Atenção", "Por favor digite o Nome do Contato.")
                self.txt_name_contact.focus()

            elif main_number == "" or main_number.isdigit() is False:
                tkinter.messagebox.showwarning("Atenção", "Por favor digite o Número Principal do Contato "
                                                          "corretamente.")
                self.txt_main_number.focus()

            elif secundary_number != "" and secundary_number not in ("Não possuí um 2º Número", "Não possuí um 2"):
                secundary_number = secundary_number.replace("-", "").replace(".", "")
                if secundary_number.isdigit() is False:
                    try:
                        check_secundary_number = int(secundary_number)
                    except ValueError:
                        error_secundary_number = True
                        tkinter.messagebox.showwarning("Atenção", "Por favor digite o Número Secundário do Contato "
                                                                  "corretamente.")
                        self.txt_secundary_number.focus()

            if error_secundary_number is False:
                if id_login is not None and name_contact != "" and main_number.isdigit():
                    if secundary_number == "" or secundary_number in ("Não possuí um 2º Número", "Não possuí um 2"):
                        secundary_number = None

                    datas_new_contact = [id_login, name_contact_recovered, name_contact, main_number, secundary_number]
                    print(datas_new_contact)
                    contact = ContactFuntionalities()
                    contact.update_datas_contact(datas_new_contact)
                    self.clear_all_components()

    def delete_contact(self):
        if tkinter.messagebox.askyesnocancel("Excluir", "Você Deseja Excluir este contato ?"):
            id_login = self.id_login
            name_recovered = self.txt_name_contact.get()

            if id_login is not None and name_recovered != "":
                contact = ContactFuntionalities()
                deleted_contact = contact.delete_contact(id_login, name_recovered)
                if deleted_contact is not None:
                    tkinter.messagebox.showinfo("Ok", "O Contato foi excluído com sucesso.")
                    self.clear_all_components()
                else:
                    tkinter.messagebox.showwarning("Atenção", "Não foi possível excluir o contato.")

    def clear_datas_components(self):
        self.txt_name_recorvered.delete(0, len(self.txt_name_recorvered.get()))
        self.txt_name_contact.delete(0, len(self.txt_name_contact.get()))
        self.txt_main_number.delete(0, len(self.txt_main_number.get()))
        self.txt_secundary_number.delete(0, len(self.txt_secundary_number.get()))

    def clear_all_components(self):
        self.activate_buttons(activate=False)
        self.txt_name_contact_searched.delete(0, len(self.txt_name_contact_searched.get()))
        self.clear_datas_components()
        self.txt_name_contact_searched.focus_force()


def instance_form_main_contacts(id_login):
    form_main_contacts = Tk()
    FormMainContact(form_main_contacts, id_login)
    form_main_contacts.iconbitmap(r"Images/IconeAgenda.ico")
    form_main_contacts.configure(relief="ridge", bg="light gray", border="4")
    form_main_contacts.geometry("480x640+470+5")
    form_main_contacts.resizable(0, 0)
    form_main_contacts.mainloop()
    exit()


# instance_form_main_contacts(3)

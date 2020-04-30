import tkinter.messagebox
from tkinter import *
from Graphic_Interfaces.FormMainMenu import FormMenu
from Funtionalities.HistoryContactFuntionalities import HistoryContact


class FormHistContacts(FormMenu):

    def __init__(self, master, id_login):
        self.master = master
        self.master.title("Histórico de Contatos")
        self.create_comp_form_hist_contac(master)
        self.id_login = id_login

    def create_comp_form_hist_contac(self, window):
        self.create_menu_component(window)

        lbl_title = Label(text="Histórico - Contatos", font="arial, 18", bg="light gray")
        lbl_title.grid(row=1, column=3, columnspan=1, pady=5)

        canvas_image = Canvas(window, width=225, height=225)
        bg_image = tkinter.PhotoImage(file=r"Images/HistoricContacts.png")
        canvas_image.create_image((0, 0), image=bg_image, anchor=NW)
        canvas_image.image = bg_image
        canvas_image.grid(row=2, column=3, columnspan=1, pady=5)

        lbl_name_hist_contact = Label(text="  Nome do Contato:", font="arial,14", bg="light gray")
        lbl_name_hist_contact.grid(row=3, column=2, columnspan=1, pady=25)

        txt_name_hist_contact = Entry(width="25", font="arial")
        txt_name_hist_contact.grid(row=3, column=3, pady=2)
        txt_name_hist_contact.focus()
        self.txt_name_hist_contact = txt_name_hist_contact

        btn_search = Button(text="Pesquisar", width=8, font="arial, 12", command=self.search_contact_historic)
        btn_search.grid(row=3, column=4, columnspan=2, padx=5, pady=5)

        lbl_name_contact = Label(text="\t    Nome:", font="arial,14", bg="light gray")
        lbl_name_contact.grid(row=5, column=2, columnspan=1, pady=5)

        txt_name_contact = Entry(width="25", font="arial")
        txt_name_contact.configure(state="read")
        txt_name_contact.grid(row=5, column=3, pady=2)
        self.txt_name_contact = txt_name_contact

        lbl_main_number = Label(text="  Número Principal:", font="arial,14", bg="light gray")
        lbl_main_number.grid(row=6, column=2, columnspan=1, pady=5)

        txt_main_number = Entry(width="25", font="arial")
        txt_main_number.configure(state="read")
        txt_main_number.grid(row=6, column=3, pady=5)
        self.txt_main_number = txt_main_number

        lbl_secundary_number = Label(text="Número Secudário:", font="arial,14", bg="light gray")
        lbl_secundary_number.grid(row=7, column=2, columnspan=1, pady=5)

        txt_secundary_number = Entry(width="25", font="arial")
        txt_secundary_number.configure(state="read")
        txt_secundary_number.grid(row=7, column=3, pady=5)
        self.txt_secundary_number = txt_secundary_number

        lbl_status_contact = Label(text="  Status do Contato:", font="arial,14", bg="light gray")
        lbl_status_contact.grid(row=8, column=2, columnspan=1, pady=5)

        txt_status_contact = Entry(width="25", font="arial")
        txt_status_contact.configure(state="read")
        txt_status_contact.grid(row=8, column=3, pady=5)
        self.txt_status_contact = txt_status_contact

        lbl_created_date = Label(text="    Data de Criação:", font="arial,14", bg="light gray")
        lbl_created_date.grid(row=9, column=2, columnspan=1, pady=5)

        txt_created_date = Entry(width="25", font="arial")
        txt_created_date.configure(state="read")
        txt_created_date.grid(row=9, column=3, pady=5)
        self.txt_created_date = txt_created_date

        lbl_updated_date = Label(text=" Data de Alteração:", font="arial,14", bg="light gray")
        lbl_updated_date.grid(row=10, column=2, columnspan=1, pady=5)

        txt_updated_date = Entry(width="25", font="arial")
        txt_updated_date.configure(state="read")
        txt_updated_date.grid(row=10, column=3, pady=5)
        self.txt_updated_date = txt_updated_date

        btn_clear = Button(text="Limpar", width=10, font="arial, 12", command=self.clear_all_components)
        btn_clear.grid(row=11, column=2, columnspan=2, padx=105, pady=5)

        btn_return_menu = Button(text="Voltar", width=10, font="arial, 12", command=self.return_form_menu)
        btn_return_menu.grid(row=11, column=3, columnspan=2, padx=105, pady=5)

    def activate_entries(self, activate):
        if activate:
            self.txt_name_contact.configure(state="normal")
            self.txt_main_number.configure(state="normal")
            self.txt_secundary_number.configure(state="normal")
            self.txt_status_contact.configure(state="normal")
            self.txt_created_date.configure(state="normal")
            self.txt_updated_date.configure(state="normal")
        else:
            self.txt_name_contact.configure(state="read")
            self.txt_main_number.configure(state="read")
            self.txt_secundary_number.configure(state="read")
            self.txt_status_contact.configure(state="read")
            self.txt_created_date.configure(state="read")
            self.txt_updated_date.configure(state="read")

    def search_contact_historic(self):

        if self.txt_name_hist_contact.get() == "":
            tkinter.messagebox.showwarning("Atenção", "Por favor digite um nome.")
            self.txt_name_hist_contact.focus_force()

        else:
            id_login = self.id_login
            name_contact_hist = self.txt_name_hist_contact.get()

            if id_login is not None and name_contact_hist != "":
                search_contact_hist = HistoryContact()
                contact = search_contact_hist.search_contact_hist(id_login, name_contact_hist)
                if contact is not None:
                    self.clear_datas_components()
                    self.activate_entries(activate=True)

                    self.txt_name_contact.insert(0, contact[0])
                    self.txt_main_number.insert(1, contact[1])
                    self.txt_secundary_number.insert(2, contact[2])
                    self.txt_status_contact.insert(3, contact[3])
                    self.txt_created_date.insert(4, contact[4])
                    self.txt_updated_date.insert(5, contact[5])

                    self.activate_entries(activate=False)

                else:
                    tkinter.messagebox.showwarning("Atenção", "Não Existe Histórico deste Contato.")
                    self.clear_all_components()

    def clear_datas_components(self):
        self.activate_entries(activate=True)

        self.txt_name_contact.delete(0, len(self.txt_name_contact.get()))
        self.txt_main_number.delete(0, len(self.txt_main_number.get()))
        self.txt_secundary_number.delete(0, len(self.txt_secundary_number.get()))
        self.txt_status_contact.delete(0, len(self.txt_status_contact.get()))
        self.txt_created_date.delete(0, len(self.txt_created_date.get()))
        self.txt_updated_date.delete(0, len(self.txt_updated_date.get()))

        self.activate_entries(activate=False)

    def clear_all_components(self):
        self.txt_name_hist_contact.delete(0, len(self.txt_name_hist_contact.get()))
        self.clear_datas_components()
        self.txt_name_hist_contact.focus_force()


def instance_form_hist_contacts(id_login):
    form_hist_contact = Tk()
    FormHistContacts(form_hist_contact, id_login)
    form_hist_contact.iconbitmap(r"Images/IconeAgenda.ico")
    form_hist_contact.configure(relief="ridge", bg="light gray", border="4")
    form_hist_contact.geometry("480x640+470+5")
    form_hist_contact.resizable(0, 0)
    form_hist_contact.mainloop()
    exit()


# instance_form_hist_contacts(1)

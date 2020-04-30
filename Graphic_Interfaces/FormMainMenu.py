import tkinter.messagebox
import tkinter
from tkinter import *
from Funtionalities.LoginFuntionalities import LoginFuntionalities


class FormMenu:

    def __init__(self, master, id_login):
        self.master = master
        self.master.title("Menu Principal")
        self.create_components_form_menu(master)
        self.id_login = id_login

    def create_menu_component(self, window):
        menu = Menu(window)

        # Sub Menu de Contatos
        menu_contacts = Menu(menu, font="Arial, 10")
        menu_contacts.add_command(label="Pesquisar Contato", command=self.form_main_contacts)
        menu_contacts.add_command(label="Adicionar um Contato", command=self.form_main_contacts)
        menu_contacts.add_command(label="Alterar Dados", command=self.form_main_contacts)
        menu_contacts.add_command(label="Excluir Contato", command=self.form_main_contacts)
        menu_contacts.add_command(label="Lista de Contatos", command=self.form_show_contacts)
        menu.add_cascade(label="Contatos", menu=menu_contacts)
        self.master.config(menu=menu)

        # Sub Menu de Historico de Contatos
        menu_historic = Menu(menu, font="Arial, 10")
        menu_historic.add_command(label="Pesquisar Histórico de um Contato", command=self.form_search_contact_hist)
        menu_historic.add_command(label="Lista de Histórico De Contatos", command=self.form_hist_all_contacts)
        menu.add_cascade(label="Histórico", menu=menu_historic)
        self.master.config(menu=menu)

        # Sub Menu - Menu Principal
        menu_main_menu = Menu(menu, font="Arial, 10")
        menu_main_menu.add_command(label="Menu Principal", command=self.return_form_menu)
        menu.add_cascade(label="Menu", menu=menu_main_menu)
        self.master.config(menu=menu)

        # Sub Menu de Opçoes Login
        menu_options_login = Menu(menu, font="Arial, 10")
        menu_options_login.add_command(label="Alterar Dados Login", command=self.form_options_login)
        menu_options_login.add_command(label="Desativar Login", command=self.deactivate_login)
        menu_options_login.add_command(label="Excluir o Login", command=self.form_options_login)
        menu.add_cascade(label="Opções", menu=menu_options_login)
        self.master.config(menu=menu)

        # Sub Menu Sair
        menu_exit = Menu(menu, font="Arial, 10")
        menu_exit.add_command(label="Sair", command=self.exit_menu)
        menu.add_cascade(label="Sair", menu=menu_exit)
        self.master.config(menu=menu)

    def create_components_form_menu(self, window):
        self.create_menu_component(window)

        lbl_title = Label(text="Menu Principal - Agenda", font="arial, 20", bg="light gray")
        lbl_title.grid(row=3, column=5, padx=30, pady=5)

        canvas_image = Canvas(window, width=225, height=200)
        bg_image = tkinter.PhotoImage(file=r"Images/Contact.png")
        canvas_image.create_image((0, 0), image=bg_image, anchor=NW)
        canvas_image.image = bg_image
        canvas_image.grid(row=4, column=5, columnspan=1, pady=15, padx=50)

        btn_contacts = Button(text="Contatos", width="30", font="arial,12bold", command=self.form_main_contacts)
        btn_contacts.grid(row=10, column=5, columnspan=3, padx=3, pady=10)

        btn_historic_contacts = Button(text="Histórico", width="30", font="arial,12bold"
                                       , command=self.form_search_contact_hist)
        btn_historic_contacts.grid(row=15, column=5, columnspan=2, padx=3, pady=10)

        btn_options_login = Button(text="Opções", width="30", font="arial", command=self.form_options_login)
        btn_options_login.grid(row=16, column=5, columnspan=2, padx=3, pady=10)

        btn_exit = Button(text="Sair", width="30", font="arial", command=self.exit_menu)
        btn_exit.grid(row=17, column=5, columnspan=2, padx=3, pady=10)

    def form_main_contacts(self):
        self.master.destroy()
        from Graphic_Interfaces.FormMainContact import instance_form_main_contacts
        instance_form_main_contacts(self.id_login)

    def form_show_contacts(self):
        self.master.destroy()
        from Graphic_Interfaces.FormListContacts import instance_form_show_contacts
        instance_form_show_contacts(self.id_login)

    def form_search_contact_hist(self):
        self.master.destroy()
        from Graphic_Interfaces.FormHistContact import instance_form_hist_contacts
        instance_form_hist_contacts(self.id_login)

    def form_hist_all_contacts(self):
        self.master.destroy()
        from Graphic_Interfaces.FormListHistAllContacts import instance_form_hist_all_contacts
        instance_form_hist_all_contacts(self.id_login)

    def form_options_login(self):
        self.master.destroy()
        from Graphic_Interfaces.FormOptionLogin import instance_form_options_login
        instance_form_options_login(self.id_login)

    def deactivate_login(self):
        if tkinter.messagebox.askyesnocancel("Desativar", "Você Deseja Desativar o seu Login ?"):
            desactive_flag = 'N'
            if self.id_login is None or desactive_flag not in ('Y', 'N'):
                tkinter.messagebox.showwarning("Atenção", "ID do Login está incorreto e com erro na flag.")
            else:
                login = LoginFuntionalities()
                login_deactived = login.deactivate_login(self.id_login, desactive_flag)
                if login_deactived == "Desativado":
                    self.master.destroy()
                    from Graphic_Interfaces.FormLogin import instance_form_login
                    instance_form_login()

    def return_form_menu(self):
        self.master.destroy()
        instance_form_menu(self.id_login)

    def exit_menu(self):
        if tkinter.messagebox.askyesnocancel("Sair", "Você Realmente Deseja Sair Da Aplicação ?"):
            self.master.destroy()
            from Graphic_Interfaces.FormLogin import instance_form_login
            instance_form_login()


def instance_form_menu(id_login):
    form_menu = Tk()
    FormMenu(form_menu, id_login)
    form_menu.iconbitmap(r"Images/IconeAgenda.ico")
    form_menu.configure(relief="ridge", bg="light gray", border="4")
    form_menu.geometry("380x600+560+50")
    form_menu.resizable(0, 0)
    form_menu.mainloop()
    exit()

# instance_form_menu(3)

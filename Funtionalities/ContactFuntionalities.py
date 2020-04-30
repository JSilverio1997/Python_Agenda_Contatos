import tkinter.messagebox
from Actions_CRUD.ContactActions import Contact
from Getters_Setters.ContactsGetSetter import ContactGetSetter


class ContactFuntionalities(ContactGetSetter):

    @staticmethod
    def insert_contact(list_datas=[]):
        try:
            if list_datas[0] is not None and list_datas[1] != "" and list_datas[2].isdigit():
                dict_contact = {}
                ContactGetSetter.id_login = list_datas[0]
                ContactGetSetter.name = list_datas[1]
                ContactGetSetter.main_number = list_datas[2]
                ContactGetSetter.secundary_number = list_datas[3]

                dict_contact['id_login'] = ContactGetSetter.id_login
                dict_contact['nome'] = ContactGetSetter.name
                dict_contact['numero_principal'] = ContactGetSetter.main_number
                dict_contact['numero_secundario'] = ContactGetSetter.secundary_number

                create_contact = Contact()
                created_contact = create_contact.insert(dict_contact)
                if created_contact is not None:
                    tkinter.messagebox.showinfo("OK", "O Contato foi cadastrado com Sucesso")
                else:
                    tkinter.messagebox.showwarning("Atenção", "Não foi possível cadastrar o usuário, "
                                                              "pois já existe este contato cadastrado em sua lista.")

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar inserir um contato.")

    @staticmethod
    def show_all_contacts(id_login):
        ContactGetSetter.id_login = id_login

        contact = Contact()
        consult_datas = contact.show_contact(ContactGetSetter.id_login)

        if consult_datas is not None:
            return consult_datas

        else:
            return None

    @staticmethod
    def search_contact(id_login, name_searched):
        ContactGetSetter.id_login = id_login
        ContactGetSetter.name = name_searched

        contact = Contact()
        search_contact = contact.search_contact(ContactGetSetter.id_login, ContactGetSetter.name)
        if search_contact is not None:
            name = search_contact[0]
            main_number = search_contact[1]
            secundary_number = search_contact[2]

            ContactGetSetter.name = name
            ContactGetSetter.main_number = main_number
            ContactGetSetter.secundary_number = secundary_number

            print(f"\nNome: {ContactGetSetter.name}")
            print(f"Número Principal: {ContactGetSetter.main_number}")
            print(f"Número Secundário: {ContactGetSetter.secundary_number}\n")

            return search_contact

        else:
            return None

    @staticmethod
    def update_datas_contact(list_datas=[]):
        if list_datas[1] != "" and list_datas[2] != "" and list_datas[3].isdigit():

            dict_datas_contact = {}
            ContactGetSetter.id_login = list_datas[0]
            ContactGetSetter.name_recovered = list_datas[1]
            ContactGetSetter.name = list_datas[2]
            ContactGetSetter.main_number = list_datas[3]
            ContactGetSetter.secundary_number = list_datas[4]

            dict_datas_contact['id_login'] = ContactGetSetter.id_login
            dict_datas_contact['nome_recuperado'] = ContactGetSetter.name_recovered
            dict_datas_contact['nome'] = ContactGetSetter.name
            dict_datas_contact['numero_principal'] = ContactGetSetter.main_number
            dict_datas_contact['numero_secundario'] = ContactGetSetter.secundary_number

            contact = Contact()
            updated_contact = contact.update(dict_datas_contact)
            if updated_contact is not None:
                tkinter.messagebox.showinfo("Sucesso", "Os Dados do Contato foi Alterado com Sucesso.")
            else:
                tkinter.messagebox.showwarning("Atenção", "Não foi Possível Alterar os dados do Contato.")

    @staticmethod
    def delete_contact(id_login, name_recovered):
        ContactGetSetter.id_login = id_login
        ContactGetSetter.name = name_recovered
        delete_contact = Contact()
        deleted_contact = delete_contact.delete(ContactGetSetter.id_login, ContactGetSetter.name)
        if delete_contact is not None:
            return delete_contact
        else:
            return None


"""id_login_test = 3
nome = "Caio"
nome_pesquisado = "pedro"
numero_principal = "977122282"
numero_secundario = "977122281"""
# datas_test = [id_login_test, nome, numero_principal, numero_secundario]
# datas_test = [id_login_test, nome_pesquisado, nome, numero_principal, numero_secundario]
# create_contact_test = ContactFuntionalities()
# print(create_contact_test.insert_contact(datas_test))
# create_contact_test.show_all_contacts(id_login_test)
# create_contact_test.search_contact(id_login_test, nome)
# create_contact_test.delete_contact(id_login_test, nome)
# create_contact_test.update_datas_contact(list_datas=datas_test)

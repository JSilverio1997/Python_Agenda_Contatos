import tkinter.messagebox
from Actions_CRUD.ContactHistoric import ContactHistoric
from Getters_Setters.ContactHistory import ContactHistoryGetSetter


class HistoryContact(ContactHistoryGetSetter):
    @staticmethod
    def search_contact_hist(id_login, name):
        ContactHistoryGetSetter.id_login = id_login
        ContactHistoryGetSetter.name = name

        search = ContactHistoric()
        searched_contact_hist = search.search_contact_historic(ContactHistoryGetSetter.id_login,
                                                               ContactHistoryGetSetter.name)
        if searched_contact_hist is not None:
            name_contact_hist = searched_contact_hist[0]
            main_number = searched_contact_hist[1]
            secundary_number = searched_contact_hist[2]
            status_contact = searched_contact_hist[3]
            created_date = searched_contact_hist[4]
            updated_date = searched_contact_hist[5]

            print("-" * 70)
            print("\t \t \t Histórico de Contatos \n")
            print(f"Nome do Contato: {name_contact_hist.title()}")
            print(f"Número Principal: {main_number}")
            print(f"Número Secundário: {secundary_number}")
            print(f"Status do Contato: {status_contact}")
            print(f"Data de Criação: {created_date}")
            print(f"Data de Alteração: {updated_date}")
            print("-" * 70)
            return searched_contact_hist
        else:
            return None

    @staticmethod
    def show_all_contact_hist(id_login):
        if id_login is not None:
            ContactHistoryGetSetter.id_login = id_login

            show_all_contact = ContactHistoric()
            all_contact_datas = show_all_contact.show_contact_historic(ContactHistoryGetSetter.id_login)

            if all_contact_datas is not None:
                return all_contact_datas

            else:
                return None


"""id_login_test = 1
name_test = "Alex"
historic = HistoryContact()"""
# historic.search_contact_hist(id_login_test, name_test)
# historic.show_all_contact_hist(id_login_test)

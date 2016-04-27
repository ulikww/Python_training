import re
from random import randrange


def test_contact_edit_fom_and_home_page(app):
    old_contacts = app.contact.get_contact_list()
    #index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()#[index]
    contact_from_edit_page =app.contact.get_contact_info_from_edit_page(index)
    merged_email = merge_email_like_on_home_page(contact_from_edit_page)
    merged_phones = merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merged_email
    assert contact_from_home_page.all_phones_from_home_page == merged_phones
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address



def merge_email_like_on_home_page(contact):
    return "\n".join (filter(lambda x:x != "",[contact.email, contact.email2, contact.email3]))

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x:x != "",
                            map(lambda x: clear(x),
                                filter(lambda x:x is not None,
                                       sorted([contact.homephone, contact.workphone, contact.secondaryphone, contact.mobilephone])))))




def clear(s):
    return re.sub("[() -]", "", s)






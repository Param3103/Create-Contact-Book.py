class AddingToBook:

    def creating_new_contact(name, phone, email, address, contact_book):
        contact = [name, phone, address, email]
        contact_book.writerow(contact)
        return contact_book

# need to work on this
    def update_existing_contact(finder_keys, finder_values, tbc_keys, new_values, contact_book_reader, contact_book_writer):
        fieldnames = ['Name', 'Phone No', 'Email ID', 'Address']
        for contact in contact_book_reader:
            contact_book_reader.remove(contact)
            if len(contact) == 0:
                continue
            else:
                temp = contact
                found = True
                for finder_key in finder_keys:
                    if contact[fieldnames.index(finder_key)] != finder_values[finder_keys.index(finder_key)]:
                        found = False
                        contact = temp
                        continue
                    else:
                        contact = temp
                        continue
                # section below need work
                if found:
                    for tbc_key in tbc_keys:
                        contact[fieldnames.index(tbc_key)] = new_values[tbc_keys.index(tbc_key)]
                        for row in contact_book_reader:
                            if row == temp:
                                pos = contact_book_reader.pos(row)
                                row = contact
                                contact_book_writer[pos] = row
                                continue
                            else:
                                continue
                else:
                    continue
        return(contact_book_writer)

AddingToBook
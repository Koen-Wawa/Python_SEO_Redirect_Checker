import csv
import requests


def read_csv(csv_file):
    url_tuples = []
    with open(csv_file, 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        first_row = next(reader)
        for row in reader:
            url_tuples.append(row)

    return url_tuples


def visit_url_and_get_all_info(url_address):
    try:
        r = requests.get(url_address)
        history = r.history
        endpoint_url = r.url
        endpoint_status_code = r.status_code

        if len(r.history) > 1:
            redirect_chain_list = []
            cursor = 0

            for element in r.history:
                redirect_chain_element = f"{r.history[cursor].url}     ({r.history[cursor].status_code})--->     "
                redirect_chain_list.append(redirect_chain_element)
                cursor += 1

            redirect_chain_destination = f"{r.url}     ({r.status_code})"
            redirect_chain_list.append(redirect_chain_destination)

            redirect_string = ''
            for element in redirect_chain_list:
                redirect_string = redirect_string + element

            redirect_chain = redirect_string

            history_status_code = history[0].status_code

        elif len(r.history) == 1:

            history_status_code = history[0].status_code
            redirect_chain = "-"

        else:
            history_status_code = r.status_code
            redirect_chain = "-"

        return history_status_code, endpoint_url, endpoint_status_code, redirect_chain

    except:
        history_status_code, endpoint_url, endpoint_status_code, redirect_chain = "-", "-", "-", "-"

        return history_status_code, endpoint_url, endpoint_status_code, redirect_chain


def create_csv_row_with_all_info(url_tuple_list):

    complete_list_with_placeholder = []

    for url in url_tuple_list:
        all_info_tuple = visit_url_and_get_all_info(url[0])
        status_code_input_url = all_info_tuple[0]
        endpoint_url = str(all_info_tuple[1])
        endpoint_status_code = str(all_info_tuple[2])
        redirect_chain = str(all_info_tuple[3])
        intended_redirect = url[1]
        actual_redirect = endpoint_url
        endpoint_status = endpoint_status_code

        if intended_redirect == actual_redirect:
            correct_redirect = 'Yes'
        else:
            correct_redirect = 'No'

        chain = redirect_chain

        final_check = 'placeholder'

        completed_list_line = (url[0], status_code_input_url, intended_redirect, actual_redirect, endpoint_status,
                               correct_redirect, final_check, chain)

        complete_list_with_placeholder.append(completed_list_line)

    return complete_list_with_placeholder


def final_check(complete_rows):

    complete_list = []

    for row in complete_rows:
        row = list(row)
        if row[7] != "-":
            row[6] = 'Redirect Chain'
            complete_list.append(row)
        elif row[4] == '200' and row[5] == 'Yes':
            row[6] = 'Yes'
            complete_list.append(row)
        else:
            row[6] = 'No'
            complete_list.append(row)

    return complete_list


def write_csv(redirect_info_list):

    header = ['Original URL', 'Status Code', 'Intended Redirect Endpoint', 'Actual Endpoint',
              'Endpoint Status Code', 'Correct Redirect?', 'Everything Correct?', 'Redirect Chain?']

    with open(f'Redirect Check.csv', 'w', encoding='utf8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for line in redirect_info_list:
            writer.writerow(line)


if __name__ == "__main__":

    urls_csv = 'URL list.csv'
    url_tuple_list = read_csv(urls_csv)
    complete_list_before_final_check = create_csv_row_with_all_info(url_tuple_list)
    final_info_list = final_check(complete_list_before_final_check)
    write_csv(final_info_list)

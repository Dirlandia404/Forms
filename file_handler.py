import csv
import os

def write_csv(url_commit, message):
    file_exists = os.path.isfile('commits.csv')
    with open('commits.csv', mode='a', newline='', encoding="utf-8") as csv_file:
        field_names = ["url_commit", "message"]

        writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter=',')

        if not file_exists:
            writer.writeheader()

        writer.writerow({ "url_commit": url_commit, "message": message})
# def write_csv_pulls(url_commit, is_comment, message):
#     with open('commits_candidatos_pulls.csv', mode='a', newline='', encoding="utf-8") as csv_file:
#         field_names = ["url_commit", "comment", "message"]

#         writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter=',')

#         # writer.writeheader()
#         writer.writerow({"url_commit": url_commit, "comment": is_comment, "message": message})
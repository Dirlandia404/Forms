
from github import Github
import github
# import os
import file_handler


# token = os.environ['TOKEN_GITHUB']
token = ""

g = Github(token)


print(g)


def search_respositories_by_topic():
    print("--------------BUSCANDO REPOSITÓRIOS----------------")

    org_name = "vtex-apps"
    org = g.get_organization(org_name)  

    repos = org.get_repos()
    search_all_commits_by_repository(repos)


def search_all_commits_by_repository(repositories):
    for repo in repositories:
        commits = repo.get_commits()

        print("----------------------------------------------------------------------")
        print(f"VERIFICANDO SE REPOSITÓRIO {repo.name} ATENDE AOS REQUISITOS")
        try:
            if commits.totalCount > 500:
                print(f"repositório {repo.name} atende aos requisitos")
                print(f"EXTRAINDO COMMITS")
                print(f"Total de commits a serem extraídos: {commits.totalCount}")


                for commit in commits:
                    if commit.author is not None and commit.author.login is not None:
                        user_commit_count = 0
                        author = commit.author.login
                        for c in repo.get_commits(author=author):
                            user_commit_count += 1
                        file_handler.write_csv(author, repo.name, user_commit_count, commits.totalCount)
                        # print(f"O usuário {author} fez um commit no repositório {repo.name}")  
            else:
                print(f"Repositório {repo.name} não atende aos requisitos")
        except github.GithubException:
            print(f"Erro desconhecido ao acessar repositório {repo.name}")

# def search_all_commits_by_repository(repositories):
#     for repo in repositories:
#         commits = repo.get_commits()

#         print("----------------------------------------------------------------------")
#         print(f"VERIFICANDO SE REPOSITÓRIO {repo.name} ATENDE AOS REQUISITOS")
#         try:
#             if commits.totalCount > 100:
#                 print(f"repositório {repo.name} atende aos requisitos")
#                 print(f"EXTRAINDO COMMITS")
#                 print(f"Total de commits a serem extraídos: {commits.totalCount}")

#                 for commit in commits:
#                     terms = ['operability', 'understandability', 'learnability', 'useable', 'usefulness', 'utility', 'usefulness', 'gui', 'accessibility', 'menu', 'configure', 'convention', 'standart', 'layout', 'responsive', 'aria-label']

#                     message = commit.commit.message

#                     for word in terms:
#                       if word in message:
#                         print(f"A palavra '{word}' está presente no commit '{message}'")
#                         file_handler.write_csv(commit.html_url, commit.commit.message)
#             else:
#                 print(f"Repositório {repo.name} não atende aos requisitos")
#         except github.GithubException:
#             print(f"Erro desconhecido ao acessar repositório {repo.name}")


search_respositories_by_topic()
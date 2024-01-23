# dict_syntax = {
#     'key': 'value',
#     'key1': 'value', # Key has to be immutable - string, number, values can be any datatype
# }

from pprint import pprint

batch1_admin_data = dict()

batch1_admin_data['nikita'] = {
    'github_access': True,
    'python3_installed': True,
    'git_cli_bash': True,
    'itellij_installed': False,
    'operating_system': 'windows'
}

batch1_admin_data['abhilash'] = {
    'github_access': False,
    'python3_installed': True,
    'git_cli_bash': True,
    'itellij_installed': False,
    'operating_system': 'windows'
}

batch1_admin_data['abhishek'] = {
    'github_access': True,
    'python3_installed': True,
    'git_cli_bash': True,
    'itellij_installed': False,
    'operating_system': 'windows'
}

batch1_admin_data['anusha'] = {
    'github_access': True,
    'python3_installed': True,
    'git_cli_bash': True,
    'itellij_installed': False,
    'operating_system': 'windows'
}

batch1_admin_data['aparna'] = {
    'github_access': True,
    'python3_installed': True,
    'git_cli_bash': True,
    'itellij_installed': False,
    'operating_system': 'Ubuntu'
}

batch1_admin_data['bhavani'] = {
    'github_access': True,
    'python3_installed': False,
    'git_cli_bash': True,
    'itellij_installed': False,
    'operating_system': 'windows'
}

# pprint(batch1_admin_data) # Pretty print

print("Team of batch1: ", batch1_admin_data.values())

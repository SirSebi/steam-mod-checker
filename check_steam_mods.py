import requests

MOD_IDS = [
# Insert ModID's here seperated by comma
    2384329562, 1231231231 
]

BASE_URL = "https://steamcommunity.com/sharedfiles/filedetails/?id={}"

# ANSI-Escape-Codes für Farbausgabe
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

not_found_mods = []  # Liste für nicht gefundene Mods

def check_url(mod_id):
    url = BASE_URL.format(mod_id)
    response = requests.get(url)
    if response.status_code == 200:
        if "Error" in response.text or "Sorry!" in response.text:
            print(f"{RED}Mod {mod_id} does not exist: {url}{RESET}")
            not_found_mods.append(mod_id)
        else:
            print(f"{GREEN}Mod {mod_id} is reachable: {url}{RESET}")
    else:
        print(f"{RED}Mod {mod_id} is not reachable (Status {response.status_code}): {url}{RESET}")
        not_found_mods.append(mod_id)

if __name__ == "__main__":
    for mod_id in MOD_IDS:
        check_url(mod_id)

    print("\n🔎 **Summary:**")
    if not_found_mods:
        print(f"{RED}❌ The following mods were not found:{RESET}")
        for mod in not_found_mods:
            print(f" - {mod}")
    else:
        print(f"{GREEN}✅ All Mods are available!{RESET}")

